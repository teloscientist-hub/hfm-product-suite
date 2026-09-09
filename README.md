# Human First Media — Product Suite

Sales site for Human First Media's AI consulting engagements: a homepage, six tier pages
and 27 individual engagement pages.

**Live:** https://teloscientist-hub.github.io/hfm-product-suite/

## What this is

A single self-contained `index.html`. No build step, no dependencies, no framework.
Poppins is loaded from Google Fonts; everything else (including all illustration) is
inline. Hash-based routing renders all 34 pages from one file.

## Structure

| Route | Page |
|---|---|
| `#/` | Homepage |
| `#/tier/t0` … `#/tier/t5` | The six tiers |
| `#/solution/01` … `#/solution/27` | The 27 engagements |
| `#/method` | How we work |
| `#/contact` | Contact |

Content lives in two objects near the top of the script block: `TIERS` and `S`.
Editing copy means editing those. The templates render from them, so a change to a
page type reaches every page of that type.

## Brand

Built to the design system extracted from humanfirstmedia.com: Poppins throughout,
`#EE2A52` primary with `#8F5ED8` / `#3CC2DB` / `#F1B900` accents, `#222639` dark ground,
`#FFFBF9` card ground, `#70666A` body text. Flat, no shadows, 5px cards, 10px buttons.

One derived value: `#1F7A8C` for Tier 5, because six tiers needed six accents and the
brand has five.

## Local preview

```
python3 -m http.server 8000
```

Then open http://localhost:8000
