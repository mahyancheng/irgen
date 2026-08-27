# FX basis and transaction costs

## 1. The conversion basis

All MYR figures in this repository use these rates, fixed at the report date.

| Pair | 1 unit → MYR | 1 MYR → unit | Grade |
|---|---:|---:|---|
| **NZD/MYR** | **2.41511** | 0.41406 | `[P3]` single source, 23 Aug 2026 |
| **JPY/MYR** | **0.025379** (¥100 = RM 2.5379) | 39.4022 | `[P3]` single source |
| **USD/MYR** | **4.03649** | 0.24774 | `[P3]` single source |

**Verification status: single-source, cross-checked only for internal consistency.** The
research environment could not reach any FX provider or central bank directly, so the brief's
"two independent sources per pair" standard **was not met for any currency.** That is stated
rather than concealed.

**The one check that was possible.** The three anchors imply **NZD/USD 0.59832**,
**USD/JPY 159.05** and **NZD/JPY 95.16**. All three are plausible cross-rates, so the anchors
are mutually coherent and unlikely to be corrupt. That is genuine evidence, and it is all there
is. `[E]`

### Not sourced — indicative bands only, do not use for pricing

`[E — low confidence]` EUR 4.36–4.84 · GBP 5.01–5.57 · CAD 2.78–3.03 · SEK 0.384–0.449 ·
CLP 0.00404–0.00448 · **TRY 0.084–0.106 (very low confidence)** · GEL 1.42–1.52.

Fill-in rule for any other currency: `X/MYR = 4.03649 ÷ (units of X per USD)`.

### Convenience conversions

| Original | MYR |
|---|---|
| NZ$ 1 m | RM 2.42 m |
| **NZ$ 2.8 m** (Mt Dobson asking, ex-GST) | **RM 6.76 m** |
| NZ$ 20 m | RM 48.3 m |
| NZ$ 50 m | RM 120.8 m |
| **¥ 10 m** (cheapest Japanese ski business found) | **RM 253,800** |
| **¥ 25 m** (Akaigawa 74.4 ha 山林) | **RM 634,500** |
| ¥ 100 m | RM 2.54 m |
| ¥ 380 m (Mt. 乗鞍) | RM 9.64 m |
| US$ 1 m | RM 4.04 m |

## 2. FX is the largest variable after price

12-month ranges could not be sourced. As a working substitute, **±10–15 % a year and ±20–30 %
over a three-to-five-year hold is normal** for these pairs. `[E]`

> **A 15 % FX move on a MYR 100 m position exceeds the entire transaction-cost stack in any
> jurisdiction in this study.** Transaction costs span about 6 percentage points across the
> whole set; annual FX volatility is 10–15 points. **Optimising for stamp duty while ignoring
> currency is the wrong order of operations.**

Rates should be re-struck at the date of any offer, and a forward or staged conversion
considered for the deposit-to-settlement window.

## 3. ⚠️ Malaysian outward-investment capacity — settle this before anything else

A resident individual **with domestic ringgit borrowing** is reportedly limited to
**RM 1 million per calendar year** of investment in foreign currency assets. A resident
**without** domestic ringgit borrowing faces **no limit**. `[U — Bank Negara Malaysia's site
was unreachable from the research environment]`

> **Every candidate in this study costs far more than RM 1 m. If the client has any domestic
> ringgit borrowing, the purchase cannot lawfully be funded in a single year.** This is a
> structural constraint on the entire mandate, not a compliance detail, and it must be
> confirmed **in writing with the client's own bank before any deposit is paid.**

## 4. All-in purchase cost for a non-resident, as a % of price

| Jurisdiction | % of price | Note |
|---|---:|---|
| **New Zealand** | **0.5–2 %** + a large fixed OIO fee | **No stamp duty.** The cost here is screening, not tax: NZ$22,800 stage one, +NZ$83,700 if referred to the national interest test |
| Georgia | 0.5–1.5 % | Cheapest — but foreigners likely cannot own the land |
| **Chile** | **1–3 %** | No transfer tax; IVA does not touch land |
| **USA (mountain west)** | **1–3 %** | MT/WY/ID/UT have no transfer tax; title insurance 0.3–0.6 % |
| Sweden | **1.7 % individual / 4.4 % company** | A 2.75-point gap — **buy personally** |
| Canada BC rural | 3–5 % | The 20 % foreign surcharge **likely does not apply** — it is residential-only *and* specified-areas-only; remote alpine fails both tests |
| Scotland | 5–7 % | LBTT non-residential tops at 5 %; ADS 8 % on any residential element |
| **Japan** | **5–8 %** | Broker commission at 3.3 % dominates, plus 不動産取得税 and 登録免許税 |
| Türkiye | 5–7 % | 4 % tapu harcı |

All `[U]` — model recall, not verified against current schedules. Confirm with local counsel.

**Transaction cost is not the deciding variable.** It spans ~6 points across the set, against
10–15 points of annual FX volatility and tenure risk that is 100 % of value.

## 5. Exit and death — where the real tax sits

| Jurisdiction | Inheritance / estate exposure for a foreign owner | Exit withholding |
|---|---|---|
| **Japan** | ⚠️ **Up to 55 %** on Japan-situs assets, **unrelieved** — the Malaysia–Japan treaty is income-tax only | 10.21 % of gross |
| **USA** | ⚠️ **40 % above a US$60,000 exemption**, and there is **no Malaysia–US estate treaty** | FIRPTA 15 % of gross |
| UK / Scotland | 40 % on UK land regardless of domicile | — |
| Canada | — | s.116, 25 % of gross |
| **New Zealand** | **Nil** | — |
| **Sweden** | **Nil** | — |

Japan also has a **capital gains cliff: 39.63 % at ≤ 5 years' holding vs 20.315 % beyond.**

## 6. Holding vehicle

- Malaysian individuals are **outside** Malaysia's capital gains tax, which applies to
  companies, LLPs and trusts.
- **A Malaysian company would therefore drag the foreign gain into Malaysian CGT on
  remittance.** `[U]`
- Sweden charges 1.7 % transfer tax to an individual against 4.4 % to a company.

> **Default: hold personally, not through a Malaysian company.** Confirm with Malaysian tax
> counsel before structuring.

**Double tax agreements are near-irrelevant here.** Articles 6 and 13(1) give the situs state
primary taxing rights over land, Malaysia exempts the individual anyway so there is nothing to
credit — and **none of them are inheritance-tax treaties**, which is where the real exposure
sits.
