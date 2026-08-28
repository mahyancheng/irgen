# Akaigawa terrain viewer

A single-page terrain tool for assessing the 赤井川カルデラ against the Rev 4 mandate. It loads
**real 国土地理院 (GSI) map tiles and real elevation data** — topographic base, aerial photography,
hillshade, and the 傾斜量図 slope-gradient raster — and measures cross-sections from the GSI DEM.

## Why this is a hosted page and not an Artifact

Artifacts run under a Content-Security-Policy that permits external **scripts** from a small CDN
allowlist but blocks external **images and fetch** entirely. Map tiles are images and the elevation
API is a fetch, so a tile-server map cannot work inside an Artifact. A plain hosted page has no such
restriction — the visitor's browser talks to `cyberjapandata.gsi.go.jp` directly.

## Running it

There is no build step and no server side — it is one static file.

### Locally, publishing nothing

The simplest option, and the right one for a private acquisition tool. The map tiles load from the
GSI servers in *your* browser, so a local file works exactly like a hosted one.

```sh
cd web && python3 -m http.server 8000
# then open http://localhost:8000
```

### GitHub Pages

`.github/workflows/pages.yml` deploys **`web/` only** — the dossiers, prices and vendor details
elsewhere in this repository are not uploaded. To turn it on:

1. Merge this branch to `main`.
2. Repo **Settings → Pages → Source: GitHub Actions**.
3. The workflow runs on any push touching `web/`, or on demand via **Actions → Deploy terrain
   viewer to Pages → Run workflow**.

To deploy from this branch before merging, also add it under **Settings → Environments →
github-pages → Deployment branches**, which defaults to the default branch only.

> **A GitHub Pages site is public** — including from a private repository, on every plan below
> Enterprise Cloud. Publishing it puts the caldera under evaluation on the open web. It carries no
> price and no vendor name, but it does disclose the target area.

### Other hosts

Vercel, Netlify, Cloudflare Pages and any other static host all work — drop the folder in. None of
them could be reached from the workspace this was written in; only GitHub was.

## What it does

| Control | Purpose |
|---|---|
| **Base layer** | 淡色地図 / 標準地図 (contours, place names, peak elevations) / 全国最新写真 (aerial) |
| **陰影起伏図** | Hillshade — reads the landform shape at a glance |
| **傾斜量図** | **Slope-gradient raster. Darker = steeper.** This is the layer that answers the mandate's gradient question directly. |
| **Measure profile** | Click two points. Samples the GSI DEM along the line and draws a real cross-section. |

The profile readout reports **the steepest band delivering 300 m of vertical** — the exact figure
the Rev 4 specification turns on (target 22–28°, hard ceiling ~30° sustained).

## Data and attribution

- Tiles and DEM: 国土地理院 (Geospatial Information Authority of Japan) — 地理院タイル.
  Attribution 「出典：国土地理院」 is rendered on the map, as their terms require.
- Elevation API: `cyberjapandata2.gsi.go.jp/general/dem/scripts/getelevation.php`.
- Review the GSI terms before any commercial or high-volume use:
  https://maps.gsi.go.jp/development/ichiran.html

## What is *not* here

**No listing photographs.** The vendor's Jimoty listing could not be retrieved — `jmty.jp` is
refused at this workspace's network egress proxy — so no listing imagery exists in this repository
to publish. The GSI aerial layer is genuine imagery of the site, but it is not the vendor's photos
of the parcel.

**No parcel boundary.** The parcel's 地番 is unknown, so nothing here draws its outline. Everything
shown is the landform, not the property. Once the 地番 is obtained the boundary can be added.
