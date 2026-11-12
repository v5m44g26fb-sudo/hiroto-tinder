import sys, json
sys.path.insert(0, "/home/hatch/.venv-tools/lib/python3.12/site-packages")
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b=pw.chromium.launch()
    pg=b.new_page(viewport={"width":402,"height":874},is_mobile=True,has_touch=True)
    errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)[:90]))
    pg.goto("http://localhost:8931/", wait_until="load"); pg.wait_for_timeout(2000)
    pg.evaluate("()=>{ const t=document.querySelector('#title-start'); if(t) t.click(); }"); pg.wait_for_timeout(400)
    pg.evaluate("()=>{ try{unlock();}catch(e){} }"); pg.wait_for_timeout(2500)
    pg.evaluate("()=>{ const c=document.querySelector('#chapter-card'); if(c) c.classList.remove('on'); }")
    def counts():
        return pg.evaluate("""()=>{ const hp=document.querySelectorAll('#v-ig .ig-post')[0];
          const vc=hp.querySelector('.v272-vc');
          return { cmts: hp.querySelectorAll('.cmt').length, news: hp.querySelectorAll('.cmt.v653-new').length,
                   label: vc? vc.textContent : '?' }; }""")
    print("before scandal:", json.dumps(counts(), ensure_ascii=False))
    pg.evaluate("()=>{ state.chapter=5; toScandal(); }")
    pg.wait_for_timeout(3000)
    print("scandal phase:", pg.evaluate("()=>state.phase"))
    pg.wait_for_timeout(25000)
    print("after wave1 (~28s):", json.dumps(counts(), ensure_ascii=False))
    nc=pg.evaluate("""()=>{ const n=document.querySelector('#nc-ov'); return n? n.textContent.replace(/\\s+/g,' ').slice(0,140) : 'no nc'; }""")
    print("NC:", nc)
    pg.wait_for_timeout(28000)
    print("after wave2 (~56s):", json.dumps(counts(), ensure_ascii=False))
    print("errors:", errs[:3])
    b.close()
