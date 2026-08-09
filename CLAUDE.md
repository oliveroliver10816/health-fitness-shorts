# health-fitness-shorts

**What this is:** the "health and fitness chat for shorts" project. Bob sends short-form
health/fitness videos; we tear them down and rebuild the format with his own tools (Veo 3).

**Status 2026-08-09:** first teardown DELIVERED. Nothing built, nothing generated, $0 spent.

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

## Open — needs Bob
1. **Which topic first?** Shortlist on the page: water · egg · skipping breakfast (strongest
   hook) · coffee · 10,000 steps.
2. Veo route: **Flow subscription (credits)** or **Gemini API (per second)**? Changes the cost
   model entirely.
3. Confirm the 7 fixes are wanted (loudness −14 LUFS · music bed · 24 fps · transparent logo ·
   **hook in the first 1.5 s** · lower bitrate · end card). The hook is the only structural one.

## Traps hit here (don't repeat)
- `gdown --fuzzy` doesn't exist in this build — use the bare file ID.
- ffmpeg scene detection at 0.15 is useless on this content (particles/captions move) — the
  real cuts only separate cleanly at **0.35+**.
- md5-hashing frames to find duplicates **fails**: codec noise makes every frame byte-unique.
  Use **perceptual mean-absolute-difference** (or mpdecimate), not hashes.
