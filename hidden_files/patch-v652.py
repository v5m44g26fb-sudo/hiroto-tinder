import io
s = io.open('index.html', encoding='utf-8').read()
assert "__v652" not in s

STYLE = r"""
<style>
/* ===== v652: story players dressed like the real Instagram ===== */
#story-view,#nao-story-view{border-radius:16px;overflow:hidden}
#story-view .story-head{display:flex;align-items:center;gap:9px;padding:8px 14px 2px;color:#fff;font-size:13.5px;font-weight:600;order:2}
#story-view .story-head .avatar{border-radius:50%}
#story-view .story-head .sto-time{color:rgba(255,255,255,.75);font-weight:400;font-size:13px}
#story-view #story-img{order:3}
#story-view .story-replybar{order:4;padding:10px 14px 30px;gap:11px}
#story-view.txtonly #story-txt{top:50%;bottom:auto;transform:translateY(-50%);font-size:21px}
#story-view .sr-icobtn{background:none;border:none;padding:2px;cursor:pointer;display:inline-flex;align-items:center}
#story-view .story-replybar #sr-send{display:none}
#story-view .story-replybar.has-text #sr-send{display:block}
#story-view .story-replybar.has-text .sr-icobtn{display:none}
#hl-player,#hl-view,#subst-player{border-radius:16px;overflow:hidden}
#nao-story-view .story-head{display:flex;align-items:center;gap:9px;padding:8px 14px 2px;color:#fff;font-size:13.5px;font-weight:600}
#nao-story-view .story-head .sto-time{color:rgba(255,255,255,.75);font-weight:400;font-size:13px}
</style>
"""

SCRIPT = r"""
<script>
/* ===== v652: story chrome - header row, bottom reply bar with icons, centered text stories ===== */
(function(){ if(window.__v652) return; window.__v652=true;
 var VER='<svg width="13" height="13" viewBox="0 0 24 24" style="flex:none"><circle cx="12" cy="12" r="10" fill="#0095f6"/><path d="M8.5 12.4l2.3 2.3 4.7-4.9" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>';
 function dress(viewSel, timeTxt){
  var view=document.querySelector(viewSel); if(!view) return null;
  var head=null;
  view.querySelectorAll(":scope > div").forEach(function(d){
   if(!head && d.querySelector("img.avatar") && !d.id && !d.classList.contains("story-replybar") && !d.classList.contains("sbar")) head=d;
  });
  if(head && !head.classList.contains("story-head")){
   head.classList.add("story-head");
   if(!head.querySelector(".sto-time")){
    var nm=head.childNodes[head.childNodes.length-1];
    var sp=document.createElement("span"); sp.className="sto-time"; sp.textContent=timeTxt;
    var ver=document.createElement("span"); ver.innerHTML=VER; ver.style.display="inline-flex";
    head.appendChild(ver); head.appendChild(sp);
   }
  }
  return view;
 }
 var v=dress("#story-view","3\u6642\u9593");
 dress("#nao-story-view","2\u6642\u9593");
 if(v){
  var img=document.querySelector("#story-img");
  function syncTxt(){ try{ v.classList.toggle("txtonly", img && img.style.display==="none"); }catch(e){} }
  if(img){ new MutationObserver(syncTxt).observe(img,{attributes:true,attributeFilter:["style"]}); }
  syncTxt();
  var bar=v.querySelector(".story-replybar");
  if(bar && !bar.querySelector(".sr-icobtn")){
   var heart=document.createElement("button"); heart.className="sr-icobtn"; heart.setAttribute("aria-label","いいね");
   heart.innerHTML='<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>';
   var plane=document.createElement("button"); plane.className="sr-icobtn"; plane.setAttribute("aria-label","シェア");
   plane.innerHTML='<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linejoin="round"><path d="M22 2L11 13"/><path d="M22 2l-7 20-4-9-9-4 20-7z"/></svg>';
   bar.appendChild(heart); bar.appendChild(plane);
   var inp=bar.querySelector("#sr-text");
   if(inp) inp.addEventListener("input",function(){ bar.classList.toggle("has-text", !!inp.value.trim()); });
   heart.addEventListener("click",function(){
    try{
     var h=document.createElement("div"); h.className="bigheart"; h.textContent="\u2764\uFE0F";
     var ph=document.querySelector("#phone").getBoundingClientRect(); var r=v.getBoundingClientRect();
     h.style.left=(r.left-ph.left+r.width/2-42)+"px"; h.style.top=(r.top-ph.top+r.height/2-42)+"px";
     document.querySelector("#phone").appendChild(h); setTimeout(function(){ h.remove(); },950);
     if(typeof pop==="function") pop();
    }catch(e){}
   });
   plane.addEventListener("click",function(){ if(inp && inp.value.trim()){ var sd=bar.querySelector("#sr-send"); if(sd) sd.click(); } });
  }
 }
})();
</script>
"""
i = s.find("</body>"); assert i > 0
io.open('index.html','w',encoding='utf-8').write(s[:i] + STYLE + SCRIPT + s[i:])
print("v652 blocks added")
