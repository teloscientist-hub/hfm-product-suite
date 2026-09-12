# -*- coding: utf-8 -*-
import json, sys, io, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_v4 import TIERS, U

V3 = "/Users/mark/Library/CloudStorage/Dropbox-BPTNB/mark lewis/_GPT Meta/HFM - Human First Media/HFM Product Suite Website/v3/index.html"
OUT = "/Users/mark/Library/CloudStorage/Dropbox-BPTNB/mark lewis/_GPT Meta/HFM - Human First Media/HFM Product Suite Website/v4/index.html"

src = io.open(V3, encoding="utf-8").read().split("\n")
# v3 CSS lives in lines 9..243 (1-indexed) across two <style> blocks
css = "\n".join(src[8:243])

EXTRA_CSS = """
<style>
/* ---------- v4 additions : AI dependency typing ---------- */
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
       "who":"The buyer who arrived saying they need AI","ages":"Fastest","proof":"Weakest. Nothing here has been run at a client yet"},
 "A": {"k":"A","slug":"ai-assisted","name":"AI-assisted","test":"Remove AI and it shrinks but survives",
       "buy":"Real work, done faster and at more volume","hex":"#8F5ED8",
       "who":"The buyer with a production problem","ages":"Slowly","proof":"Strongest. A measured ledger, a 212-case pricing register"},
 "N": {"k":"N","slug":"not-ai","name":"Not about AI","test":"Remove AI and nothing changes",
       "buy":"A decision, a standard or a structure","hex":"#2F7F5B",
       "who":"Nobody asks. It gets diagnosed","ages":"Not at all","proof":"Middling, and mostly one teacher"},
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
    <p class="lede" style="color:var(--deep-body)">If the first thing you need is not on this page we will say so. Four of the thirty-seven exist to tell you that you are not ready for the other thirty-three.</p>
    <div class="btnrow"><a class="btn" href="#/start">Start with a diagnostic</a><a class="btn ghost" href="#/limits" style="color:#fff;border-color:#4A4F66">What we do not do</a></div>
  </div></section>
  <footer style="padding:26px 0;border-top:1px solid var(--rule)"><div class="shell small" style="display:flex;gap:16px;flex-wrap:wrap;justify-content:space-between">
    <span>Human First Media</span><span>Thirty-seven engagements. Six tiers. Twelve of them are actually about AI.</span></div></footer>`;
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
  <div class="vbar">This is <b>v4</b>, built 2026-09-11 on the Mario material alone, with the source verification corrections folded in. <a href="#/types">Twelve of thirty-seven are actually about AI</a>.</div>
  <section class="hero"><div class="shell"><div class="heroGrid">
    <div class="stack">
      <div class="rule"></div>
      <p class="eyebrow">Thirty-seven engagements</p>
      <h1 class="h-hero">Find out what is true, then build on it.</h1>
      <p class="lede">Six tiers, in order. Measurement before systems, judgment before volume, and a written decision about what you will claim before any of it reaches a customer. Every engagement says which of the three it is: an AI system, work that AI makes faster, or business practice with no model in it anywhere.</p>
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
    <p class="lede narrow">Each tier assumes the one above it. Where it is not there we say so before the contract, not in week two, and Tier 1 exists because five of the engagements below it decline the same client for the same reason.</p>
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
    <h2 class="h-sec">The AI sits in the middle, not at the top.</h2>
    <div class="deck" style="margin-top:10px">
      <div class="pt"><h4>Tier 1 gates everything and contains no AI</h4><p>The precondition for buying an AI system is five pieces of measurement and architecture work with no model in any deliverable. That is why the front of this menu is buyable before you have decided anything about AI.</p></div>
      <div class="pt" style="border-color:var(--red)"><h4>Tier 2 is five for five</h4><p>Judgment capture is the only tier where every engagement is an AI system, and it is the only thing here with no competitor equivalent. It is also where a rules-only approach stops working and almost nobody says so.</p></div>
      <div class="pt" style="border-color:var(--teal)"><h4>Tier 5 is ten for ten the other way</h4><p>The top of the ladder has no model in it anywhere. Contracts, referrals, pricing and how a firm funds its own research. The outreach template in it dates to 2013 and still runs.</p></div>
    </div>
    <div class="gate" style="margin-top:34px"><b>One number worth knowing before you read further.</b> Exactly one of these thirty-seven engagements has the word AI in its name. Twelve of them are AI systems. This material was written by people describing their work rather than marketing it, which is the opposite of the usual drift and is why every page here carries a type badge.</div>
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
    <p class="band-line" style="margin-top:30px"><b>Why publish this at all.</b> Because a service menu written during an AI boom describes almost everything in AI language, and a year later nobody can say which engagements survive the tooling being replaced. Fifteen of these thirty-seven would still be sellable if the models stopped improving tomorrow.</p>
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
          <li><b>Tier 1 is the gate for every AI tier and contains no AI.</b> Five pieces of measurement and estate work, no model in any deliverable. It is the part of this menu you can buy before deciding anything about AI.</li>
          <li><b>Tier 2 is five for five and it is the only tier that is.</b> Judgment capture is the purest AI product here and the one with no competitor equivalent.</li>
          <li><b>Tier 5 is ten for ten in the other direction.</b> The top of the ladder is indifferent to which model is current.</li>
        </ul>
      </div>
      <div class="stack">
        <h3 class="h-sub">And one about the fifteen</h3>
        <p>Ten of the fifteen not-about-AI engagements are in Tier 5, and eight of those describe how a professional services firm runs itself rather than something a client buys. We adopted those before putting them on this page.</p>
        <p class="note" style="margin-top:14px">So the not-about-AI work you can actually buy from us is seven engagements, not fifteen. The number on the card is honest about the library and would be misleading about the shelf, which is why it is said here.</p>
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
      <li><b>We will not remediate a ceiling that is not binding.</b> The Ceiling Read names one of three and declines the other two in writing, even where you would pay for all three. The refusal is the only part of an audit worth anything.</li>
      <li><b>We will not bundle the claims work into something larger.</b> Bundled, it is the phase that gets cut. It is sold standing or not at all.</li>
      <li><b>We will not build a judgment pipeline for a client who cannot say which of their last twenty pieces performed.</b> We fix measurement first or we do not start, and that is Tier 1 rather than a favour absorbed into phase one.</li>
      <li><b>We will not sell Tier 2 into an organisation with nobody competent to run the judge.</b> Every process here assumes an operator with judgement. The loops compound only if somebody can tell a good output from a bad one.</li>
    </ul>
  </div></section>

  <section><div class="shell stack">
    <h2 class="h-sec">Two things the source specifies and we have not built</h2>
    <p class="lede narrow">Named rather than hidden, because both are holes a client would hit rather than read about.</p>
    <div class="deck" style="margin-top:20px">
      <div class="gapbox"><span class="pillg">Gap</span><h4>Compute remediation</h4><p>The Ceiling Read measures three ceilings and we can remediate two. If your binding constraint turns out to be compute, you get the finding and an honest referral rather than an engagement. The source specifies the track, including what it calls the best cost idea in the material. We have not built it.</p></div>
      <div class="gapbox"><span class="pillg">Gap</span><h4>Handover and gate</h4><p>The judgment tier is specified with a fifth phase we do not currently sell: teaching the gate and the defect names to the people who ship, and naming a reviewer per task. Without it the pipeline has no owner after we leave, which is the failure the correction loop exists to prevent.</p></div>
    </div>
  </div></section>

  <section class="band"><div class="shell stack">
    <h2 class="h-sec">Who this was written for, and who it was not</h2>
    <div class="two" style="margin-top:10px">
      <div class="stack">
        <p>This material came out of a direct-response operation running very large paid-media volume. That shows most in Tier 3, which assumes an ad account, a feedback loop and enough spend that a hit rate means something. If you do not have those, six of those seven engagements are the wrong purchase and we would rather say so here.</p>
        <p>Tiers 0, 1, 2 and the enforcement half of Tier 4 translate to a much wider range of businesses, because measurement, judgment and a claims boundary are not media problems.</p>
      </div>
      <div class="stack">
        <div class="nope"><h4>The source has no compliance layer, by design</h4><p>Two separate calls in the original material state that its own systems carry no compliance filter at all, and that it is treated as the operator's responsibility. Our position is the opposite. It also means the method we adapted has never been run under the constraint we are adding, and you should know that before you hear it from somebody else.</p></div>
        <div class="nope" style="margin-top:18px"><h4>The proof is uneven and we will tell you where</h4><p>The AI-centric engagements have the weakest evidence: specified, not yet run at a client. The AI-assisted ones have the strongest, including a measured ledger and a 212-case pricing register. Ask which one you are buying.</p></div>
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
