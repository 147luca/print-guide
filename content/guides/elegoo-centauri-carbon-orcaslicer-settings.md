---
title: "Best OrcaSlicer Settings for the Elegoo Centauri Carbon (6 Months of Tuning)"
date: 2026-05-21
description: "Dialed-in OrcaSlicer settings for the Elegoo Centauri Carbon, per filament — PLA, PETG, TPU, ABS, and PLA-CF. Real numbers from daily printing, not copied defaults."
tags: ["elegoo", "centauri carbon", "orcaslicer", "settings", "fdm", "petg", "tpu", "pla-cf"]
categories: ["guides"]
weight: 2
---

The Centauri Carbon prints well out of the box, but "well" and "dialed in" are different things. After six months of near-daily printing across eight-plus filament types, these are the OrcaSlicer settings that actually hold up — print to print, not just on the one calibration cube that looks good on YouTube.

This isn't a copy of someone's profile export. Every number here came from a tuning pass and a pile of failed parts.

{{< disclosure >}}

## Before You Touch Per-Filament Settings

Two things matter more than any single slider:

1. **Run a flow-rate (extrusion multiplier) calibration per filament.** OrcaSlicer's built-in calibration tools do this in two prints. Skip it and every other setting fights against bad flow.
2. **Calibrate pressure advance.** On a bowden-free direct-drive machine like the Centauri, this is what kills the blobs at corners and the bulge after every travel move.

Do those two for each new spool brand and most "the printer is bad" problems disappear.

## PLA / PLA+

The easy one. The Centauri is nearly flawless here.

- **Layer height:** 0.2mm for daily parts, 0.12mm when the surface shows.
- **Speed:** Stock "fast" profile is fine. Rapid PLA+ holds quality at the printer's recommended fast speeds without visible layer-line degradation.
- **Infill:** Gyroid at 15% for functional/daily-use objects — strong enough, fast enough, and it doesn't telegraph through top surfaces.
- **Overhangs:** Clean to ~55° before you need supports. Plan around that and you'll print supportless more often than you'd expect.

## PETG (including food-grade and carbon PETG)

PETG is where people give up on a machine that's actually fine. The fix is first-layer discipline.

- **Slower first layer.** This is the single biggest win. PETG wants to be laid down calmly.
- **Higher bed temp** than PLA to get adhesion without slamming the nozzle into the plate.
- **Line width:** 0.42–0.5mm at 0.2mm layer height worked well for food-grade carbon PETG.
- **Retraction:** Keep it modest; over-retracting PETG causes more stringing problems than it solves. Tune pressure advance first, then revisit.

Once tuned, PETG is consistent on this machine — it just punishes a lazy first layer.

## TPU (flexible)

TPU works on the Centauri's direct drive, but you have to accept it's slow.

- **Speed:** 30mm/s max. Push past it and you'll get skips and gaps.
- **Retraction:** Disable it. Flexible filament + retraction = jams and inconsistent walls.
- **Patience:** Results are genuinely good. Impatient people will hate the print times. There's no shortcut here; flexibles are slow on every consumer machine.

## ABS

Printable, but it needs ambient heat management — the Centauri isn't a sealed chamber by default.

- **Enclose it.** I print ABS with the door shut in an enclosed space. Ambient temperature control is the whole game with ABS warping.
- **Bed adhesion:** Higher bed temp and a brim. ABS lifts corners the moment it cools unevenly.
- **Drafts are the enemy.** A cold breeze across a tall ABS print will split layers. Keep it closed up.

If you can't manage ambient temp, print ASA or a tough PETG instead and save yourself the warping headaches.

## PLA-CF (carbon-fiber filled)

- **Use a {{< amzn "hardened-nozzle" "hardened steel nozzle" >}}.** Carbon-fiber and glass-filled filaments chew through brass. This is non-negotiable if you want the nozzle to survive.
- **Layer height:** 0.2mm. CF filaments don't reward going ultra-fine; the fibers matter more than the layer lines.
- **Dry the filament.** CF blends pick up moisture fast and print rough/popping when wet. A {{< amzn "filament-dryer" "filament dryer" >}} pays for itself here.

## The One Setting Most People Get Wrong

First-layer speed. Across every filament above, slowing the first layer fixed more failures than any other change. The Centauri handles slow first layers cleanly, which means fewer failed prints and far less wasted filament over a month of printing. It's the least glamorous setting and the most important one.

## Bottom Line

The Centauri Carbon doesn't need exotic settings — it needs *per-filament* settings and two calibrations (flow + pressure advance) done honestly. Do that once per spool brand and you'll spend your time printing instead of troubleshooting.

For the full long-term durability and noise breakdown, see the [6-month Centauri Carbon review](/reviews/elegoo-centauri-carbon-review/). If you're still deciding between machines, the [Bambu A1 vs Centauri Carbon comparison](/reviews/bambu-a1-vs-elegoo-centauri-carbon/) covers the trade-offs.
