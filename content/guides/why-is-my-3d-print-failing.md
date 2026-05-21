---
title: "Why Is My 3D Print Failing? 12 Common Problems and How to Fix Them"
date: 2026-05-20
description: "The 12 most common 3D printing failures — warping, stringing, poor adhesion, layer shifts — and the exact fixes that work. A troubleshooting guide you'll actually use."
tags: ["troubleshooting", "guide", "first layer", "warping", "stringing", "adhesion"]
categories: ["guides"]
weight: 3
---

Every 3D print failure has a cause, and almost all of them fall into one of a dozen buckets. This is the troubleshooting checklist worth bookmarking — symptoms, causes, and the fixes that actually work, in rough order of how often they bite people.

{{< disclosure >}}

## 1. First Layer Won't Stick

The single most common failure. If the first layer doesn't adhere, nothing else matters.

**Fixes, in order:**
- **Re-level the bed** (or re-run auto bed leveling). 80% of adhesion problems are leveling.
- **Lower the nozzle slightly** — adjust your Z-offset down in small steps (0.02-0.05mm).
- **Clean the bed.** Fingerprint oils kill adhesion. Wipe with isopropyl alcohol.
- **Raise bed temperature** 5°C. For PLA try 60°C, PETG 75-80°C.
- **Slow the first layer** to ~20mm/s.
- **Add a brim** in your slicer for extra surface contact.

## 2. Warping (Corners Lifting)

The print curls up at the edges, especially with ABS and large flat parts.

**Fixes:**
- **Use a brim or raft** for more bed grip.
- **Eliminate drafts** — an enclosure makes the biggest difference for ABS.
- **Raise bed temp** and keep the chamber warm.
- **Switch material** — if you don't have an enclosure, PETG or PLA warps far less than ABS.

## 3. Stringing (Wispy Threads Between Parts)

Thin strands of filament strung across gaps, most common with PETG.

**Fixes:**
- **Increase retraction distance and speed** in your slicer.
- **Lower print temperature** 5-10°C — too hot causes oozing.
- **Enable "wipe" and "combing"** in your slicer.
- **Dry your filament** — moisture is a major stringing cause (especially PETG and nylon).

## 4. Layer Shifting (Print Suddenly Offset)

Upper layers misalign with lower ones, ruining the print mid-way.

**Fixes:**
- **Reduce print speed and acceleration** — shifts often come from the toolhead moving faster than the motors can keep up.
- **Check belt tension** — loose belts skip steps.
- **Make sure nothing's obstructing the gantry** — a stray clip or cable can cause a skip.

## 5. Under-Extrusion (Gaps, Thin Layers)

Not enough plastic coming out — weak, gappy prints.

**Fixes:**
- **Check for a partial clog** — do a cold pull or run cleaning filament.
- **Increase flow rate / extrusion multiplier** slightly.
- **Raise temperature** 5°C so plastic flows more easily.
- **Inspect the extruder gear** for ground-down filament (a sign of a jam upstream).

## 6. Over-Extrusion (Blobs, Rough Top)

Too much plastic — messy surfaces and dimensional inaccuracy.

**Fixes:**
- **Lower flow rate / extrusion multiplier.**
- **Calibrate your E-steps** (extruder steps) if it's persistent.
- **Reduce temperature** slightly.

## 7. Clogged Nozzle

Nothing extrudes, or extrusion stops mid-print.

**Fixes:**
- **Cold pull** — heat, then pull filament out to remove the clog.
- **Use a cleaning needle** to clear the nozzle.
- **Replace the nozzle** — they're cheap and wear out, especially with abrasive filaments like PLA-CF.

## 8. Poor Overhangs / Drooping

Steep angles sag or fail.

**Fixes:**
- **Improve cooling** — turn up the part cooling fan for PLA.
- **Add supports** for overhangs beyond ~50-55°.
- **Slow down** on overhang regions.
- **Orient the part** to minimize steep overhangs in the first place.

## 9. Elephant's Foot (Bulging First Layers)

The bottom layers bulge outward.

**Fixes:**
- **Lower bed temperature** slightly.
- **Raise the Z-offset** a touch.
- **Enable "elephant foot compensation"** in your slicer.

## 10. Ghosting / Ringing (Echoes Near Edges)

Faint ripples after sharp corners.

**Fixes:**
- **Lower acceleration and jerk.**
- **Tighten belts.**
- **Make sure the printer sits on a solid, stable surface** — a wobbly table amplifies it.

## 11. Spaghetti (Print Detaches and Becomes a Mess)

The print comes loose and the nozzle keeps extruding into air.

**Fixes:**
- Almost always a **first-layer adhesion failure** (see #1) — fix that first.
- **Add a brim**, clean the bed, re-level.
- On printers with failure detection, enable it so you don't waste a whole spool.

## 12. Wet Filament (Popping, Rough Surface, Weak Layers)

Filament that's absorbed moisture from the air.

**Fixes:**
- **Dry it** — a filament dryer, or a few hours in an oven at low temp (check your filament's safe temp).
- **Store filament sealed** with desiccant going forward.
- PETG, TPU, and nylon are the worst offenders; PLA is more forgiving.

## The Universal First Three Checks

When a print fails and you don't know why, check these before anything else:
1. **Is the bed level and clean?**
2. **Is the filament dry?**
3. **Are you printing too fast for the part?**

Those three account for the large majority of failures. Master them and your success rate jumps dramatically.

## Tools Worth Having

- **A {{< amzn "filament-dryer" "filament dryer" >}}** — fixes a whole category of problems.
- **A spare {{< amzn "nozzle-set" "nozzle set" >}}** — clogs happen; swapping is faster than clearing.
- **Isopropyl alcohol + a glue stick** — the cheapest adhesion insurance there is.

*Got a failure not on this list? The cause is almost always temperature, adhesion, speed, or moisture. Work through those four and you'll find it.*
