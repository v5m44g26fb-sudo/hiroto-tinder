src=open('index.html',encoding='utf-8').read()
def rep(old,new):
    global src
    assert src.count(old)==1, f"count {src.count(old)}: {old[:60]}"
    src=src.replace(old,new)
# sub-account couple-4 (cafe au lait post, 11/1): add close-distance line to caption only.
# Sub-account keeps only the 32 couple posts; no scar image, no protected text, no branch/flag change, description-zero line kept.
rep('<b>nao_ura</b> カフェオレ、やっぱりここのが一番</div><div class="v587-date">11月1日</div>','<b>nao_ura</b> カフェオレ、やっぱりここのが一番。向かいじゃなくて隣に座るから、膝が当たってた</div><div class="v587-date">11月1日</div>')
rep('build v710','build v711')
rep('<b>v710</b>','<b>v711</b>')
open('index.html','w',encoding='utf-8').write(src)
print("patched OK")
