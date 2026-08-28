# Akaigawa terrain viewer

A single-page terrain tool for assessing the 赤井川カルデラ against the Rev 4 mandate. It loads
**real 国土地理院 (GSI) map tiles and real elevation data** — topographic base, aerial photography,
hillshade, and the 傾斜量図 slope-gradient raster — and measures cross-sections from the GSI DEM.

## Why this is a hosted page and not an Artifact

Artifacts run under a Content-Security-Policy that permits external **scripts** from a small CDN
allowlist but blocks external **images and fetch** entirely. Map tiles are images and the elevation
API is a fetch, so a tile-server map cannot work inside an Artifact. A plain hosted page has no such
restriction — the visitor's browser talks to `cyberjapandata.gsi.go.jp` directly.

## Deploy

No build step; it is one static file.

```sh
cd web
npx vercel deploy --prod
```

Or drag this folder onto https://vercel.com/new. Any static host works — Netlify, Cloudflare Pages,
GitHub Pages — since there is no server side.

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
