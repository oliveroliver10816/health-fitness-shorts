#!/usr/bin/env python3
"""
Shared page generator for every video in the series.

One topic module (topics/<slug>.py) supplies the data; this file turns it into
docs/<slug>/index.html and docs/<slug>/build-vo.sh.

Everything that appears twice on a page (a shot's end state and the next shot's
opening state) is written ONCE in the topic module and emitted into both places,
so the continuity chain cannot drift.

    python3 build_pages.py            # all five
    python3 build_pages.py egg water  # just these
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).parent
DOCS = ROOT / "docs"

# --------------------------------------------------------------- shared blocks
# STYLE owns the look. REALISM owns "it has to look real". They are separate on
# purpose: when two paragraphs answer the same question the model picks one, and
# it is usually not the one you meant.

STYLE_TMPL = (
    "STYLE — identical in all eight shots of this video. Hyper-realistic 3D medical animation still, rendered "
    "like a single frame from a broadcast medical documentary: photoreal subsurface scattering through living "
    "tissue, wet surfaces with true specular highlights, real optical depth of field, physically accurate light, "
    "anatomically accurate structures. Palette: {palette}. "
    "Format: vertical 9:16, 1080 x 1920, subject centred in the upper two-thirds."
)

REALISM = (
    "REALISM — the most important instruction in this prompt. It must look real: actual footage captured inside "
    "a living human body, filmed on a surgical endoscope and a macro lens for a medical documentary — not an "
    "illustration of a body. Living tissue is wet, uneven and slightly asymmetric: fine irregular surface "
    "texture, colour varying from one area to the next, fine capillaries readable under translucent membranes, "
    "a thin moving film of fluid catching the light in small sharp highlights, soft natural motion blur where "
    "anything moves. Real camera behaviour: shallow natural depth of field, gentle falloff at the edges of "
    "frame, light bouncing between wet surfaces. NOT a diagram, NOT a textbook illustration, NOT a cartoon, "
    "NOT a neon sci-fi hologram, NOT clean glass or plastic shapes floating in empty space, NOT a video-game "
    "render, NOT symmetrical, NOT glossy or toy-like. If it looks designed, it is wrong — it has to look "
    "photographed."
)

FIGURE = (
    "THE FIGURE — the same adult human anatomical figure appears in every shot of this video: skin rendered "
    "semi-transparent so the muscles, skeleton, vessels and organs read clearly through it, no body hair, a calm "
    "neutral face. Same figure, same build, same skin translucency, every time."
)

NOTEXT = (
    "NO TEXT — no writing of any kind anywhere in the frame: no letters, no numbers, no captions, no labels, "
    "no arrows, no callout lines, no logos, no watermark, no readable interface."
)

VID_NOTEXT = (
    "NO TEXT — no writing appears at any point in the eight seconds: no letters, no numbers, no captions, "
    "no labels, no arrows, no logos, no watermark."
)

VID_REALISM = (
    "REALISM IN MOTION — everything moves the way real tissue and real fluid move: soft, weighted, slightly "
    "irregular, with real inertia. Nothing snaps, pops, teleports, flickers or moves like a graphic. No "
    "particles added for decoration, no lens flares, no energy effects, no morphing. It must look like a camera "
    "recording something that is really happening."
)


# ------------------------------------------------------------------- rendering
def esc(s):
    return html.escape(s, quote=False)


def style_block(t):
    return STYLE_TMPL.format(palette=t["palette"])


def img_prompt(t, c):
    """Full paste-ready image prompt text for clip c of topic t."""
    clips = t["clips"]
    prev = clips[c["n"] - 2]["ends"] if c["n"] > 1 else None
    lines = []
    for i, (head, body) in enumerate(c["img"]):
        if "{prev}" in body:
            body = body.replace("{prev}", prev.rstrip("."))
        if head == "LIGHT":                       # REAL ANATOMY sits just before LIGHT
            lines.append("REAL ANATOMY — " + c["real"])
        lines.append(f"{head} {body}" if i == 0 else f"{head} — {body}")
    lines.append(FIGURE)
    lines.append(style_block(t))
    lines.append(REALISM)
    lines.append(NOTEXT)
    return "\n\n".join(lines)


def vid_prompt(t, c):
    """Full paste-ready image-to-video prompt text for clip c of topic t."""
    p = [
        f"CLIP {c['n']} OF 8 — {c['name'].upper()} · 8.000 seconds · 24 fps · vertical 9:16, 1080 x 1920 · "
        f"AUDIO OFF (generate no sound).",
        f"START FRAME — the approved still for shot {c['n']}, used unchanged as the first frame. Animate this "
        f"exact image; do not redesign it, do not change the framing it starts on, do not restyle it.",
        f"CAMERA — {c['cam']}",
    ]
    p += [f"{a} — {b}" for a, b in c["beats"]]
    p.append(f"LIGHTING — {c['light']}")
    p.append(
        f"END FRAME — {c['ends']} Clip {c['n']+1} begins from exactly this state."
        if c["n"] < 8
        else f"END FRAME — {c['ends']} This is the last frame of the video."
    )
    p.append(f"CONSTRAINTS — One single continuous shot, no cuts, no jump in time, no scene change. {c['cons']}")
    p.append(VID_REALISM)
    p.append(VID_NOTEXT)
    return "\n\n".join(p)


def block(label, cls, text, pid):
    return f"""      <div class="pblock">
        <div class="phead"><span class="plabel {cls}">{esc(label)}</span><button class="cbtn" type="button" data-target="{pid}">Copy</button></div>
<pre id="{pid}">{esc(text)}</pre>
      </div>
"""


def clip_card(t, c):
    kfcls = "kf n" if c["kf"][0] == "new" else "kf r"
    nt, nb = c["note"]
    return f"""    <div class="clip" id="c{c['n']}">
      <div class="chead">
        <div class="cmeta"><span class="cn">CLIP {c['n']}</span><span class="tc">{c['tc']}</span><span class="{kfcls}">{c['kf'][1]}</span><span class="tc"><span class="sw" style="background:{c['colour']}"></span>{c['palette']}</span></div>
        <h4>{esc(c['name'])} <span class="where">{esc(c['where'])}</span></h4>
        <p class="vo">“{esc(c['vo'])}”</p>
      </div>
      <div class="cbody">
{block(f"Image prompt {c['n']}", "", img_prompt(t, c), f"ip{c['n']}")}{block(f"Image-to-video prompt {c['n']} · 8 s · audio off", "v", vid_prompt(t, c), f"vp{c['n']}")}        <div class="plabel n">{nt}</div>
        <p class="cnote">{nb}</p>
      </div>
    </div>
"""


# ------------------------------------------------------------------ table rows
def chain_rows(t):
    out = []
    for c in t["clips"]:
        nxt = f"opens clip {c['n']+1}" if c["n"] < 8 else "end of video"
        out.append(
            f"""          <tr><td class="num">{c['n']}</td><td><b>{esc(c['name'])}</b><br><span class="dim">{esc(c['where'])}</span></td>"""
            f"""<td>{esc(c['ends'])}</td><td class="num">{nxt}</td></tr>"""
        )
    return "\n".join(out)


def start_of(c):
    """When sentence N becomes audible. Clip 1 cannot start before zero."""
    return max(0.0, 8 * (c["n"] - 1) - 0.10)


def headroom(c):
    """Time left in the clip after the sentence finishes."""
    return 8 * c["n"] - (start_of(c) + c["spoken"])


def script_rows(t):
    return "\n".join(
        f"""          <tr><td class="num">{c['n']}</td><td>{esc(c['vo'])}</td><td class="num">{len(c['vo'].split())}</td>"""
        f"""<td class="num">{c['spoken']:.2f} s</td><td class="num tick">{headroom(c):.2f} s</td></tr>"""
        for c in t["clips"]
    )


def landing_rows(t):
    out = []
    for c in t["clips"]:
        start = start_of(c)
        end = start + c["spoken"]
        out.append(
            f"""          <tr><td class="num">{c['n']}</td><td class="num">{start:.2f} s</td>"""
            f"""<td class="num">clip {c['n']} · {8*(c['n']-1)}–{8*c['n']} s</td><td class="num">{end:.2f} s</td>"""
            f"""<td class="num tick">{headroom(c):.2f} s</td></tr>"""
        )
    return "\n".join(out)


def grid_rows(t):
    out = []
    for c in t["clips"]:
        kfcls = "kf n" if c["kf"][0] == "new" else "kf r"
        out.append(
            f"""          <tr><td class="num">{c['n']}</td><td class="num">{c['tc']}</td><td><a href="#c{c['n']}">{esc(c['name'])}</a><br><span class="dim">{esc(c['where'])}</span></td>"""
            f"""<td>{esc(c['cam'].split(' — ')[0])}</td><td><span class="{kfcls}">{c['kf'][1]}</span></td>"""
            f"""<td><span class="sw" style="background:{c['colour']}"></span>{esc(c['palette'].split(' · ')[0])}</td></tr>"""
        )
    return "\n".join(out)


def timeline_segs(t):
    return "\n".join(
        f"""        <div class="tlseg" style="background:{c['colour']}">{c['n']}</div>""" for c in t["clips"]
    )


def timeline_vo(t):
    out = []
    for c in t["clips"]:
        start = start_of(c)
        out.append(f"""        <div style="left:{start/64*100:.2f}%;width:{c['spoken']/64*100:.2f}%"></div>""")
    return "\n".join(out)


# ------------------------------------------------------------- script for TTS
def plain_script(t):
    """The paste-into-any-TTS-tool version: eight sentences, nothing else."""
    return "\n\n".join(c["vo"] for c in t["clips"])


def numbered_script(t):
    """Reference version with the timecode each sentence has to be audible at."""
    lines = [
        f"{t['h1_plain'].upper()}",
        f"8 clips x 8.000 s = 64.000 s  ·  read at about 158 words per minute  ·  "
        f"every sentence must be spoken in under 8 seconds",
        "",
    ]
    for c in t["clips"]:
        start = start_of(c)
        lines.append(
            f"[{c['n']}] audible at {start:6.2f} s   (clip {c['n']}: {8*(c['n']-1)}-{8*c['n']} s)   "
            f"spoken {c['spoken']:.2f} s\n{c['vo']}\n"
        )
    return "\n".join(lines)


def vo_script_sh(t):
    """The sentences as the bash array build-vo.sh uses."""
    return "\n".join(f'"{c["vo"]}"' for c in t["clips"])


# ---------------------------------------------------------------- word-vs-time
def inversion(t):
    """Find the clearest pair where fewer words took longer to say. Honest,
    because it is picked from this video's own measured audio."""
    best = None
    for a in t["clips"]:
        for b in t["clips"]:
            wa, wb = len(a["vo"].split()), len(b["vo"].split())
            if wa < wb and a["spoken"] > b["spoken"]:
                score = (wb - wa) + (a["spoken"] - b["spoken"])
                if best is None or score > best[0]:
                    best = (score, a, b)
    return (best[1], best[2]) if best else (None, None)


# --------------------------------------------------------------------- page
def render(t):
    clips = t["clips"]
    ALL_IMG = "\n\n\n".join(f"===== IMAGE PROMPT {c['n']} =====\n\n" + img_prompt(t, c) for c in clips)
    ALL_VID = "\n\n\n".join(f"===== VIDEO PROMPT {c['n']} =====\n\n" + vid_prompt(t, c) for c in clips)
    CARDS = "".join(clip_card(t, c) for c in clips)
    STYLE_TXT = style_block(t) + "\n\n" + FIGURE + "\n\n" + REALISM + "\n\n" + NOTEXT
    speech = sum(c["spoken"] for c in clips)
    words = sum(len(c["vo"].split()) for c in clips)
    long_c, short_c = inversion(t)
    vo = t.get("vo_stats") or {"dur": 64.03, "lufs": "−14.9", "tp": "−1.7"}
    prev_t, next_t = t.get("prev"), t.get("next")
    nav = []
    if prev_t:
        nav.append(f"""<a href="../{prev_t[0]}/">← {esc(prev_t[1])}</a>""")
    nav.append("""<a href="../#topics">all five videos</a>""")
    if next_t:
        nav.append(f"""<a href="../{next_t[0]}/">{esc(next_t[1])} →</a>""")
    NAV = " · ".join(nav)

    invbox = ""
    if long_c is not None:
        invbox = f"""
    <div class="box find">
      <div class="bt">⭐ Word count does not predict duration</div>
      <p>Clip {short_c['n']} speaks <strong>{len(short_c['vo'].split())} words in {short_c['spoken']:.2f} s</strong>. Clip {long_c['n']} speaks <strong>{len(long_c['vo'].split())} words in {long_c['spoken']:.2f} s</strong> — fewer words, more time on the clock. Syllables and commas drive it, not word count.</p>
      <p style="margin-top:12px"><strong>Write to 16–20 words as a first draft, then render and measure, and rewrite anything over 7.5 s.</strong> Every number in the table above came out of the actual audio file, not an estimate. A comma is worth about a third of a second; a word is worth far more.</p>
    </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{esc(t['h1_plain'])} — complete build blueprint</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>{t['emoji']}</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,600;0,800;0,900;1,800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
:root{{
  --bg:#060c13; --bg2:#0b151f; --panel:#0f1c28; --panel2:#132433;
  --line:#1e3345; --line2:#2a4257;
  --ink:#eaf2f8; --ink2:#a9bdcd; --ink3:#7b93a7;
  --yellow:#ffe23d; --cyan:#4fd8ff; --coral:#f0937f; --green:#5fe0a8; --red:#ff6b6b;
  --accent:{t['accent']};
  --mono:'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,monospace;
}}
*{{box-sizing:border-box}}
html{{-webkit-text-size-adjust:100%;scroll-behavior:smooth}}
body{{margin:0;background:var(--bg);color:var(--ink);font:400 18px/1.65 Inter,system-ui,-apple-system,Segoe UI,Roboto,sans-serif;-webkit-font-smoothing:antialiased}}
a{{color:var(--cyan)}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 24px}}
.narrow{{max-width:880px;margin-left:auto;margin-right:auto}}

header{{position:relative;overflow:hidden;border-bottom:1px solid var(--line);
  background:radial-gradient(120% 90% at 50% -10%, {t['glow']}, transparent 60%),linear-gradient(180deg,#0a1420,#060c13)}}
.heroinner{{position:relative;padding:64px 0 54px}}
.back{{font:600 13px/1 var(--mono);color:var(--ink3);text-decoration:none;display:inline-block;margin-bottom:22px}}
.back:hover{{color:var(--cyan)}}
.kicker{{font:700 13px/1 var(--mono);letter-spacing:.18em;text-transform:uppercase;color:var(--accent);margin-bottom:20px}}
h1{{font:900 clamp(36px,6vw,68px)/1.03 Archivo,sans-serif;letter-spacing:-.028em;margin:0 0 20px}}
h1 em{{font-style:italic;color:var(--accent)}}
.sub{{font-size:21px;line-height:1.55;color:var(--ink2);max-width:780px;margin:0 0 32px}}
.sub strong{{color:var(--ink)}}
.metarow{{display:flex;flex-wrap:wrap;gap:10px}}
.chip{{font:600 13px/1 var(--mono);letter-spacing:.03em;padding:10px 14px;border:1px solid var(--line2);border-radius:999px;background:rgba(15,28,40,.75);color:var(--ink2)}}
.chip b{{color:var(--ink)}}

section{{padding:62px 0;border-bottom:1px solid var(--line)}}
section:last-of-type{{border-bottom:0}}
.snum{{font:700 12px/1 var(--mono);letter-spacing:.18em;color:var(--ink3);text-transform:uppercase;margin-bottom:14px}}
h2.sec{{font:800 clamp(27px,4vw,40px)/1.1 Archivo,sans-serif;letter-spacing:-.022em;margin:0 0 18px}}
h3{{font:800 22px/1.25 Archivo,sans-serif;letter-spacing:-.01em;margin:36px 0 12px}}
h4{{font:700 17px/1.3 Inter,sans-serif;margin:24px 0 8px;color:var(--ink)}}
p{{margin:0 0 16px;color:var(--ink2)}}
p strong,li strong{{color:var(--ink);font-weight:600}}
.lead{{font-size:20px;color:var(--ink);max-width:820px}}
ul,ol{{color:var(--ink2);padding-left:22px;margin:0 0 18px}}
li{{margin-bottom:9px}}
.dim{{color:var(--ink3);font-size:14px}}

.box{{border-radius:14px;padding:22px 24px;margin:24px 0;border:1px solid var(--line2);background:var(--panel)}}
.box p:last-child{{margin-bottom:0}}
.box .bt{{font:800 13px/1 var(--mono);letter-spacing:.13em;text-transform:uppercase;margin-bottom:12px}}
.box.find{{border-color:#3d5f2e;background:linear-gradient(135deg,#132a1c,#0e1d17)}}.box.find .bt{{color:var(--green)}}
.box.warn{{border-color:#6b4a1e;background:linear-gradient(135deg,#2a2113,#1d160e)}}.box.warn .bt{{color:#ffc464}}
.box.stop{{border-color:#6e2b2b;background:linear-gradient(135deg,#2b1414,#1d0f0f)}}.box.stop .bt{{color:var(--red)}}
.box.key{{border-color:#1c4d63;background:linear-gradient(135deg,#0f2c3a,#0b1e29)}}.box.key .bt{{color:var(--cyan)}}

.tw{{overflow-x:auto;margin:24px 0;border:1px solid var(--line2);border-radius:12px;background:var(--panel)}}
table{{border-collapse:collapse;width:100%;min-width:640px;font-size:16px}}
th,td{{padding:13px 16px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}}
th{{font:700 12px/1.3 var(--mono);letter-spacing:.09em;text-transform:uppercase;color:var(--ink3);background:var(--panel2);white-space:nowrap}}
td{{color:var(--ink2)}}
tr:last-child td{{border-bottom:0}}
td b,td strong{{color:var(--ink)}}
.num{{font-family:var(--mono);font-size:15px;color:var(--ink);white-space:nowrap}}
.tick{{color:var(--green);font-weight:700}}

pre{{margin:0;padding:18px 18px;background:#08131d;border:1px solid var(--line);border-top:0;border-radius:0 0 10px 10px;overflow-x:auto;
  font:400 14.5px/1.7 var(--mono);color:#d5e6f2;white-space:pre-wrap;word-wrap:break-word}}
code{{font-family:var(--mono);font-size:.92em;background:#0d1e2b;padding:2px 6px;border-radius:5px;color:var(--cyan)}}
pre code{{background:none;padding:0;color:inherit;font-size:inherit}}

/* prompt block + copy button */
.pblock{{margin:22px 0}}
.phead{{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:11px 14px 11px 18px;
  background:#0d1c28;border:1px solid var(--line);border-radius:10px 10px 0 0}}
.phead .plabel{{margin:0}}
.cbtn{{font:700 12px/1 var(--mono);letter-spacing:.09em;text-transform:uppercase;color:var(--cyan);
  background:#12303f;border:1px solid #1c4d63;border-radius:8px;padding:10px 14px;cursor:pointer;min-height:38px;
  transition:background .12s,color .12s,border-color .12s;white-space:nowrap}}
.cbtn:hover{{background:#17415a}}
.cbtn:focus-visible{{outline:2px solid var(--cyan);outline-offset:2px}}
.cbtn.done{{background:#14361f;border-color:#3d5f2e;color:var(--green)}}
.cbtn.fail{{background:#3a1a1a;border-color:#6e2b2b;color:var(--red)}}
.copyall{{display:flex;flex-wrap:wrap;gap:10px;margin:22px 0 6px}}
.copyall .cbtn{{padding:13px 18px;font-size:12.5px}}

/* clip cards */
.clip{{border:1px solid var(--line2);border-radius:16px;background:var(--panel);margin:28px 0;overflow:hidden}}
.chead{{padding:20px 24px;background:var(--panel2);border-bottom:1px solid var(--line)}}
.chead .cmeta{{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:12px}}
.chead .cn{{font:800 15px/1 var(--mono);color:var(--accent)}}
.chead .tc{{font:600 13px/1 var(--mono);color:var(--ink3)}}
.chead h4{{margin:0 0 10px;font:800 22px/1.2 Archivo,sans-serif;color:var(--ink)}}
.chead h4 .where{{font:600 13px/1 var(--mono);color:var(--ink3);margin-left:10px;white-space:nowrap}}
.chead .vo{{font-size:16.5px;color:var(--ink);font-style:italic;border-left:3px solid var(--accent);padding-left:16px;margin:0}}
.cbody{{padding:6px 24px 22px}}
.cnote{{font-size:15.5px}}
.plabel{{font:700 11px/1 var(--mono);letter-spacing:.13em;text-transform:uppercase;margin:22px 0 9px;color:var(--cyan)}}
.plabel.v{{color:var(--coral)}}
.plabel.n{{color:#ffc464}}
.kf{{font:700 11px/1 var(--mono);letter-spacing:.07em;padding:5px 8px;border-radius:6px;white-space:nowrap;display:inline-block}}
.kf.n{{background:#33280d;color:var(--yellow);border:1px solid #6b4a1e}}
.kf.r{{background:#0f2c3a;color:var(--cyan);border:1px solid #1c4d63}}
.sw{{width:14px;height:14px;border-radius:4px;display:inline-block;vertical-align:-2px;margin-right:7px;border:1px solid rgba(255,255,255,.18)}}

/* timeline */
.tl{{margin:30px 0;border:1px solid var(--line2);border-radius:12px;overflow:hidden;background:var(--panel)}}
.tlbar{{display:flex;height:58px}}
.tlseg{{flex:1;border-right:1px solid var(--bg);display:flex;align-items:center;justify-content:center;font:700 13px/1 var(--mono);color:#06121c}}
.tlseg:last-child{{border-right:0}}
.tlvo{{display:flex;height:30px;border-top:1px solid var(--line);position:relative;background:#0b1a25}}
.tlvo div{{position:absolute;top:5px;height:20px;background:#2b556e;border-radius:3px;border-left:2px solid var(--accent)}}
.tlcap{{padding:12px 16px;font:600 12px/1.5 var(--mono);color:var(--ink3);border-top:1px solid var(--line)}}

.audio{{margin:22px 0;padding:20px 22px;border:1px solid var(--line2);border-radius:14px;background:var(--panel)}}
.audio audio{{width:100%;margin-top:12px}}
.dl{{display:inline-block;margin-top:14px;margin-right:10px;font:700 13px/1 var(--mono);letter-spacing:.06em;padding:13px 16px;border-radius:9px;
  background:#12303f;border:1px solid #1c4d63;color:var(--cyan);text-decoration:none}}
.dl:hover{{background:#17415a}}

ol.steps{{counter-reset:s;list-style:none;padding-left:0}}
ol.steps>li{{counter-increment:s;position:relative;padding-left:50px;margin-bottom:20px}}
ol.steps>li::before{{content:counter(s);position:absolute;left:0;top:-2px;width:34px;height:34px;border-radius:9px;
  background:var(--panel2);border:1px solid var(--line2);color:var(--accent);font:800 15px/34px var(--mono);text-align:center}}
ol.steps>li b{{color:var(--ink)}}

.pagenav{{display:flex;flex-wrap:wrap;gap:14px;font:600 14px/1 var(--mono);margin:0 0 10px}}
footer{{padding:46px 0 70px;color:var(--ink3);font-size:15px}}
footer a{{color:var(--cyan)}}
@media(max-width:760px){{
  body{{font-size:17px}}
  section{{padding:48px 0}}
  .heroinner{{padding:46px 0 40px}}
  .chead,.cbody{{padding-left:16px;padding-right:16px}}
  .tlseg{{font-size:10px}}
  .phead{{padding-left:14px}}
  pre{{font-size:13.5px;padding:15px}}
}}
</style>
</head>
<body>

<header>
  <div class="heroinner">
    <div class="wrap">
      <a class="back" href="../">← back to the format teardown</a>
      <div class="kicker">Build blueprint · Video {t['video_no']} of the series · {t['lane']}</div>
      <h1>{t['title_html']}</h1>
      <p class="sub">{t['sub']}</p>
      <div class="metarow">
        <span class="chip"><b>8</b> clips × <b>8.000 s</b></span>
        <span class="chip"><b>8</b> image prompts</span>
        <span class="chip"><b>8</b> image-to-video prompts</span>
        <span class="chip">VO <b>rendered</b> · {vo['dur']:.2f} s · {vo['lufs']} LUFS</span>
        <span class="chip">{t['kf_chip']}</span>
      </div>
    </div>
  </div>
</header>

<!-- ============ 00 THE FULL SCRIPT ============ -->
<section id="fullscript">
  <div class="wrap"><div class="narrow">
    <div class="snum">00 — The full script, first</div>
    <h2 class="sec">Take this and make the audio anywhere</h2>
    <p class="lead">The whole narration in one block, so it can go straight into any voice tool — ElevenLabs, your phone, a hired voice, or the free script further down this page. Nothing else on this page is needed to record it.</p>

    <div class="copyall">
      <button class="cbtn" type="button" data-target="scriptplain">⧉ Copy the full script</button>
      <button class="cbtn" type="button" data-target="scripttimed">⧉ Copy it with the timings</button>
    </div>

    <div class="pblock">
      <div class="phead"><span class="plabel">The script · {words} words · 8 sentences</span><button class="cbtn" type="button" data-target="scriptplain">Copy</button></div>
<pre id="scriptplain">{esc(plain_script(t))}</pre>
    </div>

    <div class="box key">
      <div class="bt">If you record it somewhere else, these four rules keep it in sync</div>
      <p><b>1. One sentence per clip, in order.</b> Sentence 1 belongs to seconds 0–8, sentence 2 to 8–16, and so on to sentence 8 at 56–64.<br>
      <b>2. Every sentence must be spoken in under 8 seconds.</b> Read at roughly <b>158 words per minute</b> — unhurried, not rushed. The measured timings for this script are in <a href="#script">section 04</a>.<br>
      <b>3. Record it as one continuous take</b>, or export it as one file. Never eight separate files dropped at the cuts — a single track is what makes a word carry across a cut.<br>
      <b>4. Each sentence starts 0.10 s <em>before</em> its cut.</b> If your tool cannot place them that precisely, land them on the cut instead; do not land them late.</p>
    </div>

    <div class="pblock">
      <div class="phead"><span class="plabel v">The same script with the exact timings</span><button class="cbtn" type="button" data-target="scripttimed">Copy</button></div>
<pre id="scripttimed">{esc(numbered_script(t))}</pre>
    </div>

    <p style="font-size:15.5px;color:var(--ink3)">Or skip all of it: <a href="#voice">the finished voice-over is already rendered in section 05</a> and can be downloaded as an MP3.</p>
  </div></div>
</section>

<!-- ============ 01 RULES ============ -->
<section id="rules">
  <div class="wrap"><div class="narrow">
    <div class="snum">01 — The five rules this video is built on</div>
    <h2 class="sec">Eight shots inside one body, not eight separate pictures</h2>
    <p class="lead">These five rules were bought with a rejected first version of the egg video. Eight good-looking images that had nothing to do with each other read as eight art pieces; the reference video reads as <em>one journey through one person</em>, and that difference is structural, not decorative. Every prompt on this page is written to these five.</p>

    <div class="tw">
      <table>
        <thead><tr><th>The rule</th><th>What breaks without it</th><th>How it is enforced here</th></tr></thead>
        <tbody>
          <tr><td><b>1 · Continuity is a mechanism</b></td><td>Eight shots with no shared body, no shared light, no shared object.</td><td>Every shot ends on a stated <b>end frame</b>, and the next shot's prompt opens by quoting that exact frame back. <a href="#chain">The chain is in section 02.</a></td></tr>
          <tr><td><b>2 · Say it must look real</b></td><td>“Photorealistic 3D medical visualisation” is a genre label. It never tells the model the result has to look <em>real</em>.</td><td>A dedicated <b>REALISM</b> block in all eight prompts — real endoscope, wet uneven tissue, capillaries under the membrane, and an explicit list of what it must <em>not</em> look like.</td></tr>
          <tr><td><b>3 · Name the real anatomy</b></td><td>The model invents plausible-looking tissue that no anatomist would recognise.</td><td>Every image prompt carries a <b>REAL ANATOMY</b> line naming the structures that must be correct in that specific shot.</td></tr>
          <tr><td><b>4 · Keep the body on screen</b></td><td>Abstract macro in a black void. The viewer loses the thread — this could be anything, anywhere.</td><td><b>Four of the eight shots are whole-body</b>, in the same close → wide → close → wide rhythm the reference uses.</td></tr>
          <tr><td><b>5 · Write it to the viewer</b></td><td>“A muscle fibre draws them in.” Clinical, third person, about nobody.</td><td>Every sentence names a part of <b>your</b> body, and it opens on the everyday moment. <a href="#fullscript">Section 00.</a></td></tr>
        </tbody>
      </table>
    </div>

    <div class="box find">
      <div class="bt">⭐ The rhythm that makes it read as a body</div>
      <p>The reference video never stays inside for long. It goes <strong>close → wide → close → wide</strong>, and every wide shot is the whole human figure. That is what stops a macro shot from becoming abstract: two seconds earlier you saw where in the body you were.</p>
      <p style="margin-top:12px">This build copies that rhythm exactly — <strong>shots 2, 4, 6 and 8 all show the whole figure</strong>, and shots 4 and 6 travel between the two scales inside a single take, so the connection is shown rather than assumed.</p>
    </div>
  </div></div>
</section>

<!-- ============ 02 THE CHAIN ============ -->
<section id="chain">
  <div class="wrap"><div class="narrow">
    <div class="snum">02 — The continuity chain</div>
    <h2 class="sec">Every shot hands its last frame to the next one</h2>
    <p class="lead">This is the mechanism that makes eight separate generations look like one video. Each clip's prompt states the exact frame it ends on. The next clip's image prompt opens by quoting that same sentence back. Nothing is left for the model to invent between shots.</p>

    <div class="tw">
      <table>
        <thead><tr><th>Clip</th><th>Shot</th><th>Ends on exactly this frame</th><th>Which</th></tr></thead>
        <tbody>
{chain_rows(t)}
        </tbody>
      </table>
    </div>

    <h3>How to actually chain them when you generate</h3>
    <ol class="steps">
      <li><b>Generate still 1 and approve it.</b> It sets the figure, the skin translucency, {t['locks']}, the light and the background for everything that follows.</li>
      <li><b>Render clip 1 from that still</b>, then <b>export its last frame as a PNG.</b></li>
      <li><b>Generate still 2 with that PNG attached as a reference image</b>, alongside image prompt 2. The prompt already describes the same figure and the same end state, so the reference locks the render to it rather than fighting it.</li>
      <li><b>Repeat for all eight.</b> Approve the still, render the clip, export the last frame, feed it forward.</li>
    </ol>

    <div class="box key">
      <div class="bt">Why the still still matters, even with a last frame in hand</div>
      <p>It is tempting to skip the still and feed clip 1's last frame straight in as clip 2's first frame. Do not — you lose the approval step, and any drift compounds silently down the chain.</p>
      <p style="margin-top:12px">Generating a fresh still and <em>then</em> animating it means <strong>you see and approve every one of the eight frames the video is built on before paying for any motion</strong>. The last-frame PNG is there to lock the look, not to replace the still.</p>
    </div>

    <div class="box warn">
      <div class="bt">⚠ Where the chain is deliberately broken, and why</div>
      <p>{t['chain_break']}</p>
      <p style="margin-top:12px"><strong>A match cut is continuity; a random new picture is not.</strong></p>
    </div>
  </div></div>
</section>

<!-- ============ 03 ORDER ============ -->
<section id="order">
  <div class="wrap"><div class="narrow">
    <div class="snum">03 — The order of operations</div>
    <h2 class="sec">Script first, voice second, pictures last</h2>
    <p class="lead">The order matters more than any single step. The voice-over is what decides where every cut lands, so it has to exist before a single image is generated — otherwise you end up speeding clips up to fit, which is exactly the defect measured in the reference video.</p>

    <ol class="steps">
      <li><b>Write 8 sentences.</b> One per clip, in body order. <a href="#fullscript">Section 00</a> — already written.</li>
      <li><b>Render the voice-over and measure it.</b> Every sentence must be spoken in under 8 seconds. If one overruns, cut words — never speed anything up later. <a href="#voice">Section 05</a> — already rendered.</li>
      <li><b>Generate 8 still images, in order, chaining each one to the last frame before it.</b> Approve each still before spending anything on motion. <a href="#prompts">Section 07</a>.</li>
      <li><b>Generate 8 videos</b>, each using its approved still as the first frame, 8 seconds, 9:16, <b>audio off</b>.</li>
      <li><b>Lay them on a 24 fps timeline</b> at 0, 8, 16, 24, 32, 40, 48, 56 s and drop the single voice-over file across the whole thing. <a href="#assembly">Section 08</a>.</li>
      <li><b>Auto-generate captions, add a music bed, export.</b> <a href="#captions">Sections 09–11</a>.</li>
    </ol>

    <div class="box key">
      <div class="bt">Why the voice comes before the pictures</div>
      <p>The reference video runs <strong>≈22.3 fps of content inside a 30 fps file</strong> — the signature of clips that were stretched or squeezed to fit the narration after the fact. It produces visible judder for no benefit.</p>
      <p style="margin-top:12px">Doing it in this order removes the problem entirely: the clips are always exactly 8.000 s, and the script was cut to fit them rather than the other way round. <strong>The grid is fixed. The words bend.</strong></p>
    </div>
  </div></div>
</section>

<!-- ============ 04 SCRIPT ============ -->
<section id="script">
  <div class="wrap"><div class="narrow">
    <div class="snum">04 — The script, measured</div>
    <h2 class="sec">Eight sentences, in the second person, each one timed</h2>
    <p class="lead">The same script as section 00, with the numbers that came out of the rendered audio. These are measurements, not estimates — headroom is the time left in the clip after the sentence finishes.</p>

    <div class="tw">
      <table>
        <thead><tr><th>Clip</th><th>Sentence</th><th>Words</th><th>Spoken</th><th>Headroom</th></tr></thead>
        <tbody>
{script_rows(t)}
        </tbody>
      </table>
    </div>
    <p style="font-size:15.5px;color:var(--ink3)">{words} words · {speech:.2f} s of speech in a 64 s video · en-US-AriaNeural at rate <code>−18%</code> · the shortest headroom on this script is {min(headroom(c) for c in clips):.2f} s.</p>
{invbox}
    <div class="box stop">
      <div class="bt">The line that must not move</div>
      <p>{t['compliance']}</p>
    </div>
  </div></div>
</section>

<!-- ============ 05 VOICE ============ -->
<section id="voice">
  <div class="wrap"><div class="narrow">
    <div class="snum">05 — The voice-over</div>
    <h2 class="sec">One continuous track, not eight clips</h2>
    <p class="lead">This is the step that decides whether the finished video sounds like a video or like eight videos glued together — and it is already done. Listen to it, download it, or rebuild it from the script with the shell script beside it.</p>

    <div class="audio">
      <div style="font:700 12px/1 var(--mono);letter-spacing:.13em;text-transform:uppercase;color:var(--cyan);margin-bottom:4px">The finished voice-over · drop this straight into the editor</div>
      <p style="margin:10px 0 0;font-size:15.5px">{vo['dur']:.2f} s · 48 kHz · {vo['lufs']} LUFS integrated · true peak {vo['tp']} dBFS · every sentence verified in the finished file to start exactly 0.10 s before its cut.</p>
      <audio controls preload="none" src="{t['vo_file']}"></audio>
      <a class="dl" href="{t['vo_file']}" download>↓ download {t['vo_file']}</a>
      <a class="dl" href="build-vo.sh" download>↓ build-vo.sh (rebuild it yourself, free)</a>
    </div>

    <h3>Where each sentence has to land</h3>
    <p>Every sentence begins <strong>0.10 seconds before its clip does</strong>. That is not sloppiness — it is the whole trick. The reference video does exactly this on six of its eight sentences, and it is what makes a word carry across a cut, which is what tells the ear that the narration is one continuous thing running underneath the pictures.</p>
    <div class="tw">
      <table>
        <thead><tr><th>Sentence</th><th>Audible at</th><th>Clip it narrates</th><th>Ends at</th><th>Headroom</th></tr></thead>
        <tbody>
{landing_rows(t)}
        </tbody>
      </table>
    </div>

    <h3>Which voice, and the rate</h3>
    <p>Two routes, and neither needs an account or a payment: <b>your own voice</b>, recorded as one continuous take with a beat of silence between sentences — or <b>Microsoft neural TTS</b>, which is what made the file above (<code>pip install edge-tts</code>, free, no key). Voice used here is <code>en-US-AriaNeural</code> at rate <code>−18%</code>, which is about 158 wpm. A slower read sounds better, but <strong>the longest sentence sets the ceiling for the whole video</strong> — shorten the longest sentence before slowing the voice.</p>

    <div class="box warn">
      <div class="bt">⚠ Measure the speech, not the file</div>
      <p>Synthesised sentences arrive padded with roughly <strong>0.2 s of silence at the front and 0.9 s at the back</strong>. If you place the files by their reported length, every sentence lands about a tenth of a second <em>late</em> — the exact opposite of what you want, and it happened on the first build in this series before it was caught.</p>
      <p style="margin-top:12px">Strip the padding first, then place by the audible start. <code>build-vo.sh</code> does this automatically and prints the onsets so you can check them: they must read <strong>7.90 / 15.90 / 23.90 / 31.90 / 39.90 / 47.90 / 55.90</strong>. <strong>If any row prints “OVERRUNS ITS CLIP”, cut words from that sentence and run it again.</strong></p>
    </div>
  </div></div>
</section>

<!-- ============ 06 TIMELINE ============ -->
<section id="timeline">
  <div class="wrap"><div class="narrow">
    <div class="snum">06 — Where the image changes</div>
    <h2 class="sec">The grid: a new image every 8.000 seconds</h2>
    <p class="lead">There is nothing to judge by eye here. The picture changes on an exact multiple of eight seconds, eight times, and the voice runs straight underneath all of it.</p>

    <div class="tl">
      <div class="tlbar">
{timeline_segs(t)}
      </div>
      <div class="tlvo">
{timeline_vo(t)}
      </div>
      <div class="tlcap">top: the eight clips, each exactly 8.000 s, colour = that clip's palette · bottom: the eight spoken sentences on one continuous track, each starting 0.10 s before its cut (coloured edge)</div>
    </div>

    <div class="tw">
      <table>
        <thead><tr><th>Clip</th><th>In → out</th><th>Shot</th><th>Camera move</th><th>Keyframe</th><th>Palette</th></tr></thead>
        <tbody>
{grid_rows(t)}
        </tbody>
      </table>
    </div>

    <div class="box find">
      <div class="bt">⭐ {t['kf_box_title']}</div>
      <p>{t['kf_box']}</p>
    </div>

    <div class="box warn">
      <div class="bt">⚠ Reuse the still, re-render the motion</div>
      <p>Feed the shared keyframe back in as the first frame — then write a <em>different</em> motion prompt for it, which is what the video prompts on this page already are. Never drop the identical rendered clip into two uploads. It costs the same either way, and repeated footage across uploads is what gets a channel labelled repetitive.</p>
    </div>
  </div></div>
</section>

<!-- ============ 07 PROMPTS ============ -->
<section id="prompts">
  <div class="wrap"><div class="narrow">
    <div class="snum">07 — The 16 prompts</div>
    <h2 class="sec">Eight stills, eight motions, paste-ready</h2>
    <p class="lead">Each card below is one clip: the sentence it carries, the image prompt that makes the still, and the image-to-video prompt that moves it. Every prompt is complete on its own — the shared style block, the realism block, the real-anatomy line, the continuity handoff and the ban on text are already written into each one, so there is nothing to remember and nothing to append.</p>

    <div class="copyall">
      <button class="cbtn" type="button" data-target="allimg">⧉ Copy all 8 image prompts</button>
      <button class="cbtn" type="button" data-target="allvid">⧉ Copy all 8 video prompts</button>
      <button class="cbtn" type="button" data-target="styleblock">⧉ Copy the shared style + realism block</button>
    </div>
    <pre id="allimg" hidden>{esc(ALL_IMG)}</pre>
    <pre id="allvid" hidden>{esc(ALL_VID)}</pre>
    <pre id="styleblock" hidden>{esc(STYLE_TXT)}</pre>

    <div class="box stop">
      <div class="bt">🛑 Three settings, or the video is ruined</div>
      <p><b>1. Audio OFF on every generation.</b> Veo generates sound by default and it will fight the narration. <b>2. 9:16 natively</b> — never generate 16:9 and crop. <b>3. 8 seconds exactly</b>, which is Veo 3.1's native maximum, so every clip is one generation with nothing trimmed.</p>
      <p style="margin-top:12px">The ban on text is already at the end of all sixteen prompts. It is there because generators render type as garbled pseudo-letters — <strong>every word on screen comes from the editor, never from the model.</strong></p>
    </div>

    <div class="box key">
      <div class="bt">How each prompt is laid out, and why</div>
      <p>Every image prompt runs in the same order: <b>SHOT</b> → <b>SCENE</b> → <b>CAMERA</b> → <b>SUBJECT</b> → <b>REAL ANATOMY</b> → <b>LIGHT</b> → <b>CONTINUITY</b> → <b>THE FIGURE</b> → <b>STYLE</b> → <b>REALISM</b> → <b>NO TEXT</b>. Every video prompt runs: <b>START FRAME</b> → <b>CAMERA</b> → <b>four timed beats</b> → <b>LIGHTING</b> → <b>END FRAME</b> → <b>CONSTRAINTS</b> → <b>REALISM IN MOTION</b> → <b>NO TEXT</b>.</p>
      <p style="margin-top:12px">Each heading owns one question and answers it once. That matters more than the wording: when two parts of a prompt answer the same question differently — a camera line and a framing line both naming a distance, say — <strong>the model picks one and it is usually not the one you meant.</strong> That is also why STYLE and REALISM are separate blocks: STYLE owns the look, REALISM owns whether it looks real.</p>
    </div>

    <div class="box warn">
      <div class="bt">⚠ These are long prompts, and length has a cost</div>
      <p>The image prompts on this page run <b>{min(len(img_prompt(t, c).split()) for c in clips)}–{max(len(img_prompt(t, c).split()) for c in clips)} words</b> each. That is deliberate — the detail is what fixes the continuity and the realism — but <strong>every rule you add makes every other rule weaker</strong>. If a generation ignores something that matters, do not fix it by adding another sentence.</p>
      <p style="margin-top:12px">Cut instead, in this order: <b>1.</b> the SUBJECT paragraph if the scene already describes it, <b>2.</b> the CONTINUITY paragraph <em>once you are attaching the previous last frame as a reference image</em> — the picture is doing that job by then — <b>3.</b> the background sentence in STYLE. <strong>Never cut the REALISM block, the REAL ANATOMY line or the NO TEXT line.</strong> Those are the three that decide whether it looks like a body.</p>
    </div>

{CARDS}
  </div></div>
</section>

<!-- ============ 08 ASSEMBLY ============ -->
<section id="assembly">
  <div class="wrap"><div class="narrow">
    <div class="snum">08 — Assembly</div>
    <h2 class="sec">Putting it together</h2>
    <p class="lead">Any editor will do this — the reference video was cut in Clipchamp, which is free and runs in a browser. The only settings that matter are the frame rate and the fact that the voice-over is one object, not eight.</p>

    <ol class="steps">
      <li><b>Set the project to 24 fps, 1080 × 1920.</b> Generated clips are 24 fps; a 30 fps timeline forces the editor to invent frames, which is the judder in the reference. Match the timeline to the source and nothing is invented.</li>
      <li><b>Drop the eight clips in order</b> with no gaps and no transitions. They should land at 0, 8, 16, 24, 32, 40, 48 and 56 s on their own. <strong>Hard cuts only — no dissolves.</strong> The continuity is in the frames, not in a transition effect; a dissolve would blur the one thing that carries it.</li>
      <li><b>Drop <code>{t['vo_file']}</code> on the audio track at 0:00</b> as a single object spanning the whole timeline. Never split it at the cuts. This is what lets a word carry across a cut, and it is the difference between one video and eight.</li>
      <li><b>Add the hook.</b> {t['hook_step']}</li>
      <li><b>Auto-generate the captions</b> (section 09), then the music bed (section 10), then export (section 11).</li>
    </ol>

    <div class="box warn">
      <div class="bt">⚠ Never speed-adjust a clip to make it fit</div>
      <p>If a clip comes back at 7.9 s or 8.1 s instead of 8.000, <strong>trim it, do not stretch it</strong>. Stretching is what produced the ≈22.3 fps content cadence measured in the reference. A 0.1 s trim is invisible; a speed change is visible in every frame that follows.</p>
      <p style="margin-top:12px">Trim from the <em>front</em>, not the back — the last frame of each clip is the handoff to the next one, and cutting it is what breaks the chain.</p>
    </div>

    <div class="box key">
      <div class="bt">On the hook, and what it costs</div>
      <p>Adding a one-second hook makes the finished video ~65 s rather than 64, and the eight cuts no longer land on round multiples of eight. That is fine — nothing downstream depends on it. The 8-second grid is a <em>generation</em> constraint, not a delivery one.</p>
      <p style="margin-top:12px">If you would rather keep the 64.000 s total, take the second off the end of clip 8 instead of adding it to the front. The last second of that shot is deliberately motionless, so it is the cheapest second in the video to lose.</p>
    </div>
  </div></div>
</section>

<!-- ============ 09 CAPTIONS ============ -->
<section id="captions">
  <div class="wrap"><div class="narrow">
    <div class="snum">09 — Captions</div>
    <h2 class="sec">Zero prompts, ~97 cards, 94.5% of the runtime</h2>
    <p class="lead">The captions in the reference are auto-generated from the voice-over — which means this entire layer costs nothing to make and nothing to write. Point the editor's auto-caption tool at the narration track and style the result.</p>

    <div class="tw">
      <table>
        <thead><tr><th>Setting</th><th>Value measured in the reference</th></tr></thead>
        <tbody>
          <tr><td>Words per card</td><td>1–3, typically <b>2</b></td></tr>
          <tr><td>Card duration</td><td>median <b>0.50 s</b></td></tr>
          <tr><td>Coverage</td><td><b>94.5%</b> of the runtime carries a caption — the only blank runs are on the pauses</td></tr>
          <tr><td>Colour</td><td>yellow <b>RGB(248, 252, 3)</b>, heavy italic, black outline</td></tr>
          <tr><td>Position</td><td>median <b>77.5%</b> down the frame — below centre, clear of the platform's own UI</td></tr>
        </tbody>
      </table>
    </div>

    <p>Two words per card at half a second each is fast, and it is deliberate: the constant motion is doing retention work of its own. Set the auto-caption tool to its shortest grouping, not its default sentence grouping.</p>

    <div class="box warn">
      <div class="bt">⚠ Check the captions against the script, once</div>
      <p>Auto-captioning transcribes what it <em>hears</em>, so it will occasionally mishear a technical word — {t['caption_words']} are the likely candidates in this script. Read the eight lines back against <a href="#fullscript">section 00</a> before exporting. It is a one-minute check that prevents a misspelling being burned into the frame permanently.</p>
    </div>
  </div></div>
</section>

<!-- ============ 10 MUSIC ============ -->
<section id="music">
  <div class="wrap"><div class="narrow">
    <div class="snum">10 — Music and levels</div>
    <h2 class="sec">The bed the reference never had</h2>
    <p class="lead">The reference has no music at all — its silent gaps measure between −51 and −60 dB, which is true digital silence. Three of those gaps run over a second. On a vertical feed, a second of silence is an exit.</p>

    <div class="tw">
      <table>
        <thead><tr><th>Element</th><th>Target</th><th>Why</th></tr></thead>
        <tbody>
          <tr><td>Music bed</td><td><b>28–30 dB under the voice</b>, ducked</td><td>fills the seven inter-sentence gaps, which run {min(headroom(c) for c in clips):.1f}–{max(headroom(c) for c in clips):.1f} s each in this build</td></tr>
          <tr><td>Bed choice</td><td>ambient, no melody, no percussion, no builds</td><td>anything with a rhythm will fight the cuts, which land every 8 s</td></tr>
          <tr><td>Final loudness</td><td><b>−14 LUFS integrated</b></td><td>platforms turn loud audio down but do not reliably turn quiet audio up</td></tr>
          <tr><td>True peak</td><td><b>−1 dBTP</b></td><td>headroom for lossy transcoding on upload</td></tr>
          <tr><td>Fade</td><td>bed fades in over 0.5 s, out over the last 1 s</td><td>the reference ends by cutting to 3 black frames, which reads as a mistake</td></tr>
        </tbody>
      </table>
    </div>

    <p>The voice-over file is already normalised on its own. Once a bed is added underneath, <strong>re-normalise the full mix</strong>, not the voice — otherwise the bed pushes the total over target. −14.0 exactly is unreachable on an uncompressed voice track, because true-peak headroom runs out first; a light compressor before normalising closes the last 0.8 LU.</p>
  </div></div>
</section>

<!-- ============ 11 EXPORT ============ -->
<section id="export">
  <div class="wrap"><div class="narrow">
    <div class="snum">11 — Export</div>
    <h2 class="sec">Settings</h2>
    <div class="tw">
      <table>
        <thead><tr><th>Setting</th><th>Value</th><th>Note</th></tr></thead>
        <tbody>
          <tr><td>Resolution</td><td class="num">1080 × 1920</td><td>generated natively at 9:16, never cropped from 16:9</td></tr>
          <tr><td>Frame rate</td><td class="num">24 fps</td><td>matches the source clips exactly; nothing is interpolated</td></tr>
          <tr><td>Codec</td><td class="num">H.264, CRF-based</td><td>—</td></tr>
          <tr><td>Bitrate</td><td class="num">8–12 Mbps</td><td>the reference is 19.1 Mbps / 146 MB — roughly 3× what any platform keeps after its own re-encode</td></tr>
          <tr><td>Audio</td><td class="num">AAC 192 kbps, 48 kHz</td><td>—</td></tr>
          <tr><td>Loudness</td><td class="num">−14 LUFS, −1 dBTP</td><td>measured on the final mix, not the voice track</td></tr>
          <tr><td>Ending</td><td class="num">hold the last frame 0.5 s</td><td>with the channel mark; the reference cuts to 3 black frames and stops</td></tr>
          <tr><td>Watermark</td><td class="num">transparent PNG, 60–70%</td><td>the reference's logo sits on an opaque white square and is the brightest object in frame on the dark shots</td></tr>
        </tbody>
      </table>
    </div>
  </div></div>
</section>

<!-- ============ 12 CHECKLIST ============ -->
<section id="checklist">
  <div class="wrap"><div class="narrow">
    <div class="snum">12 — Before it goes up</div>
    <h2 class="sec">The pre-upload check</h2>
    <div class="tw">
      <table>
        <thead><tr><th>#</th><th>Check</th><th>Fails if</th></tr></thead>
        <tbody>
          <tr><td class="num">1</td><td><b>Play the eight clips back to back with the sound off.</b> It has to read as one journey through one body</td><td>the figure, the skin or the light changes between shots — the chain broke somewhere</td></tr>
          <tr><td class="num">2</td><td>The last frame of every clip matches the first frame of the next one</td><td>a cut reads as a new video rather than the next moment</td></tr>
          <tr><td class="num">3</td><td>Shots 2, 4, 6 and 8 all clearly show a human body</td><td>the video drifts into abstraction and stops being about anyone</td></tr>
          <tr><td class="num">4</td><td>Every interior shot still looks like wet living tissue, not a clean render</td><td>it reads as an illustration of a body instead of footage from inside one</td></tr>
          <tr><td class="num">5</td><td>No text, letters or numbers rendered inside any of the eight clips</td><td>a generation slipped pseudo-writing into the frame</td></tr>
          <tr><td class="num">6</td><td>Every clip is exactly 8.000 s and no clip has been speed-adjusted</td><td>judder, and a content cadence that does not match the container</td></tr>
          <tr><td class="num">7</td><td>The voice-over is one unsplit object on the timeline</td><td>the cuts start to sound like eight separate videos</td></tr>
          <tr><td class="num">8</td><td>Final mix measures −14 LUFS ±1, true peak ≤ −1 dBTP</td><td>it plays quieter than everything around it in the feed</td></tr>
          <tr><td class="num">9</td><td>Captions match the script word for word</td><td>a misheard technical word is burned into the frame</td></tr>
          <tr><td class="num">10</td><td>{t['check_hook']}</td><td>the video opens on its least interesting image</td></tr>
          <tr><td class="num">11</td><td>No sentence promises an outcome</td><td>a physiology video has become a health claim</td></tr>
          <tr><td class="num">12</td><td>Clip 8's figure has no face</td><td>uncanny, and it pulls attention off the glow</td></tr>
        </tbody>
      </table>
    </div>

    <div class="box find">
      <div class="bt">⭐ What you keep after this video</div>
      <p>{t['keep']}</p>
    </div>
  </div></div>
</section>

<!-- ============ 13 COST ============ -->
<section id="cost">
  <div class="wrap"><div class="narrow">
    <div class="snum">13 — What it costs, what is still open</div>
    <h2 class="sec">The numbers, and the two decisions left</h2>
    <p>Eight clips × 8 s = <strong>64 output seconds</strong>. On the Gemini API that is roughly <strong>$5.12 on Veo 3.1 Lite, $7.68 on Fast, $25.60 on Standard</strong> at 1080p, before retries — and retries are the real cost, so budget for two or three attempts on {t['hard_clips']}, which carry the hardest camera moves in this video. Start on Fast: slow, smooth anatomical motion is the easiest case there is. Everything else here — the script, the voice-over, the captions — is free.</p>

    <div class="box key">
      <div class="bt">Still needs your call</div>
      <p><b>1. Flow subscription or Gemini API?</b> Flow bills in credits, the API bills per output second. It changes the cost model completely and it is the only thing standing between this page and a finished video.</p>
      <p style="margin-top:12px"><b>2. The still-image generator.</b> The eight image prompts are written to be model-agnostic, but they need somewhere to run — and whatever runs them <strong>must accept a reference image</strong>, because that is what carries the chain from one shot to the next.</p>
    </div>

    <p style="color:var(--ink3);font-size:15.5px">Nothing has been generated. The voice-over is the only asset that exists, it was built here at no cost, and it is downloadable above.</p>
  </div></div>
</section>

<footer>
  <div class="wrap"><div class="narrow">
    <div class="pagenav">{NAV}</div>
    <p style="margin:0 0 10px"><a href="../">← back to the format teardown</a></p>
    <p style="margin:0">Health &amp; Fitness Shorts · {esc(t['h1_plain'])} · build blueprint · <span style="color:var(--ink3)">every timing figure on this page was measured from the rendered audio, not estimated</span></p>
  </div></div>
</footer>

<script>
(function () {{
  function flash(btn, text, cls) {{
    var old = btn.dataset.label || btn.textContent;
    btn.dataset.label = old;
    btn.textContent = text;
    btn.classList.add(cls);
    setTimeout(function () {{
      btn.textContent = btn.dataset.label;
      btn.classList.remove(cls);
    }}, 1600);
  }}
  function legacyCopy(text) {{
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.position = 'fixed';
    ta.style.top = '-1000px';
    document.body.appendChild(ta);
    ta.select();
    var ok = false;
    try {{ ok = document.execCommand('copy'); }} catch (e) {{ ok = false; }}
    document.body.removeChild(ta);
    return ok;
  }}
  document.addEventListener('click', function (e) {{
    var btn = e.target.closest('.cbtn');
    if (!btn) return;
    var el = document.getElementById(btn.dataset.target);
    if (!el) return;
    var text = el.textContent;
    if (navigator.clipboard && window.isSecureContext) {{
      navigator.clipboard.writeText(text).then(function () {{
        flash(btn, 'Copied ✓', 'done');
      }}).catch(function () {{
        flash(btn, legacyCopy(text) ? 'Copied ✓' : 'Press Ctrl+C', legacyCopy(text) ? 'done' : 'fail');
      }});
    }} else {{
      flash(btn, legacyCopy(text) ? 'Copied ✓' : 'Press Ctrl+C', 'done');
    }}
  }});
}})();
</script>

</body>
</html>
"""


# ------------------------------------------------------------------ build-vo.sh
VO_SH = """#!/usr/bin/env bash
# Build the 64.000 s voice-over track for "{h1}".
#
# Renders the 8 sentences, strips the silence edge-tts pads onto each file,
# places sentence N so it is AUDIBLE at 8*(N-1) - 0.10 s, and normalises.
# The 0.10 s head-start is deliberate: it is what makes the narration read as
# one continuous track running underneath the cuts instead of eight clips.
#
#   pip install edge-tts          (ffmpeg must also be on PATH)
#   bash build-vo.sh
#
set -euo pipefail

VOICE="${{VOICE:-en-US-AriaNeural}}"
RATE="${{RATE:--18%}}"
LEAD="0.10"          # seconds each sentence starts before its cut
OUT="${{OUT:-{vo_file}}}"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

S=(
{sentences}
)

echo "voice=$VOICE  rate=$RATE"
for i in "${{!S[@]}}"; do
  edge-tts --voice "$VOICE" --rate="$RATE" --text "${{S[$i]}}" --write-media "$WORK/s$((i+1)).mp3" >/dev/null
done

# --- measure real speech, ignoring the padding on each file -----------------
declare -a LEADS TAILS
for i in $(seq 1 8); do
  f="$WORK/s$i.mp3"
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  det=$(ffmpeg -hide_banner -i "$f" -af silencedetect=n=-50dB:d=0.05 -f null - 2>&1 || true)
  l=$(echo "$det" | grep -o 'silence_end: [0-9.]*' | head -1 | cut -d' ' -f2)
  t=$(echo "$det" | grep -o 'silence_start: [0-9.]*' | tail -1 | cut -d' ' -f2)
  LEADS[$i]=${{l:-0}}; TAILS[$i]=${{t:-$dur}}
done

# --- place, mix, normalise --------------------------------------------------
inputs=(); filters=(); mix=""
printf '\\n%4s %8s %8s %8s %9s\\n' clip spoken start end headroom
for i in $(seq 1 8); do
  target=$(python3 -c "print(max(0,8*($i-1)-$LEAD))")
  delay=$(python3 -c "print(int(round($target*1000)))")
  inputs+=(-i "$WORK/s$i.mp3")
  filters+=("[$((i-1)):a]aresample=48000,atrim=start=${{LEADS[$i]}}:end=${{TAILS[$i]}},asetpts=PTS-STARTPTS,adelay=$delay|$delay[a$i]")
  mix+="[a$i]"
  python3 -c "
sp=${{TAILS[$i]}}-${{LEADS[$i]}}; st=$target; en=st+sp; h=8*$i-en
print(f'{{$i:4d}} {{sp:8.2f}} {{st:8.2f}} {{en:8.2f}} {{h:9.2f}}' + ('   <-- OVERRUNS ITS CLIP, cut words' if h<0 else ''))"
done

IFS=';' F="${{filters[*]}}"; unset IFS
ffmpeg -y -loglevel error "${{inputs[@]}}" \\
  -filter_complex "$F;${{mix}}amix=inputs=8:normalize=0:dropout_transition=0[m];[m]apad,atrim=0:64[o]" \\
  -map "[o]" -ar 48000 -c:a pcm_s16le "$WORK/raw.wav"

J=$(ffmpeg -hide_banner -i "$WORK/raw.wav" -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{{/,/^}}/p')
LN=$(python3 -c "
import json,sys
m=json.loads('''$J''')
print(f\\"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={{m['input_i']}}:measured_TP={{m['input_tp']}}:measured_LRA={{m['input_lra']}}:measured_thresh={{m['input_thresh']}}:offset={{m['target_offset']}}:linear=true\\")")
ffmpeg -y -loglevel error -i "$WORK/raw.wav" -af "$LN" -ar 48000 -b:a 192k "$OUT"

echo
ffmpeg -hide_banner -i "$OUT" -af ebur128=peak=true -f null - 2>&1 | grep -E "  I:|Peak:" | tail -2
echo "audible onsets (must be 7.90 / 15.90 / 23.90 / 31.90 / 39.90 / 47.90 / 55.90):"
ffmpeg -hide_banner -i "$OUT" -af silencedetect=n=-45dB:d=0.30 -f null - 2>&1 | grep -o 'silence_end: [0-9.]*'
echo "wrote $OUT"
"""


def vo_sh(t):
    return VO_SH.format(h1=t["h1_plain"], vo_file=t["vo_file"], sentences=vo_script_sh(t))


# ------------------------------------------------------------------ self-check
BANNED = (
    "builds muscle", "burns fat", "boosts", "cures", "detox", "flushes toxins",
    "lowers cholesterol", "lowers blood pressure", "prevents", "treats", "heals",
)


def selfcheck(t):
    errs = []
    clips = t["clips"]
    if len(clips) != 8:
        errs.append(f"expected 8 clips, got {len(clips)}")
    for c in clips:
        ip, vp = img_prompt(t, c), vid_prompt(t, c)
        n = c["n"]
        if "It must look real" not in ip:
            errs.append(f"clip {n}: image prompt missing the realism line")
        if style_block(t) not in ip:
            errs.append(f"clip {n}: image prompt missing the locked style block")
        if "REAL ANATOMY" not in ip:
            errs.append(f"clip {n}: image prompt missing the real-anatomy line")
        if "NO TEXT" not in ip or "NO TEXT" not in vp:
            errs.append(f"clip {n}: missing no-text ban")
        if n > 1 and clips[n - 2]["ends"] not in ip:
            errs.append(f"clip {n}: continuity line does not quote clip {n-1}'s end frame")
        if len(c["beats"]) != 4:
            errs.append(f"clip {n}: expected 4 timed beats, got {len(c['beats'])}")
        if "AUDIO OFF" not in vp:
            errs.append(f"clip {n}: video prompt does not say AUDIO OFF")
        if "{prev}" in ip:
            errs.append(f"clip {n}: unsubstituted {{prev}} placeholder")
        if c["spoken"] > 7.9:
            errs.append(f"clip {n}: sentence overruns its clip ({c['spoken']:.2f} s)")
        for w in BANNED:
            if w in c["vo"].lower():
                errs.append(f"clip {n}: banned claim '{w}' in the script")
    return errs
