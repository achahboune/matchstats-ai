const $ = (s) => document.querySelector(s);
const esc = (v) => String(v ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
function fmtDate(value){try{return new Date(value).toLocaleString([], {weekday:"short",hour:"2-digit",minute:"2-digit"});}catch{return "Schedule TBC";}}
function score(m){const h=m.goals?.home,a=m.goals?.away;return h==null||a==null?"VS":`${h} : ${a}`;}
async function load(){
  $("#matches").innerHTML='<div class="loading">Refreshing match intelligence…</div>';
  try{
    const res=await fetch("/api/matches");if(!res.ok)throw new Error("Could not load fixtures");
    const payload=await res.json();$("#match-count").textContent=payload.count;
    $("#data-source").textContent=`DATA: ${payload.source.toUpperCase()}`;
    if(!payload.matches.length){$("#matches").innerHTML='<div class="empty">No live fixtures returned. Check again shortly.</div>';return;}
    const cards=await Promise.all(payload.matches.map(async m=>{
      let analysis={summary:"Analysis unavailable",probabilities:null};
      try{const r=await fetch(`/api/matches/${m.id}/analysis`);if(r.ok)analysis=(await r.json()).analysis;}catch{}
      const p=analysis.probabilities;
      return `<article class="match-card"><div class="card-head"><span>${esc(m.league)} · ${esc(m.country)}</span><span class="status">${esc(m.status_long||"Scheduled").toUpperCase()}</span></div><div class="teams"><div class="team">${esc(m.home?.name)}</div><div class="score">${esc(score(m))}</div><div class="team">${esc(m.away?.name)}</div></div><div class="venue">${m.elapsed?`${esc(m.elapsed)}' · `:""}${esc(m.venue||fmtDate(m.date))}</div><div class="analysis"><b>Match insight</b><br>${esc(analysis.summary)}</div>${p?`<div class="prob"><span>HOME ${p.home_win}%</span><span>DRAW ${p.draw}%</span><span>AWAY ${p.away_win}%</span></div>`:""}</article>`;
    }));
    $("#matches").innerHTML=cards.join("");
  }catch(e){$("#matches").innerHTML=`<div class="empty">${esc(e.message)}. Start the API server and retry.</div>`;$("#data-source").textContent="DATA: OFFLINE";}
}
$("#refresh").addEventListener("click",load);load();
