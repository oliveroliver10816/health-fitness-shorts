#!/usr/bin/env python3
"""
Browser QA for the whole site: every page, every copy button, contrast, overflow,
console errors, and the links between pages.

    python3 -m http.server 8899 --directory docs &
    python3 qa.py

A copy button is only counted as passing if the text that actually lands on the
clipboard matches the text shown in its <pre> — clicking it is not the test.
"""
import re
import sys
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:8899"
PAGES = ["/", "/egg/", "/coffee/", "/water/", "/oats/", "/spinach/"]

CONTRAST_JS = r"""
() => {
  const srgb = c => { c/=255; return c<=0.03928 ? c/12.92 : Math.pow((c+0.055)/1.055,2.4); };
  const lum = ([r,g,b]) => 0.2126*srgb(r)+0.7152*srgb(g)+0.0722*srgb(b);
  const parse = s => { const m = s.match(/[\d.]+/g); return m ? m.slice(0,4).map(Number) : null; };
  // composite a colour with alpha over the already-composited backdrop
  const over = (fg, bg) => { const a = fg.length>3 ? fg[3] : 1;
    return [0,1,2].map(i => fg[i]*a + bg[i]*(1-a)); };
  const bgOf = el => {
    let cur = el, stack = [];
    while (cur) { const c = parse(getComputedStyle(cur).backgroundColor);
      if (c && (c.length<4 || c[3] > 0)) stack.push(c);
      if (c && (c.length<4 || c[3] === 1)) break;
      cur = cur.parentElement; }
    let base = [6,12,19];
    for (let i = stack.length-1; i >= 0; i--) base = over(stack[i], base);
    return base;
  };
  const out = [];
  for (const el of document.querySelectorAll('p,li,td,th,h1,h2,h3,h4,a,span,button,div,em,b,strong,pre,code')) {
    if (!el.textContent.trim() || el.children.length && !Array.from(el.childNodes).some(n=>n.nodeType===3 && n.textContent.trim())) continue;
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || el.closest('[hidden]')) continue;
    const r = el.getBoundingClientRect();
    if (!r.width || !r.height) continue;
    const fg = over(parse(cs.color), bgOf(el));
    const ratio = (Math.max(lum(fg), lum(bgOf(el))) + 0.05) / (Math.min(lum(fg), lum(bgOf(el))) + 0.05);
    const size = parseFloat(cs.fontSize), bold = parseInt(cs.fontWeight) >= 700;
    const large = size >= 24 || (size >= 18.66 && bold);
    const need = large ? 3.0 : 4.5;
    if (ratio < need) out.push({t: el.textContent.trim().slice(0,40), ratio: +ratio.toFixed(2), need, size});
  }
  return out;
}
"""


def main():
    fails, checked = [], {"buttons": 0, "contrast": 0, "pages": 0}
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        ctx = b.new_context(viewport={"width": 1600, "height": 1000},
                            permissions=["clipboard-read", "clipboard-write"])
        pg = ctx.new_page()
        errors = []
        pg.on("console", lambda m: errors.append(f"{m.type}: {m.text}") if m.type == "error" else None)
        pg.on("pageerror", lambda e: errors.append(f"pageerror: {e}"))

        for path in PAGES:
            errors.clear()
            pg.goto(BASE + path, wait_until="networkidle")
            checked["pages"] += 1

            # 1. every copy button: compare the clipboard to the <pre> it points at
            for btn in pg.query_selector_all(".cbtn"):
                tid = btn.get_attribute("data-target")
                want = pg.eval_on_selector(f"#{tid}", "el => el.textContent")
                btn.click()
                got = pg.evaluate("navigator.clipboard.readText()")
                checked["buttons"] += 1
                if got != want:
                    fails.append(f"{path} copy button -> #{tid}: clipboard does not match the block "
                                 f"({len(got)} chars vs {len(want)})")

            # 2. contrast
            bad = pg.evaluate(CONTRAST_JS)
            checked["contrast"] += 1
            for x in bad:
                fails.append(f"{path} contrast {x['ratio']} < {x['need']} on “{x['t']}”")

            # 3. horizontal overflow, desktop and phone
            for w, label in ((1600, "desktop"), (390, "phone")):
                pg.set_viewport_size({"width": w, "height": 900})
                over = pg.evaluate("() => document.documentElement.scrollWidth - document.documentElement.clientWidth")
                if over > 1:
                    fails.append(f"{path} horizontal overflow at {label}: {over}px")
            pg.set_viewport_size({"width": 1600, "height": 1000})

            # 4. console
            for e in errors:
                fails.append(f"{path} console {e}")

        # 5. the links out of the main page actually land on the right build page
        for slug, title in (("egg", "eat an egg"), ("coffee", "drink coffee"), ("water", "glass of water"),
                            ("oats", "eat oats"), ("spinach", "eat spinach")):
            pg.goto(BASE + "/", wait_until="domcontentloaded")
            pg.click(f'.tcard[href="{slug}/"]')
            pg.wait_for_load_state("domcontentloaded")
            h1 = pg.text_content("h1").replace("\n", " ")
            if slug not in pg.url or title.split()[-1] not in h1:
                fails.append(f"tile {slug} -> {pg.url} h1={h1!r}")
        b.close()

    print(f"pages {checked['pages']} · copy buttons verified {checked['buttons']} · contrast sweeps {checked['contrast']}")
    if fails:
        print(f"\nFAIL — {len(fails)}")
        for f in fails[:40]:
            print("  -", f)
        sys.exit(1)
    print("QA: PASS")


if __name__ == "__main__":
    main()
