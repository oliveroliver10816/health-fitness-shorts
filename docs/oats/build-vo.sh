#!/usr/bin/env bash
# Build the 64.000 s voice-over track for "What happens when you eat oats".
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

VOICE="${VOICE:-en-US-AriaNeural}"
RATE="${RATE:--18%}"
LEAD="0.10"          # seconds each sentence starts before its cut
OUT="${OUT:-vo-oats-64s.mp3}"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

S=(
"Every morning when you eat oats, your teeth break the soft flakes apart in your mouth."
"Your esophagus moves the warm spoonful down in slow waves, into your stomach below."
"The fibre soaks up water, and the whole mass thickens into a slow, heavy gel."
"That gel coats the wall of your small intestine, and everything moving through it slows down."
"Sugars cross the lining gradually now, a few at a time, through the tiny folds."
"Your blood receives them as a slow, steady rise instead of one sudden surge."
"Further along, the fibre that survived becomes food for the bacteria living in your gut."
"Your body is running on a steady supply instead of a spike, hour after hour."
)

echo "voice=$VOICE  rate=$RATE"
for i in "${!S[@]}"; do
  edge-tts --voice "$VOICE" --rate="$RATE" --text "${S[$i]}" --write-media "$WORK/s$((i+1)).mp3" >/dev/null
done

# --- measure real speech, ignoring the padding on each file -----------------
declare -a LEADS TAILS
for i in $(seq 1 8); do
  f="$WORK/s$i.mp3"
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  det=$(ffmpeg -hide_banner -i "$f" -af silencedetect=n=-50dB:d=0.05 -f null - 2>&1 || true)
  l=$(echo "$det" | grep -o 'silence_end: [0-9.]*' | head -1 | cut -d' ' -f2)
  t=$(echo "$det" | grep -o 'silence_start: [0-9.]*' | tail -1 | cut -d' ' -f2)
  LEADS[$i]=${l:-0}; TAILS[$i]=${t:-$dur}
done

# --- place, mix, normalise --------------------------------------------------
inputs=(); filters=(); mix=""
printf '\n%4s %8s %8s %8s %9s\n' clip spoken start end headroom
for i in $(seq 1 8); do
  target=$(python3 -c "print(max(0,8*($i-1)-$LEAD))")
  delay=$(python3 -c "print(int(round($target*1000)))")
  inputs+=(-i "$WORK/s$i.mp3")
  filters+=("[$((i-1)):a]aresample=48000,atrim=start=${LEADS[$i]}:end=${TAILS[$i]},asetpts=PTS-STARTPTS,adelay=$delay|$delay[a$i]")
  mix+="[a$i]"
  python3 -c "
sp=${TAILS[$i]}-${LEADS[$i]}; st=$target; en=st+sp; h=8*$i-en
print(f'{$i:4d} {sp:8.2f} {st:8.2f} {en:8.2f} {h:9.2f}' + ('   <-- OVERRUNS ITS CLIP, cut words' if h<0 else ''))"
done

IFS=';' F="${filters[*]}"; unset IFS
ffmpeg -y -loglevel error "${inputs[@]}" \
  -filter_complex "$F;${mix}amix=inputs=8:normalize=0:dropout_transition=0[m];[m]apad,atrim=0:64[o]" \
  -map "[o]" -ar 48000 -c:a pcm_s16le "$WORK/raw.wav"

J=$(ffmpeg -hide_banner -i "$WORK/raw.wav" -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
LN=$(python3 -c "
import json,sys
m=json.loads('''$J''')
print(f\"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true\")")
ffmpeg -y -loglevel error -i "$WORK/raw.wav" -af "$LN" -ar 48000 -b:a 192k "$OUT"

echo
ffmpeg -hide_banner -i "$OUT" -af ebur128=peak=true -f null - 2>&1 | grep -E "  I:|Peak:" | tail -2
echo "audible onsets (must be 7.90 / 15.90 / 23.90 / 31.90 / 39.90 / 47.90 / 55.90):"
ffmpeg -hide_banner -i "$OUT" -af silencedetect=n=-45dB:d=0.30 -f null - 2>&1 | grep -o 'silence_end: [0-9.]*'
echo "wrote $OUT"
