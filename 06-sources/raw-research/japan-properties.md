# Japan — Alpine / Large-Landholding Sourcing File
**Workstream:** Japan acquirable properties (ski areas seeking transferees, defunct ski areas, large forest/ranch land)
**Prepared:** 27 August 2026
**Client thesis:** Large landholding where LEGAL TITLE (所有権) includes genuine skiable alpine terrain; buy cheap, minimise carry, run a private ski mountain (snowcat / snowmobile / ski touring / rope tow) first, offset carry with forestry, grazing, hunting and lodging; expand to a commercial ski area only if demand justifies it.
**Currency:** All prices in Japanese yen (円) as instructed. An indicative MYR figure is given only where useful and is flagged — no live FX rate was obtainable this session.

---

## Evidence tags
- `[PRIMARY]` — government body, statutory filing, land registry, JMA
- `[SECONDARY]` — reputable media (北海道新聞, 新潟日報, 中日新聞, 秋田魁新報, 信濃毎日新聞, 日経, Bloomberg)
- `[BROKER-CLAIM]` — assertion in a listing / M&A platform / agency marketing. **This is the default for anything on BATONZ, TRANBI, 楽待, 山いちば, 家いちば, 現代不動産.** NOT verified fact.
- `[INFERENCE]` — my reasoning from the above, or structural/background knowledge

---

## ⚠️ TOOLING CAVEAT — READ BEFORE USING THIS FILE

Network egress was almost entirely closed for this workstream:

- **WebFetch: blocked for every domain attempted.** Confirmed blocked this session: `blog.skibumpslabo.com`, `yamaichiba.com`, `gendaifudousan.com`, `www.tranbi.com`, `www.nihon-ma.co.jp`. Per brief also blocked: `batonz.jp`, `skibumpslabo.com`, `nippon.com`, `ja.wikipedia.org`.
- **Direct HTTP via the CONNECT proxy: refused (403).** The proxy log explicitly records denials for `www.data.jma.go.jp`, `www.maff.go.jp`, `en.wikipedia.org`.
- **WebSearch: session budget exhausted at 200/200 calls** (consumed session-wide by parallel workstreams) after I had made **32** searches. The brief targeted 45–70. Searches B (large-forest portals), C (ranch), D (depopulated villages) and E (JMA snow/elevation verification) are therefore **materially incomplete**.

**Consequence: not one listing page, registry extract, or JMA table was read directly.** Everything below is WebSearch-synthesis plus source URLs. Every price, hectarage, elevation and — critically — **every claim about whether land is freehold (所有権) or leasehold (借地)** must be re-verified against the actual listing, the 登記簿謄本 and the 公図 before any offer. Sections marked **[GAP]** were not reached.

---

## MASTER TABLE — Ski areas & operating businesses

| # | Name (JP / romaji) | Pref. / Municipality | Area (ha) | 地目 / land type | Tenure | Price (¥) | Elevation | Existing plant | Status | Tag | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 | Mt.乗鞍スノーリゾート / Mt. Norikura Snow Resort | 長野県松本市 Matsumoto, Nagano | **12.99 ha** (129,900 m²) | not stated | **所有権 (freehold)** stated in listing | **¥380,000,000** asking (listed on 楽待); separately quoted **¥400,000,000** 譲渡希望額 | not obtained | RC hotel 6,195.21 m², built Nov 1978 (46 yrs); ski area + onsen | Owner 株式会社Blue Resort乗鞍 signalled withdrawal 2024; local group + ¥21.17M crowdfund (1,235 backers, Dec 2024) attempting continuation | [BROKER-CLAIM] | skibumpslabo blog 9403; norikura.gr.jp; camp-fire.jp/projects/796807 |
| A2 | 東北のスキー場・ホテル / unnamed Tohoku ski area + hotel | 東北 (region only disclosed) | not stated | not stated | **事業譲渡 (business transfer) — asset/land inclusion UNVERIFIED** | **¥10,000,000** 譲渡希望金額 | not stated | **2 lifts**, wide slopes, 600 m dedicated sled course, hotel 150 beds, 50-yr history | Live listing, 後継者不在; conditions: retain staff (5 or fewer, aged 50s–60s) + continue supplier relationships | [BROKER-CLAIM] | batonz.jp/sell_cases/73343 |
| A3 | 北海道スキー場 / unnamed Hokkaido ski area + lodge | 北海道 (region only) | not stated | not stated | 事業承継 — UNVERIFIED | **¥10,000,000–30,000,000** | not stated | lifts + lodge, night skiing | Live, **黒字 (profitable)**, sales ¥10–25M/yr, "excellent access" | [BROKER-CLAIM] | tranbi.com/buy/detail/?id=3202 |
| A4 | 長野県の人気スキー場+グランピング / Nagano ski area + glamping | 長野県 | not stated | n/a | **借地 (LEASED) — buyer must contract with landowner post-transfer** | **¥50,000,000**, later raised **+¥5,000,000 → ¥55,000,000** | not stated | **2 lifts, 10 courses**, bowl terrain, illumination event; rental fleet initial value >¥70M included | Live (listed Dec 2024); owner 株式会社信光オールウェイズ; annual profit ~¥8M; 1 manager + ~20 contract staff | [BROKER-CLAIM] | skibumpslabo blog 9403; tranbi.com/buy/detail/?id=15833 |
| A5 | 長野県リゾート（スキー場+ゴルフ場+ホテル）| 長野県 | not stated | not stated | 会社譲渡 (share deal) | **¥500,000,000** | not stated | ski area + golf course + hotel | Live | [BROKER-CLAIM] | via skibumpslabo blog 9403 / M&A platforms |
| A6 | スキー場の運営（非公開）| undisclosed | not stated | not stated | not stated | **<¥200,000,000** | not stated | not stated | Live, location withheld | [BROKER-CLAIM] | nihon-ma.co.jp/anken/needs_convey_single.php?no=16254 |
| A7 | 糸魚川シーサイドバレースキー場 / Itoigawa Seaside Valley | 新潟県糸魚川市 | not obtained | municipal | **市有 (city-owned)** | no price — **公募 (open solicitation) from FY2026** | not obtained | full ski area, opened 1980 | **City studying 民間譲渡; Seaside Valley enters public-solicitation process in FY2026.** City spend FY2022–24 ≈ ¥80–90M/yr; 指定管理料 ¥39M/yr | [SECONDARY] | niigata-nippo.co.jp/articles/-/748304; j-times.jp/archives/122351 |
| A8 | シャルマン火打スキー場 / Charmant Hiuchi | 新潟県糸魚川市 | not obtained | municipal | **市有 (city-owned)**, operated by 火打山麓振興(株) | no price | not obtained | full ski area, known for deep snow / off-piste | Also under 民間譲渡 study by Itoigawa City | [SECONDARY] | niigata-nippo; j-times.jp/archives/122351 |
| A9 | 室蘭市だんパラスキー場 / Muroran Danpara | 北海道室蘭市 | not obtained | municipal | 市有 | no price | not obtained | lifts, lodge | **廃止 scheduled end of FY2026**; operator 室蘭リゾート開発(株) to be dissolved; 振興公社 + marina to merge. No private-takeover solicitation found | [SECONDARY] | hokkaido-np.co.jp/article/1134360 |
| A10 | 士別市あさひスキー場 / Shibetsu Asahi | 北海道士別市朝日町 | not obtained | municipal | 市有 | no price | not obtained | lifts | Final ski day **22 Mar 2026**; **abolished 30 June 2026**; consolidated into 日向スキー場. Site's future use not announced | [SECONDARY]+[PRIMARY city page] | hokkaido-np.co.jp/article/1315330; city.shibetsu.lg.jp |
| A11 | 野麦峠スキー場 / Nomugitoge | 長野県松本市（旧奈川村）| not obtained | municipal | 市有 | no price | not obtained | lifts | **Abolished 2026** (reports differ: 廃止 1 Mar 2026 vs final day 29 Mar 2026 — treat as FY2025 year-end). Opened 1981; city was bearing ~**¥100M/yr**. Local volunteer group「盛りあげ隊」pursuing a local restart | [SECONDARY] | chunichi.co.jp/article/1215341 |
| A12 | 横向高原スキー場 / Yokomuki Kogen | 福島県 | not obtained | not obtained | not obtained | no price | not obtained | lifts | **Distressed.** All staff resigned July 2024 over unpaid wages; DMC aizu aimed to reopen Jan 2026; **18 Feb 2026 the 2025/26 season was cancelled** (repairs needed more time) | [SECONDARY] | skibumpslabo 7963 |
| A13 | 藤里町営スキー場 / Fujisato town ski area | 秋田県藤里町 | not obtained | municipal | 町有 | no price | not obtained | lifts | **Abolished** (announced 11 Sep 2025). July 2023 heavy rain collapsed part of the slope; town: "維持、継続は困難" | [SECONDARY]+[PRIMARY town page] | sakigake.jp/news/article/20250911AK0017; town.fujisato.akita.jp/kanko/notices/1794 |
| A14 | 荘川高原ファミリースキー場 / Shokawa Kogen Family | 岐阜県高山市 | not obtained | not obtained | not obtained | no price | not obtained | lifts | Abolition announced for 2025/26 | [SECONDARY] | skibumpslabo 7325 |
| A15 | ふるさとの森スキー場 | not obtained | not obtained | not obtained | not obtained | no price | not obtained | lifts | Abolition announced for 2025/26 | [SECONDARY] | skibumpslabo 7325 |
| A16 | 稚内市上勇知スキー場 / Wakkanai Kamiyuchi | 北海道稚内市 | not obtained | municipal | 市有 | no price | not obtained | lifts | **Abolition under consideration** | [SECONDARY] | skibumpslabo 7325 |
| A17 | 魚沼市のスキー場（複数）| 新潟県魚沼市 | not obtained | municipal | 市有 | no price | not obtained | lifts | City ends 指定管理者制度 at **end of FY2027**; three operating corporations to form a new company which must judge continuation | [SECONDARY] | skibumpslabo 7963 |
| A18 | 柏崎市所有スキー場 | 新潟県柏崎市 | not obtained | municipal | 市有 | no price | not obtained | lifts, ageing groomers | City will **not replace** ageing snow groomers; abolition anticipated once the groomer fails | [SECONDARY] | skibumpslabo 7963 |
| A19 | グリーンバレー神室スキー場 / Green Valley Kamuro | 山形県金山町 | not obtained | municipal | 町有 | no price | not obtained | lifts | Town-run, weekend-only operation while **discussions with a private company** continued | [SECONDARY] | skibumpslabo 4992; greenvalleykamuro.com |
| A20 | 村上市ぶどうスキー場 → ぶどうスノーリゾート | 新潟県村上市 | not obtained | was municipal | transferred to private operator | terms not disclosed | not obtained | lifts, east-facing slopes | **PRECEDENT: closed by the city 9 Mar 2025, reopened for 2025/26 by 株式会社シンクファースト (Sync First) as「ぶどうスノーリゾート」.** This is the working template for the "take over a closing municipal ski area" play | [SECONDARY] | snow.budoh-resorts.jp; skibumpslabo |

**Correction to a brief assumption:** the brief referenced "旧ぶどうの丘 / グレープスキー場 → 無償譲渡 → Sync First". The real case is **村上市ぶどうスキー場 (Niigata) → ぶどうスノーリゾート, operator 株式会社シンクファースト**. I could not confirm whether the transfer was 無償 (free). 「ぶどうの丘」is an unrelated 甲州市 (Yamanashi) winery facility. Treat the "free transfer" element as **unverified**.

---

## MASTER TABLE — Land (forest / ranch)

| # | Name / location | Pref. / Municipality | Area | 地目 | Tenure | Price (¥) | ¥/ha | Elevation | Status | Tag | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B1 | 北海道浜頓別大自然林 / Hamatonbetsu Grand Forest | 北海道枝幸郡浜頓別町 (Sōya, far N Hokkaido) | **~1,100,000 坪 ≈ 363.6 ha** | marketed as 山林; **unverified** | sale (所有権 implied, unverified) | **NOT PUBLISHED — enquiry only** | unknown | **[INFERENCE] LOW.** Coastal town; described as "gently undulating hills", ~1/3 flat. Likely 20–150 m | Live listing (two agencies) | [BROKER-CLAIM] | gendaifudousan.com/hamatonbetsu/; daikyosangyo.com/hamatonbetsu/; gendaifuchisan.com/hokkaido/hamatonbetsu.php |
| B2 | 余市郡赤井川村字富田 / Akaigawa Village, Tomita | 北海道余市郡赤井川村 | **225,000 坪 ≈ 74.4 ha** | 山林 (stated) | sale | **¥25,000,000** | **≈¥336,000/ha (≈¥111/坪)** | not obtained. [INFERENCE] village floor ~250 m; caldera rim 700–1,100 m | Live | [BROKER-CLAIM] | yamaichiba.com (via search synthesis) |
| B3 | 登別温泉 普通山林 | 北海道登別市 | **42,000 坪 ≈ 13.9 ha** | 普通山林 | sale | not captured | — | elevated plateau, gentle terrain; good sun; road + utility poles present | Live | [BROKER-CLAIM] | yamaichiba.com |
| B4 | 士別西士別町 牧場（牛舎付）| 北海道士別市西士別町 | house ~100 m² + garden ~600 m² + **barn/pasture ~15,000 m² (1.5 ha)** | mixed | sale | not captured | — | low | **Not accepting inquiries** | [BROKER-CLAIM] | ieichiba.com/project/P202200291士別西士別町 |
| B5 | 北海道の牧場（M&A）| 北海道 | not stated | not stated | 事業譲渡 | not stated | — | — | Live; sales ¥40M/yr | [BROKER-CLAIM] | sakura-ma.jp/sales/113 |
| B6 | 山いちば Hokkaido inventory (sold) | 北斗市茂辺地 #110; 小樽市桃内 #101; 河東郡音更町 #123 | various | 山林 | — | — | — | — | **済 (SOLD)** — useful only as comparables, prices not captured | [BROKER-CLAIM] | yamaichiba.com |

---

## Property notes

### B1 — 浜頓別 363 ha: big, cheap-ish, but **wrong for the ski thesis**
Marketed for forestry, agriculture (post-permit), **ranching (牧場経営)**, solar, wind and theme-park use; 5 minutes by car from the town centre; the 十七線川 stream runs through the parcel; roughly one third flat. That is a genuinely large, road-accessible, multi-use block. **But [INFERENCE]: Hamatonbetsu sits on the Okhotsk coast in far northern Hokkaido and the parcel is explicitly described as gently undulating hills — there is almost certainly no meaningful skiable vertical.** It scores well on the *carry-offset* half of the thesis (grazing, forestry, possibly wind) and near-zero on the *private ski mountain* half. **Price is not published; the agency must be contacted.** Two separate agencies market it, which may indicate a long-standing unsold parcel.

### B2 — 赤井川村 74 ha at ¥25M: **the best land lead found**
¥336,000/ha is at the very bottom of the national forest-price band (see benchmarks below) *despite* sitting in the Yoichi / Akaigawa caldera — adjacent to **キロロリゾート (Kiroro)** and inside the Niseko–Yoichi snow belt, among the most reliably deep-snow inhabited terrain on earth. [INFERENCE] That combination is either a real bargain or a signal of a defect: no legal road frontage (無道路地), a 保安林 (protected-forest) designation that bars clearing, split/unconsolidated title, or terrain too flat to matter. **74 ha is also small** for the client's brief — it is a base-area or single-drainage parcel, not a mountain. Priority actions: pull the 登記簿謄本 and 公図 for 字富田, confirm 地目, check the 保安林 register and the 森林経営計画, and read contours off the GSI 地理院地図 to measure actual vertical.

### A7/A8 — 糸魚川市: **the single most actionable municipal opportunity in Japan right now**
A city that owns two full ski areas, is explicitly studying transfer to private operators, and **enters an open public solicitation for Seaside Valley in FY2026** — i.e. the window is open now. Charmant Hiuchi in particular is nationally known for deep snow and lift-served off-piste. The economics disclosed are the negotiating lever: the city is spending ¥80–90M/yr with a ¥39M/yr management fee, so it is paying to keep these open and has a strong incentive to hand them over cheaply. **Critical unknown: does the city's title include the slopes, or is the mountain 国有林 / leased?** [INFERENCE] For a Niigata mountain area at this elevation, a substantial 国有林 or 財産区 component is likely. That must be resolved first — it is the difference between a real fit and a non-fit.

### A2 — BATONZ 73343 at ¥10M: cheapest lift-served entry found
A 50-year-old Tohoku ski area with **two lifts** plus a 150-bed hotel for a ¥10M ask is, at face value, the cheapest lift-served ski entry in the dataset. Two hard cautions: (1) it is structured as an **事業譲渡 (business transfer)**, which in Japan does *not* automatically convey real property — the brief's assumption that 土地建物 + 2 lifts are included **could not be verified this session**; (2) the seller conditions require retaining the existing staff and supplier relationships, which conflicts with a minimum-carry holding strategy. The region is disclosed only as "東北" — the municipality is withheld pending NDA.

### A4 — Nagano ski + glamping: **disqualified on tenure**
2 lifts, 10 courses, an existing glamping business and a >¥70M rental fleet for ¥55M looks attractive, but the listing states the **land is leased and the buyer must contract directly with the landowner after transfer.** That fails the client's core requirement that legal title include the skiable terrain. Useful mainly as evidence of what an operating small Japanese ski business is worth (~6–7× earnings on ~¥8M annual profit).

### A20 — 村上市ぶどう: the precedent that proves the play
A city closed a ski area in March 2025; a private company (Sync First) took it over and reopened it for the following season under a new brand. This is the exact manoeuvre available at Itoigawa, Muroran, Shibetsu, Nomugitoge and Kashiwazaki. **Terms were not disclosed** and I could not confirm the "free transfer" claim.

---

## E. Elevation, vertical drop and snow — analysis

**[GAP] No JMA data was obtained.** `www.data.jma.go.jp` returned 403 at the egress proxy (confirmed in the proxy's own failure log). No 最深積雪の平年値 was verified for any candidate. The figures below are **[INFERENCE] from general knowledge and must be re-pulled from JMA before they are relied on.**

### The structural finding — and it is the important one for this brief

**[INFERENCE] In Japan, private freehold title that contains 500 m+ of skiable vertical is close to non-existent, and where it exists it is not cheap.** The reasons are structural, not market timing:

1. **Above roughly 1,000–1,500 m in Honshū's main ranges, land is overwhelmingly 国有林 (national forest, administered by 林野庁).** It is not for sale. Where high ground is not national forest it is typically held by a **財産区 (property ward)**, a **生産森林組合**, old village commons (部落有林), or legacy corporate forest estates (王子, 日本製紙, 住友林業, 三井物産フォレスト) — none of which are ordinary open-market vendors.
2. **Most Japanese ski areas therefore do not own their slopes.** They hold 貸付 / 分収林 agreements with 林野庁, or leases from a 財産区 or village common. **This is the single biggest obstacle to the client's thesis in Japan**, and listing A4 — an operating 2-lift, 10-course ski area explicitly on 借地 — is a live illustration of exactly that pattern.
3. **National- and quasi-national-park zoning (国立公園 / 国定公園 特別地域)** overlays most of the high terrain in 八幡平, 鳥海, 蔵王, 栗駒, 妙高, 乗鞍, 白山 and 大雪, restricting clearing, lift construction and new structures even on privately-owned parcels.
4. **保安林 (protected forest) designation** independently bars felling and earthworks on a large share of steep private forest, and does not appear on a casual listing.

### Where the thesis *can* actually work in Japan

**[INFERENCE] Hokkaido, at 250–450 m of freehold vertical, is the achievable version — and the snow compensates for the modest drop.** Candidate belts:
- **余市 / 赤井川 / 喜茂別 / 留寿都** (Niseko–Kiroro snow belt) — village floors 200–400 m, caldera rims and independent cones 700–1,100 m. Lead **B2** sits here.
- **富良野 / 南富良野 / 大雪山麓** — 400–700 m bases, private former 開拓 blocks exist.
- **日高山脈西麓** — large private forest, low prices, but access and avalanche exposure are serious.

In Hokkaido the effective snow line is at sea level, land is dominated by private and municipal (not national-forest) ownership far more than in Honshū, and 600–1,000 m private blocks genuinely exist. The trade is **less vertical, better and colder snow, cleaner title.**

**Japanese ski-area vertical for calibration [INFERENCE, unverified]:** typical Japanese areas run 300–700 m of vertical; only a handful exceed 800 m (八方尾根 ~1,070 m, 蔵王 ~880 m, ニセコ全山 ~900 m, 苗場, 志賀高原). A private 300–400 m freehold drop is therefore not far below a *median* commercial Japanese ski area — a genuinely encouraging point for the snowcat/rope-tow model.

**Snow depth reference points [INFERENCE — unverified recollection, NOT JMA-sourced; re-pull before use]:** 酸ヶ湯 (Sukayu, Aomori, ~890 m) is Japan's snowiest AMeDAS station, max-depth normals well above 350–400 cm with records over 500 cm; 倶知安 (Kutchan) roughly 180–200 cm; 津南 / 十日町 (Niigata) 250–300+ cm; 浜頓別 far lower, likely 70–100 cm. **The Hamatonbetsu lead (B1) is not merely low-relief — it is also likely to be a comparatively thin-snow site by Hokkaido standards.**

---

## F. Reference transactions and asking prices (10 data points)

| Asset | Date | Consideration (¥) | Note | Tag |
|---|---|---|---|---|
| HANAZONO, ニセコ | 2004 | **¥3,000,000,000** | Acquired by Japan Harmony Resort (Australian capital) from Tokyu Real Estate, which had invested a reported ¥160bn — a ~98% discount to development cost | [SECONDARY] |
| 斑尾高原 (Madarao Kogen), 長野 | 2005 | **~¥800,000,000** | Ski area + hotel assets + operating rights out of civil rehabilitation (¥5.2bn liabilities, filed Apr 2005) | [SECONDARY] |
| 西武HD → GIC portfolio | agreed 10 Feb 2022 | **~¥150,000,000,000** for 31 facilities (15 hotels, 10 golf, **6 ski resorts**) | Gain ~¥80bn vs 31 Mar 2021 book. Incl. 苗場スキー場 + 苗場プリンスホテル; reports also name かぐら, 焼額山, 八海山. Seibu subsidiaries continue to operate | [SECONDARY] |
| 星野リゾート トマム, 北海道占冠村 | ~2025 | **~¥40,800,000,000** | Shanghai Yuyuan (Fosun) selling to real-estate investment LLC "YCH16" amid funding stress | [SECONDARY] |
| ハーレスキーリゾート, 長野 | Oct 2015 | undisclosed | Share acquisition by 日本スキー場開発 [6040] | [SECONDARY] |
| 日本スキー場開発 [6040] 固定資産譲渡 | **31 Mar 2026** | not obtained | TDnet: 「固定資産の譲渡及び固定資産売却益の発生見込み」then 「連結子会社における固定資産の譲渡手続完了」. **Which asset, and to whom, could not be determined this session — worth chasing, it is a recent, real, disclosed ski-asset disposal** | [PRIMARY filing, content not read] |
| Mt.乗鞍 (A1) | current | **¥380,000,000** asking (12.99 ha freehold + 6,195 m² RC building) / **¥400,000,000** 譲渡希望額 | ≈ **¥29,000,000/ha** including a large 1978 building | [BROKER-CLAIM] |
| Tohoku ski area + hotel (A2) | current | **¥10,000,000** asking | 2 lifts + 150-bed hotel; asset inclusion unverified | [BROKER-CLAIM] |
| Hokkaido ski area + lodge (A3) | current | **¥10,000,000–30,000,000** asking | Profitable, ¥10–25M sales | [BROKER-CLAIM] |
| 赤井川村 74.4 ha 山林 (B2) | current | **¥25,000,000** asking | **¥336,000/ha** | [BROKER-CLAIM] |

---

## Forest-land price benchmarks (for the ¥/ha model)

| Source / class | ¥/坪 | ¥/ha equivalent | Tag |
|---|---|---|---|
| 林地ドットコム national average, 2026, n=177,901 | **¥2,141** | ≈¥6,480,000 | [BROKER-CLAIM] — a portal aggregate of **asking** prices, not transactions |
| 都市近隣山地 (peri-urban) | 3,300–5,000 | ¥10.0M–15.1M | [SECONDARY] |
| 農村山地 (rural) | 1,000–2,600 | ¥3.0M–7.9M | [SECONDARY] |
| 林業本場山地 (forestry heartland) | 300–1,600 | ¥0.9M–4.8M | [SECONDARY] |
| **山村奥地山地 (remote mountain interior)** | **150–650** | **¥450,000–1,970,000** | [SECONDARY] |
| Per-m² framing | 都市近郊 ¥1,000–5,000/m²; 農村 ¥100–1,000/m²; 林業本場 & 山村奥地 **<¥100/m²** | | [SECONDARY] |
| Per-ha regional examples | 宮崎 ¥150k–600k/ha; 大分 ¥100k–500k/ha; 千葉 ¥500k–2.0M/ha | | [SECONDARY] |

**[INFERENCE] Reconciliation with the client's ¥100–1,000/坪 (¥300k–3.0M/ha) assumption:** that band is correct, but only for the **山村奥地 / 林業本場** classes — remote interior mountain forest. It is *not* achievable near an existing resort, near a road network, or on land with development potential, where 農村山地 and 都市近隣 rates (¥3M–15M/ha) apply. The Akaigawa lead (B2) at **¥336k/ha** prices as remote interior despite a premium snow location, which is the anomaly to investigate.

**Tax note [SECONDARY]:** on disposal, standing timber is taxed as **山林所得** and the land as **譲渡所得** — two separate computations. Relevant to exit modelling and to how a vendor prices timber-in-situ.

---

## C. Ranch / grazing land — legal constraint (this governs the whole category)

**[PRIMARY-adjacent / INFERENCE] The 地目 on the title determines whether the client can buy at all:**
- **地目 = 田 or 畑 (farmland):** acquisition requires 農業委員会 permission under 農地法第3条. For a non-resident foreign individual with no farming plan and no local operating record, this is effectively closed. 旭川市 notes the rules changed again from April 2025 (令和7年4月).
- **地目 = 山林 / 原野 / 牧場:** **not** 農地法 land — acquisition is unrestricted, including by a foreign individual. **This is the category to buy in**, and it should be a hard screening filter on every lead.
- **Practical implication:** buy 山林/原野 and graze it, rather than buying 牧場-as-farmland. Grazing does not require the land to be 農地.

**Channels identified but not worked [GAP]:**
- **全国公共牧場マップ** (souchi.lin.gr.jp/farmmap), 一般社団法人日本草地畜産種子協会 — the national register of public pastures. **This is the correct primary tool for finding 町営牧場 being wound down** and was not reachable this session.
- 農林水産省「公共牧場について」(maff.go.jp) — proxy-blocked.
- 北海道農政部 生産振興局畜産振興課 — the prefectural pipeline for public-pasture policy.
- **北海道農業担い手育成センター「第三者農業経営継承」** (adhokkaido.or.jp/ninaite/transfer/) — the formal third-party farm-succession programme, the legitimate route into a ranch for a non-heir.
- 北海道庁 農業施設管理課「自作農財産の管理」 — prefectural land disposals.
- BATONZ shows **24 listings** matching 「牧場」; these were not individually reviewed.

---

## D. Depopulated villages / whole-hamlet sales — **[GAP]**

Not researched. The WebSearch budget was exhausted before this section. Search terms to run next session: 「限界集落 売却」「集落 まるごと 売り」「無人集落 売買」「廃村 土地 売却」「分校跡地 売却」.

---

## Channels identified but not exhausted — next-session work list

**Ski-area intelligence (highest value, all currently unreadable):**
- `blog.skibumpslabo.com/archives/9403`「譲渡先を探しているスキー場」— **the single most valuable page for this brief.** It carries a structured table of ski areas seeking transferees with owner, operating status and 譲渡希望額. I extracted only 3–4 rows from search snippets; the full table was never read.
- `skibumpslabo.com/archives/7963` (2026/27 closures), `/7325` (2025/26 closures), `/6520` (2024/25), `/4992` (2023/24 — records **10 abolished, 14 effectively abolished, 4 suspended** in that season alone), `/7965` and `/7335` (ownership / operator / lift changes).

**M&A platforms (listing detail pages all blocked):** BATONZ 73343 and its 「牧場」×24 and スポーツ・レジャー施設×長野県×20 result sets; TRANBI 3202 / 3569 / 15833; 日本M&Aセンター 16254; スピードM&A 7070; M&Aクラウド 6431; M&A Circle; さくらMAアドバイザリー 113.

**Land portals:** 山いちば (yamaichiba.com) full 販売中 inventory + its 「山林の価格と相場」page; 山林バンク (sanrinbank.jp); 家いちば (ieichiba.com); 不動産連合隊 (fudosanlist.cbiz.ne.jp — has リゾート and 土地 filters for Hokkaido); ジモティー (jmty.jp) 山林 category; 林地ドットコム (tochi-d.com).

**Primary/official:** 林野庁「森林の売買・評価に関する情報」; JMA 過去の気象データ (最深積雪平年値); 国土地理院 地理院地図 (contours, for measuring real vertical on any candidate); each target municipality's 未利用財産売却 / 一般競争入札 page (糸魚川市, 室蘭市, 士別市, 松本市, 柏崎市, 魚沼市, 金山町 are the live ones).

---

## Sources

1. https://blog.skibumpslabo.com/archives/9403 — 譲渡先を探しているスキー場 (**blocked; snippet-level only**)
2. https://skibumpslabo.com/archives/7963 — 2026/2027 廃止・閉鎖する（かもしれない）スキー場
3. https://skibumpslabo.com/archives/7325 — 2025/2026 廃止・閉鎖する（かもしれない）スキー場
4. https://skibumpslabo.com/archives/6520 — 2024/2025 廃止・閉鎖する（かもしれない）スキー場
5. https://skibumpslabo.com/archives/4992 — 2023/2024 廃止・閉鎖する（かもしれない）スキー場
6. https://skibumpslabo.com/archives/7965 — 2026/2027 所有者・運営会社・名称変更、リフト新設・廃止
7. https://skibumpslabo.com/archives/7335 — 2025/2026 所有者・運営会社・名称変更
8. https://blog.skibumpslabo.com/archives/3209 — 【考察】Mt.乗鞍スノーリゾートの売却検討について
9. https://batonz.jp/sell_cases/73343 — 【スキー場・ホテル運営】東北の施設 (**blocked**)
10. https://batonz.jp/sell_cases/?q=%E7%89%A7%E5%A0%B4 — BATONZ 牧場 listings (24)
11. https://batonz.jp/sell_cases/bk_1700000/bk_1702004/pref_23/ — BATONZ スポーツ・レジャー施設×長野県 (20)
12. https://www.tranbi.com/buy/detail/?id=3202 — 【黒字】北海道スキー場の事業承継 (**blocked**)
13. https://www.tranbi.com/buy/detail/?id=15833 — 長野県グランピングリゾート所有権の譲渡
14. https://www.tranbi.com/buy/detail/?id=3569 — スキー場至近の温泉宿事業
15. https://www.nihon-ma.co.jp/anken/needs_convey_single.php?no=16254 — スキー場の運営（非公開｜2億円未満）(**blocked**)
16. https://www.niigata-nippo.co.jp/articles/-/748304 — 糸魚川市所有の2スキー場、民間譲渡を検討
17. https://j-times.jp/archives/122351 — ２スキー場 民間譲渡へ（上越タイムス）
18. https://www.hokkaido-np.co.jp/article/1134360/ — 室蘭リゾート開発解散へ、だんパラ廃止
19. https://www.hokkaido-np.co.jp/article/1315330/ — 士別・あさひスキー場、6月末に廃止
20. https://www.hokkaido-np.co.jp/article/1292283/ — 士別市「スキーのまち」朝日地区ゲレンデ閉鎖へ
21. https://www.city.shibetsu.lg.jp/.../610.html — あさひスキー場（士別市）
22. https://www.chunichi.co.jp/article/1215341 — 松本・野麦峠スキー場「盛りあげ隊」
23. https://www.sakigake.jp/news/article/20250911AK0017/ — 藤里町、町営スキー場を廃止
24. https://www.town.fujisato.akita.jp/kanko/notices/1794 — 藤里町営スキー場 専用ページ
25. https://snow.budoh-resorts.jp/ — ぶどうスノーリゾート（Sync First）
26. https://greenvalleykamuro.com/ — グリーンバレー神室スキー場
27. https://norikura.gr.jp/2024/10/mt-norikurasnowrresortinformation3/ — Mt.乗鞍 営業継続 経過報告
28. https://camp-fire.jp/projects/796807/view — Mt.乗鞍 クラウドファンディング（¥21,169,001 / 1,235名）
29. https://www.bloomberg.com/jp/news/articles/2022-02-10/R72OVMT0AFB401 — 西武HD 31施設 GIC
30. https://www.nikkei.com/article/DGKKZO62215370Q2A630C2DTA000/ — 西武HD 売却益800億円
31. https://tabiris.com/archives/prince-naeba/ — 苗場スキー場売却の衝撃
32. https://www.nikkei.com/nkd/disclosure/tdnr/20260331593612/ — 日本スキー場開発 固定資産譲渡手続完了 (2026-03-31)
33. https://moneyworld.jp/stock/6040/news/disclosure/3949432 — 日本スキー場開発 固定資産の譲渡及び売却益見込み
34. https://skis-hijikata.o.oo7.jp/story_Skiarea_monay.htm — スキー場のいろいろな金額（HANAZONO ¥3bn、斑尾 ¥800M）
35. https://gendaifudousan.com/hamatonbetsu/ — ［売土地］北海道浜頓別大自然林 (**blocked**)
36. https://gendaifuchisan.com/hokkaido/hamatonbetsu.php — 浜頓別町 大規模土地
37. http://daikyosangyo.com/hamatonbetsu/ — 大京産業 同物件
38. https://yamaichiba.com/ / /forest-brokerage/ / /category/sanrin-hokkaido/ — 山いちば (**blocked**)
39. https://yamaichiba.com/山林の価格と相場/ — 山林の価格と相場
40. https://www.tochi-d.com/rinchi/ — 林地ドットコム 坪単価一覧（2026年 177,901件）
41. https://rinchi.tochi-d.com/?a=1&choice=area&p=北海道 — 北海道の林地取引価格
42. https://www.rinya.maff.go.jp/j/keikaku/shinrinbaibai/sinrinbaibai_hyouka.html — 林野庁 森林の売買・評価
43. https://www.yamabaton.com/media/forest-land-price-guide — 山林の価格相場 都道府県別
44. https://sanrinbank.jp/ — 山林バンク
45. https://www.ieichiba.com/project/P202200291士別西士別町 — 家いちば 士別 牧場
46. https://souchi.lin.gr.jp/farmmap/ — 全国公共牧場マップ
47. https://www.maff.go.jp/j/chikusan/sinko/lin/l_siryo/koukyou_bokujyou.html — 農水省 公共牧場について (**proxy-blocked**)
48. https://www.adhokkaido.or.jp/ninaite/transfer/ — 北海道 第三者農業経営継承
49. https://www.pref.hokkaido.lg.jp/ns/ssk/home1.html — 北海道 自作農財産の管理
50. https://www.city.asahikawa.hokkaido.jp/.../d081535.html — 農地の売買・貸借の制度変更（令和7年4月）
51. https://sakura-ma.jp/sales/113/ — さくらMAアドバイザリー 北海道の牧場
52. https://fudosanlist.cbiz.ne.jp/list/sale/?prop=1&nstg=2&area=hokkaido&eq=1008 — 北海道不動産連合隊 リゾート
53. https://www.pref.nagano.lg.jp/zaikatsu/kensei/koyu/baikyaku/annai/nyusatu-ichiran.html — 長野県 一般競争入札 売却物件一覧
