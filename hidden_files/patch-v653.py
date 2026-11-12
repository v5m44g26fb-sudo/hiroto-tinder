import io
s = io.open('index.html', encoding='utf-8').read()
assert "__v653" not in s

BLOCK = r"""
<script>
/* ===== v653: while the scandal burns, comments keep arriving on their IG posts ===== */
(function(){ if(window.__v653) return; window.__v653=true;
 var HER=[["mita_hito111","このカフェ、11月1日に二人でいたって本当？"],
          ["oshi_hako","推しを傷つけないで…"],
          ["shinpai_dayo","荒れてるけど、大丈夫…？無理しないでね"]];
 var HIS=[["hrt_suki","大翔、ちゃんと説明して"],
          ["m_support","本人の言葉だけ信じるって決めた"],
          ["hiro_fan88","楽しそうな写真だったのに…"]];
 function addCmt(post, pair, withTm){
  if(!post) return;
  var d=document.createElement("div"); d.className="cmt v653-new";
  var b=document.createElement("b"); b.textContent=pair[0]; d.appendChild(b);
  d.appendChild(document.createTextNode(pair[1]));
  if(withTm){ var tm=document.createElement("span"); tm.className="tm"; tm.textContent="たった今"; d.appendChild(tm); }
  post.appendChild(d);
 }
 function herPost(){ var ps=document.querySelectorAll("#v-ig .ig-post"); return ps&&ps[0]; }
 function hisPost(){ var ps=document.querySelectorAll("#v-hisig .ig-post"); return ps&&ps[0]; }
 function alive(){ return typeof state!=="undefined" && state.phase==="scandal" && !state.ended && !state.act2; }
 function notify(pair){
  if(typeof push==="function") push("Instagram","linear-gradient(45deg,#fa7e1e,#d62976,#962fbf)","\uD83D\uDCF7", pair[0]+" がコメントしました", "\u300C"+pair[1]+"\u300D");
 }
 function wave(i){
  if(!alive()) return;
  if(i===0){ addCmt(herPost(), HER[0], true); notify(HER[0]); }
  if(i===1){ addCmt(herPost(), HER[1], true); notify(HER[1]); }
  if(i===2){ addCmt(hisPost(), HIS[0], false); addCmt(hisPost(), HIS[1], false); }
  if(i===3){ addCmt(herPost(), HER[2], true); addCmt(hisPost(), HIS[2], false); notify(HER[2]); }
 }
 if(typeof startScandal==="function"){
  var _ss653=startScandal;
  startScandal=function(){ _ss653(); try{
   if(typeof state==="undefined"||state._igFlood653) return; state._igFlood653=true;
   [22000,50000,85000,120000].forEach(function(t,i){ later(function(){ wave(i); }, t); });
  }catch(e){} };
 }
})();
</script>
"""
i = s.find("</body>"); assert i > 0
io.open('index.html','w',encoding='utf-8').write(s[:i]+BLOCK+s[i:])
print("v653 block added")
