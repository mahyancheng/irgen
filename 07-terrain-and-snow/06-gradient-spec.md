# Gradient: the client is right, and 19° was too conservative

The client: *"But of course a steeper hill is preferred"*.

**Correct, and for a stronger reason than preference.** On a small-plot mandate, gradient is the
mechanism that converts limited horizontal extent into useful vertical. The 19° figure carried
through this study came from the 吉雪 benchmark's *measured average* — it was never a
specification, and it should not have been used as one.

---

## Why gradient matters more on a small parcel than on a large one

`V = L × tan θ`. On a fixed parcel, every degree of gradient is vertical you do not have to buy
land for.

**Vertical available from a 632 m run — the side of a square 40 ha parcel:**

| Gradient | Vertical | vs. 19° |
|---|---|---|
| 15° | 169 m | −22% |
| **19°** (吉雪 average) | **218 m** | — |
| 22° | 255 m | +17% |
| **25°** | **295 m** | **+35%** |
| **28°** | **336 m** | **+54%** |
| 30° | 365 m | +67% |
| 33° | 410 m | +88% |

Read the other way — **land required to deliver the 300 m benchmark**, as a 200 m-wide corridor:

| Gradient | Horizontal run | Corridor area |
|---|---|---|
| 19° | 871 m | **17.4 ha** |
| 25° | 643 m | 12.9 ha |
| **28°** | **564 m** | **11.3 ha** |
| 33° | 462 m | 9.2 ha |

> **Going from 19° to 28° cuts the land needed for a 300 m hill by 35%, and it cuts the clearing
> bill by the same proportion.** On a mandate defined by buying as little land as possible, that is
> not a stylistic preference. It is the central economic lever.

## Where the ceiling actually is

The ceiling is not skiing ability. Three separate constraints bind, at different angles, and the
lowest one that matters governs.

| Band | Skiing | Slab avalanche | Snowcat | Verdict |
|---|---|---|---|---|
| < 15° | Flat; skating required | None | Trivial | Runout and base only |
| 15–22° | Easy | Negligible | Easy | Usable, unexciting |
| **22–28°** | **Good — solid blue to easy black** | **Low** | **Conventional cat to ~25°** `[E]` | **The target band** |
| 28–34° | Genuinely steep | **Entering the slab band** | **Winch cat only** | Acceptable in *short* pitches |
| 34–45° | Expert | **Prime slab band — peak 35–38°** | Winch, difficult | **Incompatible with the thesis** |
| > 45° | Extreme | Sloughs continuously; less slab | No | Not relevant |

Three notes on that table, because each is a real cost:

1. **The dry-slab avalanche band is 30–45°, peaking around 35–38°** `[P2]` — which is exactly where
   "good steep skiing" lives. Below roughly 30°, slab avalanches are rare.
2. **A conventional snowcat is limited to roughly 25°; a winch cat reaches about 45°** `[E]`. The
   thesis is built on a *used conventional cat*. Terrain above ~28° deletes that and forces a winch
   machine plus top anchors — a large step in CAPEX.
3. **Steep ground holds less snow.** Above ~35–40° snow sloughs rather than accumulating, so the
   steepest terrain simultaneously needs the *most* depth to bury rock and sasa stubble and
   receives the *least*. It works against `D_min`, not for it.

## The constraint that actually decides it

> **This hill will have no patrol, no forecasting, no explosive control, and no closures.** That is
> the thesis, and it is correct on cost. But it means avalanche terrain cannot be managed — only
> avoided.

Commercial areas hold 35° faces open through daily forecasting, hand charges, Gazex and avalaunchers,
and the authority to close terrain. Every one of those is the "expensive resort infrastructure" the
thesis exists to avoid. **You cannot have long steep faces, zero infrastructure, and safety. Two of
the three.**

## But steep is still available — the distinction is size, not angle

This is the part that lets the client have most of what they want.

**An avalanche needs a slab large enough to bury someone.** A 35° pitch that is 50 m long with a
flat bench beneath it cannot produce one. A 33° face 300 m long and 200 m wide certainly can. So:

- **Short steep pitches, broken by benches → acceptable.** Nothing can run far enough to matter.
- **Long continuous steep faces → not acceptable** without control work.
- **Terrain traps decide severity.** A 30° slope draining into a gully or creek bed is far more
  dangerous than a 35° pitch above an open flat, because the trap concentrates debris and buries
  deep. **What is below the slope matters more than the slope.**
- **Convex rollovers are where slabs are triggered** — tension is highest at the convexity. A
  uniform or concave profile is safer at the same angle.
- **Lee aspects load with wind slab.** On a small hill, the ridge-top scour and lee-side deposition
  pattern is predictable and can be designed around when choosing which face to clear.

## The revised specification

Superseding the gradient row in `01-screening/07-mandate-correction.md`:

| Parameter | Old | **Revised** |
|---|---|---|
| Average gradient | 19° | **22–28°** |
| Sustained maximum | "nothing above 33°" | **~30°** for continuous pitches |
| Short pitches | — | **to 38° acceptable if under ~80 m long, benched, with clean runout** |
| Hard exclusion | — | **Long continuous faces 33–40°; any steep slope draining into a gully or creek** |
| Preferred profile | — | **Uniform or concave; avoid large convex rollovers** |
| Snowcat assumption | Conventional | **Conventional — this is what caps sustained pitch at ~28°** |

**Net effect: a 40 ha parcel at 28° yields ~336 m of vertical — above the 吉雪 benchmark — and
needs 35% less clearing than the 19° version to do it.** The client's instinct improves the
economics and the skiing at the same time. It is the avalanche ceiling, not the gradient itself,
that has to be respected, and it binds at around 30° sustained rather than anywhere near the limit
of what is skiable.

## Consequence for the live search

The terrain workstream was briefed to find 250–400 m of relief at ~19° average. **That brief was too
flat and will have been over-rejecting.** Hills dismissed as "too steep" against a 33° cap may be
good candidates; hills accepted as gentle may be too flat to deliver the vertical within the parcel.

Re-screen on: **average 22–28°, sustained pitches ≤ 30°, no long 33–40° faces, no gully runouts.**
