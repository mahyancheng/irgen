# Snow Reliability, Terrain Suitability & Avalanche Risk — Physical Viability Screen
**Workstream:** the mountain itself (snow, terrain, avalanche). Law/tenure and listings are covered by other analysts.
**Client:** Malaysia-based private buyer. Large alpine landholding where **legal title includes skiable alpine terrain**. Phase 1 = private ski mountain (snowcat, snowmobile, ski touring, possibly a rope tow), minimal CAPEX. Phase 2 = optional commercial resort.
**Prepared:** 27 August 2026

---

## 0. EVIDENCE STATUS — READ THIS FIRST

**This session's live evidence channels were exhausted or blocked before this workstream began.**

| Channel | Status |
|---|---|
| `WebSearch` | ❌ **Session budget fully consumed (200/200) by earlier workstreams before this analyst ran.** Zero searches available. |
| `WebFetch` | ❌ Tested on 4 distinct high-value domains (`www.data.jma.go.jp`, `niwa.co.nz`, `tc.copernicus.org`, `arxiv.org`) — all returned `EGRESS_BLOCKED`. |
| `curl` via agent proxy | ❌ 403 CONNECT denial (organisation egress policy). Proxy log shows ~20 hosts denied this session incl. `en.wikipedia.org`, `www.google.com`, `duckduckgo.com`, `www.bing.com`, `r.jina.ai`. |

**Consequence:** no number in this document was verified against a live source in this session. The tagging below is therefore deliberately conservative and every quantitative claim carries an explicit verification instruction.

### Tag set used in this document
| Tag | Meaning |
|---|---|
| `[PRIMARY-R]` | Recalled from a met-agency or peer-reviewed primary source that I can name. **Source named, value unverified this session.** Treat the *source pointer* as reliable and the *number* as ±. |
| `[SECONDARY-R]` | Recalled from reputable secondary literature / industry sources. Lower confidence on the number. |
| `[INFERENCE]` | My own derivation, calculation or engineering judgement. Explicitly not a citation. |
| `[XWS]` | Cross-workstream — taken from the NZ property analyst's file `nz-properties.md` in this same scratchpad. |
| `[NOT VERIFIED]` | Could not establish; flagged as an open item. |

**Sections 1, 3, 4 and 5 are analytical and are not degraded by the tooling failure** — they are framework, method, and judgement. **Section 2 (regional numbers) is the part that most needs re-verification**, and §7 gives the exact URLs and dataset paths to do it. The §4 workflow is designed so the client's analyst can *generate their own primary data* and never has to rely on my recall at all — that is the intended remedy.

---

## 1. EXECUTIVE SUMMARY — THE TEN DECISION-RELEVANT CONCLUSIONS

1. **A private mountain is governed by different physics-economics than a resort.** A resort needs a *reliable opening date*; a private owner needs *any good window*. This asymmetry lets a private buyer tolerate 2–3× the interannual variance a commercial operator can, which widens the candidate set and lowers the price. Do not screen candidate properties against resort standards.

2. **Ground cover matters as much as elevation, and almost nobody prices it.** Required base depth to ski without grooming ≈ *(height of the dominant roughness element) + 30–40 cm*. That is ~25–30 cm over mown pasture, ~100–150 cm over New Zealand snow tussock, and 200–300 cm over Japanese *sasa* bamboo. **A smooth, grazed, de-rocked slope is skiable on one-third the snow of a tussock slope at the same elevation.** Hard-grazed stations and volcanic ash flanks are therefore worth a large elevation premium.

3. **Summer rock-picking and land-smoothing is the highest-ROI snow intervention available and is not usually thought of as a snow investment.** Dropping area-weighted `D_min` by 40–60 cm typically buys **3–5 additional weeks of season** at no operating cost. `[INFERENCE]` It should be modelled as a CAPEX line before any lift or snowmaking is considered.

4. **Buy terrain that has no avalanche problem, rather than buying terrain and then managing one.** A minimum credible avalanche programme (2 trained forecaster/controllers, explosives licence, magazine, records) is realistically **NZ$150k–400k/yr** `[INFERENCE]`, and a Gazex/Wyssen remote-control installation is a **seven-figure CAPEX** item. Both are categorically incompatible with "minimal CAPEX". §4 gives the DEM test that eliminates this cost line at the *screening* stage.

5. **The terrain that eliminates avalanche cost is also the terrain a private family operation actually wants.** A pole-facing, lee-loaded, open basin at **15–28°** with a rounded (not cliffed) headwall and no confined gullies is ATES Class 0–1, needs no explosives, no forecaster, no insurance loading — and is exactly the beginner-to-strong-intermediate, cat-friendly, flat-light-tolerant terrain a family and guests will ski 90% of the time.

6. **New Zealand has a structural conflict between the snow screen and the title screen.** The snow screen wants a base at **≥1,500–1,600 m**. Tenure review (1998–2022) systematically **freeholded the lower productive country and transferred the alpine tops to the Crown** `[XWS]`. So NZ freehold land is, by construction, mostly below the snow-reliability line. The highest freehold ski terrain identified in NZ is Mt Lyford at a top of **~1,460 m** `[XWS]` — **below** the threshold. This is the single most important finding for the NZ leg and it emerges only by combining the two workstreams.

7. **The NZ precedent for exactly this concept already exists and it used snowcats.** Erewhon Park / Mt Potts operated as an **exclusive private ski field until 2011 with vertical transport by snowcat and helicopter and no lifts**, with a hut at 1,750 m `[XWS]`. That is a direct operational template — and a warning, since it stopped.

8. **Chile 36–39°S is the most under-appreciated candidate on physical grounds.** Volcanic ash/scoria flanks are the smoothest ground cover in the candidate set (`D_min` ~30–50 cm), snow reliability is far better than central Chile's drought-hit 33°S, large private *fundos* reach 1,400–2,400 m, and 600–1,200 m of vertical on private title is achievable. Offsets: active volcanoes, lahar risk, and no wind shelter above treeline.

9. **Japan's constraint is tenure and vertical, never snow.** The efficient Japanese route is a **defunct ski area on 民有地 (private land)** — Japan has lost roughly 200+ ski areas since the early-1990s peak `[SECONDARY-R]`, and a closed area already has cleared, stump-free, graded runs (collapsing `D_min` from ~250 cm over bamboo to ~50–80 cm), a road, and often a power supply.

10. **Two candidate regions should be struck on non-snow physical/legal grounds even though their snow is excellent:** the **Scandinavian fjäll** (*allemansrätten* / *allemannsretten* makes exclusive private use of uncultivated alpine land legally impossible `[PRIMARY-R]` — a fatal flaw for a *private* mountain) and the **BC interior** (world-class snow, but alpine terrain is overwhelmingly Crown land; cat-ski operations hold tenures/licences, not title).

---

## 2. THE SNOW-RELIABILITY SCREENING FRAMEWORK

### 2.1 What the screen must actually answer

> On how many days per season is there enough snow, of adequate quality, over enough **contiguous** terrain in the **right slope band**, on the **right aspects**, **within the legal title**, to ski **without snowmaking and without piste preparation**?

Every word in that sentence is a separate measurable. §6 turns each into a number.

Four physical variables govern it:

| Variable | Why it binds | How to measure (free) |
|---|---|---|
| **Seasonal mean temperature at the base** | Sets whether precipitation falls as snow and whether the pack survives | ERA5-Land 2 m temperature, lapse-corrected to site |
| **Cold-season precipitation** | Sets how much SWE can accumulate | ERA5-Land total precipitation; nearest station |
| **Freezing-level distribution on precipitation days** | Sets rain-on-snow destruction risk | ERA5 `deg0l` (0 °C isothermal level) conditioned on precipitating hours |
| **Wind regime + terrain shelter** | Redistributes 30–60% of the pack; scours ridges, loads lee basins | Winstral–Marks Sx index from DEM + ERA5 wind rose |

### 2.2 The SWE arithmetic — the calculation that anchors everything

Work in **snow water equivalent (SWE)**, not snow depth. SWE is what reanalysis and satellite products give, it is conserved, and depth is a derived quantity that depends on density.

| Snow state | Typical density | 1.0 m depth = |
|---|---|---|
| Fresh, cold, low-density (Hokkaido/Utah) | 60–90 kg/m³ | 60–90 mm SWE |
| Fresh, typical | 80–120 kg/m³ | 80–120 mm SWE |
| Settled mid-winter seasonal pack | **250–350 kg/m³** | **250–350 mm SWE** |
| Spring / ripe isothermal pack | 400–500 kg/m³ | 400–500 mm SWE |

**Working rule `[INFERENCE]`:** *a 1.0 m settled base ≈ 300 mm SWE on the ground.*

**Therefore:** to carry a ≥1.0 m base through a season against melt, sublimation, wind-scour export and rain-on-snow loss, cumulative cold-season precipitation falling as snow must be roughly **2× the target standing SWE**, i.e. **~600 mm w.e. of snowfall in the season** for a 1 m base, **~350–400 mm** for a 60 cm base. `[INFERENCE]`

This gives a fast, defensible first screen from ERA5-Land alone:

> **Screen A (precipitation sufficiency):** cold-season (JJA in SH, DJF–Mar in NH) precipitation at the candidate elevation ≥ **600 mm w.e.** for a tussock/rough site, ≥ **400 mm w.e.** for a smooth/pasture/ash site.
>
> **Screen B (temperature sufficiency):** cold-season mean 2 m temperature at the **base** elevation ≤ **−2 °C** for high confidence; **−2 to 0 °C** acceptable only where precipitation is abundant and the site is pole-facing and lee-loaded; **> 0 °C at the base = reject.**
>
> **Screen C (rain-on-snow):** fraction of cold-season *precipitating hours* with the 0 °C isotherm **above the base elevation** ≤ **15%** good, 15–30% marginal, **>30% reject.** `[INFERENCE — thresholds are my construct]`

Lapse rate for downscaling: use **0.6 °C/100 m** as the environmental default (saturated adiabatic ≈ 0.5, dry adiabatic ≈ 0.98). In strongly inversion-prone continental basins (Central Otago, Kyrgyz Tien Shan, interior Hokkaido) the *winter* lapse rate is often near zero or inverted below the inversion top — **do not blindly lapse-correct valley stations upward in those places**; use the reanalysis free-atmosphere profile instead. `[INFERENCE]`

### 2.3 The "100-day rule" — what it is and where it fails this client

**The rule `[PRIMARY-R — Abegg 1996; adopted in OECD (2007), *Climate Change in the European Alps*, Abegg, Agrawala, Crick & de Montfalcon]`:** a ski area is *snow-reliable* if, in **7 winters out of 10**, there is a snow cover of at least **30 cm** for at least **100 days** between **1 December and 15 April**.

**The derived snow-reliability line `[PRIMARY-R — OECD 2007]`:** in the Swiss Alps that line historically sat at about **1,200 m**, rising to roughly **1,500 m at +1 °C**, **1,800 m at +2 °C**, and **2,100 m at +4 °C** — i.e. approximately **+150 m of elevation per +1 °C** of warming. The same report found the share of Swiss ski areas meeting the criterion falling from ~85% today to ~63% (+1 °C), ~44% (+2 °C) and ~11% (+4 °C). **Verify all six numbers against the OECD 2007 report before using them in an investment paper.**

**Eight reasons the 100-day rule is the wrong screen for this buyer `[INFERENCE]`:**

1. **The 30 cm threshold is calibrated on groomed piste over European alpine *pasture*.** It is a machine-prepared, smooth-ground number. Over NZ tussock it is meaningless — 30 cm of snow on tussock is unskiable tussock-tops.
2. **It assumes grooming.** This client's phase-1 concept is ungroomed or minimally cat-tracked. Ungroomed needs more base, not less.
3. **It ignores snowmaking**, which is how the European industry actually adapted — and which is high-CAPEX, water-rights-dependent and power-hungry, i.e. explicitly out of scope here.
4. **It is a *cover-duration* rule, blind to snow quality.** Rain crust, breakable sun crust, wind slab and unconsolidated depth hoar all count as "snow cover".
5. **It has no wind term.** In New Zealand and Patagonia, above-treeline operations lose more days to *wind* than to lack of snow. `[SECONDARY-R]`
6. **It is binary at the whole-resort scale.** Viability is elevation-band-resolved: the same property can be reliable at 1,900 m and hopeless at 1,300 m.
7. **The 1 Dec – 15 Apr window is Northern-Hemisphere-specific** and must be translated (SH: ~1 June – 15 Oct; Japan: ~15 Dec – 10 Apr).
8. **It says nothing about whether the days fall in the demand window.** New Zealand's deepest snowpack typically arrives in **late September–October**, *after* the July–September holiday peak — a structural mismatch. `[SECONDARY-R]`

### 2.4 The replacement screen for a private mountain: the **"60 / 80 / 1.0" rule**

`[INFERENCE — my construct, offered as the operative standard for this mandate]`

> A property qualifies as a **private ski mountain** if, in **8 seasons out of 10**, it carries a settled base of **≥1.0 m** (≈300 mm SWE, or the site-specific `D_min` from §2.6 if lower) over **≥60% of the primary skiable envelope** for **≥60 days**, and that period contains at least one **contiguous 3-week block**.

The three parameters are deliberate:
- **8-in-10, not 7-in-10** — because a private owner flying from Kuala Lumpur cannot easily re-plan; a 30% failure rate is intolerable at *trip* scale even though it is tolerable at *business* scale.
- **60 days, not 100** — because there is no season-pass revenue to defend and no fixed opening date to hit.
- **1.0 m / site `D_min`, not 30 cm** — because there is no grooming and (in NZ) no smooth ground.
- **The contiguous 3-week block** is the operationally binding term. It is what makes the property *usable* rather than merely *sometimes snowy*, and it is the term most candidate properties fail.

**For a boutique commercial phase 2**, revert to something close to the classic rule but harden the date: **≥100 operating days in ≥7 of 10 seasons, AND reliably open by a fixed calendar date** (NZ: ~1 July for the school-holiday block; Japan: ~20 December for the New Year block; Chile: ~15 July for *Fiestas Patrias*/holiday demand). The fixed date, not the day count, is what kills marginal commercial areas.

### 2.5 Operating-day requirements

| Operation type | Days/season needed | Notes |
|---|---|---|
| **Absolute floor — credible private mountain** | **40–50** skiable days with one contiguous ≥21-day block | Below ~30 days you own a "sometimes ski" property, not a ski mountain. `[INFERENCE]` |
| **Comfortable private family/club target** | **80–110** | Matches what NZ club fields actually achieve. `[SECONDARY-R]` |
| **Boutique commercial (lodge + cat)** | **100–120**, with a reliable opening date | The date reliability binds harder than the count. `[INFERENCE]` |
| **Full commercial resort** | **120–150+** | Out of scope for phase 1. |

**Observed comparators `[SECONDARY-R — verify]`:** NZ commercial fields typically run ~90–120 days (roughly late June to early October); NZ club fields shorter and more weather-dependent. Japan: ~120–150 days. Colorado: ~130–170 days. BC interior: ~140–170 days. Northern Scandinavia: 150–200 days but with a December daylight problem.

### 2.6 Base depth by ground cover — **the most under-priced variable in the screen**

**Rule `[INFERENCE, physically grounded]`:**
> **Minimum base depth to ski without piste preparation ≈ (height of dominant roughness element) + 30–40 cm working layer.**

The working layer exists because (a) you must not contact the roughness elements at speed, (b) the top 20–30 cm is the layer that actually gets skied and redistributed, and (c) skier compaction locally reduces depth by 20–40%.

| Ground cover | Roughness height | Min base to **ski** | Min base for **snowcat** | Min base to be **good** |
|---|---|---|---|---|
| Mown pasture / smooth improved grass | 5–15 cm | **25–30 cm** | 30–40 cm | 50 cm |
| Short alpine turf / herbfield / grazed sward | 10–20 cm | **30–40 cm** | 40–50 cm | 60 cm |
| **Volcanic ash / scoria (Chilean & Japanese cones)** | 5–20 cm | **30–50 cm** | 40–60 cm | 70 cm |
| Cleared, stumped, graded ski run (defunct ski area) | 10–25 cm | **40–60 cm** | 50–70 cm | 80 cm |
| Rough pasture with scattered rock | 20–40 cm | 60–80 cm | 80–100 cm | 120 cm |
| Moraine / blocky ground / scree | 30–60 cm | **80–120 cm** | 100–150 cm | 150 cm+ |
| **NZ snow tussock (*Chionochloa rigida / macra*)** | 60–100 cm | **100–150 cm** | 120–180 cm | **200 cm** |
| Matagouri / *Dracophyllum* / low scrub | 50–150 cm | 150–250 cm | 200 cm+ | avoid |
| **Japanese *sasa* bamboo (笹)** | 100–200 cm | **200–300 cm** | 250 cm+ | Japan only manages this because depths reach 3–5 m |
| Mature forest floor / glades (deadfall) | 20–40 cm | 60–100 cm | n/a (tour/ski only) | 120 cm |
| Boulder field / talus / *lenga* krummholz | 100 cm+ | 200 cm+ | reject | reject |

**Why this table is the most commercially important thing in the document:**

- **It reprices elevation.** A smooth, hard-grazed slope at 1,400 m can be skiable more days per year than a tussock slope at 1,650 m, because it converts a much larger fraction of the season's snowfall into skiable days. Screening on elevation alone will systematically misrank candidates.
- **It explains New Zealand's snow reports.** NZ fields quote 1.0–1.5 m as "good" where a European resort opens on 40 cm. That is not conservatism — it is *Chionochloa*. It is also why NZ fields cannot open early on a thin base.
- **It identifies the cheap intervention.** Summer rock-picking, boulder removal, hollow-filling and light smoothing on the primary runs reduces `D_min` by **40–60 cm**, worth **3–5 weeks of season**. `[INFERENCE]` Cost must be quoted locally against agricultural land-development contract rates; budget it as a snow investment, not as farm development.
- **It creates a non-obvious acquisition preference:** land that has been **hard-grazed for a century** (classic NZ high-country stations, Chilean *fundos*, Patagonian *estancias*) is often **smoother and less tussocky** than adjacent ungrazed conservation land. Retired/de-stocked conservation land reverts to tall tussock and scrub and gets *worse* for skiing over time. Grazing history is a snow variable.
- **Tussock cuts both ways.** Before burial it is a hazard (edge-catching, base damage, unskiable). *After* burial it is an asset: it anchors the snowpack against wind scour and strongly suppresses full-depth **glide** avalanches — which are, conversely, a real hazard on very smooth grass. `[INFERENCE]`

**Snowcat / snowmobile ground-pressure notes `[SECONDARY-R / INFERENCE — verify with vendor specs]`:**
- A tracked groomer (PistenBully 100/400, Prinoth Husky) exerts roughly **0.05–0.07 kg/cm²** — comparable to a person on skis. Depth is not limited by flotation but by **what the tracks, blade and tiller hit**. Over smooth ground a cat works on ~30–40 cm; over rock it needs 100–150 cm or it destroys grousers and tiller teeth.
- Snowmobiles need less depth (~20–30 cm smooth, 60 cm+ rough) but are poor guest-uphill devices — they carry 1–2 people, are noisy, and cannot make a track for others.
- **For a private mountain the realistic uphill machine is a used groomer or a Tucker Sno-Cat with a passenger cabin**, not a fleet of snowmobiles.
- **Cat uphill economics:** a groomer climbs roughly **500–700 m vertical in 20–30 minutes** on a prepared skin/road line. Realistically **4–8 laps/day**. So **400 m vertical × 6 laps = 2,400 m/day**, comparable to a modest lift day. This is why 300–500 m of vertical is acceptable for phase 1 and why the road/skin line up the hill is as important an asset as the runs.

### 2.7 Aspect

**Southern Hemisphere (NZ, Chile, Argentina):** pole-facing = **south**. Optimum band **SE (135°) → S (180°) → SSW (202°)**; acceptable **E (90°) → SW (225°)**; **reject N (360°/0°) ± 45°**.

**Northern Hemisphere (Japan, Rockies, BC, Caucasus, Tien Shan, Türkiye):** mirror. Optimum **NE (45°) → N (0°) → NNW (337°)**; acceptable **NW (315°) → E (90°)**; reject S ± 45°.

**Two effects stack, and the second is usually forgotten:**

1. **Radiation.** At ~44° latitude a 25° pole-facing slope receives roughly **40–55%** of the mid-winter insolation of an equator-facing slope of the same angle `[INFERENCE — standard slope-insolation geometry; compute exactly for the site with a solar-radiation model in QGIS/GRASS `r.sun`]`. That is worth weeks of snow-lie.
2. **Lee loading.** Snow is redistributed, not just deposited. Where the prevailing storm wind and the pole-facing aspect **coincide on the lee side**, depth can be **1.5–3× the areal average**. `[INFERENCE]`

| Region | Prevailing winter storm wind | Lee (loaded) aspects | Pole-facing aspects | **Coincidence?** |
|---|---|---|---|---|
| **NZ Southern Alps** | W–NW (nor'wester / föhn) | E, SE | S, SE | ✅ **SE is the double optimum** — and this is exactly where NZ club fields sit |
| **Japan Sea-of-Japan side** | NW (Siberian monsoon) | SE, E | N, NE | ⚠️ partial — **E/NE cirques** are the compromise, and are where Japanese ski areas sit |
| **Chile 36–40°S** | W–NW (westerlies) | E, SE | S, SE | ✅ **SE double optimum**, same as NZ |
| **Colorado** | W–NW | E, NE | N, NE | ✅ **NE is the double optimum** |
| **Caucasus (Georgia)** | W / SW | E, NE | N, NE | ✅ NE |

**Screening rule `[INFERENCE]`:** at least **60% of the intended skiable envelope should lie in the optimum-plus-acceptable aspect band**, and the single best sub-basin should be **pole-facing AND lee-loaded**.

**The most valuable single landform on a marginal-elevation property is a lee-side, pole-facing cirque or basin at 15–28°.** It concentrates radiation shelter, wind loading and safe slope angle in one place. It is why NZ club fields, Japanese ski areas and Chilean volcano fields all look, from a DEM, like the same object.

### 2.8 Slope angle

Percent grade = tan(angle): 6° = 11%, 15° = 27%, 25° = 47%, 30° = 58%, 35° = 70%, 45° = 100%.

| Band | Classification | Role on a private mountain | Avalanche |
|---|---|---|---|
| **0–6°** | Flat / runout / cat track / base area | Necessary but not skiable as a run (requires poling) | Runout & deposition zone — can still be *hit* |
| **6–15°** | Beginner ("green") | Learning terrain, family, cat road | Effectively none as a start zone |
| **15–25°** | **Intermediate ("blue") — the money band** | **The core of the property.** Best snow retention, best in flat light, cat-groomable, tour-friendly | Essentially none as a start zone |
| **25–30°** | Advanced-intermediate | Adds interest without adding avalanche cost | Rare; wet-slab and **glide** possible on smooth ground |
| **30–35°** | Advanced | **The threshold. Avalanche starting-zone territory begins at 30°** | Yes |
| **35–45°** | Expert | **Peak slab-avalanche frequency, mode ≈ 36–39°** `[PRIMARY-R — standard avalanche literature; Schweizer/McClung & Schaerer]` | **Maximum** |
| **>45°** | Extreme | Snow sluffs continuously, deep slabs rarely build | High consequence, lower frequency |

**Three points beyond difficulty grading `[INFERENCE]`:**
- **Slope angle is also a snow-retention variable.** >40° sheds snow continuously; <8° needs *more* depth to be skiable because you cannot generate speed over roughness.
- **Convexities are doubly bad** — they are both the classic slab trigger point and the most wind-scoured part of a slope.
- **Concavities (gullies, cirque floors, bowl bottoms) accumulate** — but confined gullies are terrain traps that turn a small slide into a burial. Prefer **broad, open concavity** (a basin) over **confined concavity** (a gully).

### 2.9 Vertical drop thresholds

| `V_ski` (continuous fall-line vertical within title, 6–30°) | Verdict |
|---|---|
| **< 150 m** | **Reject.** Laps too short; cat-skiing pointless; a rope-tow hill at best. |
| 150–300 m | Viable family hill / rope tow. Cat lap gives a 2–4 minute descent. |
| **300–500 m** | **Sweet spot for a low-CAPEX private mountain.** |
| 500–800 m | Excellent — supports real cat-ski economics and a boutique phase 2. |
| > 800 m | Commercial-grade. |

### 2.10 Minimum reliable base and top elevation, by setting

`[INFERENCE, calibrated on the OECD line + latitude/continentality reasoning + recalled ski-area elevations. Every row should be re-derived from ERA5-Land for a specific candidate — see §6.]`

| Setting | Lat. | **Min. reliable BASE (today)** | Preferred TOP | Binding constraint |
|---|---|---|---|---|
| European Alps, continental interior | 46–47°N | **1,500 m** (1,800 m by ~2050) | 2,500 m+ | Warming; the OECD 1,200 m line is now historic |
| **NZ inland/continental** (Two Thumb, Ben Ōhau, Pisa, Old Woman, Dunstan) | 43–45°S | **1,500–1,600 m** | 2,000–2,200 m | **Tussock `D_min`; wind; NW föhn.** NZ treeline is only ~1,000–1,400 m and eastern ranges are largely treeless |
| NZ maritime W / Kaikōura / Nelson | 41–44°S | **1,600 m+** | 2,000 m+ | Rain-on-snow — *higher* base needed despite more precipitation |
| **Japan Hokkaido** | 42–44°N | **200–400 m** | 1,000–1,300 m | **Vertical, not snow.** Annupuri 1,308 m; Yōtei 1,898 m; Asahidake 2,291 m |
| **Japan Honshū Sea-of-Japan** | 36–39°N | **500–700 m and rising** | 1,500–2,000 m | Rain risk at the base is rising fast |
| Chile/Argentina 32–35°S | 32–35°S | **2,500–2,800 m** | 3,300–3,600 m | Megadrought + extreme variance |
| **Chile 36–40°S** | 36–40°S | **1,300–1,600 m** | 1,800–2,400 m | Rain at base; volcanic hazard |
| US Rockies — Colorado | 37–40°N | 2,400–2,900 m | 3,500–4,000 m | Federal land tenure |
| US Rockies — MT/WY | 44–46°N | 1,800–2,100 m | 2,800–3,400 m | Federal land tenure |
| BC interior (Columbias) | 49–52°N | 1,100–1,500 m | 2,000–2,500 m | **Crown land** |
| Scandinavian fjäll | 62–69°N | 400–700 m | 900–1,400 m | Vertical; darkness; **right-to-roam** |
| Caucasus (Georgia) | 42–43°N | 1,600–2,000 m | 3,000–3,300 m | Avalanche; access; geopolitics |
| Tien Shan (Kyrgyzstan) | 42°N | 2,000–2,300 m | 3,000–3,500 m | Continental depth hoar; foreign-ownership limits |
| Türkiye — Erzurum/Palandöken | 39–40°N | 1,900–2,200 m | 2,800–3,200 m | Foreign-ownership area caps |
| Türkiye — Kaçkar (Black Sea) | 40–41°N | 1,500 m | 3,000–3,900 m | Access; foreign-ownership caps |

**Latitude heuristic `[INFERENCE]`:** in the mid-latitudes the winter snow line falls roughly **100–150 m per degree of latitude poleward**. Use it only to interpolate between the rows above, never as a substitute for reanalysis at the site.

---

## 3. REGIONAL SNOW DIAGNOSTICS

> ⚠️ **Every number in §3 is recalled, not verified this session** (see §0). Values are given with the source that should be used to confirm them. Confirm before any number reaches an investment paper.

### 3.1 NEW ZEALAND — SOUTH ISLAND

#### 3.1.1 Ski-area elevation reference (the calibration set)

| Area | Range / region | Base (m) | Top (m) | Vertical (m) | Aspect | Tag |
|---|---|---|---|---|---|---|
| **Mt Dobson** | Two Thumb, Mackenzie | **1,600** (car park cited **1,725–1,740**, "highest ski-field parking in NZ") | **2,030** | **~305** | S–SE bowl | `[XWS]` — sources conflict; **the brief's "top 2,100 m" was not corroborated** |
| **Roundhill** | Two Thumb / Tekapo | ~1,350 | ~2,133 (top of the "Heritage Express" rope tow) | ~780 (claimed NZ's largest) | SE | `[SECONDARY-R]` **verify** |
| **Ōhau Snow Fields** | Ben Ōhau Range | ~1,425 | ~1,825 | ~400 | **S/SE** | `[SECONDARY-R]` verify |
| **Fox Peak** | Two Thumb | ~1,500 | ~1,900 | **580** | S–SE | vertical `[XWS]`; elevations `[SECONDARY-R]` |
| **Mt Hutt** | Canterbury front range | ~1,450 | ~2,086 | ~683 | W/SW (atypical) | `[SECONDARY-R]` verify |
| **Craigieburn Valley** | Craigieburn Range | ~1,564 | ~1,978 | ~415 | SE | `[SECONDARY-R]` verify |
| **Broken River** | Craigieburn | ~1,400 | ~1,830 | ~430 | SE | `[SECONDARY-R]` verify |
| **Temple Basin** | Arthur's Pass | ~1,350 | ~1,900 | ~550 | S/SE | `[SECONDARY-R]` verify |
| **Mt Olympus** | Craigieburn | ~1,455 | ~1,860 | ~405 | SE | `[SECONDARY-R]` verify |
| **Porters** | Craigieburn | ~1,280 | ~1,980 | ~700 | SE | `[SECONDARY-R]` verify |
| **Treble Cone** | Harris Mtns, Wanaka | ~1,260 | ~1,960 | **~700** | S/SE | `[SECONDARY-R]` verify |
| **Cardrona** | Pisa/Cardrona | ~1,260 | ~1,936 | ~680 | S/SE | `[SECONDARY-R]` verify |
| **Mt Lyford** ⭐ | Inland Kaikōura / Hurunui | ~1,150 | **~1,460** (Mt Lyford peak 1,516) | ~310 | — | `[XWS]` — **the highest FREEHOLD ski terrain identified in NZ** |
| **Erewhon / Mt Potts** | Ashburton headwaters | — | hut at **1,750** | — | — | `[XWS]` — **ran as an exclusive private field to 2011 on snowcat + heli, no lifts** |
| Snow Farm / Waiorau (nordic) | Pisa Range | ~1,500–1,600 | ~1,700 | — | plateau | `[SECONDARY-R]` — a genuinely relevant *private snow business* precedent |
| Awakino | St Marys Range, Waitaki | ~1,300 | ~1,600 | — | — | `[SECONDARY-R]`; land is Oteake Conservation Park `[XWS]` |

**Calibration takeaway `[INFERENCE]`:** the NZ operating set clusters at **base 1,250–1,600 m, top 1,830–2,133 m, vertical 300–780 m**, with **S–SE aspect near-universal**. Mt Dobson's ~1,600 m base is the highest and it is treated in NZ as the reliability benchmark. **A candidate NZ property with a base below ~1,400 m should be presumed unreliable unless the DEM/ERA5 work in §6 proves otherwise.**

#### 3.1.2 The six New Zealand physical problems

1. **Rain-on-snow.** The 0 °C isotherm regularly exceeds 2,000 m in NZ mid-winter during NW flow. **No NZ elevation fully escapes rain** — you screen on *frequency*, not absence. `[SECONDARY-R]`
2. **Nor'west föhn.** Warm, dry, violent downslope gales east of the Main Divide. They destroy snow by sublimation and scour as well as by melt, and they close ski fields. **NZ fields lose more operating days to wind than to any other cause.** `[SECONDARY-R]`
3. **Wind scour above treeline.** NZ treeline is only ~1,000–1,400 m and the eastern ranges are largely treeless tussock (partly a post-Polynesian fire legacy). There is **no forest to anchor snow** in the operating elevation band. Ridges and convexities strip; lee basins load. This makes the Sx/lee-loading analysis in §6 unusually valuable in NZ.
4. **Thin, late, variable early season.** The pack builds late; **peak SWE is typically late September–October at high elevation — after the July–September demand peak.** `[SECONDARY-R]` A structural mismatch for commercial use, but **much less of a problem for a private owner who can simply schedule the trip for the peak.** This is a genuine private-buyer advantage.
5. **Tussock.** `D_min` ≈ 100–150 cm (§2.6). The dominant reason NZ needs deep bases.
6. **Interannual variability driven by SAM and ENSO.** Broadly, **El Niño** winters bring more SW flow and better South Island snow; **La Niña** brings warmer NE flow and poorer seasons. The **Southern Annular Mode** modulates storm-track latitude. `[SECONDARY-R]`

#### 3.1.3 Which NZ ranges are most snow-reliable, and why

| Range | Reliability | Why `[INFERENCE from the physics + the calibration set]` |
|---|---|---|
| **Two Thumb Range** (Mt Dobson, Fox Peak, Roundhill) | ⭐ **Best in NZ** | Highest base elevations in the country; sits in the **rain shadow east of the Main Divide** so lower rain-on-snow frequency; cold and continental. Trade-off: **less precipitation**, so it depends on getting the storms it does get. |
| **Ben Ōhau Range** (Ōhau) | ⭐ Very good | Strong S-facing aspect, good elevation, moderately continental, close enough to the divide for precipitation. |
| **Pisa / Old Woman / Old Man / Dunstan / Hector (Central Otago)** | Good | Cold, continental, high plateaux (Mt Pisa 1,963 m `[XWS]`; Old Man Range 1,690 m `[XWS]`). **Driest of the candidates** — low `D_min` ground would matter a lot here. Snow Farm proves a private snow business works on the Pisa Range. |
| **Craigieburn Range** | Good | High bases (1,400–1,560 m) and closer to the divide so more precipitation — but **more wind and more rain-on-snow.** |
| **Harris / Cardrona (Wanaka)** | Good but lower base | Big vertical, good aspects; bases at ~1,260 m are the weak point. |
| **Inland Kaikōura / Seaward Kaikōura** | Marginal | Tapuae-o-Uenuku reaches 2,885 m, but access is brutal and the operating band (Mt Lyford ~1,150–1,460 m) is **too low and too maritime.** Warming will hit this first. |
| **West Coast / maritime divide** | ❌ Reject | Enormous precipitation but the freezing level is too high, terrain too steep and glaciated. |

**→ NZ verdict on physical grounds:** the **Mackenzie Basin ranges (Two Thumb, Ben Ōhau, Dalgety, Hall) at 1,500–2,100 m** are the sweet spot: highest bases in NZ, rain-shadowed, cold, S–SE aspects, and rolling tussock basins rather than glacially-carved cliff terrain (i.e. naturally **low avalanche exposure**).

#### 3.1.4 ⚠️ THE NEW ZEALAND STRUCTURAL CONFLICT

**Combining this workstream with the tenure workstream produces the decisive NZ finding:**

- The **snow screen** requires a base at **≥1,500–1,600 m**.
- **Tenure review (Crown Pastoral Land Act 1998, run 1998–2022) systematically freeholded the lower productive country and transferred the alpine tops to the Crown as conservation land** `[XWS]`. Documented: Earnscleugh — 8,060 ha to the Crown, "mostly the higher altitude land"; Godley Peaks — 11,875 ha to the Crown vs 2,676 ha freeholded `[XWS]`.
- **Tenure review is now closed** (Crown Pastoral Land Reform Act 2022) — there is no pathway to convert alpine leasehold to freehold `[XWS]`.
- Therefore **NZ freehold land is, by construction, disproportionately below the snow-reliability line.** The highest freehold ski terrain identified in NZ tops out at **~1,460 m** (Mt Lyford) `[XWS]` — below the threshold, in a maritime coastal range, and the most warming-exposed part of the NZ set.

> `[INFERENCE]` **In New Zealand the snow screen and the title screen are close to mutually exclusive, and this is not an accident of the market — it is the direct result of a 24-year government policy that deliberately separated them.** Any NZ candidate that appears to satisfy both is either (a) rare pre-tenure-review freehold high country, (b) a station where the tops were never Crown leasehold, or (c) mis-described. Each of those must be tested against the actual title, not the marketing.

#### 3.1.5 NIWA Snow and Ice Network (SIN) — the primary NZ dataset

`[PRIMARY-R — source pointer reliable; station elevations approximate and unverified]`

NIWA operates the **Snow and Ice Network (SIN)** — automatic alpine snow-weather stations measuring **snow water equivalent (snow pillow / scale), snow depth, temperature, radiation and precipitation**. Named stations in the brief, with my best recall of elevation:

| Station | Region | Approx. elev. | Character |
|---|---|---|---|
| **Mueller Hut** | Aoraki/Mt Cook | ~1,818 m | Maritime, very high accumulation; among the highest peak SWE in the network |
| **Albert Burn** | Otago (Hāwea/Wanaka hinterland) | ~1,280 m | Lower, drier, more marginal |
| **Mahanga** | St Arnaud Range, Nelson Lakes | ~1,940 m | Northern South Island |
| **Ivory Glacier** | West Coast | ~1,400 m | Maritime extreme |
| **Upper Rakaia** | Canterbury headwaters | ~1,750 m | Divide-adjacent |
| **Castle Mount** | Canterbury | ~1,400 m | Inland |
| **Philistine** | Arthur's Pass | ~1,650 m | Divide, high precipitation |

**Actionable regardless of my recall:** SIN is the **single best free primary dataset for an NZ property screen**, and NIWA supplies station time series on request (bulk data is chargeable). **Instruction to the client's analyst: request the full SWE and snow-depth records for Albert Burn, Castle Mount and Upper Rakaia** — these are the three closest analogues in elevation and continentality to a Mackenzie/Central Otago candidate — **and regress them against the ERA5-Land grid cell to build a site transfer function** (method in §6.5). NIWA also runs a national **snow model** whose gridded output is the right thing to ask for if the property is far from a SIN station.

**Also free and useful:** NIWA **CliFlo** (national climate database, free registration) for long station records; **NZ Avalanche Advisory** (avalanche.net.nz, run by the NZ Mountain Safety Council) for regional forecasts and an observation archive.

#### 3.1.6 New Zealand climate projections

- **As supplied in the client brief** `[SECONDARY — brief-supplied, NOT independently verified this session]`: a Salinger study of Cardrona/Treble Cone projecting **−5% snow depth by 2030, −8% by 2040, and −20% under 1.5 °C warming by 2040.** ⚠️ The −20%-by-2040-at-1.5 °C figure is far larger than the −8%-by-2040 figure and the two are only reconcilable as different scenarios; **obtain the paper and check which scenario each belongs to before quoting.**
- **Hendrikx & Hreinsson and colleagues, NZ seasonal snow modelling** `[SECONDARY-R]`: projected reductions in snow duration are **strongly elevation-dependent**, with large losses (tens of days) at **1,000–1,500 m** and materially smaller losses above ~1,800 m by late century under high emissions. **The shape of the result — high sites are relatively resilient, low sites collapse — is the robust finding and is the one that matters for acquisition.** `[INFERENCE]`
- **Practical implication `[INFERENCE]`:** buy elevation headroom, not marginal elevation. On a 30–50 year hold, the difference between a 1,400 m base and a 1,700 m base is not 300 m — it is the difference between an asset that degrades gracefully and one that fails inside the hold period. Apply the OECD **+150 m per +1 °C** rule to the intended holding period and require the base to sit **above the projected line at the end of the hold, not the start.**

---

### 3.2 JAPAN

#### 3.2.1 Why Japan gets extreme snow at low elevation

`[PRIMARY-R — standard JMA / meteorological description]`

In winter the **Siberian High** drives a cold, dry **NW monsoon** across the **Sea of Japan**. Sea-surface temperature is ~10–15 °C while the 850 hPa air is −10 to −20 °C. The resulting sensible and latent heat fluxes destabilise the boundary layer, generate **convective snow bands**, and organise the **JPCZ (Japan Sea Polar-air-mass Convergence Zone)**. The airmass then hits the Sea-of-Japan-side mountains and is **orographically forced**. The result is the heaviest snowfall in the world at this latitude and elevation — Japan gets at 300 m what the Alps get at 2,000 m.

**Two consequences that matter for acquisition `[INFERENCE]`:**
- The snow is **wet-ish by continental standards** and the depths are so large that **`D_min` over sasa bamboo (200–300 cm) is actually achievable** — Japan is the only candidate region where that is true.
- Because the mechanism is a **sea-surface-temperature-driven heat flux**, a warming Sea of Japan initially *increases* moisture supply while raising the rain/snow line. Hence the observed pattern: **snowfall holding up or increasing at high elevation while collapsing at low elevation.** This is the key structural risk.

#### 3.2.2 Normal annual maximum snow depth (最深積雪平年値)

⚠️ **ALL VALUES BELOW ARE RECALLED AND UNVERIFIED — `[SECONDARY-R]`.** Confirm every one against JMA 平年値 (1991–2020 normals) at `https://www.data.jma.go.jp/obd/stats/etrn/` (過去の気象データ検索 → 平年値 → 最深積雪).

| Station | Pref. | Approx. elev. | **Normal annual max snow depth** | Record max | Note |
|---|---|---|---|---|---|
| **酸ヶ湯 Sukayu** | Aomori | ~890 m | **~380–400 cm** | **~566 cm (Feb 2013)** | ⭐ **The deepest official station in Japan** |
| **肘折 Hijiori** | Yamagata | ~330 m | ~290–320 cm | ~445 cm (Feb 2018) | Extraordinary depth for the elevation |
| **守門 Sumon** | Niigata | ~380 m | ~280–320 cm | — | |
| **大井沢 Ōisawa** | Yamagata | ~330 m | ~280–300 cm | — | |
| **津南 Tsunan** | Niigata | ~450 m | ~250–290 cm | ~416 cm | |
| **十日町 Tōkamachi** | Niigata | ~100–200 m | ~190–220 cm | ~391 cm (1981) | Lowland — the most warming-exposed |
| **野沢温泉 Nozawa Onsen** | Nagano | ~600 m (village) | ~180–220 cm | — | Far more on the upper mountain |
| **朱鞠内 Shumarinai (幌加内 Horokanai)** | Hokkaido | ~280 m | ~180–200 cm | — | Japan's **cold pole** — −41.0 °C, 1978, lowest official Japanese temperature `[PRIMARY-R]` |
| **倶知安 Kutchan** | Hokkaido | ~170 m | ~180–190 cm | — | Niseko base area |
| **白馬 Hakuba** | Nagano | ~700 m (village) | ~120–150 cm | — | Happō-One upper mountain (to ~1,830 m) far deeper |

**Reading the table `[INFERENCE]`:** the *Honshū Sea-of-Japan side* (Aomori, Yamagata, Niigata) delivers **2–3× the depth of Hokkaido at comparable or lower elevation.** Hokkaido's reputation rests on snow *quality* and *reliability*, not depth. That distinction drives the acquisition logic below.

#### 3.2.3 The elevation / latitude trade-off

| | **Hokkaido (42–44°N)** | **Honshū Sea-of-Japan side (36–39°N)** |
|---|---|---|
| Temperature | Cold and reliable; low rain risk | Warmer; **rain to 800–1,000 m now occurs mid-winter** |
| Snow depth | Moderate (180–200 cm normals at low stations) | **Extreme (250–400 cm normals)** |
| Snow quality | Dry, consistent powder | Heavier, more variable, more rain crust |
| Mountain height | **Low** — Niseko Annupuri 1,308 m; Yōtei 1,898 m; Asahidake 2,291 m | **High** — Northern Alps to ~2,900 m; Myōkō 2,454 m; Naeba 2,145 m |
| **Vertical available** | **Poor** — short, and the high ground is national forest/park | **Better** — 500–1,000 m physically present |
| Warming trend | **Least-bad in Japan**; some projections show little change at altitude to 2050 | **Poor at low elevation; severe below ~800 m** |

#### 3.2.4 The real Japanese constraint is tenure, not snow

`[SECONDARY-R / INFERENCE — this intersects the legal workstream; flagged because it is the binding *physical availability* constraint]`

Japanese high ground with 500 m+ of vertical is overwhelmingly:
- **国有林 (national forest)**, administered by the **林野庁 (Forestry Agency)**; or
- inside **国立公園 / 国定公園** under the **自然公園法 (Natural Parks Act)**, with special-zone restrictions on clearing and construction; or
- **保安林 (protection forest)** under the Forest Act, where felling and land-form change are restricted.

**A single 民有 (private) title spanning 500 m+ of vertical with road access and reliable snow is rare.**

> ⭐ **THE EFFICIENT JAPANESE ROUTE — DEFUNCT SKI AREAS.** Japan had roughly **700 ski areas at the early-1990s peak and now has on the order of 450–500; 200+ have closed** `[SECONDARY-R — verify against 日本生産性本部『レジャー白書』or 全国スキー場活性化協議会 data]`. A closed area typically offers, in one package:
> - **cleared, stumped, graded runs** — which collapses `D_min` from ~250 cm (over sasa) to **~50–80 cm**, the single biggest snow-economics lever available anywhere in this study;
> - an **existing access road** built for buses, already engineered for winter;
> - **existing power supply and often a lodge**;
> - frequently a **mix of 民有林 and municipal land** that a motivated buyer can consolidate;
> - a **municipality that wants the problem solved**, which is the difference between a 5-year and a 15-year approvals path.
>
> **Screening filter for Japan:** defunct area, Sea-of-Japan side, **base ≥700 m, top ≥1,300 m**, on 民有地, within ~2.5 h of a Shinkansen station. Find them with **GSI 地理院地図 historical aerial photography (1960s–80s)** — old cleared runs are unmistakable from the air and persist for decades (see §6.7).

#### 3.2.5 Japanese climate projections

`[SECONDARY-R — verify against 文部科学省・気象庁『日本の気候変動2025』(or the current edition) and 気象庁『気候変動監視レポート』]`

- Projections show **large decreases in maximum snow depth on the Sea-of-Japan side of eastern and western Japan**, concentrated at **low elevation**.
- Under high-end warming, **near-total loss of seasonal snow cover in the lowlands of western Japan**, with the largest *absolute* decreases in the Niigata/Tōhoku lowlands (because that is where the snow is today).
- **Some studies project little change or even local increases at the highest elevations of northern Honshū and interior Hokkaido** under moderate warming — more atmospheric moisture, still below freezing. `[SECONDARY-R]`
- **Acquisition implication `[INFERENCE]`:** the projected pattern is a **squeeze from below**. Everything the buyer should want in Japan sits **above ~900–1,000 m**, and the 250–400 cm normals at 300–500 m stations, spectacular as they are, describe **exactly the elevation band that is projected to fail.** Do not buy a Japanese property on the strength of a low-elevation station normal.

---

### 3.3 CHILEAN AND ARGENTINE ANDES

#### 3.3.1 Central Chile (32–35°S) — the megadrought

`[PRIMARY-R — Garreaud et al. (2017), "The 2010–2015 megadrought in central Chile", *Hydrology and Earth System Sciences*; Garreaud et al. (2020), *International Journal of Climatology*. Source pointers reliable; verify the numbers.]`

- Central Chile has been in an uninterrupted **"megadrought" since 2010** — the longest and most severe in the instrumental record — with sustained mean precipitation deficits on the order of **25–30%**.
- Andean **snow cover and snowpack at 30–37°S have declined markedly**; snow-cover duration has shortened and the snow line has risen. 2019 and 2021 were extreme years in which the Santiago-region resorts (Valle Nevado, La Parva, El Colorado) had near-catastrophic seasons. `[SECONDARY-R]`
- **Interannual variance at 33°S is the worst in the entire candidate set.** Santiago-region annual precipitation has a coefficient of variation of roughly **40–50%**, and Andean **peak SWE variability is higher still — plausibly CV ≈ 45–60%.** `[SECONDARY-R / INFERENCE — verify against Masiokas et al. (2006, 2020) Andean snowpack reconstructions and the CR2 Explorador Climático]`
- Variability is strongly **ENSO-coupled**: **El Niño → wet and snowy** in central Chile; **La Niña → dry**. `[PRIMARY-R — Masiokas et al.]`

> `[INFERENCE]` **A CV near 50% means a private mountain at 33°S is close to a coin-flip each season.** Against the "8-in-10 seasons" standard of §2.4, **central Chile fails**, and it fails for a reason (a multi-decadal drying trend consistent with poleward-shifted westerlies) that is expected to persist. **Reject 32–35°S.**

#### 3.3.2 The reliable band — Chile/Argentina 36–40°S

Further south the westerlies deliver far more consistent precipitation and the ENSO signal weakens sharply. Snow becomes much more reliable, though warmer and wetter at the base.

| Area | Lat. | Base (m) | Lift top (m) | Summit (m) | Note |
|---|---|---|---|---|---|
| **Nevados de Chillán** | 36.9°S | ~1,600 | ~2,700 | 3,212 (volcano) | Big vertical; active volcano |
| **Antuco** | 37.4°S | ~1,400 | ~1,900 | 2,979 | |
| **Corralco / Lonquimay** | 38.4°S | ~1,500 | ~1,900 | 2,865 | Excellent snow reliability |
| **Las Araucarias / Llaima** | 38.7°S | ~1,400 | ~1,800 | 3,125 | Araucaria forest — **protected** |
| **Villarrica / Pucón** | 39.4°S | ~1,200 | ~1,800 | 2,847 | Very active volcano (erupted 2015) |
| **Caviahue** (AR) | 37.9°S | ~1,600 | ~2,000 | 2,979 | |
| **Chapelco** (AR) | 40.1°S | ~1,200 | ~1,980 | — | |
| **Cerro Catedral, Bariloche** (AR) | 41.1°S | ~1,030 | ~2,180 | — | Largest in S. America |

`[SECONDARY-R — all elevations recalled; verify]`

- **Winter snow line:** central Chile ~1,800–2,200 m in normal years, rising above 2,500 m in warm/drought years; at 38–40°S roughly **1,100–1,400 m.** `[SECONDARY-R]`

#### 3.3.3 ⭐ The volcanic-ash advantage — the strongest physical finding in the Chilean leg

`[INFERENCE — physically grounded, and I regard it as high-confidence]`

Southern-Andean ski terrain is largely **volcanic cones**: smooth, **ash- and scoria-mantled**, treeless above ~1,400–1,600 m, with regular concave/convex flanks at 20–35°.

**Ash and scoria are the smoothest natural ground cover in the entire candidate set.** From §2.6, `D_min` ≈ **30–50 cm**, versus 100–150 cm over NZ tussock and 200–300 cm over Japanese sasa.

**What that is worth:** at a given snowfall rate, a site that becomes skiable at 40 cm rather than 130 cm reaches skiable condition **weeks earlier**, retains it **weeks longer**, and survives mid-season melt events that would end a tussock season. `[INFERENCE]` Roughly, it can convert a marginal 55-day site into a comfortable 95-day site without a single metre of extra elevation.

**Offsets, which are real:**
- **Active volcanoes.** Villarrica, Lonquimay and Nevados de Chillán are all active; Villarrica erupted in 2015 and carries frequent alert-level changes. **Volcanic and lahar hazard is a genuine insurance and life-safety line item** and must be assessed against SERNAGEOMIN hazard maps.
- **Lahar paths** occupy exactly the valleys you would want for access roads and a base area.
- **No wind shelter** above treeline on an open cone; conical geometry means **every aspect exists**, which is good for choice and bad for consistency.
- ***Araucaria araucana* is a protected Natural Monument in Chile** — clearing is restricted `[SECONDARY-R]`. Below the araucaria/lenga treeline, *Nothofagus* (lenga/ñirre) gives good glade skiing, but **lenga krummholz is unskiable** and occupies the transition band.

#### 3.3.4 Chile verdict

> `[INFERENCE]` **Chile 36–39°S is the most physically attractive under-priced region in this study**: reliable snow, large private *fundos* reaching 1,400–2,400 m, 600–1,200 m of achievable vertical, an ENSO signal weak enough to satisfy the 8-in-10 standard, and **the best ground cover in the world for a low-snow-depth operation.** Reject 32–35°S on drought and variance.

---

### 3.4 COMPARATIVE NOTE — THE OTHER CANDIDATE REGIONS

`[SECONDARY-R / INFERENCE throughout — elevations recalled, verify]`

**US Rockies (Colorado / Wyoming / Montana).**
Continental, cold, dry, low-density snow (7–9% density). Colorado bases 2,400–2,900 m, tops 3,500–4,000 m; MT/WY bases 1,800–2,100 m. Seasons 130–170 days, rain-on-snow risk very low. **The problem is avalanche character, not snow supply:** the shallow, cold, continental snowpack produces **depth hoar and persistent weak layers**, giving the most difficult and least forecastable slab problem of any candidate region. Colorado leads the US in avalanche fatalities `[SECONDARY-R]`. **Land:** alpine terrain is overwhelmingly USFS; the exceptions are patented mining claims and large private ranches. ⭐ **The Yellowstone Club (Montana, ~2,100–3,150 m, ~890 m vertical) is the world's benchmark private ski mountain and the closest existing analogue to this client's stated concept** — worth studying as a template for land assembly, membership structure and avalanche programme scope. `[SECONDARY-R]`

**BC interior (Monashee / Selkirk / Purcell — the Columbia Mountains).**
Physically the best snow in the study: 10–15 m annual snowfall, bases 1,100–1,500 m, tops 2,000–2,500 m, seasons 140–170 days, and — critically — **treed terrain**, which solves both wind scour and ground roughness (glades have `D_min` ≈ 60–100 cm and anchor the snowpack against slab release). **But:** alpine land is overwhelmingly **Crown land**. Cat-ski and heli-ski operators hold **tenures and licences, not title.** Freehold alpine terrain (old railway grants, Crown-granted mineral claims) exists but is rare and small. **Physical grade A+, title availability grade F.**

**Scandinavian fjäll (Norway / Sweden / Finland).**
Reliable snow Dec–May in the north (Riksgränsen ~500–900 m; Åre 380–1,275 m; Hemsedal 620–1,450 m; Ylläs top 718 m). Low vertical, severe wind on open fjäll, and a December daylight problem at high latitude.
> ⛔ **DISQUALIFYING, AND IT IS A PHYSICAL-USE ISSUE AS MUCH AS A LEGAL ONE:** **Sweden's *allemansrätten* and Norway's *allemannsretten*** (Norway: *friluftsloven*, applying to **utmark** — uncultivated land, which is precisely alpine terrain) **give the public a right of access and passage over exactly the land the client wants to hold privately.** `[PRIMARY-R — verify with counsel]` **You cannot own an exclusive private ski mountain in Norway or Sweden.** Strike the region.

**Caucasus (Georgia).**
Large vertical and heavy snow at low cost: Gudauri ~1,990–3,280 m; Tetnuldi ~1,600–3,165 m; Hatsvali/Mestia. Season ~Dec–April. **Risks:** significant and poorly controlled avalanche terrain (the Gudauri area in particular); the Jvari Pass road closes; geopolitical risk; and **Georgian constitutional restrictions on foreign ownership of agricultural land** (2017/2018 amendment) which channel acquisitions through Georgian legal entities. `[SECONDARY-R — legal workstream to confirm]`

**Tien Shan (Kyrgyzstan).**
Very cold, very continental, very high — Karakol ~2,300–3,040 m; Too-Ashuu and the Suusamyr valley host the cat/heli terrain. **Precipitation is moderate (~300–500 mm winter), so base depths are modest and the snowpack is faceted and weak — a textbook continental depth-hoar / persistent-slab problem, the worst possible pairing with an inexperienced private operation.** Foreign ownership of agricultural land is restricted. Season Dec–April.

**Türkiye.**
Two distinct settings. **Erzurum / Palandöken** (39.9°N): base ~2,200 m, top ~3,125 m — very high, cold, continental, 150+ day season, modest depths. **Kaçkar Mountains** (Rize/Artvin, ~40.8°N): maritime Black Sea moisture, **enormous snowfall**, heli-ski terrain to ~3,900 m.
> ⚠️ **Structural constraint for a *large* landholding:** Turkish law caps foreign real-property acquisition at **30 ha per foreign natural person (extendable to 60 ha by Presidential/Cabinet decision)** and at **10% of the area of any given district**, with military-zone clearance required. `[SECONDARY-R — legal workstream to confirm]` **These caps are incompatible with a "large alpine landholding" held personally**; a Turkish company structure would be required.

---

## 4. AVALANCHE RISK AND WHAT IT ACTUALLY COSTS

### 4.1 Terrain classification — ATES

**Avalanche Terrain Exposure Scale**, Parks Canada — Statham et al. (2006); **ATES v.2 (2022, Statham & Campbell)** adds Class 0 and Class 4. `[PRIMARY-R]`

| Class | Name | Description | Fit for a low-CAPEX private mountain |
|---|---|---|---|
| **0** | **Non-avalanche terrain** | No avalanche hazard whatsoever | ⭐ **Target** |
| **1** | **Simple** | Low-angle or primarily forested terrain; some forest openings; runouts of infrequent avalanches; **exposure can be reduced or eliminated by route choice** | ⭐ **Target** |
| **2** | **Challenging** | Well-defined avalanche paths, start zones or terrain traps; **routefinding required** | ⚠️ Costs money — forecasting, closures, possibly control |
| **3** | **Complex** | **Multiple overlapping paths**, large expanses of steep open terrain, **terrain traps unavoidable** | ⛔ Effectively uninsurable for a small private operation |
| **4** | **Extreme** | Glaciated, sustained exposure, no options | ⛔ Reject |

> **Acquisition rule `[INFERENCE]`: buy Class 0/1. Class 2 is a permanent cost line. Class 3/4 should not be screened in at all.**

### 4.2 Explosives — who may hold them, and what that implies

`[PRIMARY-R on the statutes named; verify current instrument names and thresholds with local counsel]`

| Country | Regime | Practical position for a private landowner |
|---|---|---|
| **New Zealand** | **HSNO Act 1996** + **Health and Safety at Work (Hazardous Substances) Regulations 2017**; **WorkSafe NZ** and the **EPA**. Requires a **Controlled Substance Licence (CSL)**, an approved **magazine** with a location test certificate, and vetting. NZ Mountain Safety Council runs the **NZ Avalanche Advisory**. | **Obtainable but onerous.** Commercial NZ fields run patrol teams with CSL holders. A private owner would be building a regulated explosives operation from scratch. |
| **Japan** | **火薬類取締法 (Explosives Control Act)** — highly restrictive. Requires a **火薬類取扱保安責任者** (explosives handling safety supervisor) qualification plus prefectural governor permits for purchase (譲受許可), storage and use (消費許可). | ⛔ **Realistically not obtainable** by a private landowner without major institutional effort. **Japanese ski areas do comparatively little explosive control** — they close terrain instead, and much terrain is forested. **In Japan you must choose terrain that needs no control.** |
| **Chile** | **Ley 17.798 sobre Control de Armas y Explosivos**; administered by the **DGMN (Dirección General de Movilización Nacional)** under Army oversight. Requires registration as a *usuario de explosivos*, an authorised *polvorín* (magazine), and per-purchase permits. | **Obtainable but bureaucratic and military-supervised.** Chilean resorts (Portillo, Valle Nevado, Chillán) do run control programmes. |
| **United States** | **ATF Federal Explosives Licence/Permit (FEL/FEP)**, 18 U.S.C. ch. 40; magazine storage per **27 CFR Part 555**; plus state permits; plus USFS permit conditions on federal land. | **Routine but expensive.** Even small US areas run six-figure patrol/avalanche budgets. |

### 4.3 What an avalanche programme costs

**Operating cost — a minimum credible programme:** `[INFERENCE — built up from staffing, not quoted]`
- 2–4 trained forecaster/controllers through the season (the dominant cost)
- explosives licensing, magazine construction and compliance
- daily snowpack observation, pit work, record-keeping (records are the legal defence)
- ongoing training and re-certification, radios, rescue cache

> **Realistic annual cost of a minimum credible avalanche programme at a small NZ ski area: NZ$150,000–400,000/yr.** `[INFERENCE]` **This alone plausibly exceeds the entire intended operating budget of a private family mountain.**

**Capital cost — remote avalanche control systems (RACS):** `[SECONDARY-R / INFERENCE — order-of-magnitude only; obtain vendor quotes]`

| System | Indicative installed CAPEX | Recurring |
|---|---|---|
| **Gazex** (TAS) — fixed exploder tube, oxygen + propane fed from a shelter | **~US$80k–180k per exploder**, plus **~US$150k–400k per gas shelter** serving several exploders, plus helicopter installation | ~US$5k–15k per exploder per year (gas + service) |
| **Wyssen avalanche tower** — tower with rotating charge magazine | **~US$100k–200k per tower** installed | ~US$150–400 per charge, plus annual service |
| **O'Bellx** — removable Gazex-derived unit, heli-removed in summer | **~US$100k–200k per unit** | gas + service |
| **Avalauncher / hand charges** | Low capital | High labour, high licensing burden, **direct human exposure** |

> **A small system of 4–6 exploders realistically lands at US$0.8M–2.0M installed.** `[INFERENCE]`

> ### ⛔ **CONCLUSION: any explosive or RACS avalanche programme is a six-figure annual and seven-figure capital line. It is categorically incompatible with "minimal CAPEX private ski mountain." The correct response is not to budget for it — it is to make it unnecessary at the screening stage.**

### 4.4 ⭐ THE RECOMMENDATION — the terrain profile that eliminates avalanche control as a cost line

**Buy a property whose primary skiable envelope satisfies all six of these:**

1. **All start zones < 30°.** Allow short pitches to ~32° only where the ground is well anchored (dense tussock, scrub, trees) and the pitch is short and unconfined.
2. **No overhead exposure.** Nothing above any skiable area is steeper than 30°, and no avalanche path from outside the ski area discharges into it. *(This is the criterion most often missed — a 22° run under a 38° headwall is not safe terrain.)*
3. **A rounded headwall, not a cliffed one.** Ridge geometry above the basin should be convex-rounded. Cliff bands are both a start-zone problem and a cornice problem.
4. **No confined gullies or terrain traps** in the run layout, and no creek gullies, road cuts, or depressions at the runout that would deepen a burial. Prefer **broad open concavity** (a basin) to **confined concavity** (a gully).
5. **Below treeline where the option exists** (Japan, BC, Chile *Nothofagus*, US). Forested terrain with tree spacing under ~10 m almost never produces destructive slabs.
6. **The access road is included in the assessment.** ⚠️ **On properties of this type the road is frequently the real avalanche hazard, not the ski terrain** — it traverses below slopes for kilometres, is used daily, and is used by people who are not thinking about avalanches. **Screen the road with the same test as the runs.**

**What this terrain profile buys you:**

| Line item | Controlled operation | **Class 0/1 property** |
|---|---|---|
| Explosives licence, magazine, compliance | Required | **None** |
| RACS capital | US$0.8M–2.0M | **None** |
| Forecaster/controller payroll | NZ$150k–400k/yr | **None** |
| Insurance loading for avalanche exposure | Material | **None** |
| Residual risk management | — | Written terrain-use policy; a handful of closed features; transceiver/probe/shovel discipline; subscription to the national avalanche advisory; guest briefing |
| **Annual avalanche cost** | **NZ$150k–400k+** | **< US$10k** `[INFERENCE]` |

### 4.5 How much skiable terrain does the sub-30° rule sacrifice?

`[INFERENCE — slope-angle distributions vary enormously with geology; these are planning figures to be replaced by the actual DEM histogram from §6.2]`

Indicative alpine slope-angle distribution by area:

| Slope band | Rolling / dissected tussock or ash terrain | Glacially-carved cirque terrain |
|---|---|---|
| < 15° | 20–30% | 10–18% |
| 15–25° | 30–35% | 20–28% |
| 25–30° | 12–18% | 12–16% |
| 30–35° | 10–15% | 14–18% |
| 35–45° | 8–15% | 18–25% |
| > 45° | 2–6% | 8–15% |

- **A "<30° only" rule typically retains 55–70% of the terrain on rolling terrain, but only 35–48% on steep glacially-carved terrain.**
- **Then subtract the overhead-exposed fraction of that sub-30° terrain — commonly another 10–25%** of total area. This second subtraction is the one people forget, and it is why the DEM test in §6.3 is worth running.
- **Net: expect to retain roughly 45–60% of a rolling property and 25–40% of a steep one.**

**But the retained terrain is not a consolation prize.** The 6–28° band is precisely: beginner and intermediate terrain, cat-groomable and cat-accessible, tourable, usable in flat light and poor visibility, safest for guests and children, and the terrain a family will actually ski 90% of the time. **The terrain given up is the terrain a private owner should not be skiing unguided anyway.**

> ### **BOTTOM LINE `[INFERENCE]`**
> **Target a broad, pole-facing (S–SE in NZ/Chile; N–NE in Japan), lee-loaded open basin or rolling spur system: 15–28° mean slope, 300–600 m vertical, rounded headwall, no path steeper than 30° discharging into it, no confined gullies, and a road that is itself out of avalanche paths.**
>
> **Such a property is ATES Class 0–1. It requires no explosives, no remote control system, no forecasting staff, no explosives licence and no avalanche insurance loading — and it is measurable from a free DEM before you ever visit the site.**
>
> **Screening threshold: reject any candidate where less than 60% of the pole-facing 15–28° terrain is free of overhead >30° slopes.**

### 4.6 Two residual hazards that survive the sub-30° rule

`[INFERENCE / SECONDARY-R]`

1. **Glide avalanches.** On **smooth** ground (grass, ash, rock slabs) a wet snow-ground interface lets the whole pack creep and release **even at 25–30°**. Precursor "glide cracks" (*Schneemäuler*, "whale mouths") open days to weeks before release. **Note the tension with §2.6: the smooth ground that minimises `D_min` slightly increases glide risk.** Management is cheap and effective: glide cracks are visible, so you close what is below them. **This does not require explosives** — glide avalanches are notoriously unresponsive to control anyway.
2. **Cornices.** Ridge-crest cornices form on lee aspects — the same aspects you want for loading. They fail spontaneously and can trigger slopes below. Manage by keeping run entries away from cornice fall lines and by not travelling on the ridge crest above them.

**Also note, for NZ specifically `[PRIMARY-R — Accident Compensation Act 2001]`:** New Zealand's **ACC no-fault scheme bars most personal-injury litigation**, which materially reduces the liability tail of a private ski operation compared with the US or Chile. **This is a genuine and often-overlooked advantage of the NZ jurisdiction for this concept.** It does **not** remove **health-and-safety prosecution risk under HSWA 2015** if there are workers or the owner is a PCBU — verify with the legal workstream.

---

## 5. THE METRIC SET — WHAT TO MEASURE ON EVERY CANDIDATE PROPERTY

Produce these **16 numbers** for each shortlisted property. They fit on one page and they are the whole physical case.

### A. Vertical and access
| # | Metric | Definition |
|---|---|---|
| 1 | `Base_elev` | Elevation of the realistic base / parking / lodge site (m) |
| 2 | `Top_elev` | Elevation of the highest usable start point **within title** (m) |
| 3 | `V_road` | Vertical between the highest reliably road-accessible point and the property high point (m) |
| 4 | **`V_ski`** | **Vertical of the longest continuous fall-line descent entirely within title and entirely within 6–30°** (m) — *the single most important number* |
| 5 | `Road_grade_max` | Maximum grade of the access route (%) |
| 6 | `Road_km_above_snowline` | km of access road above the median seasonal snow line — the clearing burden |

### B. Terrain quality
| # | Metric | Definition |
|---|---|---|
| 7 | `A_skiable` | Contiguous area (ha) with slope 6–30°, above `Base_elev`, within title |
| 8 | **`A_core`** | **Contiguous area (ha) in 15–25° — the money band** |
| 9 | `Aspect_dist` | Aspect distribution of `A_skiable` across 8 sectors (%) |
| 10 | `A_pole` | % of `A_skiable` on pole-facing aspects (SH 112.5–247.5°; NH 292.5–67.5°) |
| 11 | **`A_safe`** | **% of `A_skiable` with no upslope terrain >30° in its catchment — the avalanche-clean fraction** |
| 12 | `Sx_lee` | % of `A_skiable` that is lee-loaded under the prevailing storm wind |

### C. Snow
| # | Metric | Definition |
|---|---|---|
| 13 | `SCD_p50(z)`, `SCD_p10(z)` | Median and 10th-percentile snow-cover duration by 100 m elevation band, from a 20+ yr satellite record (days/yr) |
| 14 | **`D_ski_p50`, `D_ski_p10`** | **Median and bad-year count of days with modelled SWE ≥ site `D_min` equivalent** — the defensible "skiable days" number |
| 15 | `Onset_p50 / Melt_p50` | Median first and last day of continuous cover at `Base_elev` |
| 16 | `RoS_freq` | % of cold-season precipitating hours with the ERA5 freezing level above `Base_elev` |

### D. Ground cover (from imagery + one field visit)
Map the property into the roughness classes of §2.6, assign each polygon its `D_min`, and report an **area-weighted `D_min` for the ski envelope**. This converts directly into metric 14 and is the number most likely to change the ranking of two otherwise-similar properties.

---

## 6. THE REPEATABLE VERIFICATION WORKFLOW

> Designed so a competent GIS analyst can run it on a shortlisted property in **2–3 days per property using entirely free data and free software**, and produce three deliverables: **(a) a slope/aspect map, (b) a skiable-terrain area figure, (c) a 20-year satellite snow-cover-duration curve by elevation band.**

### 6.0 Free datasets — the register

#### Global
| Dataset | What it gives | Access |
|---|---|---|
| **Copernicus DEM GLO-30** (30 m) | ⭐ **Best free global DEM in mountains** (TanDEM-X derived; far better than SRTM) | AWS Open Data `s3://copernicus-dem-30m/`; OpenTopography; ESA |
| **Copernicus DEM GLO-90** (90 m) | Fully open incl. commercial use | Same |
| **ALOS World 3D-30 m (AW3D30)** | JAXA 30 m — often superior in Japan | JAXA, free registration |
| **NASADEM / SRTM 1-arcsec** | Legacy 30 m; voids in steep terrain | Fallback only |
| **OpenTopography** (opentopography.org) | ⭐ **One-stop portal**: GLO-30, SRTM, NASADEM, ALOS, regional LiDAR, **plus on-the-fly slope/aspect/hillshade and an API** | Free; **best single starting point** |
| **ESA WorldCover 10 m** | First-pass land cover / treeline / ground-roughness proxy | Free |
| **Sentinel-2 L2A** (10–20 m, 5-day) | Property-scale NDSI snow mapping, 2015– | Copernicus Data Space Ecosystem (free) |
| **Landsat 5/7/8/9** (30 m, 1984–) | ⭐ **The only free 40-year record at property scale** — for trend | USGS / GEE |
| **MODIS `MOD10A1` / `MYD10A1`** (500 m daily, 2000–) | ⭐ **The workhorse 25-year snow-cover-duration record** | NSIDC / GEE |
| **VIIRS `VNP10A1`** (375 m, 2012–) | MODIS continuity | NSIDC / GEE |
| **Sentinel-1 SAR** | Wet-snow mapping; works through cloud (vital in NZ west and Japan) | Copernicus (free) |
| **ERA5-Land** (9 km hourly, 1950–) | ⭐ **`snow_depth_water_equivalent`, `snow_cover`, `snowfall`, `snowmelt`, `2m_temperature`, `total_precipitation`** | Copernicus **CDS API** (`cdsapi` Python package) |
| **ERA5** (31 km) | **`deg0l`** (0 °C isothermal level) → rain-on-snow screen; pressure-level winds | CDS API |
| **Google Earth Engine** | ⭐ **Hosts all of the above co-registered — this is how you run 25 years of analysis in an afternoon** | Free for research/non-commercial |
| **QGIS + GDAL + GRASS/SAGA** | All terrain analysis | Free |

#### New Zealand
| Dataset | Notes |
|---|---|
| **LINZ Data Service** (data.linz.govt.nz) | ⭐ Free with registration: **national 8 m DEM**; **1 m LiDAR DEM** tiles (extensive Canterbury/Otago/Marlborough coverage) and point clouds; aerial imagery 0.075–0.5 m; Topo50. **Crucially, also `NZ Property Titles` and `NZ Primary Parcels` — the actual cadastre, free.** You can clip every analysis to the exact legal parcel. |
| **Manaaki Whenua LRIS Portal** (lris.scinfo.org.nz) | ⭐ **LCDB v5 (Land Cover Database)** — free, and its classes map *directly* onto the §2.6 roughness table: *Tall Tussock Grassland*, *Low Producing Grassland*, *High Producing Exotic Grassland*, *Sub Alpine Shrubland*, *Alpine Gravel and Rock*, *Depleted Grassland*. **This is the ground-roughness map, ready-made.** Also LENZ and S-map soils. |
| **NIWA CliFlo** (cliflo.niwa.co.nz) | National climate database, free registration |
| **NIWA SIN + national snow model** | Alpine SWE/depth; supplied on request |
| **NZ Avalanche Advisory** (avalanche.net.nz) | Forecasts + observation archive |
| **Canterbury Maps / Otago Regional Council GIS** | Free hazard, property and access layers |

#### Japan
| Dataset | Notes |
|---|---|
| **国土地理院 基盤地図情報 数値標高モデル** (`fgd.gsi.go.jp`) | ⭐ **5 m mesh DEM (5A LiDAR / 5B photogrammetric)** where available, **10 m mesh (10B)** nationwide. Free registration. The 5 m DEM is excellent. |
| **地理院地図 (maps.gsi.go.jp)** | ⭐ Free web GIS with **傾斜量図 (slope-angle overlay)**, 陰影起伏図 (hillshade), 自分で作る色別標高図, cross-sections, 3D — **and historical aerial photography back to the 1960s–70s, which is how you find defunct ski areas (see §6.7)** |
| **JMA 過去の気象データ検索** (`www.data.jma.go.jp/obd/stats/etrn/`) | ⭐ Daily/monthly **最深積雪**, **降雪量合計**, and **平年値 (1991–2020)** for every AMeDAS station (~330 with snow depth). **This is where §3.2.2 must be verified.** |
| **文部科学省・気象庁『日本の気候変動2025』** | Projections |
| **林野庁 国有林野データ / 都道府県 森林GIS・森林簿** | ⭐ **国有林 vs 民有林 boundaries — the tenure screen** |
| **法務省 登記所備付地図データ** (via G空間情報センター) | Cadastral map open data — parcel polygons |
| **NIED 雪氷防災研究センター** | Snow research; 雪おろシグナル snow-load product |

#### Chile
| Dataset | Notes |
|---|---|
| **IDE Chile / Geoportal de Chile** (ide.cl) | National spatial data infrastructure |
| **CR2 — Centro de Ciencia del Clima y la Resiliencia** (cr2.cl) | ⭐ **Free and excellent**: Explorador Climático, long station records, Andes snow-persistence products |
| **DGA — Dirección General de Aguas** | Snow and hydrology stations (some snow-route/pillow data) |
| **SERNAGEOMIN** | ⚠️ **Volcanic and lahar hazard maps — mandatory for any volcano-flank property** |
| **CIREN** | Soils / land capability |
| **Copernicus GLO-30** | The practical DEM (no free national LiDAR) |
| **Conservador de Bienes Raíces** | Property registry, per-comuna, paid |

---

### 6.1 Step 0 — Get the legal parcel boundary

Everything must be clipped to **title**, not to the mountain. A property that "has a 2,000 m peak" is worthless if the title stops at 1,300 m.

- **NZ:** LINZ `NZ Property Titles` / `NZ Primary Parcels` → filter by title reference → export GeoJSON. **Free and authoritative.**
- **Japan:** 法務省 登記所備付地図 open data → 地番 polygons; cross-check against 森林簿 for 国有林/民有林.
- **Chile:** usually only a scanned *plano* from the Conservador — **digitise it manually against a GLO-30 hillshade**, and expect boundary ambiguity in the alpine zone.

### 6.2 Step 1 — DEM preparation and slope/aspect (QGIS / GDAL)

```bash
# 1. Reproject and clip to title. Use a metric CRS:
#    NZ  -> EPSG:2193 (NZTM2000)
#    JP  -> EPSG:6669..6687 (JGD2011 plane rectangular, zone-dependent) or EPSG:3095
#    CL  -> EPSG:32719 (UTM 19S)
gdalwarp -t_srs EPSG:2193 -tr 8 8 -r bilinear \
         -cutline parcel.geojson -crop_to_cutline \
         dem_raw.tif dem_parcel.tif

# 2. CRITICAL: smooth before computing slope.
#    Raw 1 m LiDAR slope is dominated by tussock, boulders and microtopography.
#    Ski-relevant slope is the slope a 15 m ski turn feels.
gdal_translate -tr 15 15 -r average dem_parcel.tif dem_15m.tif

# 3. Derivatives
gdaldem slope     dem_15m.tif slope_deg.tif  -compute_edges
gdaldem aspect    dem_15m.tif aspect_deg.tif -zero_for_flat
gdaldem hillshade dem_15m.tif hillshade.tif  -az 315 -alt 45
gdaldem TRI       dem_parcel.tif tri_fine.tif   # roughness proxy on the FINE dem
```

> ⚠️ **The resampling step is not cosmetic.** ATES and avalanche-terrain modelling conventionally work at **~20–30 m**. Computing slope on a raw 1 m DEM produces a slope histogram dominated by noise and will materially overstate the steep fraction. **Compute the ski/avalanche slope on a 15–30 m DEM; keep the fine DEM only for the roughness (TRI) layer.**

**Ski mask (QGIS raster calculator, Southern Hemisphere, pole-facing):**
```
("slope_deg@1" >= 6) AND ("slope_deg@1" <= 30)
AND ("aspect_deg@1" >= 112.5) AND ("aspect_deg@1" <= 247.5)
AND ("dem_15m@1" >= 1500)
```
Northern Hemisphere pole-facing band wraps through zero:
```
AND ( ("aspect_deg@1" >= 292.5) OR ("aspect_deg@1" <= 67.5) )
```

Then `gdal_polygonize` the mask, drop polygons under ~2 ha, and take the **largest contiguous polygon** — contiguity matters far more than total area, because scattered patches are not a ski mountain.

**Outputs:** slope-band map with area (ha) per band; aspect rose weighted by area within 6–30°; `A_skiable`, `A_core`, `A_pole`.

### 6.3 Step 2 — ⭐ The avalanche-clean fraction `A_safe`

This is the step that converts the §4.4 recommendation into a number, and it is the highest-value non-obvious analysis in the workflow.

**Method:**
1. Build `STEEP = slope >= 30°` from the 15–30 m DEM.
2. For every cell in `A_skiable`, test whether any `STEEP` cell lies upslope **within plausible runout**.
3. Use the **alpha-angle** runout rule: avalanche runout rarely extends beyond a line drawn from the top of the start zone at an **alpha angle of ~18–25°** to the stopping point `[PRIMARY-R — standard runout statistics, e.g. Lied & Bakkehøi; McClung & Schaerer]`. Use **α = 20°** for a conservative screen and **α = 25°** for a moderate one.
4. **Practical implementation** — "alpha cone" test: for each candidate cell, compute the maximum vertical angle to any upslope `STEEP` cell. If that angle **exceeds α**, the cell is **exposed**. Implement with a GRASS `r.viewshed`-style sweep, or a simple Python/NumPy loop over the (small) parcel raster.
5. `A_safe` = area of `A_skiable` not flagged exposed.
6. **Run the identical test along the access road centreline.** Report `Road_exposed_km`.

**Cross-check with published and modelled ATES:**
- Published ATES maps exist for parts of Canada, NZ (via avalanche.net.nz), Norway (NVE/varsom) and Switzerland (SLF).
- ⭐ **`AutoATES` v2 is an open-source automated ATES model** (Sykes, Hendrikx et al.; published in *Natural Hazards and Earth System Sciences*) that runs in Python/QGIS and takes **a DEM + a forest-density layer** and outputs an ATES raster. `[SECONDARY-R — verify the current release and citation]` **Recommend running it on every shortlisted property.** Forest density can come from ESA WorldCover or a Sentinel-2 NDVI composite.

### 6.4 Step 3 — Ground-roughness and treeline mapping

- **NZ:** clip **LCDB v5** to the parcel → map classes to `D_min` per §2.6 → compute **area-weighted `D_min`** over the ski envelope. *(Tall Tussock Grassland → 100–150 cm; Low Producing Grassland → 40–60 cm; High Producing Exotic Grassland → 25–35 cm; Alpine Gravel and Rock → 100–200 cm; Sub Alpine Shrubland → reject.)*
- **Japan:** GSI 植生図 / 環境省 植生調査 + Sentinel-2 to separate 笹 sasa, deciduous broadleaf, conifer plantation, and **existing cleared runs**.
- **Chile:** ESA WorldCover + Sentinel-2 to separate bare ash/scoria, *lenga*, *araucaria* (protected), *matorral*.
- **Everywhere:** compute **TRI on the finest available DEM**. Where 1 m LiDAR exists (much of NZ), TRI at 1 m is a direct boulder/tussock proxy — **calibrate it against a dozen GPS-tagged field photographs** and you have a quantitative, defensible roughness map.
- **Treeline:** take the **95th-percentile elevation of the tree-cover class** within the parcel. Note whether the ski envelope sits **above** treeline (wind scour, flat light, no anchoring, no shelter — NZ, Chilean cones, Central Otago) or **below** it (Japan, BC, US — glades, shelter, anchored snowpack, better visibility).

### 6.5 Step 4 — ⭐ The 20-year snow-cover-duration curve by elevation band (Google Earth Engine)

```javascript
// ---------------------------------------------------------------
// Snow-cover duration by elevation band, 25 years, MODIS Terra
// Southern Hemisphere season: 1 Apr (y) -> 31 Mar (y+1). NH: 1 Sep -> 31 Aug.
// ---------------------------------------------------------------
var parcel = ee.FeatureCollection('users/you/parcel');       // title boundary
var region = parcel.geometry().buffer(5000);                 // buffer: MODIS is 500 m
var dem    = ee.Image('COPERNICUS/DEM/GLO30').select('DEM').clip(region);
var band   = dem.divide(100).floor().multiply(100).rename('elev_band');   // 100 m bands

var snow = ee.ImageCollection('MODIS/061/MOD10A1')
             .filterDate('2001-01-01','2026-03-31')
             .select('NDSI_Snow_Cover')
             .map(function(img){
               // NDSI_Snow_Cover >= 40  == standard snow threshold (NDSI >= 0.4)
               return img.gte(40).rename('snow')
                         .copyProperties(img, ['system:time_start']);
             });

var years = ee.List.sequence(2001, 2025);
var scd = ee.ImageCollection(years.map(function(y){
  y = ee.Number(y);
  var start = ee.Date.fromYMD(y, 4, 1);            // <-- 9,1 for Northern Hemisphere
  var end   = ee.Date.fromYMD(y.add(1), 3, 31);
  return snow.filterDate(start, end).sum()
             .rename('scd').set('year', y);
}));

// p10 (bad year), p50 (median), p90 (good year) of SCD at every pixel
var scdP = scd.reduce(ee.Reducer.percentile([10, 50, 90]));

// Zonal statistics by 100 m elevation band
var stats = scdP.addBands(band).reduceRegion({
  reducer : ee.Reducer.mean().group({groupField: 3, groupName: 'elev_band'}),
  geometry: region, scale: 500, maxPixels: 1e9
});
print('SCD p10/p50/p90 by 100 m elevation band', stats);

// Trend: Sen's slope of SCD vs year (days per decade)
var trend = scd.map(function(i){
    return ee.Image.constant(ee.Number(i.get('year'))).float()
             .rename('year').addBands(i);
  }).reduce(ee.Reducer.sensSlope());
Map.addLayer(trend.select('slope').multiply(10), {min:-15, max:5}, 'SCD trend (days/decade)');
```

#### ⚠️ Five caveats — this is where analysts get it wrong

1. **MODIS 500 m is coarser than most properties.** A 500 ha property is ~20 MODIS pixels. **Use MODIS for the long record and the elevation gradient of the surrounding massif; use Sentinel-2 and Landsat for the property itself.** Buffer the parcel before the zonal statistics (as above).
2. **Cloud.** The MODIS product flags cloud. **Without gap-filling you systematically UNDERESTIMATE snow-cover duration.** Standard remedies: combine Terra (`MOD10A1`) + Aqua (`MYD10A1`); temporal nearest-neighbour fill; and the "snow persists between two snow observations" rule.
3. **NDSI ≥ 0.4 detects *any* snow, including a 2 cm dusting. Snow-cover duration ≠ skiable days.** Either (a) regress MODIS SCD against a nearby station's days-with-≥X-cm to build a transfer function, or (b) report SCD as an **upper bound** and apply a haircut — **typically 20–35% of snow-covered days are not skiable.** `[INFERENCE]` **Never present raw SCD as a season length.**
4. **Forest canopy masks snow** from optical sensors — a real bias in Japan and BC. Use **Sentinel-1 wet-snow** mapping to compensate, or accept and state the bias.
5. **Terra sensor degradation and the Terra/Aqua record ends** — bridge to **VIIRS `VNP10A1`** for continuity beyond the MODIS era.

#### The more defensible "skiable days" metric — ERA5-Land SWE

```python
import cdsapi
c = cdsapi.Client()
c.retrieve('reanalysis-era5-land', {
    'variable': ['snow_depth_water_equivalent', '2m_temperature',
                 'total_precipitation', 'snowfall', 'snowmelt'],
    'year'  : [str(y) for y in range(1995, 2026)],
    'month' : ['%02d' % m for m in range(1, 13)],
    'day'   : ['%02d' % d for d in range(1, 32)],
    'time'  : ['00:00', '06:00', '12:00', '18:00'],
    'area'  : [lat_n, lon_w, lat_s, lon_e],     # small box around the property
    'format': 'netcdf',
}, 'era5_land_snow.nc')
```
Then:
1. **Correct for orography.** ERA5-Land's 9 km grid under-represents peaks; its model elevation is often hundreds of metres below the real summit. **Fit an SWE-vs-elevation regression against nearby stations (NZ: SIN + CliFlo; Japan: AMeDAS; Chile: DGA/CR2) and apply it**, or lapse-correct the temperature field and re-run a simple degree-day/accumulation model.
2. Compute **days per season with SWE ≥ the site-specific threshold** (300 mm for a 1 m tussock site; ~150 mm for a smooth-ground or ash site — derived from the area-weighted `D_min`).
3. Report **`D_ski_p50` and `D_ski_p10`** (median and bad-year), plus the **coefficient of variation** — the CV is the number that decides whether the property meets the 8-in-10 standard of §2.4.

> ⭐ **`D_ski` — days with modelled SWE above the site's own `D_min` threshold — is the single most defensible headline number in this whole workflow.** It is the only metric that combines snow supply, temperature, elevation and *ground cover* into one figure, and it is directly comparable across countries.

#### The 40-year trend — Landsat
Use `LANDSAT/LC09/C02/T1_L2`, `LC08`, `LE07`, `LT05`. Compute **NDSI = (Green − SWIR1)/(Green + SWIR1)**, threshold ≥ 0.4. Because Landsat revisits every 16 days you get **snow *persistence*, not duration**: report **"% of cloud-free observations with snow, by month, by elevation band, 1984–present"** and fit the trend. **This is the best free way to detect a warming signal at property scale**, and it reaches back far enough to be meaningful.

### 6.6 Step 5 — Rain-on-snow and wind

**Rain-on-snow (`RoS_freq`):** pull ERA5 hourly **`deg0l`** (0 °C isothermal level) and `total_precipitation`. For all hours in the ski season with precipitation > 0.5 mm, compute the fraction with `deg0l > Base_elev`, and separately `> Top_elev`. Apply the §2.2 Screen C thresholds (≤15% good / 15–30% marginal / >30% reject).
> In New Zealand expect a **materially non-zero number even at 1,800 m** — the correct use of this metric in NZ is to **rank candidates against each other**, not to find one with a zero.

**Wind exposure (`Sx_lee`):** compute the **Winstral & Marks maximum-upwind-slope index (Sx)** for the prevailing storm direction — **NZ 290–320°, Japan 300–330°, Chile 36–40°S 270–300°, Colorado 270–300°**. Negative Sx = sheltered/lee (accumulating); positive Sx = windward/exposed (scouring). Free Python implementation: **`topocalc`**; full CFD if needed: **WindNinja** (free, USFS).
> **A lee-loaded, pole-facing basin can carry 1.5–3× the areal-average snow depth `[INFERENCE]`.** This is how a marginal-elevation property can still work, and it is why the Sx analysis is worth the day it takes. **Caveat: lee loading also builds wind slab — which is precisely why it must be paired with the sub-30° rule of §4.4. On <30° terrain, wind loading is pure upside.**

### 6.7 Step 6 — Finding defunct ski areas (Japan and elsewhere)

`[INFERENCE — method]` Old ski runs are cleared linear corridors through forest and remain visible for decades.
1. Open **地理院地図** → 年代別の写真 → the 1961–1969 / 1974–1978 / 1979–1983 aerial photo layers.
2. Scan the Sea-of-Japan-side ranges between 700 and 1,600 m for straight cleared corridors, lift lines and cleared summit platforms.
3. Cross-reference the modern layer: if the corridors are still open (or only lightly regrowing), the clearing cost is largely already spent.
4. Confirm 民有 vs 国有 status from the prefectural 森林GIS / 林野庁 layer **before** any further work.
5. Repeat the trick elsewhere with **Landsat 1984–2000** imagery for Chile, NZ and the US.

### 6.8 Step 7 — The cheapest and highest-value due-diligence spend of all

> ⭐ **Before committing, install 3–5 snow stakes with time-lapse trail cameras at different elevations and aspects on the candidate property, and run them for one full season.**
>
> **Cost: under US$3,000.** `[INFERENCE]`
>
> **It produces the only site-specific, ground-truth snow record that will ever exist for that property**, it calibrates every satellite and reanalysis product in this workflow, and it is admissible evidence in a negotiation in a way that a MODIS pixel is not. Add a cheap automatic weather station (temperature, wind, precipitation) if the budget allows.
>
> **Second-cheapest:** scrape **10+ years of daily published base-depth and open/closed reports** from the nearest operating ski areas (in NZ: Mt Dobson, Ōhau, Roundhill, Fox Peak). Operators publish these daily and they constitute a long, free, *skiable-condition-calibrated* record that no satellite product can match. Regress them against ERA5-Land to build the site transfer function of §6.5.

### 6.9 Step 8 — Road, operations and the output pack

**Road:** extract the access route from the DEM; compute the grade profile; count km above the median snow line; **and run the §6.3 alpha-cone test along the centreline.**
> **Design recommendation `[INFERENCE]`: plan for a "snow-line car park" — plough only to where the snow reliably starts and run the snowcat from there.** This eliminates most of the snow-clearing cost and most of the road-avalanche exposure in one decision, and it is the single biggest OPEX lever available at the design stage.

**Output pack per property (2 pages):**
- **Terrain sheet** — hillshade + slope-band map, aspect rose, `A_safe` / ATES map, ground-roughness map with area-weighted `D_min`.
- **Snow sheet** — `SCD` and `D_ski` curves by 100 m elevation band with a p10–p90 ribbon, the 1984–present Landsat persistence trend, and `RoS_freq` at base and top.
- **The 16 metrics table**, scored against §6.10.

### 6.10 Go / no-go thresholds

`[INFERENCE — my constructed thresholds; calibrate against the client's actual tolerance]`

| Metric | ⛔ Reject | ⚠️ Marginal | ✅ Good |
|---|---|---|---|
| `V_ski` (continuous, in title, 6–30°) | < 200 m | 200–350 m | **> 350 m** |
| `A_core` (15–25°, pole-facing, contiguous) | < 25 ha | 25–60 ha | **> 60 ha** |
| `A_safe` / `A_skiable` | < 50% | 50–75% | **> 75%** |
| `D_ski_p50` (days SWE ≥ site threshold) | < 45 | 45–75 | **> 75** |
| `D_ski_p10` (bad-year days) | < 20 | 20–45 | **> 45** |
| CV of `D_ski` | > 40% | 25–40% | **< 25%** |
| `RoS_freq` at base | > 30% | 15–30% | **< 15%** |
| Area-weighted `D_min` | > 150 cm | 80–150 cm | **< 80 cm** |
| `Road_km_above_snowline` | > 12 km | 5–12 km | **< 5 km** |
| `Road_exposed_km` (avalanche paths crossing road) | > 1.0 km | 0.2–1.0 km | **0** |

---

## 7. THE SNOW-RELIABILITY VERDICT TABLE

`[INFERENCE — scores are my judgement, built on the recalled data in §3 and the framework in §2. Season lengths are natural-snow operating days, not lift-served resort seasons.]`

### 7.1 Physical snow scorecard

| Region | Season (days, natural snow) | Reliability / variance | Rain-on-snow risk | Wind | Trend under warming to ~2050 | **Snow score /10** |
|---|---|---|---|---|---|---|
| **NZ Mackenzie / Central Otago** (Two Thumb, Ben Ōhau, Pisa, Old Woman, Dunstan) | 90–120 at 1,600–2,000 m | Moderate–high (SAM + ENSO) | **Moderate** (NW föhn) | ⛔ **High — the main operational killer** | Moderate loss; **high sites relatively resilient** | **7.0** |
| **NZ Marlborough / Kaikōura** (Inland Kaikōura, St Arnaud, Mt Lyford) | 70–100 | High | Higher (more maritime) | ⛔ Very high | Poor — most exposed NZ region | **4.5** |
| **Hokkaido** | 130–160 | ⭐ **Lowest variance in the study** | ⭐ **Very low** | Low–moderate | ⭐ **Least-bad in Japan**; little change projected at altitude | **9.5** |
| **Honshū Sea-of-Japan side** (Niigata, Nagano, Tōhoku) | 120–150 | Low–moderate | ⚠️ **Rising fast below ~900 m** | Moderate | ⛔ **Poor at low elevation; severe below 800 m** | **8.0** |
| **Chilean Andes 36–39°S** (Chillán, Antuco, Corralco, Villarrica) | 90–130 | Moderate (weak ENSO signal) | Moderate–high at base | Moderate–high | Moderate | **7.5** |
| Chilean/Argentine Andes 32–35°S | 70–110 typical; **30–50 in drought years** | ⛔ **Extreme — CV ≈ 45–60%** | Low (very high base) | High | ⛔ **Severe — megadrought since 2010** | **3.5** |
| **US Rockies** (CO / WY / MT) | 130–170 | Low–moderate | ⭐ Very low | Moderate | Moderate | **8.5** |
| **BC interior** (Columbias) | 140–170 | ⭐ **Very low** | Low at elevation | ⭐ Low (treed) | Low–moderate | **9.5** |
| **Caucasus (Georgia)** | 110–140 | Moderate | Low | Moderate | Moderate | **7.5** |
| **Tien Shan (Kyrgyzstan)** | 120–150 | Moderate | ⭐ Very low | Moderate | Low | **7.5** |
| **Scandinavian fjäll** | 150–200 | Low | Low | ⛔ **Very high on open fjäll** | Low | **8.0** |

### 7.2 The combined verdict — snow × terrain × **vertical available on private title**

**This is the ranking that matters, because the client's first-order requirement is that *legal title includes the skiable terrain*.**

| Rank | Region | Snow /10 | **Vertical on private title** | Avalanche burden | **Combined /10** | Verdict |
|---|---|---|---|---|---|---|
| **1** | **Chilean Andes 36–39°S** | 7.5 | ⭐ **Very good** — large private *fundos* on volcano flanks; **600–1,200 m achievable** | Low–moderate; smooth cones, mostly sub-30° available | **8.0** | ⭐ **Most under-priced. Best ground cover in the world (`D_min` 30–50 cm). Reliable snow. Real vertical on real title.** Offsets: volcanic/lahar hazard, protected *araucaria*, no wind shelter. |
| **2** | **NZ Mackenzie / Central Otago** | 7.0 | ⚠️ **Conflicted** — physically excellent, but **tenure review freeholded the low land and gave the tops to the Crown** `[XWS]`; highest freehold ski terrain found is ~1,460 m | ⭐ Low — rolling tussock basins, not cirques | **6.5** | ✅ Right mountains, right aspects, right avalanche profile, **wrong tenure**. Viable only on rare pre-tenure-review freehold. Verify title elevation before anything else. |
| **3** | **Honshū Sea-of-Japan side** | 8.0 | ⚠️ **Moderate** — via **defunct ski areas on 民有地**, 300–600 m | ⭐ Low — forested, and control is unobtainable anyway so terrain must be chosen safe | **6.5** | ✅ **Buy a closed ski area.** Cleared runs collapse `D_min` to 50–80 cm. Screen: base ≥700 m, top ≥1,300 m. Warming squeezes from below. |
| **4** | **US Rockies (MT / WY)** | 8.5 | ⚠️ Limited — alpine mostly federal; **patented claims and large ranches are the exception** | ⛔ **High — continental depth hoar, worst forecasting problem in the study** | **6.5** | ⚠️ **Yellowstone Club is the benchmark precedent** — study the model. Expensive, and the snowpack character raises the avalanche cost line. |
| **5** | **Caucasus (Georgia)** | 7.5 | ✅ Good — cheap, privatisable, big vertical | ⛔ High and poorly controlled | **6.0** | ⚠️ Cheapest real vertical in the study. Agricultural-land ownership restrictions + geopolitical risk. |
| **6** | **Hokkaido** | 9.5 | ⛔ **Poor** — high ground is 国有林 / park; private title rarely exceeds ~300 m vertical | ⭐ Low | **5.5** | **Best snow in the study, least available terrain.** Fine for a lodge, not for a mountain. |
| **7** | **Tien Shan (Kyrgyzstan)** | 7.5 | ⛔ Restricted for foreigners | ⛔ High — faceted continental pack | **5.0** | ⚠️ Cheap, cold, high. Ownership restrictions and a dangerous snowpack. |
| **8** | **NZ Marlborough / Kaikōura** | 4.5 | ⚠️ Freehold exists (Mt Lyford, Glazebrook, Upton Fells) but **too low** — Upton Fells peaks at 1,250 m with the majority under 850 m `[XWS]` | Moderate | **4.0** | ⛔ **Right tenure, wrong altitude.** The clearest illustration of the NZ conflict. |
| **9** | **BC interior** | 9.5 | ⛔ **Very poor — Crown land.** Cat-ski operators hold tenures, not title | Moderate–high | **3.5** | ⛔ **Physical A+, availability F.** Strike unless a rare freehold parcel surfaces. |
| **10** | **Chilean/Argentine Andes 32–35°S** | 3.5 | ✅ Good | Moderate | **3.5** | ⛔ **Strike on megadrought and CV ≈ 50%.** Fails the 8-in-10 standard structurally. |
| **11** | **Scandinavian fjäll** | 8.0 | ⛔ **Right-to-roam makes exclusive private use legally impossible** | Low–moderate | **2.5** | ⛔ **Strike.** *Allemansrätten* / *allemannsretten* is fatal to the core concept. |

### 7.3 The three physical archetypes worth pursuing

`[INFERENCE — the actionable output]`

**Archetype A — Chilean volcanic flank, 37–39°S.**
A *fundo* on the **S–SE flank of a volcano**, base 1,400–1,700 m, top 2,200–2,600 m, ash/scoria ground cover, `D_min` 30–50 cm, 600–1,000 m vertical, mostly sub-30° on the mid-flank. **Precedents: Corralco/Lonquimay, Nevados de Chillán, Antuco.** Must clear: SERNAGEOMIN volcanic/lahar hazard, *araucaria* protection, water rights.

**Archetype B — NZ Mackenzie station with a S/SE tussock basin.**
Base 1,500–1,700 m, top 1,950–2,150 m, 350–600 m vertical, S–SE lee-loaded basin, rolling not cirqued. **Then spend on summer rock-picking and smoothing to cut `D_min` from ~130 cm to ~70 cm — worth 3–5 weeks of season for a fraction of the cost of any lift.** ⚠️ **The binding question is whether *freehold title* reaches above 1,500 m — and per §3.1.4 it usually does not.** **Precedents: Mt Dobson, Fox Peak, Snow Farm; and Erewhon/Mt Potts as the operating model (snowcat + heli, no lifts, private, to 2011).**

**Archetype C — Japanese defunct ski area, Sea-of-Japan side.**
Base ≥700 m, top ≥1,300 m, on 民有地, within ~2.5 h of a Shinkansen station, with cleared runs still open on recent imagery. `D_min` 50–80 cm on the old runs. Enormous snow. **The road, the power and the clearing are already paid for.** Find them with GSI historical aerials (§6.7).

---

## 8. SOURCE REGISTER AND VERIFICATION TASK LIST

⚠️ **No source below was accessed in this session** (see §0). This register is therefore structured as a **verification task list**: it names the authoritative source for each claim and where to get it.

### 8.1 Framework and thresholds
| Claim | Source to verify against | Priority |
|---|---|---|
| 100-day rule; 1,200 m snow-reliability line; +150 m per °C; Swiss resort share at +1/+2/+4 °C | **OECD (2007), *Climate Change in the European Alps*** (Abegg, Agrawala, Crick, de Montfalcon); Abegg (1996) dissertation | **HIGH** |
| Slab avalanches concentrate on 30–45°, mode ~36–39° | **McClung & Schaerer, *The Avalanche Handbook***; Schweizer et al. | HIGH |
| Alpha-angle runout 18–25° | Lied & Bakkehøi; McClung & Schaerer | MEDIUM |
| ATES definitions; ATES v.2 Class 0 and 4 | **Statham et al. (2006)**; **Statham & Campbell (2022)**, Parks Canada | HIGH |
| AutoATES v2 open-source model | **Sykes, Hendrikx et al., *Natural Hazards and Earth System Sciences*** — confirm current release and repository | HIGH |
| Snow density / SWE conversions | Any standard snow-hydrology text; validate against local SIN/AMeDAS data | MEDIUM |
| §2.6 ground-cover `D_min` table | ⚠️ **My construct — no published source. Validate by field measurement and by interviewing operators at Mt Dobson, Fox Peak, Ōhau, Corralco.** | **HIGH** |

### 8.2 New Zealand
| Claim | Source | Priority |
|---|---|---|
| Mt Dobson base 1,600 m / summit 2,030 m / vertical ~305 m; car park 1,725–1,740 m | Mt Dobson operator; **LINZ Topo50 + 8 m DEM** (definitive). ⚠️ **Sources conflict; the brief's "top 2,100 m" was not corroborated** `[XWS]` | **HIGH** |
| Roundhill top ~2,133 m / vertical ~780 m | Operator; LINZ DEM | HIGH |
| All other NZ ski-area elevations in §3.1.1 | **LINZ Topo50 + 8 m DEM — do not rely on operator marketing** | **HIGH** |
| SIN station names, elevations, SWE records | **NIWA** — request Albert Burn, Castle Mount, Upper Rakaia time series directly | **HIGH** |
| Salinger Cardrona/Treble Cone −5%/−8%/−20% projections | ⚠️ **Brief-supplied and internally inconsistent — obtain the paper and identify the scenario for each figure** | **HIGH** |
| NZ snow-duration projections by elevation | **Hendrikx & Hreinsson et al.**, NZ seasonal snow modelling | MEDIUM |
| Tenure review outcomes; CPLRA 2022 | LINZ tenure-review documents; legislation.govt.nz `[XWS]` | **HIGH** |
| ACC bar on personal-injury litigation | **Accident Compensation Act 2001** — confirm scope with counsel | HIGH |

### 8.3 Japan
| Claim | Source | Priority |
|---|---|---|
| **All 最深積雪平年値 in §3.2.2** | ⚠️ **JMA `https://www.data.jma.go.jp/obd/stats/etrn/` → 過去の気象データ検索 → 平年値 → 最深積雪 (1991–2020).** **Every value in that table is unverified recall.** | **CRITICAL** |
| Sukayu as Japan's deepest station; ~566 cm record (Feb 2013) | JMA station records | **HIGH** |
| Shumarinai −41.0 °C (1978) as Japan's lowest official temperature | JMA | MEDIUM |
| Ski-area closures: ~700 at peak → ~450–500 today | **日本生産性本部『レジャー白書』**; 全国スキー場活性化協議会; MLIT statistics | HIGH |
| Snow projections / low-elevation collapse | **文部科学省・気象庁『日本の気候変動2025』**; 気象庁『気候変動監視レポート』 | **HIGH** |
| 国有林/民有林, 自然公園法, 保安林 constraints | 林野庁; 環境省; prefectural 森林GIS | **HIGH** (legal workstream) |
| 火薬類取締法 explosives regime | e-Gov 法令検索 | HIGH |

### 8.4 Chile / Argentina
| Claim | Source | Priority |
|---|---|---|
| 2010– megadrought; ~25–30% precipitation deficit | **Garreaud et al. (2017), *HESS***; **Garreaud et al. (2020), *Int. J. Climatol.*** | **HIGH** |
| Andean snowpack variability; CV ≈ 45–60%; ENSO coupling | **Masiokas et al. (2006, 2020)**; **CR2 Explorador Climático**; DGA snow-route data | **HIGH** |
| Snow-line elevations by latitude | CR2; DGA; MODIS snow-line analysis (run it yourself per §6.5) | MEDIUM |
| Ski-area elevations (§3.3.2) | Operators + Copernicus GLO-30 | MEDIUM |
| Volcanic and lahar hazard | ⚠️ **SERNAGEOMIN hazard maps — mandatory** | **CRITICAL** |
| *Araucaria araucana* Natural Monument status | CONAF; Chilean legislation | HIGH |
| Ley 17.798; DGMN explosives authorisation | leychile.cl | MEDIUM |

### 8.5 Other regions
| Claim | Source | Priority |
|---|---|---|
| Yellowstone Club elevations and private-mountain model | Public reporting; USGS DEM | MEDIUM |
| Norway/Sweden right-to-roam over *utmark* | **Friluftsloven (NO)**; Swedish constitutional *allemansrätten* — **confirm with counsel; this is a strike criterion** | **HIGH** |
| Georgian agricultural-land ownership restrictions | Georgian constitution (2017/18 amendment) + counsel | HIGH |
| Turkish 30 ha / 60 ha / 10%-of-district caps; military-zone clearance | Turkish Land Registry Law + counsel | HIGH |
| Kyrgyz land-ownership restrictions | Counsel | MEDIUM |
| ATF FEL/FEP; 27 CFR Part 555 | ATF | LOW |
| NZ CSL regime (HSNO 1996; HSW(HS) Regs 2017) | WorkSafe NZ; EPA | HIGH |

### 8.6 Cost figures — all require quotes, none are quoted
| Item | Status |
|---|---|
| Avalanche programme NZ$150k–400k/yr | `[INFERENCE]` — build up from actual NZ patrol salaries and licensing fees |
| Gazex ~US$80k–180k/exploder + US$150k–400k/shelter | `[SECONDARY-R]` — **obtain a quote from TAS** |
| Wyssen tower ~US$100k–200k | `[SECONDARY-R]` — **obtain a quote from Wyssen** |
| O'Bellx ~US$100k–200k/unit | `[SECONDARY-R]` — obtain quote |
| Rock-picking / smoothing cost per ha | `[NOT VERIFIED]` — quote locally against agricultural land-development rates |
| Used groomer (PistenBully 100 / Prinoth Husky / Tucker) | `[NOT VERIFIED]` — check the used market |

---

## 9. OPEN ITEMS FOR THE NEXT SESSION

1. ⚠️ **Re-run this workstream's evidence gathering with a fresh WebSearch budget.** §3 is recall-based throughout. The framework (§2), avalanche analysis (§4) and workflow (§5–6) do not depend on it.
2. **Verify the JMA 最深積雪平年値 table (§3.2.2) in full** — highest-value single verification task.
3. **Verify Mt Dobson's true summit elevation and vertical from the LINZ DEM** — three sources conflict, and it is the NZ benchmark.
4. **Obtain the Salinger Cardrona/Treble Cone paper** and reconcile the −8%/−20%-by-2040 inconsistency.
5. **Request NIWA SIN time series** for Albert Burn, Castle Mount and Upper Rakaia.
6. **Validate the §2.6 ground-cover `D_min` table** by interviewing operators at Mt Dobson, Fox Peak, Ōhau and Corralco. It is my construct and it is doing a lot of work in the analysis.
7. **Run the §6 workflow end-to-end on one test property** to debug it before applying it to a live shortlist.
8. **Chile 36–39°S has not been researched for actual listings** — it ranks first on physical grounds and appears to be outside the current sourcing effort. **Recommend opening a Chilean sourcing workstream.**
9. **Quote the avalanche and machinery cost lines properly** (§8.6).
10. **Cross-check the §7.2 combined ranking** with the legal workstream once Chilean and Japanese tenure positions are established.
