# Alpine Landholding — Cost & Revenue Evidence Base
**Workstream:** Phase 1 ski CAPEX · annual carrying cost · offsetting rural income
**Client:** Malaysia-based private buyer, reporting currency MYR
**Prepared:** 27 August 2026

---

## ⚠️ CRITICAL PROVENANCE WARNING — READ BEFORE USING ANY NUMBER

**No figure in this document was retrieved or verified during this session.** The research
tooling failed completely:

| Channel | Status | Evidence |
|---|---|---|
| WebSearch | **Exhausted at session level** — 200 of 200 calls consumed before this workstream began | Tool returned: *"this session has used its web search budget (200 of 200 WebSearch calls)"* on first call |
| WebFetch | **Egress-blocked** | `beeflambnz.com` → `EGRESS_BLOCKED` |
| Direct HTTPS (curl via proxy) | **Blocked by org egress policy** | Proxy `__agentproxy/status` shows 403-on-CONNECT for all 20 distinct hosts attempted this session |

Hosts confirmed 403 by the egress proxy this session (all analysts):
`www.google.com`, `www.bing.com`, `duckduckgo.com`, `html.duckduckgo.com`, `lite.duckduckgo.com`,
`en.wikipedia.org`, `r.jina.ai`, `search.marcia.cc`, `www.maff.go.jp`, `www.sii.cl`, `www.conaf.cl`,
`www.leychile.cl`, `www.sea.gob.cl`, `snia.mop.gob.cl`, `vlex.cl`, `www.carey.cl`,
`www.portalinmobiliario.com`, `www.yapo.cl`, `chile.trovit.com`, `www.goplaceit.com`.
Plus `www.beeflambnz.com` via WebFetch.

### What this means

The brief asked for figures tagged `[PRIMARY]` / `[SECONDARY]`. **I have deliberately used
neither tag anywhere in this document**, because attaching a source tag to a number I did not
retrieve would be fabricating a citation. Instead:

| Tag | Meaning | Trust level |
|---|---|---|
| `[EST]` | My derived figure. **Derivation shown inline.** | Use the *logic*; re-run with verified inputs |
| `[RECALL]` | A figure I believe reflects a real published/market number, from analyst prior knowledge (cutoff ~May 2026). **Not retrieved, not verified, may be wrong or stale.** | Treat as a *prior for sizing only* — verify before any decision |
| `[STRUCTURAL]` | A statement about mechanism, law or engineering logic — not a number | Higher confidence; still verify legal points with the legal workstream |

**Nothing here is decision-grade until §E (Verification Queue) has been worked through.**
The durable value of this document is the *model structure, the derivations, and the
questions* — §A7 (three-tier bill of quantities), §B7 (carrying-cost stack), §C11
(revenue ceiling model) and §D (synthesis). The point estimates are scaffolding.

### FX — SINGLE ASSUMPTION BLOCK (verify and re-run everything)

All figures are stated in **local currency** so they survive FX revision. To report in MYR,
update this block only.

**⭐ UPDATED — superseded by the FX/tax analyst's file (`fx-tax-title.md`), which carries
better anchors than my own recall.** Three pairs were supplied in the client brief and are
mutually consistent; the rest are that analyst's derived crosses:

| Pair | 1 unit → MYR | Source |
|---|---|---|
| **1 NZD → MYR** | **2.41511** | `[BRIEF]` via fx-tax-title.md — inverted from MYR→NZD 0.41406 |
| **1 USD → MYR** | **4.03649** | `[BRIEF]` via fx-tax-title.md |
| **100 JPY → MYR** | **2.5379** | `[BRIEF]` via fx-tax-title.md |
| 1 EUR → MYR | 4.36 – 4.84 | `[EST]` derived cross, low confidence |
| 1,000 CLP → MYR | 4.04 – 4.48 | `[EST]` derived cross, low confidence |
| 1 CAD → MYR | 2.78 – 3.03 | `[EST]` derived cross, low confidence |

⚠️ The FX analyst notes these imply a **historically firm ringgit** (USD/MYR ≈ 4.04 against a
multi-year band well above that), and that a **±10–15% swing over 12 months is unremarkable,
±20–30% over a 3–5 year hold well within precedent.** A firm ringgit today makes the land
cheap in MYR but **inflates the MYR cost of every future year of foreign-currency OPEX if it
weakens.** Since this workstream is about *recurring* cost, that asymmetry runs against the
client: **stress-test the carrying cost at a 20–30% weaker ringgit, not just at spot.**

> **Rule for the client deck:** never quote a converted MYR figure without the date of the FX
> rate beside it. A 10% FX move on an NZ$12M purchase is MYR 3.1M.

---

# A. PHASE 1 SKI DEVELOPMENT CAPEX

## A1. Snowcats (piste groomers)

### A1.1 Used machine price bands

Market structure `[STRUCTURAL]`: the used groomer market is thin, dealer-mediated, and
priced almost entirely on **engine hours** and **track/undercarriage condition**, not age.
A 20-year-old machine with 8,000 h and fresh tracks is worth more than a 12-year-old with
18,000 h on worn gear. Principal makes: Kässbohrer **PistenBully** (PB), **Prinoth**
(Husky/Bison/Leitwolf), legacy **Bombardier/LMC** and **Thiokol** in North America.

| Machine | Class | Typical used band | Hours | Tag |
|---|---|---|---|---|
| PistenBully 100 / 100/4F | Compact (~180 hp), narrow — ideal club-field / small private hill | EUR 25,000 – 90,000 | 8,000–15,000 h | `[RECALL]` |
| PistenBully 100, later build | Compact | EUR 90,000 – 160,000 | <5,000 h | `[RECALL]` |
| PistenBully 300 / 300 Polar | Mid workhorse (~250–330 hp) | EUR 30,000 – 95,000 | 10,000–18,000 h | `[RECALL]` |
| PistenBully 300, 2010s build | Mid | EUR 120,000 – 260,000 | 4,000–8,000 h | `[RECALL]` |
| PistenBully 400 | Mid-large | EUR 150,000 – 320,000 | 5,000–10,000 h | `[RECALL]` |
| PistenBully 600 / 600 W (winch) | Large, steep-terrain | EUR 200,000 – 420,000 | 5,000–12,000 h | `[RECALL]` |
| Prinoth Husky | Compact, PB100 analogue | EUR 35,000 – 150,000 | wide | `[RECALL]` |
| Prinoth Bison / Bison X | Mid | EUR 90,000 – 300,000 | wide | `[RECALL]` |
| Prinoth Leitwolf | Large | EUR 180,000 – 400,000 | wide | `[RECALL]` |
| **NEW** PB100 | Compact | EUR 280,000 – 380,000 | 0 h | `[RECALL]` |
| **NEW** PB600 W | Large + winch | EUR 500,000 – 750,000 | 0 h | `[RECALL]` |

**Passenger-cabin cats (for cat-skiing)** `[STRUCTURAL]`: two routes —
(a) factory passenger machines (PistenBully "Paranger"-type, Prinoth passenger variants), or
(b) an **aftermarket 10–14 seat cabin bolted to the rear deck** of a used PB300/400.
Route (b) is how most small cat-ski operations start.

| Item | Cost | Tag |
|---|---|---|
| Aftermarket 12-passenger cabin, fitted | USD 45,000 – 110,000 | `[RECALL]` |
| Engineering sign-off for passenger carriage (NZ: certified seating, restraints, egress) | NZ$ 15,000 – 50,000 | `[EST]` — basis: automotive/LVV-style certification plus structural PE review |
| **Practical entry package: used PB300 + cabin, landed** | EUR 90,000 – 220,000 | `[EST]` — sum of rows above, mid-band |

### A1.2 Running costs — the numbers that actually matter

These are the figures that decide whether a private mountain is affordable. Fuel and
undercarriage dominate; purchase price is a one-off.

| Cost item | Figure | Basis / tag |
|---|---|---|
| Fuel burn, compact cat (~180 hp) | 12 – 20 L/h diesel | `[RECALL]` |
| Fuel burn, mid cat (250–330 hp) working | 20 – 35 L/h diesel | `[RECALL]` |
| Fuel burn, large cat + winch, steep | 30 – 45 L/h | `[RECALL]` |
| **Fuel cost/h @ NZ$1.90/L off-road diesel** | **NZ$ 38 – 67/h** (mid cat) | `[EST]` = 20–35 L/h × NZ$1.90. Diesel price `[RECALL]`, verify |
| Track (belt) set — full replacement | EUR 20,000 – 45,000 | `[RECALL]` |
| Track life | 3,000 – 6,000 h | `[RECALL]` — **halves on rock/dirt contact and early/late season thin cover** |
| **Track cost per hour** | **EUR 4 – 13/h** | `[EST]` = EUR 20–45k ÷ 3,000–6,000 h |
| Grousers/cleats (consumable, replaced piecemeal) | EUR 2,000 – 8,000/yr | `[EST]` |
| Engine rebuild/replacement, at 10,000–15,000 h | EUR 30,000 – 70,000 | `[RECALL]` |
| Hydraulics (pumps/motors) — the other big failure centre | EUR 10,000 – 40,000 per event | `[RECALL]` |
| **All-in maintenance, older working cat** | **EUR 15,000 – 45,000/yr** or ~10–15% of machine value | `[RECALL]` rule of thumb |
| Operator (groom shift, night) NZ | NZ$ 30 – 45/h loaded | `[EST]` — skilled machine operator + night loading |

> **`[EST]` — All-in cat operating cost per hour (mid cat, NZ, Phase 1 private use):**
> fuel NZ$38–67 + tracks NZ$7–24 + other maintenance/reserve NZ$25–60 + operator NZ$30–45
> = **NZ$ 100 – 195 per machine-hour**, excluding capital recovery.
> At 150 grooming hours/season (private, low intensity) = **NZ$ 15,000 – 29,000/yr**.
> At 500 h/season (cat-ski operation) = **NZ$ 50,000 – 98,000/yr**.

### A1.3 Shipping and import

`[STRUCTURAL]` A groomer is ~2.6 m wide with the blade and tiller removed (blade alone is
4.5–6 m), 8–12 t, and too tall/heavy for a standard box. It moves as **RoRo, flat-rack or
breakbulk**, not a standard container. Cost drivers: lift-on/lift-off, out-of-gauge surcharge,
and destination biosecurity.

| Leg / item | Cost | Tag |
|---|---|---|
| Europe → NZ / Chile / Japan, flat-rack or RoRo, one groomer | USD 8,000 – 22,000 | `[EST]` — out-of-gauge heavy-lift band |
| Port handling, customs clearance, inland transport to mountain | USD 3,000 – 10,000 | `[EST]` |
| **NZ MPI biosecurity — pre-shipment cleaning to MPI standard** | NZ$ 2,000 – 8,000 | `[EST]` |
| **NZ MPI — failed inspection → on-arrival cleaning/fumigation** | NZ$ 5,000 – 25,000 + demurrage | `[EST]` — **material risk; used earthmoving/ag machinery into NZ is a known biosecurity chokepoint** `[STRUCTURAL]` |
| NZ GST on import (15% of landed value) | 15% | `[RECALL]` — recoverable if GST-registered |
| Chile: import duty + IVA 19% | ~6% duty + 19% IVA | `[RECALL]` — verify; FTAs may zero the duty |
| Japan: consumption tax 10% + duty | 10% | `[RECALL]` |

> **`[EST]` Landed cost, used mid cat with cabin, to a NZ high-country station:**
> machine EUR 90,000–220,000 (≈ NZ$160,000–390,000) + freight/handling NZ$20,000–55,000
> + biosecurity NZ$2,000–25,000 + GST (recoverable) = **NZ$ 185,000 – 470,000 landed, ex-GST.**

---

## A2. Snowmobiles

| Item | Cost | Tag |
|---|---|---|
| New utility sled (Ski-Doo Skandic/Expedition, Polaris Titan, wide track) | USD 12,000 – 19,000 | `[RECALL]` |
| New mountain sled (Summit, Pro-RMK, Alpha One) | USD 14,000 – 19,000 | `[RECALL]` |
| Used, 3–8 yrs, serviceable | USD 4,000 – 11,000 | `[RECALL]` |
| Cargo/rescue toboggan sled (Otter, Siglin, Ski-Doo LinQ) | USD 500 – 2,800 | `[RECALL]` |
| Fuel burn, working in deep snow | 10 – 20 L/h petrol | `[EST]` — high-load 2/4-stroke ~600–850cc |
| Drive belt (consumable) | USD 120 – 220, several per season in hard use | `[RECALL]` |
| Annual maintenance/consumables per sled, hard use | USD 600 – 1,800/yr | `[EST]` — belts, track, suspension, clutch, oil |
| **Practical Phase 1 fleet: 3 used utility + 1 mountain + 2 tow sleds** | **USD 25,000 – 55,000** | `[EST]` |

`[STRUCTURAL]` Snowmobiles are the highest-leverage Phase 1 asset: they open the terrain,
do the avalanche/rescue and logistics work, tow ski tourers back up on low-angle ground, and
cost ~2% of a groomer. **Recommend the fleet precedes the cat, not follows it.**

---

## A3. Surface lifts — and why the sticker price is the small number

### A3.1 Equipment cost

| Lift type | New, installed | Used equipment only | Tag |
|---|---|---|---|
| **NZ club-field "nutcracker" rope tow** (DIY: diesel engine, drive wheel, sheave poles, wire rope) | NZ$ 30,000 – 180,000 | n/a — usually built | `[EST]` — basis: engine + rope + poles + anchors + volunteer/contract labour split |
| Short beginner/handle tow (proprietary, e.g. conveyor-style or portable rope tow) | USD 25,000 – 90,000 | USD 8,000 – 30,000 | `[RECALL]` |
| Platter / poma (fixed-grip surface, 300–600 m) | USD 450,000 – 1,300,000 | USD 25,000 – 120,000 | `[RECALL]` |
| **T-bar, 500–900 m** (Doppelmayr / Leitner / Skytrac) | USD 1.1M – 2.6M | USD 30,000 – 180,000 | `[RECALL]` |

### A3.2 THE RELOCATION TRAP — quantified `[STRUCTURAL]` + `[EST]`

This is the single most misunderstood number in small ski development, and the brief was
right to flag it. **Buying a second-hand T-bar for USD 60,000 does not give you a
USD 60,000 lift.** The purchase is typically **10–20% of delivered cost**.

Cost stack to relocate one used T-bar (~700 m) onto an undeveloped alpine site:

| Component | Cost | Basis `[EST]` unless noted |
|---|---|---|
| Purchase of used lift (as-standing) | USD 30,000 – 180,000 | `[RECALL]` |
| **Dismantle + tag + crate at origin** | USD 40,000 – 120,000 | Crane/heli time, labour crew, documenting every component for re-erection |
| Transport (origin → site, incl. ocean if imported) | USD 25,000 – 90,000 | Towers are long out-of-gauge loads |
| **Refurbishment** — sheave bearings, gearbox, rope (usually a NEW haul rope), drive, safety circuits | USD 150,000 – 450,000 | Haul rope alone is a major item; used rope is rarely re-certifiable |
| **Foundations** — survey, geotech, drill/rock-anchor, concrete to each tower + drive + return | USD 250,000 – 900,000 | Dominant cost in alpine terrain; concrete may need helicopter placement |
| **Helicopter placement** (towers, concrete, drive) | USD 60,000 – 300,000 | Heavy-lift heli hire `[RECALL]` NZ$3,000–8,000/h; 20–60 h |
| Electrical supply + controls (new PLC/safety system almost always required) | USD 120,000 – 400,000 | Old control systems will not certify |
| **Engineering design, verification, certification** | USD 80,000 – 250,000 | Design verification by a recognised ropeway engineer + as-built certification |
| Site works, access track to towers, drainage | USD 40,000 – 150,000 | |
| Contingency @ 20% | — | Mandatory on relocations; unknowns are discovered at dismantle |
| **DELIVERED TOTAL, relocated used T-bar** | **USD 800,000 – 2,600,000** | `[EST]` sum + contingency |

> **Conclusion `[EST]`: a relocated second-hand T-bar costs 70–100% of a new one.**
> The used-lift market saves money only when (i) the lift is close by, (ii) the receiving
> site already has road access, power and foundations-friendly ground, and (iii) you have
> in-house engineering. **For a greenfield alpine site, buying new is often cheaper and
> always lower-risk.** The genuine Phase 1 answer is a **rope tow**, not a T-bar.

`[STRUCTURAL]` **Regulatory tail (coordinate with legal workstream):** in NZ, passenger
ropeways — including surface lifts and, on the face of it, club rope tows — fall under
the amusement-devices/passenger-ropeway regime administered by WorkSafe NZ, requiring
design verification, registration, and **annual inspection/certification by a recognised
engineer**. Budget `[EST]` **NZ$ 8,000 – 30,000/yr** per lift in inspection and
certification, plus the design verification cost at build. *A private/members-only status
does not obviously remove this — legal workstream must confirm.* This recurring cost is
a strong argument for staying rope-tow-only or lift-free in Phase 1.

---

## A4. Chairlift — Phase 3 reference point only

| Item | Cost | Tag |
|---|---|---|
| Fixed-grip double, 800–1,200 m, installed | USD 2.5M – 5.5M | `[RECALL]` |
| **Fixed-grip quad, 1,000–1,500 m, installed** | **USD 3.5M – 8M** | `[RECALL]` |
| Per-metre, fixed-grip, installed, alpine greenfield | USD 3,000 – 5,500 /m | `[EST]` = row above ÷ length |
| Detachable quad / six-pack | USD 10M – 28M | `[RECALL]` |
| Annual lift maintenance + certification, per fixed-grip lift | USD 60,000 – 180,000/yr | `[EST]` — mechanic time, NDT rope testing, parts, inspection |

`[STRUCTURAL]` Costs in this sector rose steeply post-2020 (steel, freight, electrical
components, specialist labour). Any figure older than ~2022 understates materially.

> **THE GAP, stated plainly `[EST]`:** the entire Tier-3 Phase 1 programme (§A7) lands at
> **NZ$ 1.6M – 4.6M**. **One** new fixed-grip quad is **NZ$ 6M – 14M** plus
> NZ$100k–300k/yr to run. A real resort is not an incremental step from Phase 1 —
> it is a different asset class requiring a different capital structure and, critically,
> a *public* consenting pathway the private model avoids entirely.

---

## A5. Access, services and base infrastructure

### A5.1 Roads and access

| Item | Cost | Tag |
|---|---|---|
| 4WD track formation, easy rolling country (dozer-formed, no structures) | NZ$ 15,000 – 45,000 /km | `[EST]` |
| 4WD track, steep alpine sidling — benching, rock, drainage | NZ$ 70,000 – 220,000 /km | `[EST]` — machine hours dominate; rock breaking or blasting escalates fast |
| Engineered all-weather access road (resort standard, 2-lane, gravel) | NZ$ 400,000 – 1,200,000 /km | `[EST]` |
| Culvert, installed (0.6–1.2 m) | NZ$ 1,500 – 7,000 each | `[EST]` |
| Annual track maintenance (grading, washouts, drainage) | NZ$ 2,500 – 9,000 /km/yr | `[EST]` — high variance; a single storm event can exceed a decade of routine spend |
| Snow clearing — contract loader/grader | NZ$ 180 – 400 /h | `[EST]` |
| Snow clearing — own loader (used wheel loader w/ blade) | NZ$ 60,000 – 180,000 capital | `[RECALL]` |

`[STRUCTURAL]` **Avalanche-safe alignment is a design decision with a large cost consequence.**
Routing a road *out* of runout zones — even at the cost of extra length and switchbacks —
avoids the alternative: an active avalanche-control programme over the road (see §A6),
seasonal closure protocols, and an exposure that insurers and regulators both price. On a
private mountain the correct answer is almost always **relocate the road, accept the extra
kilometre**. Rule of thumb `[EST]`: 1 extra km of track (NZ$70k–220k, one-off) versus a
road avalanche-control programme (NZ$100k+/yr recurring plus explosives licensing) —
**the road relocation pays back in under 2 years.**

### A5.2 Off-grid power

Sizing `[EST]` for a base hut (6–10 beds) + workshop with hand tools and a compressor:
daily demand 10–18 kWh, peak 6–9 kW, with winter solar yield at high latitude/altitude
**as low as 15–25% of summer yield** (short days, low sun angle, panel snow cover).

| Component | Spec | Cost (NZ) | Tag |
|---|---|---|---|
| Solar array | 8 – 14 kW (oversized for winter) | NZ$ 12,000 – 26,000 | `[EST]` |
| Battery | 25 – 45 kWh LFP | NZ$ 15,000 – 40,000 | `[EST]` |
| Inverter/charger + MPPT + switchgear | 6 – 10 kW | NZ$ 8,000 – 20,000 | `[EST]` |
| Backup diesel genset, auto-start | 10 – 20 kVA | NZ$ 12,000 – 35,000 | `[EST]` |
| Install, mounting (snow/wind rated), cabling, shed | — | NZ$ 15,000 – 45,000 | `[EST]` |
| **TOTAL off-grid power** | | **NZ$ 62,000 – 166,000** | `[EST]` |
| Genset fuel + servicing, winter-heavy | 400–1,500 L/yr | NZ$ 1,500 – 6,000/yr | `[EST]` |
| Battery replacement reserve (10–15 yr life) | — | NZ$ 1,500 – 4,000/yr | `[EST]` |

`[STRUCTURAL]` **Snow-covered panels produce zero.** Steep-tilt or vertical bifacial mounting,
and physical access to sweep, matter more than array size at an alpine site. A micro-hydro
supplement (§C10) is transformative where a stream with head exists — it produces *most* in
winter/spring, exactly counter-cyclical to solar.

### A5.3 Water

| Item | Cost (NZ) | Tag |
|---|---|---|
| Spring/stream intake + gravity-fed pipeline (cheapest, preferred) | NZ$ 6,000 – 30,000 | `[EST]` |
| Bore drilling | NZ$ 180 – 420 /m | `[EST]` |
| Bore, 60 m + pump + headworks | NZ$ 20,000 – 55,000 | `[EST]` |
| Storage 25,000–30,000 L (freeze-protected/buried) | NZ$ 4,000 – 12,000 | `[EST]` |
| Filtration + UV treatment (potable, commercial-grade if guests) | NZ$ 4,000 – 14,000 | `[EST]` |
| **TOTAL water, spring-fed** | **NZ$ 14,000 – 56,000** | `[EST]` |

`[STRUCTURAL]` Water **take** may require a regional council resource consent depending on
volume and whether it is for commercial use — legal workstream. Winter freeze protection
(buried lines below frost, trace heating, drain-down design) is a real design cost usually
omitted from budgets.

### A5.4 Communications

| Item | Cost | Tag |
|---|---|---|
| Starlink hardware (standard / high-performance) | NZ$ 400 – 1,400 | `[RECALL]` |
| Starlink service plan (residential → priority/mobile tiers) | NZ$ 80 – 400+ /month | `[RECALL]` — verify current NZ plan tiers |
| VHF handheld radios, commercial grade | NZ$ 450 – 1,300 each | `[EST]` |
| Base station + antenna | NZ$ 2,500 – 7,000 | `[EST]` |
| **Solar-powered VHF repeater on a ridge** (mast, solar, battery, hut, heli install) | NZ$ 12,000 – 40,000 | `[EST]` |
| Satellite messenger / PLB per party (inReach etc.) | NZ$ 500 – 900 + plan | `[RECALL]` |

`[STRUCTURAL]` **Radio, not cellular or satellite internet, is the safety-critical system.**
Starlink is a base-camp convenience; a VHF repeater with ridge-to-valley coverage is what
makes a rescue work. Budget it as safety CAPEX, not IT.

### A5.5 Base building — cost per m²

| Country | Build type | Cost /m² | Tag |
|---|---|---|---|
| **NZ** | Container conversion | NZ$ 1,600 – 3,600 | `[EST]` |
| **NZ** | Relocatable/transportable cabin, delivered | NZ$ 2,200 – 4,800 | `[EST]` |
| **NZ** | Built on site, alpine (snow + wind loading, heli-assisted delivery, remote labour) | NZ$ 4,500 – 9,000 | `[EST]` — alpine remoteness premium of 40–100% over urban `[STRUCTURAL]` |
| **Japan** | Simple timber building, rural | ¥ 220,000 – 480,000 | `[EST]` |
| **Japan** | Heavy-snow-region spec (Hokkaido/Tohoku, high snow load) | ¥ 350,000 – 650,000 | `[EST]` |
| **Chile** | Simple rural construction | CLP 700,000 – 1,500,000 | `[EST]` |

> **`[EST]` Phase 1 base hut, NZ, 80 m² relocatable + siting + services:**
> building NZ$180,000–380,000 + foundations/siting NZ$25,000–70,000 + power NZ$62,000–166,000
> + water NZ$14,000–56,000 + wastewater NZ$15,000–45,000 = **NZ$ 296,000 – 717,000.**
> A container-based workshop/garage for the cat adds **NZ$ 60,000 – 180,000** `[EST]`
> (the cat must be stored under cover and plugged in, or it will not start).

---

## A6. Safety, snow-safety and the avalanche-control cost being avoided

| Item | Cost | Tag |
|---|---|---|
| Avalanche transceiver (modern 3-antenna) | NZ$ 500 – 950 each | `[RECALL]` |
| Avalanche airbag pack | NZ$ 1,200 – 2,200 each | `[RECALL]` |
| Probe + shovel set | NZ$ 150 – 300 per set | `[RECALL]` |
| **Guest safety kit, 12 guests + 3 staff (transceiver/probe/shovel/airbag)** | **NZ$ 30,000 – 52,000** | `[EST]` = 15 × (700 + 225 + 1,700) mid-band |
| Rescue toboggan (Cascade/Sled-type) | NZ$ 3,000 – 9,000 each | `[EST]` |
| First aid — trauma kits, oxygen, vacuum splints, AED | NZ$ 8,000 – 25,000 | `[EST]` |
| Signage, boundary marking, hazard marking | NZ$ 5,000 – 25,000 | `[EST]` |
| **Automatic weather station** (wind, temp, snow depth, telemetry) | NZ$ 18,000 – 55,000 installed | `[EST]` |
| Snow study plot equipment | NZ$ 3,000 – 10,000 | `[EST]` |
| **Annual snow-safety programme** (forecaster time, daily obs, record-keeping, InfoEx-type participation) | **NZ$ 55,000 – 160,000/yr** | `[EST]` — 1 seasonal forecaster + guide obs time |
| Ski patroller / guide wage, NZ | NZ$ 28 – 45 /h | `[EST]` |
| IFMGA/NZMGA-qualified guide, day rate | NZ$ 550 – 1,000 /day | `[RECALL]` |

### The "what we are avoiding" figure `[EST]`

| Avoided item | Capital | Recurring |
|---|---|---|
| **Gazex-type remote avalanche exploder, per unit installed** (unit, shelter, gas pipework, foundations, heli) | NZ$ 180,000 – 450,000 each | — |
| A working system for one road + one face (6–10 exploders) | **NZ$ 1.1M – 4.5M** | NZ$ 60,000 – 180,000/yr gas, servicing, inspection |
| Explosives programme alternative (hand charges / avalauncher) | NZ$ 60,000 – 250,000 setup (magazine construction, avalauncher) | NZ$ 40,000 – 150,000/yr explosives, licensing, training, audit |
| Licensed-explosives compliance burden (NZ: controlled-substances licensing, secure magazine, personnel vetting, record-keeping, audit) | — | `[STRUCTURAL]` significant management overhead, not just cash |

> **KEY STRATEGIC FINDING `[STRUCTURAL]`:** the decision to ski **low-angle, low-consequence
> terrain** (roughly <30° with benign runouts and no overhead hazard) is worth
> **NZ$1.1M–4.5M of avoided capital and NZ$100k–330k/yr of avoided operating cost**, and it
> removes an entire licensing regime from the business. This should be a *stated design
> constraint on the property search*, not an operational afterthought — it means the
> shortlist should favour **broad, moderate-angle, above-treeline basins** over steep,
> dramatic, high-consequence faces. Communicate this to the listings analyst: **terrain
> angle distribution is an economic screening criterion, not just a skiing one.**

---

## A7. PHASE 1 CAPEX — BILL OF QUANTITIES, THREE TIERS

All NZ$, excluding GST, excluding land. `[EST]` throughout — sums of the line items above.

### TIER 1 — "Minimum Viable Private Mountain"
*Ski touring + snowmobiles + a hut. No grooming, no lifts. Uses existing farm tracks.*

| Line | Low | High |
|---|---|---|
| Snowmobile fleet (3 utility + 1 mountain + 2 tow sleds, used/new mix) | 110,000 | 240,000 |
| Touring equipment, 8 sets (skis/skins/boots — or guests bring own) | 0 | 40,000 |
| Safety kit — transceivers, airbags, probes, shovels, toboggans, first aid | 25,000 | 60,000 |
| Radios + base station + 1 ridge repeater | 20,000 | 55,000 |
| Base hut 80 m² relocatable, sited + services (power/water/wastewater) | 296,000 | 717,000 |
| Track upgrade / winter access improvement, 3 km | 45,000 | 200,000 |
| Basic weather station + obs setup | 20,000 | 60,000 |
| Tools, workshop fit-out, fuel storage (bunded diesel tank) | 25,000 | 70,000 |
| Contingency 15% | 81,000 | 216,000 |
| **TIER 1 TOTAL** | **NZ$ 622,000** | **NZ$ 1,658,000** |

### TIER 2 — "Snowcat-Served Private Mountain"
*Tier 1 + a used groomer with passenger cabin + covered workshop + real snow-safety.*

| Line | Low | High |
|---|---|---|
| Tier 1 subtotal (ex contingency) | 541,000 | 1,442,000 |
| Used mid snowcat + passenger cabin, landed NZ (§A1.3) | 185,000 | 470,000 |
| Covered workshop / cat shed (container or portal frame) | 60,000 | 180,000 |
| Cat spares inventory (belt, filters, hoses, hydraulic stock) | 15,000 | 45,000 |
| Additional track/benching for cat access & turnarounds | 60,000 | 220,000 |
| Upgraded snow-safety: AWS, study plot, forecasting setup | 25,000 | 75,000 |
| Passenger-carriage engineering certification | 15,000 | 50,000 |
| Contingency 18% | 162,000 | 447,000 |
| **TIER 2 TOTAL** | **NZ$ 1,063,000** | **NZ$ 2,929,000** |

### TIER 3 — "Private Club with One Surface Lift"
*Tier 2 + a rope tow (NOT a relocated T-bar) + guest-capable lodge + compliance.*

| Line | Low | High |
|---|---|---|
| Tier 2 subtotal (ex contingency) | 901,000 | 2,482,000 |
| Rope tow / nutcracker tow, 400–600 m, installed | 30,000 | 180,000 |
| Lift design verification, registration, first certification | 25,000 | 90,000 |
| Power supply to lift (extended off-grid or genset at drive) | 20,000 | 70,000 |
| Lodge upgrade to guest standard (+80 m², kitchen, fire, accessibility) | 250,000 | 700,000 |
| Wastewater upgrade to commercial standard | 30,000 | 90,000 |
| Signage, boundary, guest safety systems | 15,000 | 45,000 |
| Contingency 20% | 254,000 | 731,000 |
| **TIER 3 TOTAL** | **NZ$ 1,525,000** | **NZ$ 4,388,000** |

> **If a relocated second-hand T-bar were substituted for the rope tow in Tier 3, add
> NZ$ 2.0M – 6.6M `[EST]` (§A3.2) — i.e. it would roughly TRIPLE Tier 3.** This is the
> decisive Phase 1 capital-discipline call.


---

# B. ANNUAL OPEX / CARRYING COST

## B1. Land rates / property tax

### New Zealand — council rates on a high-country station

`[STRUCTURAL]` NZ rates are levied by district/regional councils on land value (LV) or capital
value (CV), with **differentials by land use**. Pastoral/rural differentials are generally
*lower* per dollar of value than residential or commercial. Two consequences that matter here:

1. **A station's rates are driven by its rateable value, which is driven by its productive
   capacity — not by its scenic or ski value.** Remote alpine country carries a low LV.
2. **Converting use (farm → tourism/commercial ski) can trigger a differential change and a
   revaluation.** A commercial ski operation may be rated on a commercial differential over
   the developed area. This is a real Phase 2/3 cost step, easily 2–5× the rural rate on the
   affected land `[EST]`.

| Holding | Annual rates | Tag |
|---|---|---|
| Large South Island pastoral station, 5,000–15,000 ha, low-value alpine country (Mackenzie / Waitaki / Central Otago districts) | NZ$ 15,000 – 55,000 /yr | `[EST]` — basis: rural differential on a low LV plus fixed/uniform charges; **must be replaced with the actual rates assessment from the LIM/vendor for any specific property** |
| Same, but in a high-rating district (e.g. Queenstown Lakes) or with high CV from amenity/lifestyle value | NZ$ 40,000 – 150,000 /yr | `[EST]` |
| Regional council rates (catchment/biosecurity levies) — additional | NZ$ 3,000 – 25,000 /yr | `[EST]` |

> **Action:** rates are one of the few carrying costs that can be established *exactly and
> cheaply* pre-offer — the rates assessment is public and on the LIM. **Do not model this;
> obtain it.**
>
> ✅ **Independent cross-check:** the FX/tax analyst (`fx-tax-title.md`) independently estimated
> NZ high-country rates at **NZD 1.5 – 6 /ha/yr**, i.e. **NZ$12,000 – 48,000/yr on 8,000 ha**.
> That sits inside my NZ$15,000–55,000 band — **two independent estimates agree**, which raises
> confidence in this line specifically. That analyst also flags that **if any part of the title
> is Crown pastoral lease, Crown rent is payable in addition** under the CPLA 1998 (as amended
> 2022) — a line I had not captured. **Add Crown rent as a separate carrying-cost item for any
> leasehold component.**

### Japan — 固定資産税 (fixed asset tax) on 山林 / 原野

`[STRUCTURAL]` This is the standout finding for Japan and it is *structural*, not a market view:

- Standard 固定資産税 rate is **1.4%** of the 課税標準額 (taxable assessed value) `[RECALL]`,
  set by the municipality. 都市計画税 (city planning tax, ~0.3%) generally does **not** apply to
  forest land outside urban planning areas `[RECALL]`.
- **山林 (forest land) and 原野 (wasteland/moor) are assessed at extremely low values** — orders of
  magnitude below residential land — because assessment follows productive/market value and
  Japanese rural forest land has very little of either `[STRUCTURAL]`.
- There is a **免税点 (tax-free threshold)**: if a person's total assessed land value within one
  municipality falls below ¥300,000, no fixed asset tax is levied `[RECALL]`. Many forest
  holdings fall under it entirely.

| Item | Figure | Tag |
|---|---|---|
| 固定資産税 standard rate | 1.4% of assessed value | `[RECALL]` |
| Typical 山林 assessed value | ¥ 30,000 – 250,000 /ha | `[RECALL]` — very wide; verify with a 固定資産税評価証明書 |
| **⇒ Effective tax** | **¥ 400 – 3,500 /ha/yr** | `[EST]` = 1.4% × assessed value |
| **⇒ On 8,000 ha** | **¥ 3.2M – 28M /yr** (≈ NZ$ 35,000 – 300,000) | `[EST]` — *but* much alpine land in Japan is national park / national forest and not privately held at all |

> **`[STRUCTURAL]` Japan's real barrier is not holding cost — it is availability and
> fragmentation.** High alpine land is overwhelmingly 国有林 (national forest) or national park.
> Private forest holdings are small, fragmented, and often have **unknown or untraceable owners**
> (所有者不明土地 — a nationally recognised problem that prompted the 2019 森林経営管理制度 and the
> 2024 compulsory inheritance-registration reform `[RECALL]`). Assembling 8,000 contiguous
> private hectares in the Japanese Alps or Hokkaido is likely **impossible**, not merely expensive.
> **Flag to the listings analyst as a probable knock-out for Japan.**

### Chile — contribuciones (impuesto territorial)

| Item | Figure | Tag |
|---|---|---|
| Rate on predios agrícolas (agricultural) | ~1% of avalúo fiscal /yr | `[RECALL]` — verify current SII schedule and surcharges |
| Exemption threshold for agricultural property | exists; a portion of avalúo is exempt | `[RECALL]` — verify amount |
| Avalúo fiscal on remote cordillera / secano land | very low per ha | `[STRUCTURAL]` — assessment follows productive value |
| **⇒ Carrying tax on a large Andean holding** | **plausibly the lowest of the three countries in absolute terms** | `[EST]` |

`[STRUCTURAL]` Chile's carrying costs are low but its **water rights (derechos de aprovechamiento
de aguas), native forest law (Ley 20.283) and access/servidumbre issues** are the substantive
constraints — legal workstream. The 2022 water code reform changed permits from perpetual to
temporally limited `[RECALL]` — verify, it affects long-run asset value.

### United States — ranch property tax (reference only)

| State | Character | Tag |
|---|---|---|
| Wyoming, Montana, Idaho | Agricultural-use valuation keeps effective tax low **while the land qualifies as agricultural** | `[STRUCTURAL]` |
| Colorado | Ag land assessed on earning capacity — very low; **but recreational/resort reclassification can raise it dramatically** | `[STRUCTURAL]` |
| **Universal US risk** | **Converting a ranch to a private ski/recreational use can strip agricultural classification and multiply the tax bill.** | `[STRUCTURAL]` — this, plus §B2 liability, is why the US is the worst jurisdiction for this specific plan |

---

## B2. INSURANCE — the decisive jurisdictional difference

This is, in my assessment, **the most important non-obvious economic finding in the whole
workstream**, and it runs strongly in favour of New Zealand.

### New Zealand — the ACC bar `[STRUCTURAL]`

- The **Accident Compensation Act 2001** establishes a universal, no-fault personal injury
  compensation scheme funded by levies.
- In exchange, the Act **bars proceedings for compensatory damages for personal injury**
  covered by the scheme (the statutory bar, s 317). A guest injured skiing on a NZ mountain
  **cannot sue the operator for damages for that injury.**
- Residual exposures that remain:
  1. **Exemplary (punitive) damages** — available but rare and require outrageous conduct.
  2. **Property damage** and **non-personal-injury** claims.
  3. **⚠️ Health and Safety at Work Act 2015 prosecution** — this is the real risk. A PCBU
     owes duties to workers *and* to others affected by its work. Penalties run to
     **NZ$1.5M for a reckless-conduct offence by a body corporate**, plus **reparation orders
     to victims** `[RECALL] — verify current penalty bands`. Directors/officers have a
     personal due-diligence duty with personal penalties.
  4. **Building/consent and ropeway compliance liability.**

> **⇒ The NZ risk profile is: near-zero tort liability for guest injury, but real regulatory
> criminal liability for the operator and its officers.** The insurance product needed is
> therefore **statutory liability / HSWA defence cover and D&O**, not a large public liability
> tower. That is a *much cheaper* combination. `[STRUCTURAL]`
>
> ✅ **Independent cross-check:** the NZ regulatory analyst reached the same conclusion
> independently — *"With ACC removing compensatory personal-injury claims, the insurance
> requirement is materially narrower than in the US/Europe: statutory liability …, property/
> material damage on remote alpine assets, plant and machinery (snowcats are expensive and hard
> to insure remotely), business interruption, and employers' liability gap cover."* They add
> two lines I had not: **business interruption** and the point that **snowcats are hard to
> insure in remote locations** — budget for a higher plant rate or a deductible, and get a
> **NZ broker quote early**, as this is not commodity business.

### United States — the liability barrier

`[STRUCTURAL]` The US position is the mirror image. Ski-area statutes (e.g. Colorado's Ski
Safety Act and equivalents in most ski states) codify inherent-risk assumption and limit some
claims, but they **do not prevent suits**; litigation is frequent, discovery is expensive, and
defence costs are borne even on won cases. Liability insurance availability and cost are
widely reported as an existential issue for **small, independent US ski areas**, with the
market having contracted to a handful of willing carriers.

| Jurisdiction | Indicative annual liability premium, small ski operation | Tag |
|---|---|---|
| **USA**, small independent ski area | **USD 60,000 – 350,000+ /yr** | `[EST]` — basis: repeatedly reported as a leading cause of small-area closure; scales with skier visits and lift count |
| **NZ**, small private ski operation (statutory liability + D&O + property + motor) | **NZ$ 25,000 – 80,000 /yr** | `[EST]` — basis: ACC bar removes the guest-injury damages layer |
| **Japan**, 施設賠償責任保険 (facility liability) | modest; low tort damages environment | `[EST]` — but note Japan has produced **criminal** negligence prosecutions arising from skiing collisions and avalanche incidents `[RECALL]` |
| **Chile** | Intermediate; smaller insurance market, may require offshore placement | `[EST]` |

> **`[EST]` The NZ-vs-US insurance delta alone is plausibly USD 40,000–280,000/yr — over a
> 20-year hold, USD 0.8M–5.6M in present-cost terms. For a private mountain, this difference
> is larger than the entire Tier 1 CAPEX.** It is the strongest economic argument for NZ,
> and it *partially offsets* the OIO consenting difficulty the properties analyst identifies.

**Other insurance lines to budget** `[EST]`:

| Line | NZ$ /yr |
|---|---|
| Property/material damage on buildings + plant (remote, no fire service → high rate) | 8,000 – 30,000 |
| Snowcat & mobile plant (specified items) | 4,000 – 15,000 |
| Motor fleet | 3,000 – 10,000 |
| Statutory liability / HSWA defence + D&O | 6,000 – 25,000 |
| Public/products liability (residual) | 4,000 – 15,000 |
| **Total insurance, NZ private mountain** | **25,000 – 95,000** |

---

## B3. Staff — minimum viable crew

| Role | Model | NZ cost /yr | Tag |
|---|---|---|---|
| **Caretaker / station manager** (year-round, on-site, housed) | 1 FTE | NZ$ 75,000 – 130,000 + housing | `[EST]` |
| **Cat operator / diesel mechanic** (the critical hire — must be both) | 1 seasonal-to-FT | NZ$ 70,000 – 110,000 | `[EST]` |
| **Lead guide / snow safety** (qualified) | seasonal, 100 days | NZ$ 55,000 – 100,000 | `[EST]` = ~NZ$550–1,000/day × 100 |
| **Second guide** (required for rescue redundancy) `[STRUCTURAL]` | seasonal, 100 days | NZ$ 45,000 – 85,000 | `[EST]` |
| Casual/shoulder labour (fencing, tracks, pest control) | 0.5 FTE | NZ$ 25,000 – 45,000 | `[EST]` |
| **MINIMUM CREW, snowcat private operation** | **~3.5 FTE** | **NZ$ 270,000 – 470,000 /yr** | `[EST]` |

`[STRUCTURAL]` **Two guides is not optional.** A single guide cannot run a companion rescue
while also managing a group and the machine. Any model showing one guide is not a real model.

### Wage reference points

| Country | Reference | Tag |
|---|---|---|
| NZ adult minimum wage | ~NZ$ 23.50 /h (2025-26) | `[RECALL]` — verify current rate |
| NZ station hand | NZ$ 55,000 – 78,000 /yr | `[EST]` |
| NZ farm/station manager | NZ$ 90,000 – 150,000 /yr + house | `[EST]` |
| Japan 最低賃金 (national weighted average) | ~¥ 1,050 – 1,180 /h (2024-26) | `[RECALL]` — rising fast; Hokkaido below national average; verify |
| Chile sueldo mínimo | ~CLP 500,000 – 560,000 /month | `[RECALL]` — verify |

> `[STRUCTURAL]` **Chile is by far the cheapest labour of the three; NZ the most expensive
> in absolute terms but with the deepest pool of qualified alpine guides and cat operators
> (a genuine operational advantage). Japan has the labour cost of NZ with a much thinner
> pool of English-capable mountain guides.**

---

## B4. Land management — the NZ pest and weed liability

`[STRUCTURAL]` **This is an inherited legal liability, not a discretionary cost.** Under
regional pest management plans made under the Biosecurity Act 1993, occupiers can be
**directed to control** listed pest plants and animals, with cost recovery if the council
does the work. A buyer inherits the infestation and the obligation. **This must be a
due-diligence line item with a physical inspection, not a budget assumption.**

### Wilding conifers

| Situation | Control cost | Tag |
|---|---|---|
| Scattered/outlier trees, ground control (search & fell, basal treatment) | NZ$ 30 – 150 /ha | `[EST]` |
| Moderate density, mixed ground + aerial | NZ$ 150 – 600 /ha | `[EST]` |
| Dense infestation, aerial boom spray / heli operations | NZ$ 600 – 2,500 /ha | `[EST]` |
| **Follow-up cycle** (mandatory — seed bank re-infests) | every 2–4 yrs, ~30–50% of initial | `[STRUCTURAL]` |
| **⇒ 8,000 ha station, 1,500 ha lightly infested, initial programme** | **NZ$ 45,000 – 900,000 one-off** | `[EST]` = 1,500 ha × NZ$30–600 |
| **⇒ Annualised maintenance thereafter** | **NZ$ 25,000 – 180,000 /yr** | `[EST]` |

> ⚠️ **A wilding-infested station is a materially impaired asset.** The National Wilding
> Conifer Control Programme exists precisely because the problem outruns landowners
> `[RECALL]`. **Ask the listings analyst to add "wilding conifer density" as a screening
> field on every NZ candidate** — it can be assessed from aerial imagery before any site
> visit and can swing the economics by NZ$1M+.
>
> **Note the direct conflict with §C3 (carbon forestry):** the same species that pays the
> carbon money is the pest you are legally obliged to control. Planting *Pinus contorta*
> is illegal-adjacent; even radiata plantations adjacent to alpine country create wilding
> spread liability and are increasingly opposed in consenting. **These two revenue lines
> are not simply additive.**

### Rabbits (Central Otago / Mackenzie)

| Item | Cost | Tag |
|---|---|---|
| Rabbit control in prone country (night shooting, Pindone/1080 carrot, fumigation, RHDV) | NZ$ 12 – 70 /ha/yr on affected area | `[EST]` |
| **⇒ 2,000 ha of rabbit-prone lower country** | **NZ$ 24,000 – 140,000 /yr** | `[EST]` |

`[STRUCTURAL]` Rabbit-prone semi-arid Central Otago country is notorious; RHDV immunity has
eroded biological control effectiveness. Also budget: **hares, hieracium/hawkweed (Mackenzie),
broom/gorse, wallabies (South Canterbury), feral pigs/deer/goats/possums.**

---

## B5. Other operating costs

| Item | NZ$ /yr, 8,000 ha station | Tag |
|---|---|---|
| Vehicle & machinery running (utes, quads, tractor, loader) — fuel, tyres, servicing | 35,000 – 85,000 | `[EST]` |
| Machinery depreciation/replacement reserve | 30,000 – 90,000 | `[EST]` |
| Track & road maintenance (20–40 km of farm track) | 30,000 – 120,000 | `[EST]` = §A5.1 rate × length |
| Fencing & water infrastructure maintenance | 15,000 – 60,000 | `[EST]` |
| Buildings maintenance | 10,000 – 40,000 | `[EST]` |
| Power, fuel, comms (off-grid) | 8,000 – 25,000 | `[EST]` |
| Accounting, tax, audit | 8,000 – 30,000 | `[EST]` |
| Legal & compliance (consents, renewals, reporting) | 8,000 – 40,000 | `[EST]` |
| **Overseas-owner compliance overhead** (OIO consent conditions monitoring & annual reporting) `[STRUCTURAL]` | 10,000 – 50,000 | `[EST]` — **a cost specific to this buyer**; OIO consents carry ongoing conditions and reporting obligations that must be actively managed, with penalties for breach |
| Insurance (§B2) | 25,000 – 95,000 | `[EST]` |

---

## B6. Phase 1 ski operating add-on (incremental to holding the land)

| Item | NZ$ /yr | Tag |
|---|---|---|
| Snowcat operating, 150–500 h (§A1.2) | 15,000 – 98,000 | `[EST]` |
| Snowmobile fleet operating | 6,000 – 20,000 | `[EST]` |
| Guides (2, seasonal) — from §B3 | 100,000 – 185,000 | `[EST]` |
| Snow-safety programme (§A6) | 55,000 – 160,000 | `[EST]` |
| Safety equipment replacement/servicing reserve | 8,000 – 25,000 | `[EST]` |
| Incremental insurance for ski activity | 10,000 – 40,000 | `[EST]` |
| Rope tow annual inspection & certification (Tier 3 only) | 8,000 – 30,000 | `[EST]` |
| **PHASE 1 SKI OPEX ADD-ON** | **NZ$ 194,000 – 558,000 /yr** | `[EST]` |

> **`[EST]` Stripped-back variant** — owner-operated, no employed guides, ski-touring only,
> guests are experienced friends carrying their own risk, no commercial snow-safety programme:
> **NZ$ 25,000 – 70,000 /yr.** *This is the true "Phase 1 minimum" and it is genuinely cheap.
> The cost explosion between this and the table above is caused entirely by **carrying
> third-party guests**, which triggers staffing, snow safety and insurance.* **The single
> biggest operating-cost lever available to this client is to keep Phase 1 strictly private
> and non-commercial for as long as possible.**

---

## B7. CARRYING-COST SUMMARY — 5,000–15,000 ha alpine property

### New Zealand (NZ$/yr) — modelled at 8,000 ha

| Line | Low | High |
|---|---|---|
| District + regional rates | 18,000 | 80,000 |
| Insurance | 25,000 | 95,000 |
| Staff (caretaker + part-time labour, NO ski crew) | 100,000 | 175,000 |
| Vehicles, machinery, depreciation reserve | 65,000 | 175,000 |
| Tracks, fences, water, buildings maintenance | 55,000 | 220,000 |
| Pest & weed control (wildings + rabbits) | 49,000 | 320,000 |
| Power, fuel, comms | 8,000 | 25,000 |
| Accounting, legal, compliance, OIO condition management | 26,000 | 120,000 |
| **BASELINE CARRY, land only, no skiing** | **NZ$ 346,000** | **NZ$ 1,210,000** |
| Phase 1 ski add-on — private/minimal (§B6 stripped) | 25,000 | 70,000 |
| **CARRY WITH PRIVATE SKIING (Tier 1–2, non-commercial)** | **NZ$ 371,000** | **NZ$ 1,280,000** |
| Phase 1 ski add-on — guest-carrying (§B6 full) | 194,000 | 558,000 |
| **CARRY WITH GUEST-CARRYING OPERATION** | **NZ$ 540,000** | **NZ$ 1,768,000** |

`[EST]` **Central planning figure for NZ, 8,000 ha, private skiing: ~NZ$ 600,000 – 750,000/yr.**
Scale roughly with area for the land-management lines (pest, tracks, fences) and hold the
fixed lines (staff, insurance, compliance) constant: a 5,000 ha property is perhaps 15% cheaper,
a 15,000 ha property perhaps 40% dearer — **not proportional**, because the fixed overhead
dominates. `[STRUCTURAL]` **⇒ Bigger is disproportionately cheaper per hectare. Do not
buy small to save carry.**

### Japan (¥/yr) — modelled at 8,000 ha (hypothetical — see availability caveat)

| Line | Low | High |
|---|---|---|
| 固定資産税 (§B1) | 3,200,000 | 28,000,000 |
| Insurance (施設賠償責任 + 火災 + 車両) | 1,500,000 | 6,000,000 |
| Staff (1 caretaker + seasonal) | 5,000,000 | 11,000,000 |
| Forest management obligations (森林経営計画 upkeep, 作業道 maintenance) | 3,000,000 | 15,000,000 |
| Machinery, vehicles, fuel | 3,000,000 | 9,000,000 |
| Roads/access (heavy snow country — snow removal is a major line) | 3,000,000 | 14,000,000 |
| Accounting, legal, compliance (+ foreign-owner complexity) | 1,500,000 | 6,000,000 |
| **JAPAN BASELINE CARRY** | **¥ 20.2M** | **¥ 89M** |
| | *(≈ NZ$ 212k – 935k)* | |

### Chile (CLP/yr) — modelled at 8,000 ha

| Line | Low | High |
|---|---|---|
| Contribuciones | 2,000,000 | 15,000,000 |
| Insurance | 6,000,000 | 22,000,000 |
| Staff (capataz + 2 workers — cheapest of the three) | 18,000,000 | 42,000,000 |
| Machinery, vehicles, fuel | 12,000,000 | 35,000,000 |
| Roads/access maintenance | 10,000,000 | 40,000,000 |
| Fencing, water rights administration, guardería (squatter/access control) `[STRUCTURAL]` | 6,000,000 | 25,000,000 |
| Accounting, legal, compliance | 6,000,000 | 20,000,000 |
| **CHILE BASELINE CARRY** | **CLP 60M** | **CLP 199M** |
| | *(≈ NZ$ 106k – 351k)* | |

> **`[EST]` RANKING ON PURE CARRYING COST: Chile cheapest ≪ Japan ≈ NZ dearest.**
> Chile's advantage is roughly **2–4× on annual carry**. But carry is only one term —
> see §D, where NZ's income side (carbon + hunting + tourism) and its liability regime
> pull the ranking back.


---

# C. OFFSETTING INCOME — THE "RANCH PAYS THE RATES" TEST

## C1. Merino / fine wool

### Price reference

| Micron | NZ$/kg **clean** | Tag |
|---|---|---|
| 17.0 – 17.5 (superfine) | NZ$ 20 – 32 | `[RECALL]` — **verify against current NZ Wool Services / AWEX indicators; wool is volatile** |
| 18 – 19 (fine merino) | NZ$ 15 – 24 | `[RECALL]` |
| 20 – 21 (medium merino) | NZ$ 11 – 18 | `[RECALL]` |
| 30+ (crossbred / strong) | NZ$ 2 – 4 | `[RECALL]` — **structurally depressed for a decade; frequently below shearing cost** `[STRUCTURAL]` |

`[STRUCTURAL]` **The contract market matters more than the auction market.** The New Zealand
Merino Company runs multi-year forward contracts with apparel brands (ZQ / ZQRX
accreditation), which pay a premium over auction and, more importantly, **remove price
volatility** — the single biggest risk in wool. A high-country station's wool income should be
modelled on contract terms, not auction. **Verify current NZM contract levels and whether the
target station holds a contract — a transferable NZM contract is a genuine, valuable, and
frequently overlooked asset in a station sale.**

### Stocking and margin — 8,000 ha station

| Parameter | Value | Tag |
|---|---|---|
| Effective (grazable) area, as % of title | 40 – 70% | `[EST]` — alpine stations carry large rock/scree/ice/bluff area at zero productivity |
| ⇒ Effective ha on 8,000 ha | 3,200 – 5,600 ha | `[EST]` |
| Stocking rate on effective area, high country | 0.8 – 1.6 SU/ha | `[EST]` |
| **⇒ Total stock units** | **2,600 – 9,000 SU** | `[EST]` |
| Wool cut per merino ewe | 4.0 – 5.5 kg greasy; ~60–68% yield → 2.6 – 3.5 kg clean | `[RECALL]` |
| ⇒ Wool revenue per ewe @ NZ$18/kg clean | NZ$ 47 – 63 | `[EST]` |
| Gross revenue per SU (wool + sheep meat + surplus stock) | NZ$ 70 – 115 | `[EST]` |
| Farm working expenses per SU | NZ$ 55 – 92 | `[EST]` |
| **⇒ EBITDA per SU** | **NZ$ 15 – 40** | `[EST]` |
| **⇒ EBITDA, 5,000 SU station** | **NZ$ 75,000 – 200,000** | `[EST]` |
| Less: manager/labour already counted in §B3, depreciation, R&M | — | |
| **⇒ Realistic EBIT contribution** | **NZ$ 0 – 150,000 /yr, negative in a bad year** | `[EST]` |

### Beef + Lamb NZ benchmark — Class 1 South Island High Country

⚠️ **These are `[RECALL]` order-of-magnitude priors ONLY and are the single highest-priority
verification item in §E.** The Beef + Lamb NZ *Sheep and Beef Farm Survey* Class 1 (SI High
Country) model farm is the correct authoritative source and must be obtained.

| Metric | Prior | Tag |
|---|---|---|
| Model farm total area | ~4,000 – 8,000 ha | `[RECALL]` |
| Effective area | ~2,500 – 3,500 ha | `[RECALL]` |
| Stock units | ~6,000 – 8,000 SU | `[RECALL]` |
| Gross farm revenue | NZ$ 700,000 – 1,300,000 | `[RECALL]` |
| **Farm profit before tax** | **NZ$ 50,000 – 300,000, with years near zero or negative** | `[RECALL]` |
| **Profit before tax per effective ha** | **NZ$ 20 – 90 /ha** | `[EST]` = row above ÷ effective ha |

> ### ⭐ FINDING C1 — the headline answer to the brief's central question
> **`[EST]` High-country pastoral farming does NOT pay the carrying cost of a high-country
> station.** Modelled EBIT of NZ$0–150,000 against a baseline carry of NZ$346,000–1,210,000
> (§B7) leaves a deficit in every scenario. **Pastoral farming roughly pays for itself and
> keeps the land in a rateable, insurable, managed condition — it is a cost-neutraliser,
> not a profit centre.** Any vendor or broker presenting a station as "self-funding" from
> farming alone should be challenged for audited accounts.
>
> The realistic candidates to actually close the gap are, in order: **(1) carbon/ETS,
> (2) hunting, (3) accommodation, (4) the ski operation itself.**

---

## C2. Beef / cattle on high country

| Parameter | Value | Tag |
|---|---|---|
| Role on a high-country station | Complementary — cattle control rank pasture and use country sheep won't | `[STRUCTURAL]` |
| Typical proportion of SU carried as cattle | 15 – 35% | `[EST]` |
| Gross margin per cattle SU vs sheep SU | Generally **higher** than sheep in recent seasons on strong beef schedules; more capital-intensive per head | `[RECALL]` — **beef schedules were notably strong in 2024-26; verify current NZ bull/steer schedule NZ$/kg CW** |
| Winter constraint | Cattle need wintering feed/lower country — a hard constraint on a pure alpine block | `[STRUCTURAL]` |

`[EST]` Adding cattle shifts the pastoral EBIT range up modestly (perhaps +NZ$20,000–60,000
on the modelled station) but **does not change Finding C1.**

---

## C3. ⭐ FORESTRY AND CARBON — the largest single lever (NZ)

### C3.1 NZ ETS mechanics `[STRUCTURAL]`

- Only **post-1989 forest land** (land that was NOT forest at 31 Dec 1989) can earn NZUs.
  Pre-1990 forest earns nothing and carries deforestation liability.
- Land must meet the **forest land definition**: ≥1 ha, ≥30 m average width, tree species
  capable of ≥5 m height at maturity, ≥30% crown cover. `[RECALL]` — **this definition is the
  binding constraint on alpine land: above the treeline, nothing qualifies.**
- Two accounting routes for post-1989 forest:
  - **Averaging** — earn units up to the long-term average carbon stock, then stop; no
    surrender obligation at harvest. Standard for production forestry.
  - **Permanent forest category** (available from 1 Jan 2023) — earn on stock change with a
    **50-year commitment** not to clear-fell. `[RECALL]` — *the eligibility of **exotic**
    species in the permanent category has been subject to repeated policy change and
    reversal; **this must be verified as at 2026**, it materially changes the model.*

### C3.2 The sequestration and revenue arithmetic

| Parameter | Value | Tag |
|---|---|---|
| Radiata pine, long-term average carbon stock (averaging) | ~350 – 450 t CO₂e/ha | `[RECALL]` |
| Averaging earning period | ~16 – 20 yrs | `[RECALL]` |
| **⇒ Average annual earning rate during earning period** | **~20 – 26 NZU/ha/yr** | `[EST]` = 350–450 ÷ 16–20 |
| Indigenous / native regeneration | ~5 – 12 t CO₂e/ha/yr early decades | `[RECALL]` — far slower, but permanent and no wilding liability |
| **NZU spot price, 2026** | **NZ$ 55 – 80** | `[RECALL]` ⚠️ **live market — this is the #1 figure to verify.** Historic context: peaked ~NZ$88 (late 2022), crashed to ~NZ$34 (2023), recovered through 2024–25 |
| **⇒ Gross carbon revenue, radiata, earning period** | **NZ$ 1,100 – 2,080 /ha/yr** | `[EST]` = 20–26 NZU × NZ$55–80 |
| **⇒ Gross carbon revenue, native regeneration** | **NZ$ 275 – 960 /ha/yr** | `[EST]` = 5–12 × NZ$55–80 |
| Establishment cost, radiata (site prep, seedlings, planting, releasing, pest control) | NZ$ 1,800 – 3,800 /ha | `[EST]` |
| ETS admin, mapping, FMA field measurement, registry, consultant | NZ$ 40 – 120 /ha/yr | `[EST]` |

### C3.3 ⚠️ Why the headline number is NOT achievable on an alpine property

This is the critical analysis. A naive calculation — 8,000 ha × NZ$1,500/ha = NZ$12M/yr — is
**wrong by one to two orders of magnitude.** The reductions, in sequence:

| Filter | Effect | Tag |
|---|---|---|
| 1. **Above treeline = ineligible** — trees cannot reach 5 m at maturity | On an alpine station, typically only the **lowest 10–30%** of the title is plantable | `[STRUCTURAL]` / `[EST]` |
| 2. **Pre-1990 forest and existing scrub** may be excluded | Further reduction | `[STRUCTURAL]` |
| 3. **The plantable land is the productive farmland** — planting it ends the pastoral business | Direct trade-off, not additive | `[STRUCTURAL]` |
| 4. **Planting the lower slopes destroys ski access, views and the amenity being purchased** | Direct conflict with the client's core purpose | `[STRUCTURAL]` |
| 5. **Wilding spread liability** (§B4) — conifers adjacent to alpine country seed into it; the owner is then legally obliged to control the spread they caused | Converts a revenue line into a liability | `[STRUCTURAL]` |
| 6. **Policy restrictions on farm-to-forest conversion** — NZ moved during 2025 to restrict whole-farm conversions to exotic forest on LUC 1–6 land | High country is mostly LUC 6–8, so *may* be less affected — **VERIFY, this is recent and consequential** | `[RECALL]` |
| 7. **50-year permanence commitment** encumbers the title and constrains resale | Reduces asset flexibility | `[STRUCTURAL]` |
| 8. **NZU price risk** — a 60% drawdown occurred within 12 months in 2022-23 | Do not underwrite carry against a volatile single price | `[STRUCTURAL]` |

### C3.4 Realistic carbon model for an 8,000 ha alpine station

| Scenario | Eligible & plantable ha | Species | Gross NZ$/yr | Tag |
|---|---|---|---|---|
| **Conservative** — plant only sheltered lower gullies, minimal ski/amenity conflict | 300 ha | radiata, averaging | **NZ$ 330,000 – 624,000** | `[EST]` |
| **Moderate** — commit the lower faces, accept partial loss of pastoral & some amenity | 800 ha | radiata, averaging | **NZ$ 880,000 – 1,664,000** | `[EST]` |
| **Native-only** — no wilding liability, permanent, ski/amenity compatible, far slower | 1,500 ha | indigenous regeneration | **NZ$ 412,000 – 1,440,000** | `[EST]` |
| Establishment cost drag (radiata, amortised over the 16–20 yr earning period) | — | — | −NZ$ 90/ha/yr to −NZ$240/ha/yr | `[EST]` |

> ### ⭐ FINDING C3 — the decisive economic insight for New Zealand
> **`[EST]` Even after every reduction above, carbon is the only income line on a NZ alpine
> station capable of covering the entire carrying cost.** The conservative 300 ha scenario
> (NZ$330k–624k/yr gross) alone approximately matches the baseline carry of NZ$346k–1,210k/yr.
>
> **And the native-regeneration variant is strategically superior for this client** even though
> its gross revenue is lower per hectare: it creates **no wilding liability**, requires
> **minimal establishment cost** where regeneration is natural, **does not conflict with the ski
> terrain** (it occupies gullies and lower faces, not the open basins), improves the
> **"benefit to New Zealand" case for the OIO consent** that the properties analyst identifies
> as the binding constraint, and is far more defensible politically for a foreign owner
> than planting pines. **Recommend the native/permanent-forest route be modelled as the base
> case, not the exotic route.**
>
> ⚠️ **Caveat of equal weight:** this entire finding rests on an unverified NZU price and an
> unverified reading of current permanent-category and conversion-restriction policy. **It is
> the highest-value and highest-uncertainty item in this document.**

### C3.5 Japan forestry

| Item | Figure | Tag |
|---|---|---|
| スギ (sugi) standing timber price (立木価格) | ~¥ 2,000 – 4,500 /m³ | `[RECALL]` — structurally depressed for ~40 yrs |
| ヒノキ (hinoki) standing | ~¥ 5,000 – 12,000 /m³ | `[RECALL]` |
| カラマツ (larch, Hokkaido) | ~¥ 2,000 – 5,000 /m³ | `[RECALL]` |
| **Why Japanese forestry is loss-making** `[STRUCTURAL]` | Steep terrain; tiny fragmented parcels; very low forest-road density; high labour cost and an ageing workforce; decades of cheap imported timber; harvest+haulage cost frequently **exceeds** standing value, so the owner nets **zero or negative** | `[STRUCTURAL]` |
| 森林経営管理制度 (2019 Forest Management Act) | Lets municipalities take over management of unmanaged private forest where the owner will not or cannot manage it — **evidence of how weak private forest economics are** | `[RECALL]` |
| J-クレジット (forest management credits) | Volumes small; forest-derived credits trade at a **premium** to energy credits, plausibly ¥ 8,000 – 16,000 /t-CO₂, but **issuance volumes are tiny and transaction costs high** | `[RECALL]` — verify |
| **⇒ Japan forestry as a carry offset** | **Effectively zero to negative.** Do not model Japanese forestry as income | `[EST]` |

### C3.6 Chile forestry

| Item | Figure | Tag |
|---|---|---|
| Radiata pine / eucalyptus plantation returns | ~USD 2,000 – 5,500 /ha NPV over a rotation | `[EST]` |
| Geographic constraint `[STRUCTURAL]` | The plantation estate is concentrated in **Maule–Biobío–Araucanía (regions VII–IX)**, *not* the high Andes. An Andean cordillera property is largely **outside** the commercial plantation zone | `[STRUCTURAL]` |
| **Ley 20.283 (Ley de Bosque Nativo)** | Native forest **cannot be cleared** without a CONAF-approved management plan; effectively prohibitive. Also provides subsidies for native forest management | `[RECALL]` — legal workstream to confirm |
| Chile carbon | Chile has a carbon tax on large emitters with an offset mechanism; a voluntary market exists but is thin for forestry | `[RECALL]` |
| **⇒ Chile forestry as a carry offset** | **Low. Assume near zero for an Andean property.** | `[EST]` |

---

## C4. ⭐ HUNTING AND GAME — the best season-complementary income

### New Zealand

| Item | Rate | Tag |
|---|---|---|
| Guided trophy hunt, day rate 1×1 (incl. accommodation, meals, guide) | NZ$ 1,200 – 2,600 /day | `[RECALL]` |
| **Red stag trophy fee — management class** | NZ$ 2,500 – 6,000 | `[RECALL]` |
| **Red stag — 300–350 SCI** | NZ$ 7,000 – 16,000 | `[RECALL]` |
| **Red stag — 400+ SCI (estate-grade)** | NZ$ 20,000 – 60,000+ | `[RECALL]` |
| **Himalayan tahr** (a genuinely iconic free-range NZ trophy) | NZ$ 4,500 – 9,500 | `[RECALL]` |
| **Chamois** | NZ$ 3,500 – 7,500 | `[RECALL]` |
| Fallow / sika / rusa | NZ$ 2,000 – 6,000 | `[RECALL]` |
| **Season-lease of hunting rights to an outfitter** | **NZ$ 20,000 – 120,000 /yr** | `[EST]` — scales with trophy quality, access and exclusivity |
| Deer fence (if a high-fence estate model is contemplated) | NZ$ 28 – 50 /m → **NZ$ 280,000 – 500,000 per 10 km** | `[EST]` |

> ### ⭐ FINDING C4 — seasonal complementarity is the key structural advantage
> `[STRUCTURAL]` **The hunting season and the ski season do not collide — they interlock.**
> The red deer roar is late March–April; tahr and chamois rut April–May/June; the NZ ski
> season is July–September. **The same lodge, tracks, vehicles, radios, snowmobiles and
> guiding staff serve both.**
>
> This roughly **doubles the utilisation of the Phase 1 fixed asset base** and is the single
> most efficient way to make the ski infrastructure pay. A lodge used 60 ski-nights and
> 60 hunting-nights has half the fixed cost per revenue dollar of a ski-only lodge.
> **Recommend the Phase 1 hut be specified from the outset for dual-season use** (autumn
> hunting + winter skiing) — it changes the building brief (drying room, game larder/chiller,
> vehicle access in both seasons) at negligible marginal cost if designed in, and at large
> cost if retrofitted.

| Owner-operated hunting model, 8,000 ha station | Value | Tag |
|---|---|---|
| Hunters per season | 15 – 30 | `[EST]` |
| Days each | 4 – 6 | `[EST]` |
| Day-rate revenue | NZ$ 90,000 – 270,000 | `[EST]` = 15–30 × 4–6 × NZ$1,500 |
| Trophy fees | NZ$ 90,000 – 300,000 | `[EST]` = 15–30 × NZ$6,000–10,000 |
| **Gross** | **NZ$ 180,000 – 570,000** | `[EST]` |
| Less direct costs (guides, food, meat/trophy handling, marketing, agent commission 10–20%) | 50 – 65% | `[EST]` |
| **⇒ NET contribution** | **NZ$ 65,000 – 250,000 /yr** | `[EST]` |

`[STRUCTURAL]` Legal notes for the legal workstream: game animals on **freehold** land are
effectively controlled by the landowner; the **Wild Animal Control Act 1977** and the **Game
Animal Council** govern the framework; **tahr are subject to a national control plan** with
active DOC culling on public land, which is contentious and could affect adjacent private
herds. Also: **firearms licensing for visiting overseas hunters** is an administrative
process the outfitter normally manages.

### Japan
| Item | Figure | Tag |
|---|---|---|
| エゾシカ (Hokkaido sika) / ニホンジカ | Managed as **pest culling**, not trophy hunting | `[STRUCTURAL]` |
| Municipal culling bounties | ¥ 5,000 – 25,000 /animal paid **to** hunters | `[RECALL]` |
| Venison (ジビエ) prices | Low; processing facilities scarce; market thin | `[RECALL]` |
| **⇒ As landowner income** | **Effectively zero — it is a cost centre, not revenue** | `[EST]` |

### Chile
| Item | Figure | Tag |
|---|---|---|
| Red deer / wild boar (jabalí) in Patagonia and the Andes | Hunting tourism exists but the sector is small and informal | `[RECALL]` |
| **⇒ As landowner income** | **Modest — NZ$ 10,000 – 60,000 /yr equivalent at best** | `[EST]` |

---

## C5. Accommodation

| Market | Nightly rate | Tag |
|---|---|---|
| **NZ ultra-luxury alpine lodge, all-inclusive per person** (Minaret Station / Blanket Bay / Mahu Whenua class) | NZ$ 1,500 – 4,500 pp/night | `[RECALL]` |
| **NZ mid-market farm stay / self-contained cottage** | NZ$ 180 – 500 /night (whole unit) | `[EST]` |
| **NZ exclusive-use whole-lodge charter** | NZ$ 2,500 – 12,000 /night | `[EST]` |
| **Japan 山小屋 (mountain hut), 2食付き** | ¥ 10,000 – 16,000 pp/night | `[RECALL]` |
| **Japan グランピング** | ¥ 20,000 – 70,000 /site/night | `[RECALL]` |
| **Japan 民泊** — capped at **180 nights/yr** under 住宅宿泊事業法 | `[STRUCTURAL]` constraint | `[RECALL]` |
| **Chile lodge** | USD 250 – 1,500 /night | `[EST]` |

### Realistic revenue, 4–10 beds, NZ

| Model | Calculation | Gross NZ$/yr | Tag |
|---|---|---|---|
| **Low** — 6 beds, self-catering, whole-hut NZ$350/night, 50 nights | 350 × 50 | **17,500** | `[EST]` |
| **Mid** — 8 beds, hosted, NZ$450 pp/night, 20% occupancy (584 bed-nights) | 450 × 584 | **263,000** | `[EST]` |
| **High** — 8 beds, all-inclusive luxury NZ$1,800 pp/night, 25% occupancy (730 bed-nights) | 1,800 × 730 | **1,314,000** | `[EST]` |

> ⚠️ `[STRUCTURAL]` **The "high" line is a hospitality business, not a property income line.**
> It requires chefs, hosts, housekeeping, a liquor licence, food-safety registration, building
> compliance for public accommodation, marketing, an OTA/agent channel, and it carries
> 55–75% operating costs. **Net margin, not gross, is the number that matters — and for a
> foreign owner the OIO "benefit to New Zealand" case is *helped* by a genuine tourism
> business with local employment, which is a second reason to take it seriously.**
> `[EST]` net contribution: **Low NZ$10k · Mid NZ$70k–110k · High NZ$300k–450k.**

---

## C6. ⭐ CAT-SKIING AND PRIVATE SKI REVENUE BENCHMARKS

| Operation | Country | Indicative price | Tag |
|---|---|---|---|
| **Baldface Lodge** | Canada (BC) | CAD 1,300 – 2,200 pp/day within multi-day packages; packages CAD 6,000 – 13,000 | `[RECALL]` |
| **Mustang Powder** | Canada (BC) | Similar multi-day lodge-based model | `[RECALL]` |
| **Great Northern Powder Guides** | USA (MT) | USD 450 – 750 pp/day | `[RECALL]` |
| **Ski Arpa** | Chile | USD 450 – 750 pp/day (~4–5 runs) | `[RECALL]` |
| **Soho Basin (private cat skiing)** | NZ | NZ$ 1,200 – 2,800 pp/day | `[RECALL]` |
| **Southern Lakes Heliski** | NZ | NZ$ 1,400 – 2,600 pp for a multi-run day | `[RECALL]` |
| **Alpine Guides / Methven / Hokkaido cat operations** | NZ / JP | NZ$ 700 – 1,800 pp/day | `[RECALL]` |
| **Typical cat group size** | — | **12 guests + 2 guides per cat** | `[RECALL]` |

### C6.1 Single-cat revenue ceiling model `[EST]`

| Parameter | Low | High |
|---|---|---|
| Guests per cat per day | 10 | 12 |
| Price per person per day | NZ$ 900 | NZ$ 2,000 |
| Skiable operating days per season (after weather/snow/wind losses) | 45 | 75 |
| Load factor | 55% | 80% |
| **GROSS REVENUE, ONE CAT** | **NZ$ 223,000** | **NZ$ 1,440,000** |
| Central case (11 guests × NZ$1,400 × 60 days × 68%) | **NZ$ 629,000** | |
| Operating costs (guides, snow safety, fuel, food, marketing, admin, insurance) | 55 – 70% of gross | |
| **⇒ NET CONTRIBUTION, ONE CAT** | **NZ$ 70,000** | **NZ$ 500,000** |
| **⇒ Central net** | **~NZ$ 200,000 – 250,000** | `[EST]` |

> ### ⭐ FINDING C6 — the revenue ceiling is real and it is modest
> `[STRUCTURAL]` **A single snowcat is a hard capacity ceiling of roughly 10–12 guests per
> day.** No amount of marketing changes it. That caps a single-cat operation at
> **~NZ$0.6M gross / ~NZ$0.2M net** in a central case. Scaling means more cats, more guides,
> more snow safety and more terrain — i.e. it becomes a real business with real staff and
> real liability, which is Phase 2/3, not Phase 1.
>
> **Implication for the client:** cat-skiing revenue can *contribute meaningfully to* the
> carrying cost but cannot by itself justify a large land purchase. It is best understood
> as **a way to make the ski asset roughly self-funding**, not as an investment return.
> Weather risk is severe and uninsurable — a low-snow season can remove most of the revenue
> while all the fixed costs remain.

### C6.2 Private ski club models — the aspirational end, and the warning

| Club | Model | Tag |
|---|---|---|
| **Yellowstone Club** (Montana) | Initiation ~USD 400,000+; annual dues ~USD 45,000+; **mandatory property purchase (multi-million)**; ~900 members. The global reference point | `[RECALL]` |
| **Hermitage Club** (Vermont) | Initiation ~USD 65,000–90,000. ⚠️ **Entered bankruptcy in 2018.** | `[RECALL]` |
| **Powder Mountain** (Utah) | Reed Hastings-backed; converted part of the mountain to private/member-only terrain from ~2023–24 | `[RECALL]` |
| **Silverpeak / other emerging private clubs** | Small-scale private mountain models | `[RECALL]` — verify |

> ### ⚠️ FINDING C6.2 — the Hermitage lesson, which directly validates the client's phasing
> `[STRUCTURAL]` **Private ski clubs fail when they carry resort-scale capital (chairlifts,
> snowmaking, a large lodge) against a small member base.** The fixed cost of a chairlift
> and a clubhouse must be spread over a few hundred members instead of a few hundred thousand
> skier-visits, which requires either very high dues or very deep-pocketed members — and the
> model breaks in a recession or a low-snow year.
>
> **The client's Phase 1 → 2 → 3 sequencing is therefore correct and should be defended.**
> A club whose entire fixed asset base is a snowcat, a rope tow and a hut (Tier 3:
> NZ$1.5M–4.4M) has a break-even perhaps **an order of magnitude below** a club with a
> chairlift (add NZ$6M–14M + NZ$100k–300k/yr). **The capital discipline in Phase 1 is not
> merely thrift — it is the specific thing that killed the Hermitage Club.**

| Illustrative Phase 2 club model, NZ `[EST]` | Value |
|---|---|
| Founding members | 25 – 40 |
| Joining fee | NZ$ 20,000 – 60,000 |
| **⇒ One-off capital raised** | **NZ$ 500,000 – 2,400,000** |
| Annual dues | NZ$ 6,000 – 15,000 |
| **⇒ Recurring** | **NZ$ 150,000 – 600,000 /yr** |

⚠️ **Legal flag:** a members' club raising joining fees may constitute a **managed investment
scheme / financial product offer** requiring disclosure under the Financial Markets Conduct
Act 2013, and creates a governance structure. **Refer to the legal workstream before any
member solicitation.** It also **directly worsens the OIO "benefit to New Zealand" case**
(per the properties analyst's Finding 0.3) because it is an access-restricting, private-benefit
use — the two workstreams' conclusions are in tension and this needs an explicit decision.

---

## C7–C10. Other income lines

| Line | Value | Tag |
|---|---|---|
| **Telecommunications / radio repeater site lease** ⭐ | **NZ$ 4,000 – 25,000 /yr per site** | `[EST]` — **genuinely overlooked. A summit with line-of-sight to a valley is commercially useful to telcos, emergency services and broadcasters. Near-zero cost, near-zero conflict with any other use. Check for existing site agreements in the vendor's records — they may already exist and be assignable.** |
| **Filming / location fees** | NZ$ 2,000 – 25,000 /day; episodic and unbankable | `[EST]` — NZ has a strong location-filming sector; a dramatic alpine landscape with road access is genuinely marketable, but **do not put it in a base case** |
| **Mānuka honey / hive site leases** | NZ$ 50 – 300 /hive/yr, or a share of crop | `[EST]` ⚠️ **mānuka is a lowland/hill-country species — largely absent above the treeline.** Industry has been in oversupply since ~2019, depressing hive rentals `[RECALL]`. **Assume near-zero for an alpine title** |
| **Micro-hydro** | 20 – 100 kW; NZ$ 150,000 – 600,000 capital | `[EST]` — ⭐ **counter-seasonal to solar (peaks in winter/spring snowmelt), so it directly displaces winter generator fuel.** Grid export is normally impossible at these locations; value it as **avoided cost**, not revenue. Requires a water take/use consent |
| **Wind / solar leasing** | NZ$ 10,000 – 30,000 /turbine/yr | `[EST]` — requires **grid proximity**; a remote alpine station will almost never attract a developer. **Assume zero** |
| **Biodiversity credits** | No mature statutory market in NZ; voluntary schemes only | `[RECALL]` — **assume zero revenue, but note the *reputational/consenting* value for the OIO case** |
| **Grazing lease-out** (if not farming directly) | NZ$ 8 – 30 /SU/yr, or NZ$15–45/ha on effective area | `[EST]` — ⭐ **strategically important: leasing the grazing to a neighbouring farmer converts a volatile, management-intensive farming operation into a small but certain rent, and keeps the land managed and rateable without employing farm staff. For an absentee foreign owner whose real interest is skiing, this is very often the correct answer.** `[EST]` NZ$40,000–150,000/yr on the modelled station |


---

# D. SYNTHESIS — ONE-PAGE ECONOMICS MODEL
### Hypothetical 8,000 ha alpine station, New Zealand. All NZ$/yr. All `[EST]`.

## D1. Three operating models

| | **Model 1 "Locked Gate"** *(absentee, grazing leased out, owner-only skiing)* | **Model 2 "Working Station"** *(farmed, hunting leased, private skiing)* | **Model 3 "Full Stack"** *(carbon + hunting + lodge + cat-ski)* |
|---|---|---|---|
| **CARRYING COST** | | | |
| Rates | 45,000 | 45,000 | 45,000 |
| Insurance | 35,000 | 55,000 | 95,000 |
| Staff | 55,000 | 140,000 | 400,000 |
| Machinery, vehicles, depreciation | 35,000 | 115,000 | 150,000 |
| Tracks, fences, water, buildings | 75,000 | 130,000 | 170,000 |
| Pest & weed control | 120,000 | 150,000 | 150,000 |
| Power, fuel, comms | 15,000 | 16,000 | 25,000 |
| Accounting, legal, OIO condition compliance | 55,000 | 70,000 | 95,000 |
| Ski operating add-on | 45,000 | 45,000 | 350,000 |
| **TOTAL CARRY** | **480,000** | **766,000** | **1,480,000** |
| **INCOME** | | | |
| Pastoral (own account) | — | 70,000 | 70,000 |
| Grazing lease-out | 95,000 | — | — |
| Carbon / ETS (native, ~1,000 ha) | — | — | 480,000 |
| Hunting | — | 60,000 *(lease)* | 150,000 *(operated)* |
| Accommodation (net) | — | — | 90,000 |
| Cat-ski (net) | — | — | 220,000 |
| Telecom repeater site | 10,000 | 10,000 | 10,000 |
| **TOTAL INCOME** | **105,000** | **140,000** | **1,020,000** |
| **⇒ NET CARRY (cost − income)** | **375,000** | **626,000** | **460,000** |
| Management burden | Very low | Moderate | **Very high — four businesses** |
| Weather/price risk exposure | Low | Moderate | **High** |

> ### ⭐ FINDING D1 — the counterintuitive result
> **Model 3, which works hardest, is not much better than Model 1, which does almost nothing.**
> Adding hunting, lodging and cat-skiing raises income by ~NZ$900k but raises cost by ~NZ$1.0M.
> **The operating businesses roughly wash.** The only line that genuinely moves net carry is
> **carbon** — and even that is largely consumed by the cost of the operations bolted on beside it.
>
> **⇒ Strategic recommendation: Model 1 + carbon.** Lease out the grazing, secure an ETS/native
> forest position on the lower country, keep the skiing strictly private and owner-operated,
> and *do not* build a hospitality business unless the client actively wants to run one.
> `[EST]` **Model 1 + 1,000 ha native carbon ⇒ net carry ≈ NZ$375,000 − 480,000 = *income
> positive by ~NZ$105,000/yr*.** That is the genuinely attractive configuration, and it is
> also the **lowest-management** one — which matches the client's stated "low-cost rural
> asset" objective far better than the full-stack model does.

## D1b. ⚠️⚠️ THE CONSENT–ECONOMICS INVERSION (New Zealand only)

**This is the most important cross-workstream finding, and it changes the D1 recommendation.**

The NZ regulatory analyst's file (`nz-regulatory.md`, §on the benefit-to-New-Zealand test)
establishes that for **farmland** — which is carved out of the 2025 Overseas Investment reform
and remains under the old, harder test — the applicant must demonstrate **more jobs, more
export receipts, more productivity, more processing of primary products** than the station
produces today, and that:

> *"Cutting stock numbers to make room for a private ski operation runs the **wrong way** on the
> high-importance factor and, because the negative is directly comparable (jobs vs jobs, export
> receipts vs export receipts), it can be netted off against you."*

Now compare that against my D1 result:

| | Net carry (economics) | Effect on OIO benefit test |
|---|---|---|
| **Model 1 "Locked Gate"** — grazing leased out, minimal staff, private skiing | **BEST** (NZ$375k, or *positive* with carbon) | **WORST** — cuts jobs, cuts on-farm employment, adds no exports, access-restricting |
| **Model 2 "Working Station"** | Middle (NZ$626k) | Neutral — maintains the status quo baseline, which is *not enough*; the test requires **more** than today |
| **Model 3 "Full Stack"** — hunting, lodge, cat-ski, carbon | Middle (NZ$460k) but **very high management burden** | **BEST** — creates jobs, creates export receipts (foreign guests = export services), adds processing/tourism, demonstrable investment |

> ### ⭐⭐ FINDING D1b — in New Zealand the cheapest configuration is the least consentable
> **`[EST]/[STRUCTURAL]` The configuration that minimises carrying cost (Model 1) is precisely
> the configuration the Overseas Investment Office is least likely to consent, and the
> configuration that best satisfies the consent test (Model 3) is the one that costs the most
> to run and demands the most management.** The client cannot optimise both.
>
> **Consequences:**
> 1. **The NZ carrying-cost figure the client should plan on is Model 3's, not Model 1's** —
>    because Model 1 may never be permitted. That is **NZ$1,480,000/yr gross cost against
>    NZ$1,020,000/yr income, i.e. ~NZ$460,000/yr net carry (≈ MYR 1.11M/yr)** — *plus* the
>    obligation to actually operate four businesses, which is the opposite of a "low-cost
>    rural asset."
> 2. **The private ski club (§C6.2) is doubly adverse** — it cuts jobs *and* restricts access,
>    hitting two OIO factors at once. Phase 2 as conceived may be unconsentable in NZ.
> 3. **Carbon/native forestry (§C3.4) is the one line that is both economically strong and
>    consent-positive** — it adds investment, environmental benefit and (for native
>    regeneration) biodiversity, without cutting stock or restricting access. **This
>    materially strengthens the recommendation to make native permanent forest the base case.**
> 4. **⇒ If the client's true priority is a low-cost, low-management private mountain, the
>    consent regime is a reason to prefer Chile over New Zealand** — independent of, and
>    additional to, Chile's 2–4× cheaper carry (§D4). In Chile the client can actually run
>    Model 1. In New Zealand they may be required to run Model 3 as a condition of entry.
>
> ⚠️ This finding depends entirely on the regulatory analyst's reading of the benefit test and
> on whether the target is classified as **farmland**. **A property that is NOT farmland
> (e.g. a defunct ski area on non-farm title) may escape the carve-out and fall under the
> faster consolidated national interest test — which would restore Model 1 as viable.**
> **This is a high-value question for the legal workstream and could be worth several hundred
> thousand NZ$/yr.**

## D2. Total cost of ownership vs purchase price

Using **Model 2 (Working Station) net carry ≈ NZ$626,000** as the realistic base case, and a
**5% real opportunity cost of capital** (adjust to the client's true hurdle rate):

| Purchase price | Capital cost @5% | Net carry | **Total annual cost of ownership** | ≈ MYR/yr @2.41511 | **Net carry as % of price** |
|---|---|---|---|---|---|
| NZ$ 3M | 150,000 | 626,000 | **776,000** | MYR 1.87M | **20.9%** ⚠️ |
| NZ$ 5M | 250,000 | 626,000 | **876,000** | MYR 2.12M | **12.5%** ⚠️ |
| NZ$ 8M | 400,000 | 626,000 | **1,026,000** | MYR 2.48M | **7.8%** |
| NZ$ 12M | 600,000 | 626,000 | **1,226,000** | MYR 2.96M | **5.2%** |
| NZ$ 20M | 1,000,000 | 626,000 | **1,626,000** | MYR 3.93M | **3.1%** |
| NZ$ 35M | 1,750,000 | 626,000 | **2,376,000** | MYR 5.74M | **1.8%** |
| NZ$ 50M | 2,500,000 | 626,000 | **3,126,000** | MYR 7.55M | **1.3%** |

Plus **one-off Phase 1 ski CAPEX** (§A7), independent of purchase price:
**Tier 1 NZ$0.62–1.66M · Tier 2 NZ$1.06–2.93M · Tier 3 NZ$1.53–4.39M.**

## D3. ⭐⭐ THE HEADLINE ANSWER: at what price is this "genuinely low cost to hold"?

> ### **The premise of the question is wrong, and this is the most important finding in the workstream.**
>
> **`[STRUCTURAL]` The carrying cost of an alpine station is almost entirely INDEPENDENT of
> what you paid for it.** Rates follow a low rural valuation; pest control, tracks, fencing,
> staff, insurance and compliance follow **area, condition and remoteness** — not price. A
> cheap station and an expensive station of the same size in the same district cost roughly
> the same to hold.
>
> **⇒ Consequence: a *cheap* alpine station is not a *low-cost* alpine station.** At NZ$3M the
> carry is 21% of the asset value every year — the holding cost dominates the investment
> entirely, and within five years you have spent the purchase price again. At NZ$35M the same
> carry is 1.8% and is economically trivial. **Buying cheap maximises the ratio of carry to
> value, which is the opposite of what the client wants.**
>
> ### What actually determines "low cost to hold" — in priority order
> 1. **Pest and weed condition.** `[EST]` swing: **NZ$49,000 → NZ$320,000/yr** (§B4). The single
>    largest controllable line. A wilding-conifer-infested station can cost NZ$1M+ to
>    rehabilitate and is a *legally enforceable* obligation. **Screen this before price.**
> 2. **Existing access and buildings.** A property with a formed all-weather road, a habitable
>    dwelling, power and water avoids `[EST]` **NZ$300,000 – 1,000,000** of Phase 1 CAPEX and
>    the consenting that goes with it.
> 3. **An ETS-eligible area.** `[EST]` swing: **NZ$0 → NZ$600,000+/yr.** The only line that can
>    flip the asset to cash-positive. **Establish post-1989 status and plantable area during DD.**
> 4. **An assignable grazing lease.** Converts a loss-making farm into certain rent and removes
>    the staff line: `[EST]` worth **NZ$100,000 – 200,000/yr** of avoided cost and volatility.
> 5. **Total area.** Fixed overheads dominate, so **cost per hectare falls sharply with size**
>    (§B7). Do not buy small to save money.
> 6. **Purchase price** — genuinely the *least* important determinant of holding cost.
>
> ### The direct answer
> `[EST]` **A NZ alpine station is "genuinely low cost to hold" when net carry is under
> ~NZ$250,000/yr (≈ MYR 604,000/yr) — and reaching that depends on CONDITION and INCOME
> STRUCTURE, not on purchase price.** The configuration that achieves it is:
> **clean country + existing access + grazing leased out + a carbon position + owner-operated
> private skiing (§D1 Model 1 + carbon)**, which models at **net carry of roughly −NZ$100,000
> to +NZ$200,000/yr, i.e. break-even to modestly positive.**
>
> At that point the *only* real cost of ownership is the opportunity cost of capital, and the
> purchase price question becomes a straightforward investment question rather than a carrying
> question: **pay what the land is worth as land, and treat the ski mountain as a free option
> costing NZ$0.6M–2.9M of Phase 1 CAPEX (Tiers 1–2).**
>
> ### The counter-case the client must hear
> ⚠️ If the property is **pest-infested, roadless, and has no ETS-eligible or leasable land**,
> then even at a NZ$3M purchase the asset costs **NZ$700,000–1,000,000/yr (MYR 1.7–2.4M/yr)**
> to hold, forever, with no realistic path to reducing it. **That is the failure mode, and it
> is far more common in cheap listings than in expensive ones.** Cheap alpine land is usually
> cheap for reasons that show up in the carry.

## D4. Country comparison

| | **New Zealand** | **Japan** | **Chile** |
|---|---|---|---|
| Baseline carry, 8,000 ha `[EST]` | NZ$ 346k – 1,210k | ≈ NZ$ 212k – 935k | ≈ NZ$ 106k – 351k ⭐ |
| Property tax | Moderate | Low (but see availability) | Lowest ⭐ |
| Labour cost | Highest | High | Lowest ⭐ |
| Guide/cat-operator talent pool | Deepest ⭐ | Thin | Moderate |
| **Liability regime** | **ACC bars personal-injury damages ⭐⭐ — decisive advantage** | Low tort, but criminal-negligence exposure | Intermediate |
| Carbon / ETS income potential | **Strong ⭐⭐ — the only real carry offset** | Negligible | Low |
| Hunting income | **Strong ⭐** (free-range tahr/chamois/red) | Negligible (cost centre) | Modest |
| Forestry income | Moderate–strong | **Negative** | Low in the Andes |
| **Availability of large private alpine title** | **Very constrained** (tenure review put the tops in Crown ownership — see properties workstream) | **Probably prohibitive** (national forest/park; fragmented, unknown-owner private land) | **Best availability ⭐** |
| **Foreign-buyer regime** | **OIO farmland consent — hard; private club is adverse to the benefit test ⚠️** | Few restrictions on land purchase itself | Generally open ⭐ |
| Snow reliability / season length | Good | **Excellent ⭐** | Variable, drought-exposed |

> ### ⭐ FINDING D4 — the two countries are strong on opposite axes
> **NZ wins decisively on the *risk and income* side** (ACC liability bar, carbon income,
> hunting income, guide talent) but is **worst on availability and foreign-buyer consent.**
> **Chile wins decisively on *cost and access*** (2–4× cheaper carry, cheapest labour, open
> to foreign buyers, genuine large private cordillera holdings available) but has **no
> meaningful offsetting income** and a more complex water-rights/native-forest legal picture.
> **Japan should probably be de-prioritised on availability grounds alone** — the carrying
> costs are unremarkable but assembling 8,000 contiguous private alpine hectares is likely
> not possible.
>
> `[EST]` **A defensible framing for the client:** *Chile is the low-cost-to-hold answer;
> New Zealand is the low-risk, income-offset answer and costs roughly 2–4× more per year
> to hold, plus a materially harder and uncertain consent process.* The premium for NZ is
> roughly **NZ$250,000–600,000/yr** — the client should decide explicitly whether the ACC
> liability bar, the carbon income and the guiding talent are worth that.

## D5. Sensitivity — what actually moves the answer

| Variable | Swing | Impact on net carry | Rank |
|---|---|---|---|
| ETS/carbon position (0 → 1,000 ha native) | NZ$0 → 480k | **−480,000** | **1** ⭐ |
| Pest/weed condition (clean → infested) | 49k → 320k | **+271,000** | **2** ⭐ |
| Guest-carrying vs private-only skiing | 45k → 350k | **+305,000** | **2=** ⭐ |
| NZU price (NZ$40 → NZ$90) | ±50% on carbon line | **±240,000** | 4 |
| Farm own-account vs grazing lease-out | −70k income, +140k staff | **+70,000** | 5 |
| Wool price ±30% | ±NZ$25k on EBIT | ±25,000 | 6 |
| Purchase price NZ$3M → NZ$50M | *no effect on carry* | **0** | — |

> ⚠️ **Note that three of the top four are decisions or conditions, not prices.** The client
> controls whether to carry guests and whether to plant; due diligence controls whether they
> inherit a pest problem. **Only the NZU price is genuinely exogenous — and it is volatile
> enough (a 60% drawdown occurred in under 12 months in 2022-23) that the plan must survive
> without it.** Model the base case at NZU = NZ$0 and treat carbon as upside.

---

# E. ⚠️ VERIFICATION QUEUE — RUN THESE FIRST WHEN SEARCH BUDGET IS RESTORED

**Nothing in this document is decision-grade until these are done.** Ordered by value-at-risk.
Suggested search strings included.

## E1. TIER 1 — these change the answer (do first, ~15 searches)
| # | Item | § | Suggested query |
|---|---|---|---|
| 1 | **NZU spot price 2026** and 5-yr history | C3.2 | `NZU carbon price today NZ ETS 2026`; `carbon news NZU spot price` |
| 2 | **Permanent forest category — exotic eligibility status 2026** | C3.1 | `NZ ETS permanent forest category exotic species rules 2026`; `MPI permanent post-1989 forest` |
| 3 | **Farm-to-forest conversion restrictions (LUC classes)** | C3.3 | `New Zealand restrictions forestry conversion LUC 1-6 farmland 2025 2026` |
| 4 | **Beef + Lamb NZ Sheep & Beef Farm Survey — Class 1 SI High Country**, $/ha and farm profit | C1 | `Beef Lamb NZ Class 1 South Island High Country farm profit before tax per hectare` |
| 5 | **Wilding conifer control cost per hectare** (NZ programme data) | B4 | `wilding conifer control cost per hectare New Zealand national programme` |
| 6 | **Actual council rates on a named high-country station** | B1 | `Mackenzie District Council rates pastoral station`; `Waitaki district rural rates rating information database` |
| 7 | **ACC s317 bar on personal injury damages — ski area liability** | B2 | `Accident Compensation Act 2001 section 317 bar proceedings damages personal injury ski` |
| 8 | **HSWA 2015 penalty bands and ski-area prosecutions** | B2 | `Health and Safety at Work Act 2015 penalties body corporate reckless $1.5 million; WorkSafe ski area prosecution` |
| 9 | **US small ski area liability insurance cost** | B2 | `small ski area liability insurance premium cost closure`; `ski area insurance crisis independent ski areas` |
| 10 | **NZ passenger ropeway / rope tow regulatory regime + annual certification cost** | A3.2 | `WorkSafe New Zealand passenger ropeway registration design verification rope tow club field` |
| 11 | **Merino wool price NZ$/kg clean, 17–19 micron, current** | C1 | `merino wool price NZ auction 18 micron clean 2026`; `NZ Merino Company contract price` |
| 12 | **NZ Merino Company contract terms / ZQ premium** | C1 | `New Zealand Merino Company ZQ contract price premium grower` |
| 13 | **Used PistenBully / Prinoth asking prices** | A1.1 | `used PistenBully 300 for sale price`; `gebrauchte Pistenraupe kaufen Preis`; `中古 圧雪車 価格`; `used snowcat for sale` |
| 14 | **Relocated second-hand lift real project costs** | A3.2 | `ski lift relocation cost dismantle transport install`; `used T-bar lift for sale price installed` |
| 15 | **NZ high-country hunting block lease / trophy fee schedules** | C4 | `New Zealand red stag trophy fee SCI price list`; `tahr chamois trophy fee guided hunt NZ price` |

## E2. TIER 2 — refine the model (~20 searches)
| # | Item | § |
|---|---|---|
| 16–18 | Fixed-grip chairlift installed cost per metre, 2024–26 projects | A4 |
| 19–21 | NZ club-field rope tow build/rebuild costs (Craigieburn, Broken River, Mt Olympus, Temple Basin) | A3.1 |
| 22–23 | Snowcat fuel burn L/h and track set price/life (operator forums, dealer parts) | A1.2 |
| 24–25 | Gazex / remote avalanche control system capital cost per exploder | A6 |
| 26–27 | NZ rural building cost per m²; alpine/remote premium | A5.5 |
| 28–29 | 4WD track formation cost per km, NZ mountain terrain | A5.1 |
| 30–31 | Cat-ski day rates: Soho Basin, Southern Lakes Heliski, Baldface, Ski Arpa | C6 |
| 32–33 | Private ski club joining fees; Hermitage Club bankruptcy post-mortem | C6.2 |
| 34–35 | NZ rabbit control cost per hectare, Central Otago/Mackenzie | B4 |

## E4. ⚠️ NOT-YET-INTEGRATED SIBLING FILES
Four analyst files were delivered after this document was substantially drafted and are **not
yet reflected** in the cost tables: `japan-regulatory.md`, `japan-properties.md`,
`chile-argentina.md`, `snow-terrain.md`, `rest-of-world.md`. **Before this model is used:**
- Pull **skiable-days-per-season** from `snow-terrain.md` into §C6.1 (revenue is linear in it).
- Pull **Chile land/legal costs** from `chile-argentina.md` into §B7 Chile and §D4 — my Chile
  carry is the weakest table in this document.
- Check `rest-of-world.md` for jurisdictions (Sweden, Scotland, Georgia, Canada) that may beat
  both NZ and Chile on carry; the FX/tax analyst flags **Sweden exempts productive
  agricultural/forest land from property tax** and **Scotland exempts agricultural land from
  rates** — both potentially cheaper to hold than anything modelled here.

## E3. TIER 3 — country comparison (~20 searches)
| # | Item | § |
|---|---|---|
| 36–40 | Japan: 固定資産税 on 山林 assessed values; 免税点; スギ/ヒノキ 立木価格; J-クレジット forest credit price; 森林経営管理制度 | B1, C3.5 |
| 41–45 | Chile: contribuciones rate + agricultural exemption; sueldo mínimo; Ley 20.283 native forest; water rights 2022 reform; Ski Arpa pricing | B1, B3, C3.6 |
| 46–48 | NZ/JP/CL minimum wages and guide day rates, current | B3 |
| 49–50 | FX: NZD/MYR, USD/MYR, EUR/MYR, JPY/MYR, CLP/MYR as at date of use | FX block |

---

# F. SOURCE REGISTER

## F1. Sources actually consulted this session
**NO EXTERNAL SOURCE WAS RETRIEVED BY ME.** See the Provenance Warning at the head of this
document. The inputs were:

**(a) Sibling analysts' files, read from disk** — these carry their own source registers and
their WebSearch-derived citations; where I rely on them I attribute, and I have **not**
independently verified them:

| File | What I took from it | Used in |
|---|---|---|
| `nz-properties.md` | Tenure review (CPLA 1998 / CPL Reform Act 2022) put the alpine tops in Crown ownership; only **Mt Lyford** and **Fox Peak** credibly freehold; OIA 2005 + 2025 Amendment **farmland carve-out** | §B5, §C3.4, §C6.2, §D4 |
| `nz-regulatory.md` | **Benefit-to-NZ test requires MORE jobs/exports than today; cutting stock for a ski operation nets off against you** — the basis of §D1b; independent corroboration of the ACC/insurance conclusion | **§D1b**, §B2 |
| `fx-tax-title.md` | **FX anchors (NZD/MYR 2.41511, USD/MYR 4.03649, 100 JPY/MYR 2.5379)**; NZ rates NZD 1.5–6/ha/yr cross-check; **Crown rent** on leasehold; Japan 固定資産税 1.4% + 免税点; Chile contribuciones ~1% + sobretasa on large holdings | **FX block**, §B1 |
| `japan-regulatory.md`, `japan-properties.md`, `chile-argentina.md`, `snow-terrain.md`, `rest-of-world.md` | Not yet integrated — **see §E4** | — |

**(b) Analyst prior knowledge** (training data, cutoff ~May 2026) — tagged `[RECALL]`.
**(c) Arithmetic derivations** from (a) and (b) — tagged `[EST]`, derivations shown inline.
All §D model arithmetic was machine-checked for internal consistency.

## F2. Sources that SHOULD be used (verification targets for §E)
| Domain | Source | For |
|---|---|---|
| NZ farm economics | **Beef + Lamb NZ** Sheep & Beef Farm Survey, Class 1 SI High Country | C1 |
| NZ carbon | **MPI** ETS forestry guidance & look-up tables; **EPA** NZ ETS register; carbon market price reporters | C3 |
| NZ wool | **NZ Wool Services International**, AWEX indicators, **NZ Merino Company** | C1 |
| NZ rates | District council **Rating Information Databases** (public); the property's **LIM** | B1 |
| NZ safety law | **legislation.govt.nz** (AC Act 2001 s317; HSWA 2015); **WorkSafe NZ** ropeway guidance | A3.2, B2 |
| NZ pest control | **MPI / National Wilding Conifer Control Programme**; regional council pest management plans | B4 |
| Snowcats | **Kässbohrer/PistenBully** and **Prinoth** dealer networks; Mascus/Machineryline used listings | A1 |
| Lifts | **Doppelmayr**, **Leitner**, **Skytrac** ; Lift Blog project cost reporting | A3, A4 |
| Japan | **MAFF** 林野庁 立木価格統計; **総務省** 固定資産税 statistics; **J-クレジット制度** registry | B1, C3.5 |
| Chile | **SII** (avalúo fiscal / contribuciones); **CONAF** (Ley 20.283); **DGA** (water rights) | B1, C3.6 |
| Cat-ski pricing | Operator websites: Soho Basin, Southern Lakes Heliski, Baldface, Mustang Powder, Ski Arpa | C6 |

---

# G. RECOMMENDATIONS TO THE OTHER WORKSTREAMS

| To | Recommendation | Why |
|---|---|---|
| **Listings analyst** | Add **wilding-conifer / pest density** as a screening field on every candidate — assessable from aerial imagery pre-visit | §B4: swings carry by NZ$271,000/yr and can imply NZ$1M+ remediation |
| **Listings analyst** | Add **terrain angle distribution** as an *economic* screen — favour broad moderate-angle basins over steep faces | §A6: low-consequence terrain avoids NZ$1.1–4.5M avalanche-control capital and an explosives licensing regime |
| **Listings analyst** | Add **post-1989 / ETS-eligible plantable area** and **existing formed road access** as screening fields | §C3, §D3: the two largest determinants of whether the asset is cash-positive |
| **Listings analyst** | Flag **existing telecom/repeater site agreements** and **assignable grazing leases** in vendor records | §C7-10: free income, often already in place |
| **Legal analyst** | Confirm whether a **private members' rope tow** falls within the NZ passenger-ropeway regime | §A3.2: NZ$8–30k/yr per lift plus design verification |
| **Legal analyst** | Confirm the **ACC s317 bar** applies to a private/club ski operation, and scope residual **HSWA** exposure for the owner and its officers | §B2: the single largest jurisdictional cost advantage claimed here |
| **Legal analyst** | Advise whether a **club joining-fee model** is a regulated offer under the **FMCA 2013** | §C6.2 |
| **Legal analyst** | ⚠️ Resolve the **tension between the private-club end-state and the OIO "benefit to New Zealand" test** — my §C6.2 and your §0.3 point in opposite directions and the client needs one answer | §C6.2 / properties §0.3 |
| **Snow analyst** | Provide **skiable days per season** and low-snow-year frequency — §C6.1 revenue is linear in operating days and this is the largest revenue uncertainty | §C6.1 |
| **Snow analyst** | Provide **winter solar irradiance** at candidate latitudes/altitudes — drives §A5.2 generator sizing and fuel | §A5.2 |
| **Legal analyst** ⚠️⚠️ | **HIGHEST-VALUE OPEN QUESTION: is a defunct ski area / non-pastoral alpine title "farmland" for OIA purposes?** If NOT, it escapes the 2025 carve-out, falls under the faster consolidated national interest test, and **Model 1 becomes viable — worth NZ$100k–250k/yr plus the removal of an obligation to run four businesses** | **§D1b** |
| **Legal analyst** | Confirm whether **Crown rent** is payable on any leasehold component and at what rate — a carrying-cost line I could not size | §B1 |
| **All** | ⚠️ **My §D1b finding inverts the economic ranking of NZ.** Any recommendation that NZ is "low cost to hold" must be qualified by the consent regime forcing the high-cost operating model | §D1b |

---

*End of document. Prepared 27 August 2026. **No figure herein has been verified — see §E before use.***
