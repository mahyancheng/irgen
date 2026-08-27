# The terrain verification workflow

This is the most operationally useful part of the study: a repeatable process that lets a
buyer's analyst **generate primary data** on a shortlisted property rather than relying on
anyone's recall — including this report's.

## The metrics that matter

Sixteen metrics per property, of which four decide the outcome:

| Metric | Definition | Why it decides |
|---|---|---|
| **`V_ski`** | Vertical between road-accessible base and the highest point **inside the title** | The mandate's core question, expressed numerically |
| **`A_core`** | Contiguous area in the 15–25° band | The terrain that is actually skied and groomed |
| **`A_safe`** | Avalanche-clean fraction, via a **20° alpha-cone test** on the DEM | Determines whether avalanche control is a cost line at all |
| **`D_ski`** | Days with modelled snow water equivalent above **the site's own `D_min`** | **The only metric that combines snow, temperature, elevation and ground cover into one cross-country-comparable figure** |

`D_ski` is the number to compare candidates on. Snowfall totals are not.

## The free data stack

| Purpose | Source |
|---|---|
| Elevation | **Copernicus GLO-30** (global); **LINZ 1 m and 8 m DEM** (NZ); **GSI 基盤地図情報 5 m DEM** (Japan) |
| Cadastre | Free NZ parcel layers via LINZ Data Service; 公図 via 登記情報提供サービス (Japan); Conservador / SII (Chile) |
| Ground roughness | **LCDB v5** — a ready-made land-cover roughness map for New Zealand |
| Snow cover, 25 years | **MODIS `MOD10A1`** |
| Snow trend, 40 years | **Landsat** |
| Snow water equivalent and freezing level | **ERA5-Land** SWE and `deg0l` |
| Processing | QGIS / GDAL, and Google Earth Engine |

## Two traps that will corrupt the analysis

1. **Compute slope on a 15–30 m DEM, not on raw 1 m LiDAR.** High-resolution noise inflates the
   apparent steep fraction and will make safe terrain look dangerous.
2. **Snow-cover duration is not skiable days.** Apply a **20–35 % haircut**, or better, a
   transfer function calibrated against a nearby station.

## The cheapest high-value diligence available

> **Snow stakes plus trail cameras for one season: under US$3,000.**

This is the only site-specific ground truth that will ever exist for an unmonitored property,
and it costs less than a week of legal fees. **Install them the season before committing.**

Alongside it, **scrape ten or more years of daily published base depths** from the nearest
operating areas — Mt Dobson, Ōhau, Roundhill and Fox Peak in New Zealand — which gives a free,
long, local, daily record that no broker will provide.

## Open verification items

| # | Item |
|---|---|
| 1 | **JMA 最深積雪平年値** table — verify normals for every Japanese candidate |
| 2 | **Mt Dobson's summit elevation** — three sources conflict, and the "2,100 m" figure in the original brief was **not corroborated**. Reported base ~1,600 m, summit ~2,030 m, vertical ~305 m |
| 3 | The **Salinger** Cardrona/Treble Cone study — obtain the paper and reconcile its internally inconsistent −8 % / −20 %-by-2040 figures |
| 4 | **NIWA Snow and Ice Network** series (Mueller Hut, Albert Burn, Mahanga, Upper Rakaia, Castle Mount, Philistine) |
| 5 | **SERNAGEOMIN volcanic hazard maps** for any Chilean candidate |
| 6 | **Open a Chilean sourcing workstream** — it ranks first physically and is currently uncovered |
