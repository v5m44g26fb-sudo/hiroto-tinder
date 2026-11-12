import asyncio, json
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width":390,"height":844})
        errs=[]
        pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto("http://127.0.0.1:8931/index.html", wait_until="load")
        await pg.wait_for_timeout(2500)
        txt = await pg.content()
        print(json.dumps({
            "has_build_v711": "build v711" in txt,
            "has_caption": "膝が当たってた" in txt,
            "pageerrors": errs[:5],
        }, ensure_ascii=False))
        await b.close()

asyncio.run(main())
