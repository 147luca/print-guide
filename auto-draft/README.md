# Auto-draft system

Generates one article draft at a time in the site's voice, with a **review gate**
so nothing AI-written goes live unread (which would risk SEO).

## Flow
1. `python3 auto-draft/generate.py` — picks the next undone topic from `topics.yaml`,
   asks Claude to write the body, and saves `content/<section>/<slug>.md` with
   **`draft: true`**. Drafts are excluded from the live build.
2. **Review:** read the draft. Preview all drafts locally with `hugo serve -D`.
3. **Publish:** set `draft: false` in the file, then `./deploy.sh`.

## Add topics
Append to `auto-draft/topics.yaml` (title, slug, section, keyword, link_keys).
They're drafted in order; a topic is skipped once its file exists.

## Optional: schedule daily drafting (NOT auto-enabled)
To accumulate ~1 draft/day for review, add a cron/launchd job or a loop line, e.g.:

    # every day at 9am, draft the next topic (still requires manual publish)
    0 9 * * *  cd /Users/luca/print-guide && /usr/bin/python3 auto-draft/generate.py

Left manual on purpose: it consumes Claude usage and produces content under Luca's
name, so publishing stays a human decision. Log: `auto-draft/log.txt`.
