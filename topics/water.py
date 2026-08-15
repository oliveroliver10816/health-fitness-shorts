"""Video 3 — "What happens when you drink a glass of water."

Beats follow the map published in section 08 of the main teardown page.
Timings are measured from the rendered voice-over, not estimated.
"""

TOPIC = dict(
    slug="water",
    video_no=3,
    lane="fluid lane",
    emoji="💧",
    accent="#5fd0ff",
    glow="rgba(95,208,255,.14)",
    h1_plain="What happens when you drink a glass of water",
    title_html="What happens<br>when you drink<br><em>water.</em>",
    sub=("The safest topic in the series and the widest possible audience — nothing to sell and nothing to argue "
         "with. Full script, <strong>voice-over already rendered and measured</strong>, and all 16 prompts written "
         "out — one unbroken journey through one body, every shot handing its last frame to the next one."),
    palette=("warm flesh pink and deep red tissue, clear colourless water reading as pale blue-white highlights and "
             "refraction, cool cyan-teal rim light, dark navy background falling to black, with two or three very "
             "soft out-of-focus blue holographic panels far behind the subject blurred into pure glow"),
    vo_file="vo-water-64s.mp3",
    kf_chip="Reuses keyframes <b>A–D</b>",
    locks="the way clear water reads on camera",
    chain_break=("Two of the seven cuts are scale jumps rather than continuous handoffs: <strong>into shot 4</strong> "
                 "(the pyloric opening, out to the whole body) and <strong>into shot 8</strong> (a single kidney "
                 "filter, out to the whole body). Both sit where the egg video puts them, and both are doing a job — "
                 "shot 4 re-anchors the viewer at the 24-second retention dip, shot 8 is the payoff. They are still "
                 "matched: shot 4 opens on the glow low in the abdomen, exactly where shot 3 just was, and shot 8 "
                 "matches on the cool blue light coming out of shot 7."),
    compliance=("Sentences 1–7 describe only what happens. Sentence 8 says every cell is working in the fluid it "
                "needs — a description of a state, not a promise. <strong>Never write “flushes out toxins”, "
                "“detoxes”, “cleanses”, a glasses-per-day target, or anything about weight.</strong> Toxin language "
                "is the single most common way a water video turns into a health claim, and on this subject it is "
                "the easiest sentence in the world to write by accident. Nothing is being flushed anywhere in this "
                "script: the kidney <em>measures and decides</em>, and the sentence stops there."),
    caption_words="“esophagus”, “villi” and “kidneys”",
    hook_step=("Copy the first second of clip 7 — the kidney filter, lit warm — to the very front of the timeline, "
               "then hard-cut to the glass at the lips. Nobody expects a water video to open inside an organ. The "
               "voice-over does not move: it still starts at 0:00 and now plays over the filter."),
    check_hook="The first second is the kidney filter, not the glass",
    kf_box_title="Four of these eight stills are already made",
    kf_box=("Clips 2, 5, 6 and 8 are anatomy, not water — the torso with the esophagus and stomach, the field of "
            "villi, the vessel network, the whole body. They are <strong>keyframes A, B, C and D</strong> from the "
            "egg video and they drop straight in as the start frames here. This video needs four new stills: the "
            "glass at the lips, the stomach passing it through, water and salt crossing together, and the kidney."),
    keep=("One new permanent asset — <strong>the kidney filter still from clip 7</strong>, the only organ in the "
          "series this video visits — and a third use of keyframes A to D. Water is also the cheapest video to "
          "make in the whole run: nothing has to be broken down, so no shot needs a transformation to read."),
    hard_clips="clips 4, 6 and 7",
    prev=("coffee", "Coffee"),
    next=("oats", "Oats"),
)

CLIPS = [
    dict(
        n=1, name="The first mouthful", where="Mouth · head close-up",
        tc="0:00.000 → 0:08.000", kf=("new", "new still"),
        colour="#6fb8d9", palette="warm flesh + clear water · medium close-up",
        vo="Every time you drink a glass of water, the first cool mouthful crosses your lips and tongue.",
        spoken=5.99,
        ends="Mouth closed, a clear pool of water gathered in the centre of the mouth above the tongue, and the surface of it settling still. The glass has left the frame.",
        img=[
            ("SHOT 1 OF 8 — THE FIRST MOUTHFUL.", "A hyper-realistic anatomical human head in three-quarter profile, taking the first mouthful from a plain glass of water."),
            ("SCENE", "An adult human head and shoulders turned three-quarters toward camera against a dark navy background. The skin is semi-transparent, so the skull, the jaw and cheek muscles, the tongue and the whole row of teeth read clearly through it — the look of a high-end medical visualisation figure. The face is calm and neutral, eyes open, no expression. A plain clear drinking glass is tilted at the lower lip and water is crossing that lip and running onto the front of the tongue, catching the light in bright moving highlights as it moves. Below the jaw, through the neck, the throat and the top of the esophagus are visible as a pale ribbed tube running down behind the windpipe."),
            ("CAMERA", "Medium close-up: the frame runs from the top of the skull down to the collarbones. Camera at mouth height, level with the face, 50 mm equivalent lens, shallow depth of field with the lips, tongue and water razor sharp and the back of the head falling soft."),
            ("SUBJECT — the water, stage 1 of 8", "Clear, colourless water. Because it has no colour of its own it has to be read entirely through behaviour: bright specular highlights on its moving surface, refraction bending what is behind it, a visible meniscus where it meets the glass, and a cool pale blue cast in its depth. It must never look like milk, syrup or any tinted liquid."),
            ("LIGHT", "One warm key light from the upper left catching every wet highlight on the lip, the tongue and the surface of the water. A cool cyan rim light along the jawline and cheekbone separating the head from the background, and a second cool highlight running along the rim of the glass. Deep shadow behind the head."),
            ("CONTINUITY", "This is the opening shot and it locks the look for the whole video: this exact figure, this exact skin translucency, this way of rendering clear water, this warm-key-plus-cyan-rim lighting and this dark navy background appear in all eight shots. Nothing about the look changes after this frame."),
        ],
        real="the papillae covering the surface of the tongue, the pink gum margin around each tooth, the wet mucosa of the inner cheek and lip, the masseter and temporalis muscles under the skin, and the epiglottis and the opening of the esophagus sitting behind the base of the tongue.",
        cam="Push in, small amplitude, slow speed — the frame tightens by roughly 15% across the full eight seconds, travelling straight in toward the mouth and staying level at mouth height. Motorised smoothness, constant speed, no handheld shake, no rotation, no whip pan.",
        beats=[
            ("0.0 – 2.0 s", "The glass tilts a little further and water crosses the lower lip in a smooth unbroken stream, highlights running along its surface."),
            ("2.0 – 4.0 s", "The water spreads across the tongue and gathers, its surface moving and catching the light. The glass withdraws out of frame to the left."),
            ("4.0 – 6.0 s", "The lips close. The pool settles into the centre of the mouth, its surface rocking once and then flattening."),
            ("6.0 – 8.0 s", "Everything comes to rest: a clear still pool held above the tongue, the tongue beginning to rise underneath it."),
        ],
        light="Unchanged throughout — warm key upper left, cyan rim on the jaw, a moving highlight travelling across the water's surface as it settles. No other lighting change in this clip.",
        cons="One motion only: the mouthful. The head does not turn, nod, tilt, blink hard or speak. Nothing else in the frame moves. The water must move like water — heavy, coherent, obeying gravity — never like gel, smoke or particles.",
        note=("Note", "The hardest still in this video, and it is worth re-rolling until it is right. <strong>Clear water is defined entirely by highlight, refraction and how it moves</strong> — a generator that renders it as a pale opaque liquid has produced milk, and the whole video's subject is wrong from the first frame. Check the still for a visible meniscus and for the tongue distorting where it is seen through the water."),
    ),
    dict(
        n=2, name="The swallow", where="Throat → stomach · torso wide",
        tc="0:08.000 → 0:16.000", kf=("reuse", "reuse keyframe A"),
        colour="#b9846f", palette="warm flesh + cyan rim · medium wide",
        vo="Your esophagus carries it down in one quick wave, straight into your waiting stomach.",
        spoken=5.43,
        ends="The whole upper body is in frame. The last of the water is passing the ring of muscle at the stomach entrance, and a clear pool is lying in the bottom of the empty stomach below.",
        img=[
            ("SHOT 2 OF 8 — THE SWALLOW.", "The same figure, one step wider: head, neck and upper chest, with the esophagus visible running down inside the body."),
            ("SCENE", "The same adult anatomical figure as shot 1, at the same three-quarter angle, now framed wider so the head, the whole neck and the upper chest are in view. Through the semi-transparent skin and the pale ribcage, the esophagus runs from the back of the throat down the centre of the chest, behind the heart, as a soft ribbed muscular tube. Clear water is entering the top of that tube and running down it as a fast bright column, wetting the walls and catching the light. The ring muscles of the esophagus read as evenly spaced bands along its length. A faint cool cyan glow runs down inside the tube ahead of the water, showing the direction of travel as a soft travelling light."),
            ("CAMERA", "Medium wide: the frame runs from just above the head down to the bottom of the ribcage. Camera level, 35 mm equivalent lens, moderate depth of field with the esophagus and the water sharp and the shoulders falling slightly soft."),
            ("SUBJECT — the water, stage 2 of 8", "A fast-moving clear column, brighter and faster than any solid food would be. Water is the quickest thing that travels this tube, and the speed is the point — it barely needs the muscle wave to get down."),
            ("LIGHT", "Warm key from the upper left across the chest. Cool cyan rim down the left edge of the neck and shoulder. The esophagus glowing very faintly from within along its length, and the water carrying bright moving highlights."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is that same figure at that same angle, one step wider, with that same mouthful now entering the top of the esophagus. Same skin, same light, same background, same water."),
        ],
        real="the esophagus as a muscular tube lying behind the trachea and in front of the spine, its wall built from an inner circular and an outer longitudinal muscle layer, the aortic arch and the left main bronchus crossing in front of it, the diaphragm it passes through, and the lower esophageal sphincter where it opens into the stomach.",
        cam="Pull out, large amplitude, slow constant speed — the camera retreats and cranes down very slightly, so that by 8.0 s the frame holds the whole upper body from the top of the head to just below the stomach. One continuous move, never stopping, never speeding up. No shake, no rotation.",
        beats=[
            ("0.0 – 2.0 s", "The throat contracts once and the water drops into the top of the esophagus, running downward immediately. The camera begins its pull-out."),
            ("2.0 – 4.0 s", "Rings of muscle contract in sequence behind it, but the water is already ahead of them and nearly halfway down. The pull-out reveals the collarbones and the top of the ribcage."),
            ("4.0 – 6.0 s", "The column passes behind the heart, which beats steadily twice in this window. The pull-out reveals the whole ribcage and the lungs."),
            ("6.0 – 8.0 s", "The stomach comes into frame below the ribs, pink and empty. The ring of muscle at its entrance opens and the water pours through, gathering into a clear pool at the bottom."),
        ],
        light="The faint cyan glow inside the esophagus travels down the tube just ahead of the water, and fades out as the shot ends. Key and rim unchanged.",
        cons="One motion: the swallow, as a single continuous fall and squeeze that never stops or restarts. The figure does not move, turn or gesture; the only other movement in frame is the heartbeat.",
        note=("Note · reuse keyframe A", "This is <strong>keyframe A</strong> from the egg video — the torso with the esophagus and stomach visible. Use the same approved still as the start frame; the only difference is what travels down the tube, and here it should visibly travel <em>faster</em> than the egg's bolus. <strong>Re-run the motion prompt — never paste the egg video's rendered clip into this one.</strong>"),
    ),
    dict(
        n=3, name="Straight through the stomach", where="Stomach · cutaway → pylorus",
        tc="0:16.000 → 0:24.000", kf=("new", "new still"),
        colour="#9fb0b8", palette="cool pale grey-blue · close → macro",
        vo="Your stomach has nothing to break apart here, so the water simply passes through it.",
        spoken=5.44,
        ends="Extreme close on the round opening at the far end of the stomach, held wide open, with clear water running steadily through it into the first bend of the small intestine beyond.",
        img=[
            ("SHOT 3 OF 8 — STRAIGHT THROUGH THE STOMACH.", "The stomach, seen close inside the body, its near wall cut away so the inside is visible."),
            ("SCENE", "The same figure, now framed on the abdomen. The stomach fills most of the frame, sitting under the ribs, with the lower ribcage and the outline of the torso still visible around the edges of frame so it stays obvious that we are inside a human body. The near wall of the stomach is opened in a clean medical cutaway, revealing the interior: deep folded ridges of stomach lining in wet red-brown, and clear water lying across the floor of it and running along the valleys between the folds toward the far end. Nothing is churning and nothing is breaking apart — the water is simply passing over the surface. At the far end of the stomach the round pyloric opening is visible, relaxed and open, with water already running through it."),
            ("CAMERA", "Medium close-up on the stomach, slightly high angle looking down into the cutaway, 40 mm equivalent lens, shallow depth of field with the near folds and the running water sharp and the far wall soft behind them."),
            ("SUBJECT — the water, stage 3 of 8", "The same clear water, moving across the lining without changing at all. This is the only subject in the series that arrives at the stomach and leaves it exactly as it came in, and that is what this shot has to show."),
            ("LIGHT", "Cool light this time, not warm: a pale blue-white key from above catching the moving surface of the water, with the red-brown lining lit dimly beneath it. Cyan rim light along the cut edge of the stomach wall, tying this shot to the two before it. The frame is noticeably cooler than the equivalent shot in any other video in the series."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame picks up from there: the same body, the camera now settled on the stomach that pool just landed in, with that same water lying across the lining. Same figure, same cyan rim, same background."),
        ],
        real="the gastric rugae as thick irregular folds of pink-red mucosa, a glistening mucus layer lying over them, gastric pits reading as fine dark openings across the surface, the greater curvature of the stomach carrying the fluid, and the pyloric sphincter as a thick ring of muscle at the far end opening into the duodenum.",
        cam="Push in, large amplitude, slow steady speed — the camera moves from the medium shot of the stomach forward through the cutaway opening, low over the surface of the lining, following the water toward the far end, and ends in macro on the pyloric opening with water running through it. One continuous move on a single axis, constant speed, no shake, no rotation, no stopping.",
        beats=[
            ("0.0 – 2.0 s", "The stomach wall contracts gently once and the water slides forward along the valleys between the folds. The camera begins to follow it."),
            ("2.0 – 4.0 s", "The push-in takes the camera low over the lining. The folds pass under the lens and the water runs ahead, still completely clear and unchanged."),
            ("4.0 – 6.0 s", "The far end of the stomach comes into frame. The ring of muscle there relaxes and opens."),
            ("6.0 – 8.0 s", "The camera settles on the open ring, and water runs steadily through it into the first bend of the small intestine beyond."),
        ],
        light="Cool and even throughout, brightening slightly as the camera approaches the opening, where a soft pale light comes through from the intestine beyond. No warm amber anywhere in this clip.",
        cons="One motion: water running across the lining and out through the opening. <strong>Nothing dissolves, foams, boils, churns violently or breaks apart</strong> — the absence of digestion is the entire point of this shot. Continuous across the full eight seconds.",
        note=("Note · what makes this topic different", "Every other video in the series spends its third clip breaking something down. This one deliberately does not, and the shot has to make that legible: the water arrives, crosses, and leaves unchanged. <strong>If the generation adds churning, bubbling or dissolving, re-roll it</strong> — that is the model reaching for the digestion it has seen a thousand times, and it contradicts the sentence being spoken over it."),
    ),
    dict(
        n=4, name="Where we are now → water and salt", where="Whole body → small intestine",
        tc="0:24.000 → 0:32.000", kf=("new", "new still"),
        colour="#5fc4e8", palette="cold blue — colour break · wide → macro",
        vo="In your small intestine it moves across the wall alongside salt, the two travelling together.",
        spoken=6.15,
        ends="Clear water and small pale sodium particles drifting side by side in the fluid just above the ridged inner lining of the small intestine, moving toward it together.",
        img=[
            ("SHOT 4 OF 8 — WHERE WE ARE NOW.", "The whole body seen at full length in cool blue, with the small intestine lit up inside the abdomen."),
            ("SCENE", "The same figure, now standing at full length facing camera in a dark navy void, rendered in cool blue X-ray tones: the skeleton, the organs and the outline of the muscles all visible through translucent blue skin. The small intestine, coiled in the centre of the abdomen, glows clear cyan-white and is the brightest thing in the body. Everything else is cool and dim. The figure stands still, arms slightly away from the sides, feet together."),
            ("CAMERA", "Wide: the whole figure from above the head to below the feet, filling about four-fifths of the frame height. Camera level at chest height, 50 mm equivalent lens, the whole figure in focus, the void behind it clean and empty."),
            ("SUBJECT — the water, stage 4 of 8", "Not visible as a drink any more. Its position in the body is what is visible: the cyan-white glow low in the abdomen is where it has reached."),
            ("LIGHT", "Cold: a cyan key from the front left and a deeper blue rim on both edges of the body. The abdomen self-illuminated from within. No warm light anywhere in this frame."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This is the one deliberate step back in the video — the same figure seen whole, so the viewer re-anchors and remembers this is happening inside a body. The glowing point in the abdomen is exactly where the previous shot just was, and the camera dives straight back into it."),
        ],
        real="the jejunum and ileum coiled through the centre of the abdomen with the frame of the colon around them, the liver under the right ribs, the stomach high on the left, both kidneys sitting behind the abdominal organs against the back wall, and a correct skeleton — twelve pairs of ribs, the lumbar spine, the pelvis and the femoral heads.",
        cam="Hold, then push in, very large amplitude, accelerating from slow to moderate and easing off at the end — the camera holds on the whole figure, then travels forward into the abdomen, through the body wall, into the small intestine, and ends in macro just above its inner lining. One continuous move, no cut, no stop.",
        beats=[
            ("0.0 – 2.0 s", "The whole figure is held still in frame and the cyan-white glow in the abdomen pulses once, softly. Nothing else moves."),
            ("2.0 – 4.0 s", "The camera begins travelling forward. The figure grows until the torso fills the frame and the glow becomes the brightest part of the image."),
            ("4.0 – 6.0 s", "The camera passes through the abdominal wall into the intestine. The ridged inner surface resolves ahead, seen through moving fluid."),
            ("6.0 – 8.0 s", "The camera settles just above the lining. Clear water and small pale particles come into focus drifting side by side toward the surface."),
        ],
        light="The whole clip is cold. As the camera enters the intestine the cyan key falls away and the light becomes a soft even blue-white coming through the fluid itself, with the lining dim beneath it.",
        cons="One motion: a single continuous forward travel from the whole body down to the lining. No cut, no dissolve, no jump in scale, no rotation of the figure. The figure does not turn, move or gesture at any point.",
        note=("Note · the deliberate colour break", "Shot 3 is cool but soft; shot 4 opens hard ice blue on a whole body. That jolt is doing retention work at the 24-second mark, which is roughly where a vertical video loses people — <strong>do not soften it.</strong> The pairing of water with salt matters too: they cross together, and showing two things moving side by side is what makes the sentence land."),
    ),
    dict(
        n=5, name="Through the wall", where="Intestinal villi · macro",
        tc="0:32.000 → 0:40.000", kf=("reuse", "reuse keyframe B"),
        colour="#e8899d", palette="pink + clear · macro",
        vo="It crosses the lining through the tiny folds, into the vessels waiting underneath them.",
        spoken=5.37,
        ends="Inside the capillary within a single villus: red blood cells flowing along in plasma that is visibly clearer and thinner than it was, the vessel wall arcing around the frame.",
        img=[
            ("SHOT 5 OF 8 — THROUGH THE WALL.", "Extreme macro on the lining of the small intestine, so close that individual villi fill the frame."),
            ("SCENE", "The inner surface of the small intestine at extreme magnification: hundreds of soft finger-shaped villi rising toward camera, wet coral and rose pink, each faintly translucent with a fine red capillary network glowing just beneath its surface. Clear water moves down between them from the fluid above — visible only as refraction and moving highlights — and passes through their surfaces into the capillaries underneath, where the flow inside visibly quickens and lightens. Small pale sodium particles travel with it. The whole surface is wet, with a thin film of fluid moving slowly over it."),
            ("CAMERA", "Macro, camera low among the villi looking very slightly up, 85 mm macro equivalent, very shallow depth of field: one band of villi razor sharp, the field in front of and behind it melting into soft pink bokeh."),
            ("SUBJECT — the water, stage 5 of 8", "Clear water crossing a living surface. It has no colour and no shape of its own, so it has to be read by what it does to the light and to the vessels it enters: refraction, moving highlights, and the visible quickening of the flow inside the villus."),
            ("LIGHT", "Warm pink light raking across from the right, catching every wet villus tip. Cool cyan fill from the left keeping the shadow side from going flat. The capillaries inside the villi glowing faintly red from within, brightening as the flow inside them increases."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is that same water and those same particles seen closer, arriving at the lining they were drifting toward. Same intestine, same fluid, same light — the camera has simply arrived at the surface."),
        ],
        real="villi as finger-shaped projections of mucosa, each with a brush border of microvilli at its tip, a central lacteal running up its core, a capillary loop wrapped around that lacteal, goblet cells spaced between the absorptive cells, and the crypts sitting in the valleys at the base of each villus.",
        cam="Truck right, small amplitude, slow speed for the first six seconds, then push in, small amplitude, slow speed on one villus for the last two. Two linked moves in one continuous take — the sideways drift never stops, the push-in grows out of it. No shake, no rotation, no whip.",
        beats=[
            ("0.0 – 2.0 s", "The camera drifts steadily to the right past the field of villi, which sway very slightly in the moving fluid."),
            ("2.0 – 4.0 s", "Water moves down between the villi and against their surfaces, bending the light behind it as it goes."),
            ("4.0 – 6.0 s", "Inside the villi, the capillary network brightens and the flow within it visibly speeds up. The sideways drift slows."),
            ("6.0 – 8.0 s", "The camera pushes in on one villus until its capillary fills the frame, and ends inside the vessel with the blood running clearer and faster than at the start of the shot."),
        ],
        light="Warm pink key holds throughout. The capillaries brighten from within as the water enters them, so the last two seconds are noticeably brighter inside the villus than the first two.",
        cons="One motion: the drift and the crossing. The villi sway gently and continuously in the current — they never whip, wave, snap or pulse in unison. Nothing bursts, splits or explodes.",
        note=("Note · reuse keyframe B", "This is <strong>keyframe B</strong> from the egg video. It is the most reusable image in the series — every video ends up at this wall and only the thing crossing it changes. Here the crossing subject is invisible, so <strong>the tell is the capillary brightening and the flow speeding up</strong>. Use the approved still as the start frame and re-run the motion prompt."),
    ),
    dict(
        n=6, name="Into the blood", where="Capillary → whole body",
        tc="0:40.000 → 0:48.000", kf=("reuse", "reuse keyframe C"),
        colour="#cf6f70", palette="red + blue → whole body · macro → wide",
        vo="Your blood thins slightly and carries it out to every tissue in your body at once.",
        spoken=5.07,
        ends="The whole body seen at full length, its entire arterial and venous tree visible as a fine red-and-blue network, running evenly brighter and paler than at the start of the shot, out to the fingers and toes.",
        img=[
            ("SHOT 6 OF 8 — INTO THE BLOOD.", "Inside a blood vessel, with the branching vessel tree visible far beyond it."),
            ("SCENE", "Macro inside a blood vessel: glossy dark red biconcave red blood cells tumbling toward camera through translucent straw-coloured plasma. The plasma is visibly thinner and clearer than usual and the cells travel a little further apart from one another because of it. The vessel wall arcs around the edges of frame in translucent pink, lit with a cold rim so the shape of the tube is readable. Far beyond the cells, out of focus, the vessel branches away into a fine network."),
            ("CAMERA", "Macro inside the vessel, camera in the centre of the flow facing along it, 50 mm equivalent lens, sharp focal plane through the middle of frame with the cells at the frame edges softened by motion blur."),
            ("SUBJECT — the water, stage 6 of 8", "No longer a separate object. It is the plasma the cells are moving through — clearer, thinner and moving more freely than it was."),
            ("LIGHT", "Deep red ambient from the blood itself and a cold blue rim along the vessel wall. Strong red-and-blue contrast, warm centre and cool edges."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is that same capillary, one moment later, with the camera now inside the flow. Same blood, same clearer plasma, same light."),
        ],
        real="red blood cells with their true biconcave dimpled shape and no nucleus, an endothelial lining one cell thick with the cell junctions faintly visible, vessels branching by real bifurcation into narrower ones — and at the wide end, an arterial tree in red and a venous tree in blue following real vascular anatomy out to the hands and feet.",
        cam="Pull out, very large amplitude, one constant slow speed all the way — the camera retreats continuously from inside the capillary out through the tissue, out of the abdomen, and back until the whole standing figure and its entire vessel tree are in frame. One unbroken move, never stopping, never accelerating, no rotation, no shake.",
        beats=[
            ("0.0 – 2.0 s", "Red cells stream past the lens in thin clear plasma as the camera begins to retreat along the vessel."),
            ("2.0 – 4.0 s", "The vessel widens and joins others, branching in every direction around the lens."),
            ("4.0 – 6.0 s", "The camera leaves the abdomen. The torso resolves, then the whole figure, its vessel tree lighting up as a fine red-and-blue network through translucent skin."),
            ("6.0 – 8.0 s", "The pull-out eases to a stop on the whole standing figure, the network brightening evenly all the way out to the fingers and the toes at the same time."),
        ],
        light="Starts deep red from inside the blood and cools steadily as the camera retreats, ending on the cool blue-and-red network of the whole figure against the dark background.",
        cons="One motion: a single continuous pull-out from inside a vessel to the whole body. No cut, no dissolve, no jump in scale. The figure does not move, turn or gesture when it appears. The network must brighten <strong>evenly and everywhere at once</strong> — not as a travelling pulse.",
        note=("Note · reuse keyframe C", "This is <strong>keyframe C</strong> from the egg video, with one difference in the motion: the egg sends gold points travelling outward along the network, and here <strong>the whole network brightens at once</strong>, because that is what the sentence says. Same still, different motion."),
    ),
    dict(
        n=7, name="The kidney decides", where="Kidney · cutaway → glomerulus",
        tc="0:48.000 → 0:56.000", kf=("new", "new still"),
        colour="#b97159", palette="deep red-brown + pale blue · macro, near-still",
        vo="Your kidneys measure what arrived, and decide how much to keep and how much to release.",
        spoken=5.38,
        ends="A single kidney filter at the centre of frame — a tight tuft of capillaries inside its round capsule — glowing warm, with clear fluid passing steadily out of it into the tubule below and the blood flowing on past.",
        img=[
            ("SHOT 7 OF 8 — THE KIDNEY DECIDES.", "One kidney seen close inside the body, its near half cut away, with a single filtering unit at macro inside it."),
            ("SCENE", "The same figure, framed on the lower back so the outline of the torso and the lumbar spine are still visible at the edges of frame. One kidney fills the centre, deep red-brown and bean-shaped, its near half opened in a clean medical cutaway: the paler outer cortex, the striped pyramids of the medulla beneath it, and the branching collecting space at the centre. Inside the cortex, at extreme magnification, a single filtering unit is visible — a tight tuft of capillaries held inside a round capsule, with a fine tubule leading away from it and coiling down into the medulla. Blood arrives at the tuft in a small vessel and leaves in another; clear fluid passes out of the tuft into the capsule and runs away down the tubule."),
            ("CAMERA", "Starts medium on the whole kidney, ends extreme macro on one filtering unit. 100 mm macro equivalent at the end, very shallow depth of field: the capillary tuft razor sharp, the surrounding tissue falling away soft."),
            ("SUBJECT — the water, stage 7 of 8", "Clear fluid being separated out of blood: visible as refraction and moving highlights as it passes out of the capillary tuft, and as a clear stream running down the tubule."),
            ("LIGHT", "Deep red ambient from the kidney tissue, a warm key raking across the cut face from the upper left, and a cool pale blue highlight on the clear fluid so it separates from the red around it. Cyan rim along the cut edge, tying this shot to the rest of the video."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is one place that network leads, close up — the camera has followed the blood to the kidney. Same body, same vessels, same cool rim light."),
        ],
        real="the kidney's outer cortex and inner medulla with its striped pyramids, and one nephron in full: the glomerulus as a tuft of capillaries inside Bowman's capsule, an afferent vessel arriving and an efferent vessel leaving, the proximal tubule, the loop of Henle descending into the medulla and returning, and the collecting duct running down toward the renal pelvis.",
        cam="Push in, moderate amplitude, slow and easing to a stop — the camera moves from the whole kidney into the cortex and settles on one filtering unit by 5.0 s, then holds almost perfectly still for the last three seconds. No pan, no tilt, no rotation, no shake.",
        beats=[
            ("0.0 – 2.0 s", "The whole cut kidney is held in frame, blood moving through the vessels at its edge. The camera begins to move in."),
            ("2.0 – 4.0 s", "The cortex fills the frame and one round capsule with its capillary tuft resolves in the centre."),
            ("4.0 – 6.0 s", "The camera settles. Clear fluid passes steadily out of the tuft into the capsule around it, and begins running away down the tubule."),
            ("6.0 – 8.0 s", "Everything holds: blood flowing on past the tuft, clear fluid running down the tubule, nothing else moving."),
        ],
        light="The warm key holds; the cool blue highlight on the clear fluid strengthens as the camera settles, so the filtered stream is the most legible thing in the frame by 8.0 s.",
        cons="One motion: the camera settling and the fluid separating. Nothing pumps, throbs, flashes or pulses. This is the stillest shot in the video and the calm is deliberate.",
        note=("Note · the money shot, and the compliance line", "This is the image that makes the video worth watching, and it is also where the script is most likely to go wrong. The kidney <strong>measures and decides</strong> — it is not filtering out poison, and nothing here is being flushed. <strong>Do not let a word like “toxins”, “cleanse” or “detox” into the sentence over this shot</strong>, no matter how naturally it fits the picture."),
    ),
    dict(
        n=8, name="Every cell, working", where="Whole body · hero",
        tc="0:56.000 → 1:04.000", kf=("reuse", "reuse keyframe D"),
        colour="#7fe0ff", palette="cool blue-white — colour break 2 · full body",
        vo="Now every cell in your body is working in the fluid it needs to do its job.",
        spoken=4.81,
        ends="The whole figure standing still, lit an even cool blue-white from within with no brighter or dimmer region anywhere, the camera stopped — a clean frame to hold under the end card.",
        img=[
            ("SHOT 8 OF 8 — EVERY CELL, WORKING.", "The same figure at full length, lit an even cool blue-white from within."),
            ("SCENE", "The same adult anatomical figure standing at full length facing camera in a dark void, seen from the front. The body is translucent and smooth, the head without facial features and without hair. It glows a soft even cool blue-white from within — not from the vessels alone this time but from the whole volume of the body, evenly, with no single organ brighter than any other. A faint pale haze surrounds the figure. The background is the same dark navy falling to black as every other shot."),
            ("CAMERA", "Wide: the whole figure from above the head to below the feet, filling about two-thirds of the frame height, centred, camera level at chest height, 50 mm equivalent lens, the whole figure in sharp focus."),
            ("SUBJECT — the water, stage 8 of 8", "No longer a separate object at all. It is the even light filling the whole body — everything that was one glass of water, now everywhere at once."),
            ("LIGHT", "Cool blue-white from inside the body, even throughout, with a soft pale ambient haze around it and a slightly warmer rim on both edges to keep the figure from going flat. This is the coolest hero frame in the series and it is meant to be — every other video ends warm."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame matches on that light: the same cool clear glow, at the scale of the whole body. It reads as the camera stepping all the way back at the end of the journey. Same figure, same rim light, same background as shot 1."),
        ],
        real="a correct arterial and venous tree — the aorta arching out of the heart, the carotids up the neck, the subclavians into the arms, the femorals down the legs — over a correct skeleton, with both kidneys visible in the lower back, all in true adult human proportion.",
        cam="Push in, very small amplitude — about 8% over the first six seconds, slowing to a complete stop at 6.0 s and holding perfectly still to the end. No rotation, no orbit, no shake. The figure never turns.",
        beats=[
            ("0.0 – 2.0 s", "The cool glow rises through the whole body at once, from dim to half strength. The camera begins its very slow push in."),
            ("2.0 – 4.0 s", "The glow continues to rise, evenly, with no part of the body leading or lagging."),
            ("4.0 – 6.0 s", "It settles to a steady even blue-white. The push-in eases to a stop."),
            ("6.0 – 8.0 s", "Nothing moves. The figure stands still, lit steady, held for the end card."),
        ],
        light="A single continuous rise: dim at 0 s, full steady cool blue-white at 6 s, then held without flicker to the end. No pulsing, no strobing, no beat, no travelling wave.",
        cons="One motion: the glow rising and settling, evenly everywhere. The figure does not move, breathe visibly, turn, gesture or shift weight. No particles, no rays, no energy effects, no lens flare.",
        note=("Note · reuse keyframe D", "This is <strong>keyframe D</strong> from the egg video with the colour changed: <strong>cool blue-white, and even everywhere</strong> rather than warm gold concentrated in the torso. It is the one hero frame in the series that does not end warm, which is exactly why this video does not look like the others. Specify <em>no facial features</em> again."),
    ),
]

TOPIC["clips"] = CLIPS
