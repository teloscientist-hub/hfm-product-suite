# Human First Media – Product Suite

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

### The AI dependency badge

Every engagement page carries a badge saying how much of the delivered thing is actually AI: AI-centric
(6 pages), AI-supported (5), or not an AI engagement (16). Classified by deliverable rather than title,
and verified against the intervention specs. The typing lives in `TY` and the labels in `TYPEINFO`, both
next to `PROVEN` at the top of the script block. Set `SHOW_TYPE=false` to hide the badge everywhere.

Reasoning and the per-engagement argument: `00 - The v2 Twenty-Seven, Typed 2026-09-11.md`.
Source check: `00 - The v2 Source Verification Pass 2026-09-11.md`.

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

### v4, the Mario-only catalogue, typed

`v4/index.html` is a third cut. It sells the **37 engagements the Mario material yields on its own**,
in the six tiers of `Mario Castelli Material/00 - The Mario Menu, HFM Without Molly 2026-09-11.md`,
with **no Molly units at all**. Every engagement carries an AI-dependency label, and the label is
navigable: the whole catalogue filters by it.

| Route | Page |
|---|---|
| `#/` | Homepage |
| `#/tier/t0` ... `#/tier/t5` | The six tiers |
| `#/tier/<id>/<ai-centric\|ai-assisted\|not-ai>` | A tier, filtered by label |
| `#/unit/<slug>` | The 37 engagements |
| `#/types` | How much of this is AI: the three labels, the cross-tab, the whole catalogue |
| `#/types/<ai-centric\|ai-assisted\|not-ai>` | The catalogue, filtered |
| `#/limits` | Four refusals, two named gaps, and who this was written for |
| `#/start` | Contact |

**What is different from v3.** v3 sells only AI-centric work and drops everything else. v4 sells the
whole Mario library and labels each engagement instead, because the counts are the finding:
**12 AI-centric, 10 AI-assisted, 15 with no model in them anywhere.** Tier 1 gates every AI tier and
contains no AI-centric unit. Tier 2 is five for five. Tier 5 is ten for ten the other way.

**The source verification corrections are folded in**, which v3.1 applied to its nineteen and this
applies to all thirty-seven. Pairs Mining became Correction Capture, Taste File Build became Taste File
and Primer, Skill Server Deploy became Agent Context Architecture, Exodus Workflow Install became
Production Stack and Briefing, and Agentic Email Install became The Voice Engine and **moved from
infrastructure into judgment capture**, which renumbers everything after it.

**Two gaps are on the site rather than hidden:** compute remediation, and the handover-and-gate phase.
Both are specified in the source and neither is built.

**Build.** Content is not hand-edited in the HTML. It lives in a Python model and is compiled in:

```
python3 build_v4.py
```

Keep `data_v4.py` (the 6 tiers and 37 units) and `build_v4.py` (the templates) together. Editing the
generated `v4/index.html` directly will be overwritten on the next build.

### v5, the Perry-only catalogue, typed

`v5/index.html` is a fourth cut. It sells the **32 engagements the Perry Belcher / Ignite material
yields on its own**, in the six tiers of
`Ignite Mastermind Material/00 - The Skill Parsing 2026-09-12.md`, with no Molly and no Mario units.
Same typed structure as v4: every engagement carries an AI-dependency label and the whole catalogue
filters by it.

| Route | Page |
|---|---|
| `#/` | Homepage |
| `#/tier/t0` ... `#/tier/t5` | The six tiers |
| `#/tier/<id>/<ai-centric\|ai-assisted\|not-ai>` | A tier, filtered by label |
| `#/unit/<slug>` | The 32 engagements |
| `#/types` | How much of this is AI |
| `#/types/<ai-centric\|ai-assisted\|not-ai>` | The catalogue, filtered |
| `#/limits` | Four refusals, two named gaps, who it was written for |
| `#/start` | Contact |

**The counts are the finding: 15 AI-centric, 10 AI-assisted, 7 with no model in them anywhere.**
Tier 0 contains no AI systems at all. Tiers 2 and 3 are thirteen for thirteen. Tier 5 is five for
six the other way, which is the point worth publishing: the commercial half of what everyone calls
the AI curriculum is classic direct response.

**Source.** 77 captured sessions, 926,842 words of transcript, 44 written lesson bodies, across
Springboard Office Hours, Ignite Tech Calls, Ignite Mastermind Replays and Traffic Tuesdays, 2026.
Per-session content index at
`Ignite Mastermind Material/AI Sessions 2026 Capture 2026-09-11/03 - Session Content Index 2026-09-12.md`.

**What is different from v4.** v4's limits page carried Mario-specific proof claims - a measured
ledger and a 212-case pricing register. **Neither exists in this corpus and both were removed rather
than reworded.** The Perry material has almost no measurement in it: one production-cost figure, one
output claim, one outreach response rate, all self-reported. The limits page says so.

**Build.**

```
python3 build_v5.py
```

Keep `data_v5.py` (the 6 tiers and 32 units) and `build_v5.py` (the templates) together. `build_v5.py`
reads its CSS from `v3/index.html`, same as `build_v4.py`. Editing the generated `v5/index.html`
directly will be overwritten on the next build.

### v6, the Molly + Perry merge, Mario excluded

`v6/index.html` is a fifth cut and the first merge. It resolves the **27 Molly (v2) and 32 Perry (v5)
engagements into 44**, in **seven tiers**, with no Mario units at all. Typed like v4 and v5. Built
2026-09-12 as a proposal and published the same day on Mark's pick.

| Route | Page |
|---|---|
| `#/` | Homepage |
| `#/tier/t0` ... `#/tier/t6` | The seven tiers |
| `#/tier/<id>/<ai-centric\|ai-assisted\|not-ai>` | A tier, filtered by label |
| `#/unit/<slug>` | The 44 engagements |
| `#/types` | How much of this is AI, plus where the catalogue came from |
| `#/types/<ai-centric\|ai-assisted\|not-ai>` | The catalogue, filtered |
| `#/limits` | Five refusals, three named gaps, what stands behind it |
| `#/start` | Contact |

**The counts: 17 AI-centric, 8 AI-assisted, 19 not about AI.** Tiers 5 and 6 are thirteen for
thirteen AI-centric; tiers 0, 2 and 4 contain no AI system. The seventh tier is Perry's working
relationship, which has no home in Molly's six and cannot be filed under AI systems without being
skipped.

**What is different from v5.** Every number on the page is computed from the cross-tab - readings,
footer, hero facts, shape cards. v5 shipped with v4's typed readings still in it. The site never
names either library; provenance (`src`, `src_id`, `absorbs`) lives in `data_v6.py` and is stripped
by the build. The limits page names what leaving Mario out costs: no claims standard, no measured
pricing.

**Dispositions and the fit analysis:** `../00 - The Two-Way Merge, Molly and Perry 2026-09-12.md`.

**Build.**

```
python3 build_v6.py
```

Keep `data_v6.py` (7 tiers, 44 units) and `build_v6.py` together. `build_v6.py` reads its CSS from
`v3/index.html` like v4 and v5, and adds one derived accent, `#E0672B`, for the seventh tier.

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
