#!/usr/bin/env python3
"""
Builds every video page in the series from its topic module.

    python3 build_pages.py                 # all five
    python3 build_pages.py egg water       # just these

For each topic it writes docs/<slug>/index.html and docs/<slug>/build-vo.sh,
runs the self-check on the prompt data, and then re-reads the HTML it just
wrote to verify the continuity chain in the RENDERED page — not in the source
data, which is the only version that proves what the reader actually gets.
"""
import html
import pathlib
import re
import subprocess
import sys
import importlib.util

import pagegen

ROOT = pathlib.Path(__file__).parent
TOPICS = ["egg", "coffee", "water", "oats", "spinach"]


def load(slug):
    spec = importlib.util.spec_from_file_location(f"topic_{slug}", ROOT / "topics" / f"{slug}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.TOPIC


def verify_rendered_chain(t, page):
    """Read the emitted HTML back and confirm every handoff is quoted verbatim."""
    errs = []
    text = html.unescape(re.sub(r"<[^>]+>", " ", page))
    text = re.sub(r"\s+", " ", text)
    # every prompt appears twice in the page — once on its clip card, once inside
    # the bulk copy-all block — so both copies have to carry it, or one of the two
    # things the reader can copy is wrong.
    for c in t["clips"][1:]:
        prev = t["clips"][c["n"] - 2]["ends"].rstrip(".")
        needle = re.sub(r"\s+", " ", html.unescape(prev))
        n = text.count(f"PREVIOUS SHOT ENDED: {needle}")
        if n < 2:
            errs.append(f"clip {c['n']}: end frame of clip {c['n']-1} appears {n} time(s) in the rendered page, expected 2")
    for c in t["clips"]:
        n = text.count(re.sub(r"\s+", " ", html.unescape(c["real"]))[:60])
        if n < 2:
            errs.append(f"clip {c['n']}: REAL ANATOMY text appears {n} time(s) in the rendered page, expected 2")
    return errs


def measure_vo(path):
    """Read the finished MP3 and return what it actually is: duration, loudness,
    true peak, and where each of the eight sentences is audible. The page prints
    these, so they can never drift from the file the reader downloads."""
    if not path.exists():
        return None, []
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                "-of", "csv=p=0", str(path)], capture_output=True, text=True).stdout)
    eb = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(path), "-af", "ebur128=peak=true",
                         "-f", "null", "-"], capture_output=True, text=True).stderr
    lufs = re.findall(r"I:\s+(-?[0-9.]+) LUFS", eb)
    peak = re.findall(r"Peak:\s+(-?[0-9.]+) dBFS", eb)
    det = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(path), "-af",
                          "silencedetect=n=-45dB:d=0.30", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    ends = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", det)]
    starts = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", det)]
    onsets = ([0.0] + ends)[:8]
    spoken = []
    for on in onsets:
        nxt = [x for x in starts if x > on + 0.2]
        spoken.append(round((nxt[0] if nxt else dur) - on, 2))
    stats = {"dur": round(dur, 2),
             "lufs": ("−" + lufs[-1].lstrip("-")) if lufs else "?",
             "tp": ("−" + peak[-1].lstrip("-")) if peak else "?",
             "onsets": [round(o, 2) for o in onsets]}
    return stats, spoken


def build(slug):
    t = load(slug)
    out = ROOT / "docs" / slug
    out.mkdir(parents=True, exist_ok=True)

    errs = pagegen.selfcheck(t)

    # the page's timing numbers must match the audio file it links to
    vo_path = out / t["vo_file"]
    stats, spoken = measure_vo(vo_path)
    if stats is None:
        errs.append(f"{t['vo_file']} has not been rendered — run build-vo.sh in docs/{slug}/")
    else:
        t["vo_stats"] = stats
        for i, c in enumerate(t["clips"]):
            if abs(spoken[i] - c["spoken"]) > 0.06:
                errs.append(f"clip {c['n']}: page says {c['spoken']:.2f} s spoken, the MP3 measures {spoken[i]:.2f} s")
            want = pagegen.start_of(c)
            if abs(stats["onsets"][i] - want) > 0.05:
                errs.append(f"clip {c['n']}: sentence is audible at {stats['onsets'][i]:.2f} s, should be {want:.2f} s")
            if pagegen.headroom(c) < 0:
                errs.append(f"clip {c['n']}: sentence overruns its clip")

    page = pagegen.render(t)
    (out / "index.html").write_text(page, encoding="utf-8")
    (out / "build-vo.sh").write_text(pagegen.vo_sh(t), encoding="utf-8")
    (out / "build-vo.sh").chmod(0o755)
    errs += verify_rendered_chain(t, page)

    imgw = [len(pagegen.img_prompt(t, c).split()) for c in t["clips"]]
    vidw = [len(pagegen.vid_prompt(t, c).split()) for c in t["clips"]]
    speech = sum(c["spoken"] for c in t["clips"])
    print(f"\n{slug:8s} {len(page):>8,} bytes  ·  image {min(imgw)}–{max(imgw)}w  video {min(vidw)}–{max(vidw)}w  "
          f"·  speech {speech:.2f} s  ·  tightest headroom {min(pagegen.headroom(c) for c in t['clips']):.2f} s")
    print(f"{'':8s} SELF-CHECK: " + ("PASS" if not errs else "FAIL\n  " + "\n  ".join(errs)))
    return not errs


if __name__ == "__main__":
    wanted = sys.argv[1:] or TOPICS
    ok = all([build(s) for s in wanted])
    print("\nALL PAGES:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
