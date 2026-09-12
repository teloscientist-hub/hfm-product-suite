# -*- coding: utf-8 -*-
import json, sys, io, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_v5 import TIERS, U

V3 = "/Users/mark/Library/CloudStorage/Dropbox-BPTNB/mark lewis/_GPT Meta/HFM - Human First Media/HFM Product Suite Website/v3/index.html"
OUT = "/Users/mark/Library/CloudStorage/Dropbox-BPTNB/mark lewis/_GPT Meta/HFM - Human First Media/HFM Product Suite Website/v5/index.html"

src = io.open(V3, encoding="utf-8").read().split("\n")
# v3 CSS lives in lines 9..243 (1-indexed) across two <style> blocks
css = "\n".join(src[8:243])

EXTRA_CSS = """
<style>
/* ---------- v5 additions : AI dependency typing ---------- */
.tbadge{display:inline-flex;align-items:center;gap:6px;font-size:11px;letter-spacing:.1em;text-transform:uppercase;
  font-weight:600;padding:3px 9px;border-radius:999px;border:1px solid currentColor;white-space:nowrap;line-height:1.6}
.tbadge .dot{width:7px;height:7px;border-radius:50%;background:currentColor}
.t-C{color:#EE2A52}
.t-A{color:#8F5ED8}
.t-N{color:#2F7F5B}
:root[data-theme="dark"] .t-N{color:#5FBF8F}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .t-N{color:#5FBF8F}}
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
.ladder{display:grid;grid-template-columns:1fr 1fr;gap:40px}
@media(max-width:820px){.ladder{grid-template-columns:1fr;gap:26px}}
.rung{display:flex;align-items:center;gap:12px;padding:10px 14px;border-radius:4px;margin-bottom:6px;font-size:14px}
.rung b{font-size:12px;letter-spacing:.1em;text-transform:uppercase;opacity:.75;min-width:26px}
.note{font-size:13.5px;line-height:1.75;border-left:2px solid var(--rule);padding-left:16px;color:var(--body)}
.gapbox{border:1px dashed var(--rule);border-radius:5px;padding:22px 24px;background:none}
.gapbox h4{font-size:16px;margin-bottom:7px}
.gapbox p{font-size:14.5px;line-height:1.7}
.gapbox .pillg{display:inline-block;font-size:11px;letter-spacing:.1em;text-transform:uppercase;font-weight:600;
  padding:3px 9px;border-radius:999px;border:1px solid var(--rule);color:var(--body);margin-bottom:10px}
@media(max-width:820px){
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
       "buy":"The AI system is the deliverable","hex":"#EE2A52",
       "who":"The buyer who arrived saying they need AI","ages":"Fastest. Every one names a product that will be wrong within a year","proof":"Weakest as evidence, strongest as method. Watched being run by a practitioner on a shared screen, never at a client of ours"},
 "A": {"k":"A","slug":"ai-assisted","name":"AI-assisted","test":"Remove AI and it shrinks but survives",
       "buy":"Real work, done faster and at more volume","hex":"#8F5ED8",
       "who":"The buyer with a production problem","ages":"Slowly","proof":"Middling. One measured production cost, one output claim, both self-reported by the presenter"},
 "N": {"k":"N","slug":"not-ai","name":"Not about AI","test":"Remove AI and nothing changes",
       "buy":"A decision, a standard or a structure","hex":"#2F7F5B",
       "who":"Nobody asks for it. It gets diagnosed","ages":"Not at all","proof":"Weakest in numbers and strongest in durability. One self-reported response rate on an unstated sample, and nothing else measured teacher"},
}

ORDER = []
for t in TIERS:
    for slug, d in U.items():
        if d["t"] == t["id"]:
            ORDER.append(slug)
IDX = {s: i + 1 for i, s in enumerate(ORDER)}

for t in TIERS:
    t["units"] = [s for s in ORDER if U[s]["t"] == t["id"]]

# cross-tab
XT = []
for t in TIERS:
    row = {"id": t["id"], "name": t["name"], "n": t["n"], "hex": t["hex"]}
    for k in "CAN":
        row[k] = sum(1 for s in t["units"] if U[s]["type"] == k)
    row["tot"] = len(t["units"])
    XT.append(row)
TOT = {k: sum(r[k] for r in XT) for k in "CAN"}
TOT["tot"] = sum(r["tot"] for r in XT)

payload = {
  "TIERS": TIERS,
  "U": {s: dict(U[s], idx=IDX[s]) for s in ORDER},
  "ORDER": ORDER,
  "TYPES": TYPE_META,
  "XT": XT,
  "TOT": TOT,
}
DATA = "const D=" + json.dumps(payload, ensure_ascii=False) + ";"

SCRIPT = r"""
const {TIERS,U,ORDER,TYPES,XT,TOT}=D;
const esc=s=>String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const md=s=>esc(s).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>');
const byId=id=>TIERS.find(t=>t.id===id);
const tierOf=u=>byId(U[u].t);
const pad=n=>String(n).padStart(2,'0');
const TK=['C','A','N'];
const bySlug=s=>TK.find(k=>TYPES[k].slug===s);

function badge(k){const m=TYPES[k];return `<span class="tbadge t-${k}" title="${esc(m.test)}"><i class="dot"></i>${esc(m.name)}</span>`;}

function nav(active){
  return `<header class="top"><div class="topin">
    <a class="mark" href="#/">HUMAN FIRST<span>.</span></a>
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
  return `<section class="dark tight"><div class="shell narrow stack">
    <h2 class="h-sec">Tell us the symptom, not the solution.</h2>
    <p class="lede" style="color:var(--deep-body)">If the first thing you need is not on this page we will say so. ${TIERS[0].units.length} of the ${TOT.tot} exist to hand you a reading rather than sell you a system.</p>
    <div class="btnrow"><a class="btn" href="#/start">Start with a diagnostic</a><a class="btn ghost" href="#/limits" style="color:#fff;border-color:#4A4F66">What we do not do</a></div>
  </div></section>
  <footer style="padding:26px 0;border-top:1px solid var(--rule)"><div class="shell small" style="display:flex;gap:16px;flex-wrap:wrap;justify-content:space-between">
    <span>Human First Media</span><span>${TOT.tot} engagements. ${TIERS.length} tiers. ${TOT.C} of them are AI systems.</span></div></footer>`;
}

function heroArt(){
  const w=380,x0=14,rowh=40,gap=10;
  let out=`<svg viewBox="0 0 400 ${XT.length*(rowh+gap)+34}" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Six tiers, each split by how much of it is AI">`;
  XT.forEach((r,i)=>{
    const y=i*(rowh+gap)+16; let x=x0;
    const unit=(w-x0*2)/TOT.tot*1.0;
    const seg=(n,fill)=>{ if(!n) return ''; const ww=n*((w-x0*2)/10); const s=`<rect x="${x}" y="${y}" width="${Math.max(ww,0)}" height="${rowh}" fill="${fill}"/>`; x+=ww+2; return s; };
    out+=seg(r.C,'#EE2A52')+seg(r.A,'#8F5ED8')+seg(r.N,'#2F7F5B');
    out+=`<text x="${x+8}" y="${y+rowh/2+5}" font-family="Poppins,sans-serif" font-size="13" font-weight="600" fill="${r.hex==='#222639'?'#70666A':r.hex}">${r.tot}</text>`;
  });
  out+=`</svg>`;
  return out;
}

function home(){
  return nav('') + `
  <div class="vbar">This is <b>v5</b>, built 2026-09-12 on the Perry Belcher / Ignite material alone, from 77 captured sessions and 926,842 words. <a href="#/types">Fifteen of thirty-two are actually about AI</a>.</div>
  <section class="hero"><div class="shell"><div class="heroGrid">
    <div class="stack">
      <div class="rule"></div>
      <p class="eyebrow">Thirty-two engagements</p>
      <h1 class="h-hero">Set the thing up properly, then let it run.</h1>
      <p class="lede">Six tiers, in order. Measurement before routing, the working relationship before the agents, and the agents before anything that has to run unattended. Every engagement says which of the three it is: an AI system, work that AI makes faster, or business practice with no model in it anywhere.</p>
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
    <h2 class="h-sec">Six tiers, and the sequence is the argument.</h2>
    <p class="lede narrow">Each tier assumes the one above it. Tier 2 exists because the source material shows the same thing over and over: people fail at agent work for reasons that have nothing to do with agents. No memory file, no guardrails, no preparation.</p>
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
    <h2 class="h-sec">The AI is all in the middle. Both ends are not.</h2>
    <div class="deck" style="margin-top:10px">
      <div class="pt"><h4>Tier 0 contains no AI systems at all</h4><p>All four diagnostics are work AI makes faster rather than work AI does. Two of them have no model anywhere in the deliverable. That is why the front of this menu is buyable before you have decided anything about AI.</p></div>
      <div class="pt" style="border-color:var(--red)"><h4>Tiers 2 and 3 are thirteen for thirteen</h4><p>Every engagement in the middle is an AI system. Tier 2 has no equivalent anywhere else in our catalogue: it is the working relationship between one person and one model, which is the most-asked question in eighteen months of live sessions and the least written down.</p></div>
      <div class="pt" style="border-color:var(--teal)"><h4>Tier 5 is five for six the other way</h4><p>Pricing, outreach, positioning and an argument against monthly billing. None of it has a model in it, none of it carries a version number, and it came out of what everybody calls the AI curriculum.</p></div>
    </div>
    <div class="gate" style="margin-top:34px"><b>One number worth knowing before you read further.</b> Three of these thirty-two engagements have the word AI in their name. Fifteen of them are AI systems, and seven have no model in them at any point. The source is eighteen months of live office hours rather than a course, so what survives is what somebody did on a shared screen rather than what they sold, and that is why every page here carries a type badge.</div>
  </div></section>` + foot();
}

function tierPage(id,tk){
  const t=byId(id); if(!t) return home();
  const i=TIERS.indexOf(t), prev=TIERS[i-1], row=XT[i];
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
    ${prev?`<div class="gate" style="margin-top:30px;border-left-color:${t.c}"><b>The gate.</b> This tier assumes ${esc(prev.name.toLowerCase())} is done. Where it is not, we say so before the contract rather than discovering it in phase one.</div>`:''}
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
    <h2 class="h-sub" style="margin-top:34px">Why this one pays.</h2><p>${esc(d.money)}</p>
    ${d.gate?`<div class="gate" style="margin-top:30px;border-left-color:${t.c}">${md(d.gate)}</div>`:''}
  </div></section>
  ${sibs.length?`<section><div class="shell stack">
    <h2 class="h-sub">What sits alongside it in ${esc(t.name.toLowerCase())}.</h2>
    <div class="solgrid" style="margin-top:12px">${sibs.map(x=>card(x)).join('')}</div>
  </div></section>`:''}` + foot();
}

function typesPage(tk){
  const list = tk ? ORDER.filter(u=>U[u].type===tk) : ORDER;
  const maxr = Math.max(...XT.map(r=>r.tot));
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
    <p class="band-line" style="margin-top:30px"><b>Why publish this at all.</b> Because a service menu written during an AI boom describes almost everything in AI language, and a year later nobody can say which engagements survive the tooling being replaced. Seven of these thirty-two would still be sellable if the models stopped improving tomorrow, and every one of the fifteen AI systems names a product that will be wrong within a year.</p>
  </div></section>

  <section><div class="shell stack">
    <p class="eyebrow">The cross-tab</p>
    <h2 class="h-sec">The AI is concentrated in two tiers, and absent from two others.</h2>
    <div class="tablewrap" style="margin-top:14px"><table class="xtab">
      <thead><tr><th>Tier</th><th style="text-align:center">AI-centric</th><th style="text-align:center">AI-assisted</th><th style="text-align:center">Not about AI</th><th>Shape</th></tr></thead>
      <tbody>
      ${XT.map(r=>`<tr>
        <td><a href="#/tier/${r.id}" style="text-decoration:none;color:var(--ink);font-weight:600">${esc(r.name)}</a><br><span style="font-size:12.5px">${esc(r.n)} &middot; ${r.tot} engagements</span></td>
        <td class="num ${r.C?'':'zero'}">${r.C}</td>
        <td class="num ${r.A?'':'zero'}">${r.A}</td>
        <td class="num ${r.N?'':'zero'}">${r.N}</td>
        <td><div class="bar" style="width:${Math.round(r.tot/maxr*100)}%">
          ${r.C?`<i style="background:#EE2A52;flex:${r.C}"></i>`:''}
          ${r.A?`<i style="background:#8F5ED8;flex:${r.A}"></i>`:''}
          ${r.N?`<i style="background:#2F7F5B;flex:${r.N}"></i>`:''}
        </div></td></tr>`).join('')}
      <tr class="tot"><td><b style="color:var(--ink)">All six tiers</b></td>
        <td class="num">${TOT.C}</td><td class="num">${TOT.A}</td><td class="num">${TOT.N}</td>
        <td><div class="bar"><i style="background:#EE2A52;flex:${TOT.C}"></i><i style="background:#8F5ED8;flex:${TOT.A}"></i><i style="background:#2F7F5B;flex:${TOT.N}"></i></div></td></tr>
      </tbody></table></div>
    <div class="two" style="margin-top:38px">
      <div class="stack">
        <h3 class="h-sub">Three readings of that table</h3>
        <ul class="ticks">
          <li><b>${XT[0].n} contains no AI systems.</b> All ${XT[0].tot} diagnostics are work AI makes faster or work with no model in it, which is why the front of this menu is buyable before you have decided anything about AI.</li>
          <li><b>Tiers 2 and 3 are ${XT[2].C+XT[3].C} for ${XT[2].tot+XT[3].tot}.</b> Every engagement in the middle is an AI system, and Tier 2 has no equivalent anywhere else in our catalogue.</li>
          <li><b>${XT[5].n} is ${XT[5].N} for ${XT[5].tot} the other way.</b> Pricing, outreach, positioning and the retainer argument. None of it carries a version number.</li>
        </ul>
      </div>
      <div class="stack">
        <h3 class="h-sub">And one about the ${TOT.N}</h3>
        <p>${XT[5].N} of the ${TOT.N} not-about-AI engagements are in Tier 5, and they sell to somebody running a practice rather than somebody running a marketing function. The other ${TOT.N-XT[5].N} are measurement and deliverability work any business can buy.</p>
        <p class="note" style="margin-top:14px">The number on the card is honest about the library. Read the tier before assuming the shelf is for you.</p>
      </div>
    </div>
  </div></section>

  <section class="band"><div class="shell stack">
    <p class="eyebrow">All ${TOT.tot}</p>
    <h2 class="h-sec">The whole catalogue, filtered by label.</h2>
    ${filterbar('#/types',tk)}
    <div class="solgrid">${list.map(u=>card(u)).join('')}</div>
  </div></section>` + foot();
}

function limits(){
  return nav('limits') + `
  <section class="hero" style="padding-bottom:30px"><div class="shell narrow stack">
    <div class="rule"></div><p class="eyebrow">The boundary</p>
    <h1 class="h-hero">What this does not do.</h1>
    <p class="lede">Four things we will refuse, two engagements this material specifies that we have not built, and one honest note about who this was written for. Published because you would find all of it anyway, and later.</p>
  </div></section>

  <section class="band"><div class="shell stack">
    <h2 class="h-sec">Four refusals, in writing</h2>
    <ul class="ticks" style="margin-top:10px">
      <li><b>We will not promise a citation position in an answer engine.</b> These systems are nondeterministic. The same query returns materially different answers hours apart, the practitioners in this material confirmed it live and had no fix beyond averaging several runs. We sell the compliance work and report the measurement. Anyone guaranteeing a placement is selling you a number nobody controls.</li>
      <li><b>We will not build a routing or agent system without its scheduled re-check.</b> Every AI-centric engagement here names a model that will be wrong within a year. The re-check is not an upsell, it is the reason the build is worth buying, and we decline the build without it.</li>
      <li><b>We will not build a knowledge base without vetting its sources first.</b> It is the combination clients most often want, and a retrieval system fed from whatever was to hand returns confident answers nobody can trace. Source vetting is Tier 1 and it is a precondition, not a phase we can absorb.</li>
      <li><b>We will not author a skill for work nobody has done by hand yet.</b> A skill written before the task is understood encodes a guess, permanently, and it is the most expensive kind of thing to discover six months later. Do it manually first, then we automate what actually happened.</li>
    </ul>
  </div></section>

  <section><div class="shell stack">
    <h2 class="h-sec">Two things the source specifies and we have not built</h2>
    <p class="lede narrow">Named rather than hidden, because both are holes a client would hit rather than read about.</p>
    <div class="deck" style="margin-top:20px">
      <div class="gapbox"><span class="pillg">Gap</span><h4>The platform underneath is somebody else's</h4><p>A large share of this material assumes one white-labelled CRM platform, and several engagements are substantially about knowing where its buttons are. Nothing in eighteen months of source treats that as a risk. We do: a skill whose value is platform familiarity expires when the vendor moves, and we will say which engagements those are before you buy one.</p></div>
      <div class="gapbox"><span class="pillg">Gap</span><h4>One tool is installed and never defined</h4><p>The source runs a session installing a product it never explains, mentioned seventy-two times across eight calls with no definition anywhere. We have left it off this menu rather than selling an engagement around something we cannot describe. If you already run it, say so and we will read the session before quoting.</p></div>
    </div>
  </div></section>

  <section class="band"><div class="shell stack">
    <h2 class="h-sec">Who this was written for, and who it was not</h2>
    <div class="two" style="margin-top:10px">
      <div class="stack">
        <p>This material came out of a live weekly practice rather than a course: eighteen months of office hours where members brought problems to a screen. That shows most in Tier 3, which is a practitioner's own running stack rather than a taught method, and in Tier 0, which is diagnosis because diagnosis is what the format produces.</p>
        <p>Tier 2 translates furthest, because the working relationship between one person and one model is the same problem in every business. Tier 5 translates everywhere and needs the least from us, since none of it involves a model.</p>
      </div>
      <div class="stack">
        <div class="nope"><h4>Asked where the ethical line is, the source declined to draw one</h4><p>A paying attendee asked directly whether a technique was ethical. The answer given was about perception rather than about the line: the person with the biggest mouth is the one people pay attention to. Three techniques taught there as ordinary practice are not on this menu, and their absence is deliberate. We supply the standard here rather than inheriting it.</p></div>
        <div class="nope" style="margin-top:18px"><h4>There is almost no measurement behind any of this</h4><p>Across 926,842 words there is one production-cost figure, one output claim and one outreach response rate, all self-reported by the people who benefit from them, and none independently verified. What the source has instead is demonstration: a practitioner running the thing on a shared screen every week for eighteen months. That is real evidence of a different kind and we will not dress it up as the first kind.</p></div>
      </div>
    </div>
  </div></section>` + foot();
}

function start(){
  return nav('start') + `
  <section class="hero"><div class="shell narrow stack">
    <div class="rule"></div><p class="eyebrow">Start</p>
    <h1 class="h-hero">Describe the symptom, not the solution.</h1>
    <p class="lede">The first engagement is almost always a diagnostic: two days, or in one case an hour. It is paid, it credits against whatever follows, and it may well end with us telling you that the thing you asked about is not your binding constraint.</p>
    <h2 class="h-sub" style="margin-top:26px">Things people say that we can act on straight away</h2>
    <ul class="ticks" style="margin-top:6px">
      <li>We are using AI and the output all sounds the same.</li>
      <li>We are producing more than ever and the results are flat.</li>
      <li>Nobody can find anything we made more than a month ago.</li>
      <li>Everything routes through one person and they are the constraint.</li>
      <li>We cannot say which of our last twenty pieces performed.</li>
      <li>Something went out that should not have, and we cannot say what would stop the next one.</li>
      <li>We keep solving the same problem for different clients and accumulating nothing.</li>
    </ul>
    <div class="btnrow" style="margin-top:30px"><a class="btn" href="mailto:support@humanfirstmedia.com?subject=Diagnostic">Email us</a><a class="btn ghost" href="#/tier/t0">See the four diagnostics</a></div>
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
<title>Human First Media | Find out what is true, then build on it</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;900&display=swap">
"""

html = HEAD + css + "\n" + EXTRA_CSS + "\n<div id=\"app\"></div>\n\n<script>\n" + DATA + "\n" + SCRIPT + "\n</script>\n"

os.makedirs(os.path.dirname(OUT), exist_ok=True)
io.open(OUT, "w", encoding="utf-8").write(html)
print("wrote", OUT, len(html), "bytes")
print("units", len(U), "tiers", len(TIERS), "totals", TOT)
