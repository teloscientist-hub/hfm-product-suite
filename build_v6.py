# -*- coding: utf-8 -*-
# v6: the Molly (v2) + Perry (v5) two-way merge, Mario excluded. Seven tiers, typed by AI dependency.
# Every number on the page is computed from data_v6.py. No count is typed into copy.
import json, sys, io, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_v6 import TIERS, U, DROPPED

HERE = os.path.dirname(os.path.abspath(__file__))
V3 = os.path.join(HERE, "v3", "index.html")
OUT = os.path.join(HERE, "v6", "index.html")

src = io.open(V3, encoding="utf-8").read().split("\n")
# v3 CSS lives in lines 9..243 (1-indexed) across two <style> blocks
sty_i = src.index("<style>")
app_i = src.index('<div id="app"></div>')
css = "\n".join(src[sty_i:app_i-1])

EXTRA_CSS = """
<style>
/* ---------- v6 additions : AI dependency typing, seventh tier accent ---------- */
:root{--copper:#855013}
.tbadge{display:inline-flex;align-items:center;gap:6px;font-size:11px;letter-spacing:.1em;text-transform:uppercase;
  font-weight:600;padding:3px 9px;border-radius:999px;border:1px solid currentColor;white-space:nowrap;line-height:1.6}
.tbadge .dot{width:7px;height:7px;border-radius:50%;background:currentColor}
.t-C{color:#F9B93E}
.t-A{color:#B36F16}
.t-N{color:#8A857B}
:root[data-theme="dark"] .t-N{color:#A9A49A}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .t-N{color:#A9A49A}}
.filter{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:0 0 24px}
.filter a{font-size:12.5px;text-decoration:none;padding:6px 13px;border-radius:999px;border:1px solid var(--rule);
  color:var(--body);white-space:nowrap}
.filter a:hover{border-color:var(--ink);color:var(--ink)}
.filter a.on{background:var(--ink);border-color:var(--ink);color:var(--ground)}
.filter span.lbl{font-size:12px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:var(--body);margin-right:4px}
.xtab{width:100%;border-collapse:collapse;font-size:14.5px;min-width:520px}
.xtab th,.xtab td{padding:11px 12px;border-bottom:1px solid var(--rule);text-align:left;vertical-align:middle}
.xtab th{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink);font-weight:600}
.xtab td.num{font-variant-numeric:tabular-nums;font-weight:600;color:var(--ink);text-align:center;width:74px}
.xtab td.zero{color:var(--body);font-weight:400;opacity:.45}
.xtab tr.tot td{border-bottom:none;border-top:2px solid var(--rule);padding-top:14px}
.bar{display:flex;height:12px;border-radius:3px;overflow:hidden;min-width:120px;background:var(--rule)}
.bar i{display:block;height:100%}
.typecard{border:1px solid var(--rule);border-radius:5px;padding:26px 24px;background:var(--card);display:flex;flex-direction:column;gap:10px}
.typecard .big{font-size:40px;font-weight:700;line-height:1;color:var(--tc);font-variant-numeric:tabular-nums}
.typecard h3{font-size:19px}
.typecard p{font-size:14.5px;line-height:1.7}
.typecard .test{font-size:13px;border-top:1px solid var(--rule);padding-top:12px;margin-top:auto;color:var(--body)}
.scard .badges{display:flex;gap:7px;flex-wrap:wrap;margin-top:-2px}
.note{font-size:13.5px;line-height:1.75;border-left:2px solid var(--rule);padding-left:16px;color:var(--body)}
.gapbox{border:1px dashed var(--rule);border-radius:5px;padding:22px 24px;background:none}
.gapbox h4{font-size:16px;margin-bottom:7px}
.gapbox p{font-size:14.5px;line-height:1.7}
.gapbox .pillg{display:inline-block;font-size:11px;letter-spacing:.1em;text-transform:uppercase;font-weight:600;
  padding:3px 9px;border-radius:999px;border:1px solid var(--rule);color:var(--body);margin-bottom:10px}
.navlinks a{white-space:nowrap}
@media(max-width:980px){
  .topin{flex-wrap:wrap;gap:10px 18px;padding:12px 20px}
  .navlinks{margin-left:0;width:100%;gap:12px 16px;row-gap:8px}
  .navlinks a{font-size:13px}
  .mark{font-size:14px}
}
@media(max-width:540px){.shell{padding:0 20px}.countbar{gap:20px}}
html,body{overflow-x:hidden}
</style>
"""

TYPE_META = {
 "C": {"k":"C","slug":"ai-centric","name":"AI-centric","test":"Remove AI and the engagement disappears",
       "buy":"The AI system is the deliverable","hex":"#F9B93E",
       "who":"The buyer who arrived saying they need AI",
       "ages":"Fastest. Every one names a product or model that will be wrong within a year",
       "proof":"Weakest as evidence. Half of these come from taught material never run at a client of ours, and half were watched being run by a practitioner on a shared screen"},
 "A": {"k":"A","slug":"ai-assisted","name":"AI-assisted","test":"Remove AI and it shrinks but survives",
       "buy":"Real work, done faster and at more volume","hex":"#B36F16",
       "who":"The buyer with a production problem",
       "ages":"Slowly",
       "proof":"Middling. A scoring rubric that has been run, a production method that has been taught, and one self-reported production cost"},
 "N": {"k":"N","slug":"not-ai","name":"Not about AI","test":"Remove AI and nothing changes",
       "buy":"A decision, a standard or a structure","hex":"#8A857B",
       "who":"Nobody asks for it. It gets diagnosed",
       "ages":"Not at all",
       "proof":"Strongest in durability and weakest in numbers. Frameworks taught by one teacher each, and one self-reported outreach response rate on an unstated sample"},
}

# what each tier assumes is done, keyed by tier id. Absent means no gate is shown.
GATES = {
 "t2": "Tier 1's four company documents. An offer written from thin ground reads like every other offer in the category.",
 "t3": "Tier 1. Content built without the voice, the customer language and the differentiator comes out generic, and no amount of production fixes that.",
 "t5": "Tier 1's four documents, because they are what the model gets set up with. A working relationship built on no material is a chat window.",
 "t6": "Tier 4 and Tier 5 both. You cannot automate what nobody wrote down, and an agent built by somebody with no memory file, no guardrails and no preparation fails for reasons that have nothing to do with agents.",
}

ORDER = []
for t in TIERS:
    for slug, d in U.items():
        if d["t"] == t["id"]:
            ORDER.append(slug)
IDX = {s: i + 1 for i, s in enumerate(ORDER)}

for t in TIERS:
    t["units"] = [s for s in ORDER if U[s]["t"] == t["id"]]
    t["gate"] = GATES.get(t["id"])

# cross-tab
XT = []
for t in TIERS:
    row = {"id": t["id"], "name": t["name"], "n": t["n"], "hex": t["hex"], "short": t["short"]}
    for k in "CAN":
        row[k] = sum(1 for s in t["units"] if U[s]["type"] == k)
    row["tot"] = len(t["units"])
    row["molly"] = sum(1 for s in t["units"] if U[s]["src"] == "molly")
    row["perry"] = sum(1 for s in t["units"] if U[s]["src"] == "perry")
    XT.append(row)
TOT = {k: sum(r[k] for r in XT) for k in ("C", "A", "N", "tot", "molly", "perry")}
N_ABSORBED = sum(len(U[s].get("absorbs", [])) for s in ORDER)
PERRY_FOLDED = len({a.split(" ")[0] for s in ORDER for a in U[s].get("absorbs", [])})
SOURCE_UNITS = 27 + 32
assert TOT["tot"] == TOT["molly"] + TOT["perry"] == 44
assert TOT["molly"] + len(DROPPED) == 27 and TOT["perry"] + PERRY_FOLDED == 32

# the site never names the two libraries; the data does, for the merge document
for s in ORDER:
    U[s] = {k: v for k, v in U[s].items() if k not in ("src", "src_id", "absorbs")}

payload = {
  "TIERS": TIERS,
  "U": {s: dict(U[s], idx=IDX[s]) for s in ORDER},
  "ORDER": ORDER,
  "TYPES": TYPE_META,
  "XT": XT,
  "TOT": TOT,
  "MERGE": {"source_units": SOURCE_UNITS, "perry_folded": PERRY_FOLDED, "dropped": len(DROPPED), "two_libraries": 2},
}
DATA = "const D=" + json.dumps(payload, ensure_ascii=False) + ";"

SCRIPT = r"""
const {TIERS,U,ORDER,TYPES,XT,TOT,MERGE}=D;
const esc=s=>String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const md=s=>esc(s).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>');
const byId=id=>TIERS.find(t=>t.id===id);
const tierOf=u=>byId(U[u].t);
const pad=n=>String(n).padStart(2,'0');
const TK=['C','A','N'];
const bySlug=s=>TK.find(k=>TYPES[k].slug===s);
const list=a=>a.length<=1?a.join(''):a.slice(0,-1).join(', ')+' and '+a[a.length-1];

function badge(k){const m=TYPES[k];return `<span class="tbadge t-${k}" title="${esc(m.test)}"><i class="dot"></i>${esc(m.name)}</span>`;}

function nav(active){
  return `<header class="top"><div class="topin">
    <a class="mark" href="#/"><img class="logo" src="../assets/hfm-mark.png" srcset="../assets/hfm-mark@2x.png 2x" alt="">Human <span>First</span> Media</a>
    <nav class="navlinks">
      ${TIERS.map(t=>`<a href="#/tier/${t.id}" class="${active===t.id?'on':''}">${esc(t.short)}</a>`).join('')}
      <a href="#/types" class="${active==='types'?'on':''}">How much is AI</a>
      <a href="#/limits" class="${active==='limits'?'on':''}">Limits</a>
      <a href="#/start" class="btn ghost" style="padding:7px 15px;font-size:13.5px">Start</a>
      <button class="tglbtn" id="tgl">Theme</button>
    </nav></div></header>`;
}

function trail(cur){
  return `<div class="srail">${TIERS.map(t=>`<a href="#/tier/${t.id}" class="${t.id===cur?'on':''}">${esc(t.short)}</a>`).join('')}</div>`;
}

function filterbar(base,cur){
  const mk=(href,lab,on)=>`<a href="${href}" class="${on?'on':''}">${lab}</a>`;
  return `<div class="filter"><span class="lbl">How much is AI</span>
    ${mk(base,'All '+TOT.tot,!cur)}
    ${TK.map(k=>mk(base+'/'+TYPES[k].slug,esc(TYPES[k].name)+' '+TOT[k],cur===k)).join('')}
  </div>`;
}

function card(u){
  const d=U[u], t=tierOf(u);
  return `<a class="scard" href="#/unit/${u}" style="--accent:${t.c}">
    <div class="sn" style="color:${t.c}">${pad(d.idx)}</div>
    <h4>${esc(d.name)}</h4>
    <div class="badges">${badge(d.type)}</div>
    <p>${esc(d.promise)}</p>
    <div class="meta"><span>${esc(d.time)}</span><span>&middot;</span><span>${esc(d.who)}</span></div></a>`;
}

function foot(){
  const diag=byId('t0').units.length;
  return `<section class="dark tight"><div class="shell narrow stack">
    <h2 class="h-sec">Tell us the symptom, not the solution.</h2>
    <p class="lede" style="color:var(--deep-body)">If the first thing you need is not on this page we will say so. ${diag} of the ${TOT.tot} exist to hand you a reading rather than sell you a system.</p>
    <div class="btnrow"><a class="btn" href="#/start">Start with a diagnostic</a><a class="btn ghost" href="#/limits" style="color:#fff;border-color:#3A3631">What we do not do</a></div>
  </div></section>
  <footer style="padding:26px 0;border-top:1px solid var(--rule)"><div class="shell small" style="display:flex;gap:16px;flex-wrap:wrap;justify-content:space-between">
    <img class="flogo" src="../assets/hfm-logo.png" srcset="../assets/hfm-logo@2x.png 2x" alt="Human First Media"><span>${TOT.tot} engagements. ${TIERS.length} tiers. ${TOT.C} of them are AI systems.</span></div></footer>`;
}

function heroArt(){
  const w=380,x0=14,rowh=34,gap=9;
  const maxr=Math.max(...XT.map(r=>r.tot));
  let out=`<svg viewBox="0 0 400 ${XT.length*(rowh+gap)+30}" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="${TIERS.length} tiers, each split by how much of it is AI">`;
  XT.forEach((r,i)=>{
    const y=i*(rowh+gap)+14; let x=x0;
    const per=(w-x0*2-40)/maxr;
    const seg=(n,fill)=>{ if(!n) return ''; const ww=n*per; const s=`<rect x="${x}" y="${y}" width="${Math.max(ww,0)}" height="${rowh}" fill="${fill}"/>`; x+=ww+2; return s; };
    out+=seg(r.C,'#F9B93E')+seg(r.A,'#B36F16')+seg(r.N,'#8A857B');
    out+=`<text x="${x+8}" y="${y+rowh/2+5}" font-family="Poppins,sans-serif" font-size="13" font-weight="600" fill="${r.hex==='#3A3631'?'#5E5A52':r.hex}">${r.tot}</text>`;
  });
  out+=`</svg>`;
  return out;
}

function shapeCards(){
  const allC=XT.filter(r=>r.C===r.tot), noC=XT.filter(r=>r.C===0), mostN=XT.filter(r=>r.N>r.tot/2&&r.C===0);
  const allCn=allC.reduce((a,r)=>a+r.tot,0);
  const c1=`<div class="pt"><h4>${list(noC.map(r=>r.n))} contain no AI systems at all</h4><p>${noC.reduce((a,r)=>a+r.tot,0)} engagements across ${noC.length} tiers, and not one of them is an AI system. They are diagnosis, offers and operations: the work that decides whether any AI build is worth starting, and the work that does not age when the tooling changes.</p></div>`;
  const c2=`<div class="pt" style="border-color:var(--gold)"><h4>${list(allC.map(r=>r.n))} are ${allCn} for ${allCn}</h4><p>Every engagement in the last two tiers is an AI system. One of those tiers has no equivalent in most catalogues: the working relationship between one person and one model, which is the most-asked question in eighteen months of live sessions and the least written down.</p></div>`;
  const rev=XT.find(r=>r.id==='t2');
  const c3=`<div class="pt" style="border-color:var(--stone)"><h4>${esc(rev.n)} is ${rev.N} for ${rev.tot} the other way</h4><p>Offers, pricing, outreach, a launch and both sides of the retainer argument. None of it has a model in it, none of it carries a version number, and ${rev.perry} of the ${rev.tot} came out of what everybody calls an AI curriculum.</p></div>`;
  return c1+c2+c3;
}

function home(){
  const named=ORDER.filter(u=>/\bAI\b/.test(U[u].name)).length;
  return nav('') + `
  <div class="vbar">This is <b>v6</b>, a proposed merge built 2026-09-12 from the v2 and v5 catalogues. <a href="#/types">${MERGE.source_units} engagements across two libraries resolve to ${TOT.tot}</a>, in ${TIERS.length} tiers.</div>
  <section class="hero"><div class="shell"><div class="heroGrid">
    <div class="stack">
      <div class="rule"></div>
      <p class="eyebrow">${TOT.tot} engagements</p>
      <h1 class="h-hero">Find out what is true. Set the thing up properly. Then let it run.</h1>
      <p class="lede">${TIERS.length} tiers, in order. Diagnosis before foundation, foundation before offers and content, documentation before automation, and the working relationship with the model before any agent exists. Every engagement says which of three things it is: an AI system, work that AI makes faster, or business practice with no model in it anywhere.</p>
      <div class="btnrow"><a class="btn" href="#/tier/t0">Start with a diagnostic</a><a class="btn ghost" href="#/types">How much of this is AI</a></div>
      <div class="heroFacts">
        <div class="fact"><b>${TOT.C}</b><span>are AI systems. Take the model out and there is no engagement left</span></div>
        <div class="fact"><b>${TOT.A}</b><span>are real work that AI makes faster and cheaper</span></div>
        <div class="fact"><b>${TOT.N}</b><span>have no model in them anywhere and do not age</span></div>
      </div>
    </div>
    <div class="heroArt">${heroArt()}</div>
  </div></div></section>

  <section class="band"><div class="shell stack">
    <p class="eyebrow">The order</p>
    <h2 class="h-sec">${TIERS.length} tiers, and the sequence is the argument.</h2>
    <p class="lede narrow">Two libraries went into this catalogue and they were not two versions of the same thing. One teaches a company how to be bought: positioning, offers, content, operations, and the assistants and agents that run on top. The other teaches an operator how to set up with a model and run agents on it. Merged, one supplies the company and the other supplies the working relationship, and the tier order says which comes first.</p>
    <div class="chain" style="margin-top:12px">
      ${TIERS.map((t,i)=>`<div class="chainrow" style="--sc:${t.c}">
        <div class="sn2">${esc(t.n)}</div>
        <div><h3><a href="#/tier/${t.id}">${esc(t.name)}</a></h3>
        <p>${esc(t.promise)}</p>
        <div class="cnt2">${t.units.length} engagements &middot; ${XT[i].C} AI-centric, ${XT[i].A} AI-assisted, ${XT[i].N} not about AI</div></div></div>`).join('')}
    </div>
  </div></section>

  <section><div class="shell stack">
    <p class="eyebrow">What the shape says</p>
    <h2 class="h-sec">The AI is all at the end. Everything before it is what makes it work.</h2>
    <div class="deck" style="margin-top:10px">${shapeCards()}</div>
    <div class="gate" style="margin-top:34px"><b>One number worth knowing before you read further.</b> ${named} of these ${TOT.tot} engagements have the letters AI in their name. ${TOT.C} of them are AI systems, and ${TOT.N} have no model in them at any point. A title tells you the subject and the deliverable tells you the truth, which is why every page here carries a type badge.</div>
  </div></section>` + foot();
}

function tierPage(id,tk){
  const t=byId(id); if(!t) return home();
  const i=TIERS.indexOf(t), row=XT[i];
  let units=t.units; if(tk) units=units.filter(u=>U[u].type===tk);
  return nav(id) + `
  <section class="hero" style="padding-bottom:30px"><div class="shell stack">
    ${trail(id)}
    <div class="rule" style="background:${t.c}"></div>
    <p class="eyebrow" style="color:${t.c}">${esc(t.n)} &middot; ${t.units.length} engagement${t.units.length>1?'s':''} &middot; ${esc(t.tag)}</p>
    <h1 class="h-hero">${esc(t.name)}</h1>
    <p class="lede narrow">${esc(t.promise)}</p>
    <p class="narrow">${esc(t.lede)}</p>
    <div class="countbar">
      <div><b>${row.C}</b><span>AI-centric</span></div>
      <div><b>${row.A}</b><span>AI-assisted</span></div>
      <div><b>${row.N}</b><span>not about AI</span></div>
    </div>
    ${t.gate?`<div class="gate" style="margin-top:30px;border-left-color:${t.c}"><b>The gate.</b> This tier assumes ${esc(t.gate)} Where that is not done, we say so before the contract rather than discovering it in phase one.</div>`:''}
  </div></section>
  <section class="band"><div class="shell stack">
    <h2 class="h-sec">Why this tier exists</h2>
    <div class="deck" style="margin-top:10px">${t.why.map(w=>`<div class="pt" style="border-color:${t.c}"><h4>${esc(w.h)}</h4><p>${esc(w.p)}</p></div>`).join('')}</div>
    <p class="band-line" style="margin-top:30px"><b>How we work.</b> ${esc(t.how)}</p>
  </div></section>
  <section><div class="shell stack">
    <h2 class="h-sec">${t.units.length} way${t.units.length>1?'s':''} to work with us here</h2>
    ${filterbar('#/tier/'+t.id,tk)}
    ${units.length?`<div class="solgrid">${units.map(u=>card(u)).join('')}</div>`
      :`<p class="note">Nothing in this tier is ${esc(TYPES[tk].name.toLowerCase())}. That is the finding rather than an empty page. <a href="#/tier/${t.id}">Show all ${t.units.length}</a>.</p>`}
  </div></section>` + foot();
}

function unitPage(u){
  const d=U[u]; if(!d) return home();
  const t=tierOf(u), sibs=t.units.filter(x=>x!==u), m=TYPES[d.type];
  return nav(t.id) + `
  <section class="hero" style="padding-bottom:26px"><div class="shell narrow stack">
    <div class="crumb"><a href="#/">Home</a> <span class="sep">&rsaquo;</span> <a href="#/tier/${t.id}">${esc(t.name)}</a> <span class="sep">&rsaquo;</span> <span>${esc(d.name)}</span></div>
    <div class="rule" style="background:${t.c}"></div>
    <p class="eyebrow" style="color:${t.c}">Engagement ${pad(d.idx)} &middot; ${esc(d.time)} &middot; ${esc(d.who)}</p>
    <h1 class="h-hero">${esc(d.name)}</h1>
    <div class="badges" style="margin:2px 0 4px">${badge(d.type)}</div>
    <p class="lede">${esc(d.promise)}</p>
    <p class="note"><b>${esc(m.name)}.</b> ${esc(m.test)}. What you are buying is ${esc(m.buy.toLowerCase())}. <a href="#/types">Why we label these</a>.</p>
  </div></section>
  <section class="band"><div class="shell narrow stack">
    <h2 class="h-sub">The problem, as you would describe it.</h2><p>${esc(d.problem)}</p>
    <h2 class="h-sub" style="margin-top:30px">Why leaving it is more expensive than fixing it.</h2><p>${esc(d.cost)}</p>
    <h2 class="h-sub" style="margin-top:30px">The part that makes this worth outside help.</h2><p>${esc(d.hard)}</p>
  </div></section>
  <section><div class="shell narrow stack">
    <h2 class="h-sec">The kind of work this is.</h2>
    <div class="steps" style="grid-template-columns:1fr;gap:22px;margin-top:14px">
      ${d.work.map((w,i)=>`<div class="step" style="--stepc:${t.c}"><div class="n">${i+1}</div><p>${esc(w)}</p></div>`).join('')}
    </div>
  </div></section>
  <section class="band"><div class="shell narrow stack">
    <h2 class="h-sec">What you hold at the end</h2>
    <ul class="ticks" style="--accent:${t.c};margin-top:8px">${d.get.map(g=>`<li>${esc(g)}</li>`).join('')}</ul>
    <h2 class="h-sub" style="margin-top:34px">Why this one pays.</h2><p>${md(d.money)}</p>
    ${d.gate?`<div class="gate" style="margin-top:30px;border-left-color:${t.c}">${md(d.gate)}</div>`:''}
  </div></section>
  ${sibs.length?`<section><div class="shell stack">
    <h2 class="h-sub">What sits alongside it in ${esc(t.name.toLowerCase())}.</h2>
    <div class="solgrid" style="margin-top:12px">${sibs.map(x=>card(x)).join('')}</div>
  </div></section>`:''}` + foot();
}

function readings(){
  const allC=XT.filter(r=>r.C===r.tot), noC=XT.filter(r=>r.C===0);
  const most=XT.slice().sort((a,b)=>b.C-a.C)[0];
  const t2=XT.find(r=>r.id==='t2');
  return `<ul class="ticks">
    <li><b>${list(noC.map(r=>r.n))} contain no AI systems.</b> ${noC.reduce((a,r)=>a+r.tot,0)} engagements you can buy before deciding anything about AI, and the ones every AI tier assumes are done.</li>
    <li><b>${list(allC.map(r=>r.n))} are ${allC.reduce((a,r)=>a+r.tot,0)} for ${allC.reduce((a,r)=>a+r.tot,0)}.</b> The working relationship and the agent build are the only tiers where every engagement is a system, and ${most.n} holds the most of them at ${most.C}.</li>
    <li><b>${esc(t2.n)} is ${t2.N} of ${t2.tot} the other way.</b> Offers and pricing are indifferent to which model is current, and that is where the two libraries disagree with each other about retainers.</li>
  </ul>`;
}

function typesPage(tk){
  const lst = tk ? ORDER.filter(u=>U[u].type===tk) : ORDER;
  const maxr = Math.max(...XT.map(r=>r.tot));
  const nTiersWithC=XT.filter(r=>r.C>0).length;
  return nav('types') + `
  <section class="hero" style="padding-bottom:28px"><div class="shell narrow stack">
    <div class="rule"></div><p class="eyebrow">The honest label</p>
    <h1 class="h-hero">How much of this is actually AI.</h1>
    <p class="lede">Every engagement on this site carries one of three labels, decided by what you hold after we leave rather than by what the engagement is about. A title tells you the subject. The deliverable tells you the truth, and those are different facts.</p>
  </div></section>

  <section class="band"><div class="shell stack">
    <div class="deck">
      ${TK.map(k=>{const m=TYPES[k];return `<div class="typecard" style="--tc:${m.hex}">
        <div class="big">${TOT[k]}</div>
        <h3>${esc(m.name)}</h3>
        <p>${esc(m.buy)}.</p>
        <p style="font-size:13.5px"><b style="color:var(--ink)">Who asks for it.</b> ${esc(m.who)}. <b style="color:var(--ink)">Ages:</b> ${esc(m.ages).toLowerCase()}. <b style="color:var(--ink)">Proof we hold:</b> ${esc(m.proof.toLowerCase())}.</p>
        <div class="test"><b>The test.</b> ${esc(m.test)}.</div>
      </div>`}).join('')}
    </div>
    <p class="band-line" style="margin-top:30px"><b>Why publish this at all.</b> Because a service menu written during an AI boom describes almost everything in AI language, and a year later nobody can say which engagements survive the tooling being replaced. ${TOT.N} of these ${TOT.tot} would still be sellable if the models stopped improving tomorrow, and every one of the ${TOT.C} AI systems names a product that will be wrong within a year.</p>
  </div></section>

  <section><div class="shell stack">
    <p class="eyebrow">The cross-tab</p>
    <h2 class="h-sec">The AI is concentrated in ${nTiersWithC} of ${TIERS.length} tiers, and absent from the rest.</h2>
    <div class="tablewrap" style="margin-top:14px"><table class="xtab">
      <thead><tr><th>Tier</th><th style="text-align:center">AI-centric</th><th style="text-align:center">AI-assisted</th><th style="text-align:center">Not about AI</th><th>Shape</th></tr></thead>
      <tbody>
      ${XT.map(r=>`<tr>
        <td><a href="#/tier/${r.id}" style="text-decoration:none;color:var(--ink);font-weight:600">${esc(r.name)}</a><br><span style="font-size:12.5px">${esc(r.n)} &middot; ${r.tot} engagements</span></td>
        <td class="num ${r.C?'':'zero'}">${r.C}</td>
        <td class="num ${r.A?'':'zero'}">${r.A}</td>
        <td class="num ${r.N?'':'zero'}">${r.N}</td>
        <td><div class="bar" style="width:${Math.round(r.tot/maxr*100)}%">
          ${r.C?`<i style="background:#F9B93E;flex:${r.C}"></i>`:''}
          ${r.A?`<i style="background:#B36F16;flex:${r.A}"></i>`:''}
          ${r.N?`<i style="background:#8A857B;flex:${r.N}"></i>`:''}
        </div></td></tr>`).join('')}
      <tr class="tot"><td><b style="color:var(--ink)">All ${TIERS.length} tiers</b></td>
        <td class="num">${TOT.C}</td><td class="num">${TOT.A}</td><td class="num">${TOT.N}</td>
        <td><div class="bar"><i style="background:#F9B93E;flex:${TOT.C}"></i><i style="background:#B36F16;flex:${TOT.A}"></i><i style="background:#8A857B;flex:${TOT.N}"></i></div></td></tr>
      </tbody></table></div>
    <div class="two" style="margin-top:38px">
      <div class="stack">
        <h3 class="h-sub">Three readings of that table</h3>
        ${readings()}
      </div>
      <div class="stack">
        <h3 class="h-sub">And one about where it came from</h3>
        <p>This catalogue is a merge of two earlier ones. ${MERGE.source_units} engagements went in and ${TOT.tot} came out: ${MERGE.perry_folded} were the same engagement said twice, and were folded into the better version with the sharper half of the weaker one kept, and ${MERGE.dropped} were real work that we do not sell.</p>
        <p class="note" style="margin-top:14px">The two libraries disagree in one place and we kept the disagreement rather than averaging it. One sells a maintenance retainer because installed systems decay. The other argues against monthly billing and says to let the client ask. Both are on this menu, in ${esc(byId('t2').name)}, and which fits you is a question we will answer rather than dodge.</p>
      </div>
    </div>
  </div></section>

  <section class="band"><div class="shell stack">
    <p class="eyebrow">All ${TOT.tot}</p>
    <h2 class="h-sec">The whole catalogue, filtered by label.</h2>
    ${filterbar('#/types',tk)}
    <div class="solgrid">${lst.map(u=>card(u)).join('')}</div>
  </div></section>` + foot();
}

function limits(){
  return nav('limits') + `
  <section class="hero" style="padding-bottom:30px"><div class="shell narrow stack">
    <div class="rule"></div><p class="eyebrow">The boundary</p>
    <h1 class="h-hero">What this does not do.</h1>
    <p class="lede">Five things we will refuse, three gaps in this menu we would rather name than hide, and one honest note about what stands behind it. Published because you would find all of it anyway, and later.</p>
  </div></section>

  <section class="band"><div class="shell stack">
    <h2 class="h-sec">Five refusals, in writing</h2>
    <ul class="ticks" style="margin-top:10px">
      <li><b>We will not promise a citation position in an answer engine.</b> These systems are nondeterministic. The same query returns materially different answers hours apart, and the practitioners in our source material confirmed it live with no fix beyond averaging several runs. We sell the measurement and the compliance work. Anyone guaranteeing a placement is selling you a number nobody controls.</li>
      <li><b>We will not build an agent that publishes or transacts without a human in the path.</b> An unreviewed automated output is a system publishing on your behalf with no editor. Every agent gets one named human owner, never a team, and the review gate is built before the agent is.</li>
      <li><b>We will not build a knowledge base without vetting its sources first.</b> It is the combination clients most often want, and a retrieval system fed from whatever was to hand returns confident answers nobody can trace. Source vetting is the first step of the build, not a phase we can absorb.</li>
      <li><b>We will not build a routing table, a generation pipeline or an agent without its scheduled re-check.</b> Every AI-centric engagement here names a model that will be wrong within a year. The re-check is the reason the build is worth buying, and we decline the build without it.</li>
      <li><b>We will not automate a process nobody has written down or a task nobody has done by hand.</b> An agent built on an undocumented process encodes one person's habits, and a skill written before the task is understood encodes a guess, permanently. Do it manually first, then we automate what actually happened.</li>
    </ul>
  </div></section>

  <section><div class="shell stack">
    <h2 class="h-sec">Three gaps in this menu</h2>
    <p class="lede narrow">Named rather than hidden, because each is a hole a client would hit rather than read about.</p>
    <div class="deck" style="margin-top:20px">
      <div class="gapbox"><span class="pillg">Gap</span><h4>Nothing here checks the claims we make for you</h4><p>Neither library this menu is built from carries a claims standard. One has no unit on the subject. The other, asked directly by a paying attendee where the ethical line was, declined to draw one, and three techniques taught there as ordinary practice are not on this menu for that reason. We supply the standard ourselves, on every engagement that produces copy, and we have not yet written it up as something you can buy on its own.</p></div>
      <div class="gapbox"><span class="pillg">Gap</span><h4>Part of this assumes a platform that is somebody else's</h4><p>Several engagements in the agent build tier came out of a practice running on one white-labelled CRM, and part of their value is knowing where its buttons are. Nothing in that source treats the vendor's roadmap as a risk. We do: a skill whose value is platform familiarity expires when the vendor moves, and we will say which engagements those are before you buy one.</p></div>
      <div class="gapbox"><span class="pillg">Gap</span><h4>There is almost no measurement behind any of this</h4><p>One library is framework taught by one teacher each, with little measured. The other is eighteen months of a practitioner running things on a shared screen, with one production-cost figure, one output claim and one outreach response rate across the whole corpus, all self-reported. What both have is demonstration, which is real evidence of a different kind, and we will not dress it up as the first kind.</p></div>
    </div>
  </div></section>

  <section class="band"><div class="shell stack">
    <h2 class="h-sec">What stands behind this, and what does not</h2>
    <div class="two" style="margin-top:10px">
      <div class="stack">
        <p>Two libraries went into this catalogue. One teaches a company how to be bought and how to run: positioning, offers, content, operations, and the assistants, agents and knowledge base on top. The other is a live weekly practice about how one person sets up with a model and runs agents on it. They barely overlap, which is why merging them produced ${TIERS.length} tiers rather than six: the working relationship had no home in the first library and could not be filed under AI systems without being skipped.</p>
        <p>Where they did overlap, the same engagement said twice was folded into the better version, and the sharper half of the weaker one was kept inside it: a reporting technique inside the journey audit, a warm-up schedule inside the newsletter, a vetting precondition inside the knowledge base, a scope fence inside the agent roster.</p>
      </div>
      <div class="stack">
        <div class="nope"><h4>None of the ${TOT.tot} has been delivered to a client of ours</h4><p>Every engagement here is a specification of what could be sold, built from third-party teaching material read at a desk and from watching a practitioner work. The specifications are checked against their sources. What no check can tell you is whether the specifications are right, and the first client engagement is where that gets found out.</p></div>
        <div class="nope" style="margin-top:18px"><h4>The third library is not in this cut</h4><p>A third body of material exists with the strongest measurement of the three, including a worked pricing register and a measured creative ledger, and a whole tier on capturing one person's judgment as a runnable artifact. It was left out of this merge deliberately so the two included could be read against each other. What its absence costs is visible above: no claims standard, and pricing taught from method rather than from cases.</p></div>
      </div>
    </div>
  </div></section>` + foot();
}

function start(){
  const diag=byId('t0').units.length;
  return nav('start') + `
  <section class="hero"><div class="shell narrow stack">
    <div class="rule"></div><p class="eyebrow">Start</p>
    <h1 class="h-hero">Describe the symptom, not the solution.</h1>
    <p class="lede">The first engagement is almost always a diagnostic: a week, three days, or in one case an hour. It is paid, it credits against whatever follows, and it may well end with us telling you that the thing you asked about is not your binding constraint.</p>
    <h2 class="h-sub" style="margin-top:26px">Things people say that we can act on straight away</h2>
    <ul class="ticks" style="margin-top:6px">
      <li>We are using AI and the output all sounds the same.</li>
      <li>We are producing more than ever and the results are flat.</li>
      <li>We asked ChatGPT who the options are in our category and it did not name us.</li>
      <li>Everyone here has an AI subscription and nobody can say what any of them produce.</li>
      <li>Our agent setup worked for a month and then the model changed.</li>
      <li>Everything routes through one person and they are the constraint.</li>
      <li>Nobody can find anything we made more than a month ago.</li>
      <li>We cannot say which of our last twenty pieces performed.</li>
      <li>We keep solving the same problem for different clients and accumulating nothing.</li>
    </ul>
    <div class="btnrow" style="margin-top:30px"><a class="btn" href="mailto:support@humanfirstmedia.com?subject=Diagnostic">Email us</a><a class="btn ghost" href="#/tier/t0">See the ${diag} diagnostics</a></div>
  </div></section>` + foot();
}

function titleFor(h){
  const S='Human First Media';
  if(h.startsWith('/unit/')&&U[h.slice(6)]) return U[h.slice(6)].name+' | '+S;
  if(h.startsWith('/tier/')){const t=byId(h.slice(6).split('/')[0]); if(t) return t.name+' | '+S;}
  if(h.startsWith('/types')) return 'How much of this is AI | '+S;
  if(h==='/limits') return 'What we do not do | '+S;
  if(h==='/start') return 'Start | '+S;
  return S+' | Find out what is true, then build on it';
}

function render(){
  const h=location.hash.replace(/^#/,'')||'/';
  let out;
  if(h==='/'||h==='') out=home();
  else if(h.startsWith('/tier/')){const p=h.slice(6).split('/'); out=tierPage(p[0], p[1]?bySlug(p[1]):null);}
  else if(h.startsWith('/unit/')) out=unitPage(h.slice(6));
  else if(h.startsWith('/types')){const p=h.split('/'); out=typesPage(p[2]?bySlug(p[2]):null);}
  else if(h==='/limits') out=limits();
  else if(h==='/start') out=start();
  else out=home();
  document.getElementById('app').innerHTML=out;
  document.title=titleFor(h);
  window.scrollTo(0,0);
  const t=document.getElementById('tgl');
  if(t) t.onclick=()=>{
    const cur=document.documentElement.getAttribute('data-theme');
    const next = cur==='dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme',next);
    try{localStorage.setItem('hfm-theme',next)}catch(e){}
  };
}
try{const s=localStorage.getItem('hfm-theme'); if(s) document.documentElement.setAttribute('data-theme',s);}catch(e){}
addEventListener('hashchange',render);
render();
"""

HEAD = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet">
<meta name="googlebot" content="noindex, nofollow">
<link rel="icon" type="image/png" href="../assets/favicon.png">
<title>Human First Media | Find out what is true, then build on it</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;900&display=swap">
"""

html = HEAD + css + "\n" + EXTRA_CSS + "\n<div id=\"app\"></div>\n\n<script>\n" + DATA + "\n" + SCRIPT + "\n</script>\n"

os.makedirs(os.path.dirname(OUT), exist_ok=True)
io.open(OUT, "w", encoding="utf-8").write(html)
print("wrote", OUT, len(html), "bytes")
print("units", len(U), "tiers", len(TIERS), "totals", TOT, "perry folded", PERRY_FOLDED, "dropped", len(DROPPED))
for r in XT:
    print("  %s %-30s %2d  C%d A%d N%d  molly %d perry %d" % (r["id"], r["name"], r["tot"], r["C"], r["A"], r["N"], r["molly"], r["perry"]))
