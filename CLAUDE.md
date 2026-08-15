# health-fitness-shorts

**What this is:** the "health and fitness chat for shorts" project. Bob sends short-form
health/fitness videos; we tear them down and rebuild the format with his own tools (Veo 3).

**Status 2026-08-15: ALL FIVE VIDEOS ARE NOW BUILT OUT IN FULL.** Each topic has its own page with the
complete script as one paste-ready block, a **rendered voice-over MP3**, 8 image prompts, 8
image-to-video prompts, the timeline and the checklist. Nothing generated on a video model, $0 spent.

- egg · https://oliveroliver10816.github.io/health-fitness-shorts/egg/
- coffee · .../coffee/ · water · .../water/ · oats · .../oats/ · spinach · .../spinach/
- The main page now carries **a link button per topic** (a 5-tile grid in section 08, a button on every
  topic card, links in the side-by-side table, and the footer index).

- **LIVE deliverable:** https://oliveroliver10816.github.io/health-fitness-shorts/
- **Repo:** `oliveroliver10816/health-fitness-shorts` (public, Pages from `/docs`, page is `noindex`)
- Source video is **gitignored** (153 MB). Re-download with
  `gdown 1bcqFIFH9TjYEGDwaHrjA3WMwklHEGap9 -O video/source.mp4`
  (⚠ this `gdown` build has **no `--fuzzy`** — pass the bare file ID).
- `video/transcript.json` IS committed (Groq whisper-large-v3, word-level timestamps).

## Video 1 — "What happens when you eat Greek yogurt" (64 s)

### ⭐ The finding that decides the whole format
**8 clips × exactly 8.000 s.** Hard cuts at 8/16/24/32/40/48/56 s (frames 239→240 etc.) — no
dissolves, no hidden cuts inside any block. An 8th cut at 64.000 s drops to **3 black frames**.
The VO is **exactly 8 sentences, sentence N carrying clip N**. **8.000 s is Veo 3/3.1's native
max clip length**, so the format is built around the generator's constraint. (Consistent with
Veo; not proof of model — Kling 5/10 s, Runway 5/10 s, Hailuo 6/10 s, Sora 5–20 s.)

⚠ **Do NOT say "every sentence begins and ends inside its own clip" — that is false and I
published it once.** Six of the eight sentences begin **0.04–0.16 s before** their clip does.
That overlap is the *point*: it's what proves the narration is one continuous track.

⇒ **Answer to Bob's question: 8 image prompts + 8 image-to-video prompts = 16 per 64 s video.**

### ⭐ The reusable rule
**18.6 words per sentence at 140 wpm fills an 8 s clip with ~0.4 s to spare** (measured:
16–22 words, 6.84–8.02 s spoken). Write every line to 16–20 words and picture and voice stay
locked with zero editing. That single number is what makes the format mechanical.

### Measured facts
- 1080×1920, 30 fps container, H.264, **19.1 Mbps / 146 MB** (≈3× what platforms keep).
- **`encoder = clipchamp.com`** — assembled in Microsoft Clipchamp (free, browser).
- **VO is a SEPARATE track, proven:** a word plays across **6 of the 7 cuts** ("After"
  7.88–8.12 s; "Tiny" at 32 s; "stronger" at 56 s) — only the 40 s cut is clean. LRA **2.6 LU**;
  channels within **0.0053 dB** RMS (mono in stereo). Per-clip audio cannot straddle a cut.
- ⚠ **No music bed at all** — clean gap interiors measure **−51.4 / −55.5 / −59.9 dB** vs
  −29 to −30 dB on speech; gap spectra carry no tonal content and gap level varies by 8 dB
  (a bed would be steady). Three gaps are over 1 s long.
- ⚠ **−26.7 LUFS integrated, −11.4 dBTP** — 12.7 LU under the ~−14 LUFS platform target.
  Platforms turn loud audio down; they don't reliably turn quiet audio up.
- ⚠ **Picture is NOT natively 30 fps:** **177–181 distinct frames per 8 s block (mean 178.8 of
  240)**, duplicates perfectly periodic at offsets **≡ 1, 5, 11, 14 (mod 15)** in all 8 blocks
  ⇒ **≈22.3 fps content in a 30 fps container**. Veo 3.1 outputs **24 fps**, so it was re-timed.
  **Lesson: set the edit timeline to 24 fps and never speed-adjust a clip to make it fit.**
- ~97 caption cards, 1–3 words each (typically 2), median 0.50 s, **on screen 94.5% of runtime**
  (1818/1923 frames; 5 blank runs totalling 3.5 s, all on audio pauses), yellow RGB(248,252,3)
  heavy-italic + black outline, median y = 77.5%. Auto-generated ⇒ **zero prompts**.
- ⚠ Watermark is a circular "HEALTH & FITNESS" logo **on an opaque white square**, not a
  transparent PNG — brightest object in frame on the dark shots.
- Imagery is AI-generated (strong inference): HUD panels are **blurred pseudo-interface with
  unreadable pseudo-text**, the classic can't-render-text tell.

### Veo 3.1 facts checked 2026-08-09 (Google's own docs)
4/6/8 s per generation · **24 fps** · 720p/1080p (+4K upscale) · 16:9 **and 9:16 native** ·
image-to-video (first + optional last frame) · reference "ingredients" images · extend +7 s
up to ~148 s. **Audio is ON by default — turn it OFF**, it fights the TTS narration.
Pricing per output second (Gemini API): **Lite $0.05/720p, $0.08/1080p · Fast $0.10/$0.12 ·
Standard $0.40**. ⇒ 64 s ≈ **$5.12 Lite / $7.68 Fast / $25.60 Standard**, before retries.
**Start on Fast** — anatomical renders are slow smooth motion, the easiest case for a fast tier.

### 🛑 Three settings that ruin the video
1. **`generateAudio: false`** (or mute every clip) — else two competing ambiences.
2. **Every prompt ends "no text, no captions, no on-screen writing, no logos"** — Veo renders
   type as garbled pseudo-letters. All type comes from the editor.
3. **Generate 9:16 natively**, never 16:9-then-crop.

### Why image-first (not text-to-video)
Approve the still before paying for motion; reuse the still as start frame + reference image to
keep ONE anatomical body across 8 separate generations; and framing (the clip-6 pull-back, the
clip-8 hero pose) is a drawing decision, not a promptable one.

⭐ **Clips 2, 5, 6, 8 (esophagus / villi / bloodstream / whole-body hero) are anatomically
identical whatever the subject is** — generate those stills once and reuse across the series.
That takes a new video from 8 image prompts to ~4 and makes the series look branded.

### Compliance line (why this format is safe)
Beats 1–7 are pure physiology; beat 8 only ever promises "healthy, energized, functioning at
its best". Nothing measurable, nothing falsifiable. **Never let an outcome claim ("fixes your
bloating") creep into the script** — that is the one line that would eventually cost the
account. The pressure runs the other way — an outcome claim is a better hook — so hold the line
**in the script prompt**, not in review.

## The five topics (added 2026-08-10, section 08 of the page)

Chosen on **format fit + distinct destination**, not on measured demand (no search-volume check
was run — that is stated on the page). Each decomposes into exactly 8 beats and reuses the four
anatomy keyframes ⇒ **4 new image prompts + 4 reused, every time.**

| # | Video | Ends at | Money shot | The claim that must never appear |
|---|-------|---------|-----------|----------------------------------|
| 1 | eat an **egg** | muscle fibre | acid unwinding the coiled protein | "builds muscle" / "burns fat" |
| 2 | drink **coffee** | the brain | molecule crossing the blood–brain barrier | "boosts metabolism", mg doses |
| 3 | drink **water** | the kidney | the kidney filtering | **"flushes toxins" / "detox"** |
| 4 | eat **oats** | blood sugar | dry flakes swelling into gel | **"lowers cholesterol"** |
| 5 | eat **spinach** | a blood vessel | the vessel wall opening | **"lowers blood pressure"** |

⭐ **Build the EGG first** — not the biggest topic (coffee is), but the only one that uses all
eight slots at full strength, so it forces keyframes **A esophagus · B villi · C bloodstream ·
D hero body** to be generated properly. Every later video inherits them. Coffee second.

⭐ **Reuse the keyframe, RE-RENDER the motion.** The four shared stills are start frames, not
finished clips — never paste the same rendered 8 s clip into two uploads (that is the
repetitive-content pattern). So the saving is **4 fewer image prompts per video, not 4 fewer
clips**; render cost per video is unchanged.

⚠ **"Skipping breakfast" and "10,000 steps" were CUT and the reason matters:** nothing enters the
body, so clips 1/2/3/5 lose their subject and all four reusable keyframes die. They need a second
skeleton (fasted-state / exertion), which is a separate build — park as series 2.

## 🔴 VIDEO 1 — the egg — PROMPTS REBUILT 2026-08-11 on Bob's feedback

**Bob rejected the first prompt set.** His three complaints, all correct, and what each one
actually was:

1. **"no continuity between the image prompts"** — the eight images shared no body, no light and
   no object. A golden helix in a void, crystalline shapes in blue space, villi with no gut around
   them. Eight art pieces, not one video.
2. **"there is no looks like realistic term"** — the prompts said *"photorealistic 3D medical
   visualisation"* once as a genre label and never once told the model the result had to **look
   real**.
3. **"it doesn't look like we are explaining how it affects the human body"** — shots 3–7 were
   abstract macro in black voids, and the script was third-person and clinical (*"a muscle fibre
   draws them in"*). No **you** anywhere.

⭐ **What the reference actually does, measured off its own frames (`video/source.mp4`):** it never
stays inside for long. **close → wide → close → wide**, and every wide shot is the whole human
figure — head with the skull and jaw muscles showing through the skin, then the whole torso with
the esophagus and stomach visible, then a full blue X-ray body, then the gold hero body. **That
rhythm is what stops a macro shot from reading as abstract**: two seconds ago you saw where in the
body you were. It is not a decorative choice, it is the thing that makes it legible.

**The rebuild (all four asks delivered):**
- ⭐ **Continuity is a MECHANISM, not wording.** Every clip declares an **END FRAME**; the next
  clip's image prompt **quotes that sentence back verbatim**. Both are emitted from one source
  (`build-egg-page.py`) so they cannot drift, and the chain is **verified against the rendered
  HTML**, not the source data. Plus the generation-time chain: export clip N's last frame → attach
  as reference image for still N+1.
- ⚠ **Two of the seven cuts are deliberately scale jumps, not handoffs** (into shot 4 and shot 8) —
  both are in the reference at the same points. They are still **match cuts** (shot 4 on the
  glowing point in the abdomen, shot 8 on the warm gold). Stated on the page, not hidden.
- **Realism line in all 8:** *"It must look real — like actual footage captured inside a living
  human body."*
- **Shots 2, 4, 6, 8 are whole-body**, and 4 and 6 travel between scales inside one take.
- **Script rewritten second-person + everyday opener** (*"Every day when you eat an egg…"*), every
  sentence naming a part of **your** body. **VO re-rendered:** −14.8 LUFS, onsets exact at
  7.90/15.90/…/55.90, ≥1.20 s headroom on all 8, 52.03 s of speech.
- **Video prompts are shot orders:** camera move with amplitude + speed, **four timed beats**
  (0–2/2–4/4–6/6–8 s), the lighting change, and the exact end frame.
- **Copy button on all 16 prompts** + 3 bulk (all image / all video / style block).

⭐ **New measured finding — a comma costs more than two words.** Cutting clip 3 to fit:
*"…each folded protein, and enzymes cut the strands into shorter pieces"* = 16 words, **7.78 s**.
Remove the comma and two words → **6.40 s**. **1.38 s saved and most of it was the comma.**

⚠ **Image prompts run 461–559 words.** Deliberate, but dilution is real — the page states the cut
order if a generation ignores something (SUBJECT → CONTINUITY once a reference image is attached →
the STYLE background sentence) and that **the realism line and the NO TEXT line are never cut.**

⚠ **Keyframe A changed meaning:** it was "esophagus tunnel", it is now **"torso with the esophagus
and stomach visible"** — the wide anchor shot. B villi, C bloodstream, D hero body unchanged.
Main page label updated to match.

**QA (browser, Playwright):** 19/19 copy buttons, **clipboard content read back and compared to
each `<pre>`**, 0 WCAG contrast failures (alpha-composited), 0 console errors, no horizontal
overflow desktop or mobile.

## Original entry — FULL BLUEPRINT BUILT 2026-08-10

**LIVE: https://oliveroliver10816.github.io/health-fitness-shorts/egg/** (`docs/egg/`, linked from
section 08 of the main page). Build order · 8-sentence script · voice-over **rendered, measured and
downloadable** · all 16 prompts paste-ready · the 8.000 s timeline · assembly · captions · music ·
export · pre-upload checklist.

**The VO is a real asset, not a spec:** `docs/egg/vo-egg-64s.mp3` — 64.03 s, −14.9 LUFS, TP −1.7,
en-US-AriaNeural at `--rate=-18%`. Every sentence verified audible at exactly **8×(N−1) − 0.10 s**
(7.90 / 15.90 / 23.90 / 31.90 / 39.90 / 47.90 / 55.90). `docs/egg/build-vo.sh` reproduces it from
scratch (free, no account) and prints per-clip headroom; it flags `OVERRUNS ITS CLIP`.

⭐ **Word count does NOT predict duration — measured.** Clip 6 = **20 words in 6.42 s**; clip 3 =
**16 words in 7.07 s**. Syllables + commas drive it. Write 16–20 words as a *first draft*, then
render and **measure**; rewrite anything over 7.5 s. **The longest sentence sets the pace ceiling
for the whole video** — at −25% clip 3 hits 7.73 s and there is only 0.37 s left.

⚠ **The trap that bit me here: measure the SPEECH, not the FILE.** edge-tts pads ~**0.20 s at the
front and ~0.90 s at the back** of every render. Placing by file length put every sentence ~0.1 s
**late** — the exact opposite of the intended head-start — and my first "over 8 s" readings were
padding, not speech. `build-vo.sh` strips lead/tail with `silencedetect` before placing.
See memory [[verify-the-artifact-not-the-wrapper]], [[tts-duration-is-pauses-not-words]].

⚠ **−14.0 LUFS is unreachable on an uncompressed voice track** — true-peak headroom runs out first,
so it lands at −14.9 (still **11.8 LU louder than the reference**). Light compression before
normalising closes the last 0.9 LU.

**Prompts:** each of the 8 cards carries a full paste-ready image prompt + its image-to-video prompt,
with the shared look and the no-text ban written into every one (nothing to append). Clips 2/5/6/8
**mint keyframes A/B/C/D**. Notes flag: clip 3 = the money shot (must read as *unwinding*), clip 4 =
the deliberate cold-blue break at the 24 s retention dip, clip 7 = the stillest shot on purpose,
clip 8 = **no facial features** (and it doubles as the 1 s hook at the front).

## Open — needs Bob
1. **Confirm the topic + order** (recommended: egg → coffee → water/oats/spinach). Optional
   half-hour: re-rank the five on real search volume + short-form saturation instead of judgement.
2. Veo route: **Flow subscription (credits)** or **Gemini API (per second)**? Changes the cost
   model entirely. **This is the only thing blocking a finished video.**
3. **Which still-image generator** — Veo's own reference-image route (one place) or a separate image
   model (approve stills before paying for motion, the cheaper order).
3. Confirm the 7 fixes are wanted (loudness −14 LUFS · music bed · 24 fps · transparent logo ·
   **hook in the first 1.5 s** · lower bitrate · end card). The hook is the only structural one.

## Traps hit here (don't repeat)
- `gdown --fuzzy` doesn't exist in this build — use the bare file ID.
- ffmpeg scene detection at 0.15 is useless on this content (particles/captions move) — the
  real cuts only separate cleanly at **0.35+**.
- md5-hashing frames to find duplicates **fails**: codec noise makes every frame byte-unique.
  Use **perceptual mean-absolute-difference** (or mpdecimate), not hashes.


## 2026-08-15 — THE OTHER FOUR TOPICS BUILT, AND THE IMAGE PROMPTS MADE MORE REAL

Bob's three asks, all delivered: **(1)** refine the image prompts so they look like the realistic
internal structure of a body, **and keep that for future use**; **(2)** the same complete work for the
other four topics — prompts, script, audio, everything; **(3)** the full script at the top of each page
so the audio can be made in any other tool; **(4)** link buttons from the topic list to each page.

### The build is now one machine, not one page
`build-egg-page.py` held the egg's data *and* its template. That does not scale to five, so:

| file | what it holds |
|---|---|
| `topics/<slug>.py` | one topic: meta, 8 clips, prompts, the continuity chain, measured timings |
| `pagegen.py` | the shared template, prompt assembly, the self-check |
| `build_pages.py` | the builder — writes `docs/<slug>/index.html` + `build-vo.sh`, verifies everything |
| `qa.py` | browser QA over all six pages |
| `build-egg-page.py` | **now a shim** that calls `build_pages.py egg`, so the old command still works and can no longer overwrite the page with the weaker prompt set |

### ⭐ How the realism was actually increased (this is the transferable part)
Not by adding adjectives. Two structural blocks, and the reason each exists:

1. **A dedicated `REALISM` block, separate from `STYLE`.** STYLE owned both the look and the realism
   before, and **when two paragraphs answer the same question the model picks one**. STYLE now owns
   palette and format only; REALISM owns *is it real* — endoscope reference, wet uneven asymmetric
   tissue, capillaries under translucent membrane, real lens behaviour, and an explicit **NOT** list
   (diagram, textbook illustration, cartoon, neon hologram, floating glass shapes, game render,
   glossy toy). Ends: *"If it looks designed, it is wrong — it has to look photographed."*
2. **A per-shot `REAL ANATOMY` line naming the structures that must be correct in that shot** — rugae
   and gastric pits, villi with a brush border and a central lacteal, sarcomere cross-banding,
   endothelium with tight junctions, the nephron, the three layers of an artery wall. This is what
   turns "looks realistic" from a wish into something checkable, and it caught a real trap:
   **the colon has no villi**, and a generator that has learned "intestine" will add them
   (`topics/oats.py`, clip 7 states it explicitly).
   Video prompts gained the matching **`REALISM IN MOTION`** block — real inertia, nothing snaps,
   pops, teleports or moves like a graphic.

⚠ Cost of this: image prompts went from **461–559 words to 647–794**. That is real dilution, so the
page states the cut order if a generation ignores something — SUBJECT first, then CONTINUITY once a
reference image is attached, then the STYLE background sentence — and that **REALISM, REAL ANATOMY and
NO TEXT are never the ones cut**.

### The four new scripts
Written second-person with an everyday opener, then **rendered and measured** — not estimated.
`docs/<slug>/vo-<slug>-64s.mp3`, all 64.03 s, −14.9/−15.0 LUFS, TP −1.7, onsets exact at
7.90/15.90/…/55.90. Tightest headroom per video: coffee 1.21 s · water 1.95 s · oats 2.18 s ·
spinach 2.17 s (egg 1.20 s).

⭐ **Every one was verified by an independent transcription** (Groq whisper-large-v3) against its own
script: **136/130/124/120/114 words, word-for-word**, the only differences being the transcriber's
US spelling (fiber/fibre, traveling/travelling). Byte size is identical across all five MP3s — that is
CBR at the same duration, not a copy; the md5s differ.

### What the build now proves before it will pass
`build_pages.py` fails if any of these is false, and **each check was verified capable of failing**:
- the page's per-sentence timings match the MP3 it links to (probed with ffprobe/silencedetect)
- each sentence is audible at exactly `8(N−1) − 0.10 s` (clip 1 at 0.00)
- every handoff sentence appears **twice** in the rendered HTML — once on the clip card, once in the
  bulk copy-all block. ⚠ The first version of this check only asked for "at least once", and a
  deliberately damaged page still passed, because the second copy covered for it.
- REAL ANATOMY present in both copies too; realism line, style block, NO TEXT, AUDIO OFF, 4 beats
- no banned claim in any sentence (list in `pagegen.BANNED`)

⚠ **A headroom bug this found:** headroom was computed as `8.10 − spoken` for every clip, but **clip 1
starts at 0.00, not −0.10**, so its headroom was overstated by 0.10 s on every page. Now
`8n − (start + spoken)`.

### QA (browser, Playwright — `qa.py`)
6 pages · **115 copy buttons, each verified by reading the clipboard back and comparing it to its own
`<pre>`** · contrast swept with alpha compositing · no horizontal overflow desktop or phone · 0 console
errors · all five tiles clicked and confirmed to land on the right page.
⚠ One real failure caught and fixed: water's clip-7 swatch `#b0674f` gave **4.41:1** under the dark
timeline numeral — now `#b97159` (5.01).

### Section 00 — the full script, first
Every page opens with the narration as one plain block with a copy button, so the audio can be made
anywhere, plus a second block with the timings, plus the four rules that keep an outside recording in
sync (one sentence per clip · under 8 s each · one continuous take · start 0.10 s early, never late).

### Per-topic compliance lines (unchanged, restated in each page's section 04)
egg "builds muscle/burns fat" · coffee "boosts metabolism"/mg/cups-per-day · water
**"flushes toxins"/"detox"** · oats **"lowers cholesterol"** · spinach **"lowers blood pressure"**.

### ⚠ Caught by the independent verifier, and fixed the same day
It checked the live pages and confirmed 40/40 image prompts carry REALISM + REAL ANATOMY, 35/35
handoffs quoted verbatim, 0/40 banned claims, all five MP3s aligned — and then found the thing the
build checks could not see: **the four shared-keyframe clips had near-identical MOTION prompts across
topics.** `egg` vp2 vs `oats` vp2 measured **99.74% identical** — one noun apart in ~460 words.

That is exactly the failure in memory [[write-each-clip-not-a-template]], and it quietly broke the
series' own rule: the still is shared on purpose, but if the shot order is shared too, re-rendering
produces the same clip and the reuse becomes repetition. **Fixed by giving clips 2, 5, 6 and 8 a
different camera move in every video** (`differentiate_motion.py`, kept in the repo as the record):

| clip | egg | coffee | water | oats | spinach |
|---|---|---|---|---|---|
| 2 swallow | constant pull-out | front-loaded pull-out, then holds | **locked off, no move at all** | push IN, tightening | holds 3 s, then pulls out |
| 5 villi | truck right → push in | straight push in | **cranes up** | **descends through the gel** | trucks left, decelerates to a stop |
| 6 blood | constant pull-out | pull-out + tilt up to the head | pull-out, decelerating, holds | holds 2 s, then one fixed rate | pull-out with a slow arc to three-quarter |
| 8 hero | push in, stops at 6 s | **tilt up** to the head | **completely static** | push in, stops at 4 s, holds 4 s | **pulls back**, opening space |

Worst cross-topic similarity on those four clips went **0.997 → 0.734**. Clip 4's dive was
differentiated too (spinach descends from above, oats decelerates as it enters the gel). The most
similar pair left is **0.857, egg/oats clip 1** — both are a mouth chewing, which is genuinely the
same action, and their image prompts differ.

⚠ Two other verifier findings, judged and **not** changed, with the reason:
- egg clip 4's beats run `0.0–1.5 / 1.5–4.0 / 4.0–6.0 / 6.0–8.0` instead of the 2-second grid every
  other clip uses. That is the hold-then-dive shot and the uneven split is the shot, not a slip.
- It flagged egg sentence 7 (*"use them as the raw material to rebuild their own structure"*) as
  “builds muscle” restated. It is not: **describing what a nutrient is used for is physiology;
  promising the viewer an outcome is the claim.** That exact wording is the line this project already
  set, and it stays.

### Still open — unchanged, and still the only blocker
1. Flow subscription or Gemini API. 2. Which still-image generator (it **must accept a reference
image** or the chain cannot run). 3. Confirm topic order — recommended egg first, because it mints
keyframes A–D that the other four reuse.
