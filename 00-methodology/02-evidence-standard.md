# Evidence standard and confidence grading

Every material assertion in this repository carries a grade. The grade describes the
**source class**, not the analyst's enthusiasm.

| Tag | Meaning | Examples | How it may be used |
|-----|---------|----------|--------------------|
| `[P1]` | **Primary.** Statute, regulation, government register, court decision, official statistics, meteorological agency data, listed-company disclosure | NZ legislation, LINZ/DOC publications, 林野庁 and 気象庁 data, Chilean BCN legal texts, JMA normals | May be relied on. Still requires a date check |
| `[P2]` | **Reputable secondary.** Law-firm briefings, established trade press, national broadcasters, academic literature | Buddle Findlay, Bell Gully, RNZ, ODT, Nikkei, peer-reviewed snow science | May be relied on for direction; confirm numbers against `[P1]` before an offer |
| `[P3]` | **Marketing / listing claim.** Anything asserted by a seller, broker or agent | Broker particulars, agency press releases, portal listings, M&A platform teasers | **Never treated as fact.** Used only to identify a target and to frame questions |
| `[E]` | **Estimate or inference.** Derived by the analyst | $/ha benchmarks, CAPEX build-ups, carrying-cost models | Derivation must be shown inline |
| `[U]` | **Unverified / unavailable.** Could not be established from open sources | Sale prices withheld, concession terms not public, cadastral detail behind a paywall | Must be listed in the pre-offer checklist |

## The broker-claim rule

The client's instruction was explicit: *broker marketing claims should not be treated as fact
without verification.* In practice, four categories of listing claim are wrong or misleading
often enough to require independent corroboration every time:

1. **Area.** Marketed hectares frequently combine freehold, leasehold and licensed area into
   one headline figure. Always decompose.
2. **Tenure.** "Freehold" in a headline can describe only part of the holding. Terms like
   *"exclusive concession"*, *"long-term licence"*, *"secure tenure"* and *"perpetual lease"*
   are **not ownership** and are used interchangeably in marketing copy.
3. **Skiable terrain and vertical.** Marketed skiable area routinely includes land the seller
   does not own, and vertical is measured from points no road reaches.
4. **Income.** "Potential" income, gross turnover and EBITDA are used loosely. Always ask for
   the last three years of audited accounts and the stock reconciliation.

## Currency

All conversions use the single FX basis recorded in `00-methodology/03-fx-basis.md`,
fixed at the report date. Original-currency figures are always shown alongside the MYR figure
so the reader can re-convert at a later rate.

## Known limits of this study

- **No title searches were ordered.** Tenure findings rest on published descriptions,
  government registers accessible in open form, and secondary reporting. Section 05 specifies
  the searches to commission.
- **No site visits, and no winter site visits.** Snow, aspect and terrain findings rest on
  meteorological records, published studies and topographic data.
- **Network limits.** Several broker and government sites were unreachable from the research
  environment; where a fact could only be sourced from such a site it is graded `[U]` or is
  carried at the grade of the secondary source that reported it.
- **Listings move.** Rural campaigns close, prices are revised and sales go unreported.
  Every listing carries the date of the evidence. Anything older than ~12 months should be
  re-confirmed with the agent before it is relied on.
