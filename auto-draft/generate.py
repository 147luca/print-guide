#!/usr/bin/env python3
"""Auto-draft one article for print-guide.

Picks the first topic in topics.yaml whose target file doesn't exist yet, asks
Claude (headless) to write the BODY in the site's voice, then writes a complete
post with deterministic frontmatter and `draft: true` (so it never auto-publishes
— a human flips draft:false after a quick read, then ./deploy.sh).

No third-party deps (system python has no PyYAML), so topics.yaml is parsed by a
small purpose-built reader for its known, simple structure.

Usage:  python3 auto-draft/generate.py
"""

import datetime
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # ~/print-guide
TOPICS = Path(__file__).resolve().parent / "topics.yaml"
LOG = Path(__file__).resolve().parent / "log.txt"
CLAUDE = "/Users/luca/.local/bin/claude"
MODEL = "sonnet"  # tactical/high-volume; drafts are human-reviewed before publish


def log(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def parse_topics(path):
    """Minimal parser for the controlled topics.yaml structure."""
    topics, cur = [], None
    for raw in path.read_text().splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("- "):
            if cur:
                topics.append(cur)
            cur = {}
            line = line[2:]
        if cur is None:
            continue
        m = re.match(r"\s*([a-z_]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if key == "link_keys":
            inner = val.strip("[]").strip()
            cur[key] = (
                [x.strip() for x in inner.split(",") if x.strip()] if inner else []
            )
        else:
            cur[key] = val.strip().strip('"')
    if cur:
        topics.append(cur)
    return topics


def build_prompt(topic):
    links = topic.get("link_keys") or []
    link_hint = (
        "Weave these affiliate links in ONLY where genuinely natural, using the "
        'exact shortcode form {{< amzn "KEY" "link text" >}} (key from this list): '
        + ", ".join(links)
        if links
        else "No product links needed for this one."
    )
    return f"""You are writing a 3D-printing article for "Print Guide" — a site with a blunt, \
experience-based voice. Rules for the voice:
- Honest and specific. Real numbers, real trade-offs. No marketing fluff, no hype.
- Anti-affiliate-spam tone: rank by what helps the reader, not commission.
- Scannable: short intro, ## section headers, a "## Bottom Line" close.
- 600-900 words. Confident, plain English.

Topic: "{topic["title"]}"
Target search keyword (use naturally, don't stuff): {topic.get("keyword", "")}

{link_hint}
If you use any affiliate link, put the shortcode {{{{< disclosure >}}}} on its own line right after the intro paragraph.
Add 1-2 internal links to related articles using Markdown paths like \
[PLA vs PETG vs ABS](/guides/pla-vs-petg-vs-abs/) or \
[why your print is failing](/guides/why-is-my-3d-print-failing/) where relevant.

OUTPUT FORMAT — follow EXACTLY:
- Line 1: `DESCRIPTION: ` then a 120-160 char meta description.
- Line 2: blank.
- Then the article body in Markdown, starting with the intro paragraph.
- Do NOT include a top-level # H1 title (the site adds it). Do NOT include YAML frontmatter.
- Do NOT wrap the output in code fences. Output the article and nothing else.
"""


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def main():
    topics = parse_topics(TOPICS)
    if not topics:
        log("No topics in queue.")
        return 0

    target = None
    for t in topics:
        section = t.get("section", "guides")
        slug = t.get("slug") or slugify(t["title"])
        dest = ROOT / "content" / section / f"{slug}.md"
        if not dest.exists():
            target = (t, section, slug, dest)
            break

    if not target:
        log("Queue empty — every topic already drafted/published.")
        return 0

    t, section, slug, dest = target
    log(f"Drafting: {t['title']} -> content/{section}/{slug}.md")

    prompt = build_prompt(t)
    try:
        r = subprocess.run(
            [
                CLAUDE,
                "-p",
                prompt,
                "--permission-mode",
                "bypassPermissions",
                "--model",
                MODEL,
                "--output-format",
                "text",
            ],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
            timeout=300,
        )
    except subprocess.TimeoutExpired:
        log("ERROR: claude timed out.")
        return 1
    if r.returncode != 0:
        log(f"ERROR: claude failed: {(r.stderr or '').strip()[:200]}")
        return 1

    out = r.stdout.strip()
    # strip accidental code fences
    if out.startswith("```"):
        out = re.sub(r"^```[a-z]*\n", "", out)
        out = re.sub(r"\n```$", "", out)

    desc = ""
    m = re.match(r"DESCRIPTION:\s*(.+)", out)
    if m:
        desc = m.group(1).strip().strip('"')
        out = out[m.end() :].lstrip("\n")
    else:
        desc = f"{t['title']} — a practical Print Guide article."

    if not out or len(out) < 400:
        log(
            f"ERROR: body too short ({len(out)} chars); not writing. Raw head: {out[:120]!r}"
        )
        return 1

    today = datetime.date.today().isoformat()
    kw = t.get("keyword", "")
    tags = sorted({w for w in re.split(r"\s+", kw) if len(w) > 2} | {"3d printing"})
    frontmatter = (
        "---\n"
        f'title: "{t["title"]}"\n'
        f"date: {today}\n"
        f'description: "{desc.replace(chr(34), chr(39))}"\n'
        f"tags: [{', '.join(repr(x) for x in tags)}]\n"
        f'categories: ["{section}"]\n'
        "draft: true   # auto-drafted — review, then set draft: false and ./deploy.sh\n"
        "---\n\n"
    )
    dest.write_text(frontmatter + out + "\n")
    log(
        f"DRAFTED (draft:true): {dest.relative_to(ROOT)}  ({len(out)} chars). Review then publish."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
