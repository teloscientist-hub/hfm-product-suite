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

### v3, the AI-centric suite

`v3/index.html` is a separate cut, not a successor. It sells only the 19 engagements where the
AI system is the deliverable, dropping the 41 units of the combined library that are AI-supported
or not about AI at all. Six tiers become five stages of one dependency chain. Same design tokens,
same per-engagement block structure, 28 routes.

| Route | Page |
|---|---|
| `#/` | Homepage |
| `#/ceiling` | The Ceiling Read, alone, as the only pre-chain sale |
| `#/stage/ground` … `#/stage/governance` | The four remaining stages |
| `#/unit/<slug>` | The 19 engagements |
| `#/limits` | What this deliberately does not do |
| `#/start` | Contact |

Content lives in `STAGES` and `U` at the top of the script block. Sourced from
`Mario Castelli Material/00 - The Three Types 2026-09-11.md` and
`00 - The AI-Only Site Tree 2026-09-11.md`. Noindexed like the others.

**Review document:** a one-line summary of all nineteen, numbered to match the route order, is at
`Mario Castelli Material/00 - The Nineteen, TLDR 2026-09-11.md` and as a Google Doc at
https://docs.google.com/document/d/1JXFq15lZKUqAURBc8iwOj0KngmuhEBQiqCo1UtbeXW4/edit

### v3.1, corrected 2026-09-11

**The four engagements the source verification pass found wrong have been rewritten.** Correction Capture
replaced Pairs Mining, which described the wrong method. Agent Context Architecture replaced Skill Server
Deploy, which was built on a vendor agent its own teachers abandoned. Production Stack and Briefing
replaced Production Workflow Install, which described a commercial app we cannot install. And **The Voice
Engine, formerly Agentic Email Install, moved from governance into judgment**, which renumbered every
engagement after it. Stage three is now five and stage five is six.

**Seven engagements are still thin and unfixed:** 02, 03, 06, 08, 11, 14, 19. Two the source specifies
are missing entirely: compute remediation, and the handover-and-gate phase. See
`Mario Castelli Material/00 - The Source Verification Pass 2026-09-11.md` before editing copy.

Units carry an optional `gate` field, rendered as a callout at the foot of the page. It is used for
qualification conditions and for correction notes.

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
