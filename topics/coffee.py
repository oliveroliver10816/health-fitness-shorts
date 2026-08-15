"""Video 2 — "What happens when you drink coffee."

Beats follow the map published in section 08 of the main teardown page.
Timings are measured from the rendered voice-over, not estimated.
"""

TOPIC = dict(
    slug="coffee",
    video_no=2,
    lane="neuro lane",
    emoji="☕",
    accent="#e8a35c",
    glow="rgba(232,163,92,.14)",
    h1_plain="What happens when you drink coffee",
    title_html="What happens<br>when you drink<br><em>coffee.</em>",
    sub=("The widest audience of the five, and the only journey in the series that ends above the neck. Full script, "
         "<strong>voice-over already rendered and measured</strong>, and all 16 prompts written out — one "
         "unbroken journey through one body, every shot handing its last frame to the next one."),
    palette=("warm flesh pink and deep red tissue, dark roasted-brown coffee liquid, a pale blue-white caffeine "
             "molecule, cool cyan-teal rim light, dark navy background falling to black, with two or three very soft "
             "out-of-focus blue holographic panels far behind the subject blurred into pure glow"),
    vo_file="vo-coffee-64s.mp3",
    kf_chip="Reuses keyframes <b>A–D</b>",
    locks="the dark coffee liquid",
    chain_break=("Two of the seven cuts are scale jumps rather than continuous handoffs: <strong>into shot 4</strong> "
                 "(the stomach lining, out to the whole body) and <strong>into shot 8</strong> (a single neuron, out "
                 "to the whole body). Both sit where the egg video puts them, and both are doing a job — shot 4 "
                 "re-anchors the viewer at the 24-second retention dip, shot 8 is the payoff. They are still matched: "
                 "shot 4 opens on the glow in the abdomen, which is exactly where shot 3 just was, and shot 8 matches "
                 "on the pale blue light coming out of shot 7."),
    compliance=("Sentences 1–7 describe only what happens. Sentence 8 says the tired signal never arrives, so "
                "your brain stays alert — a description of the mechanism, not a promise. <strong>Never write "
                "“boosts your metabolism”, “burns fat”, a milligram figure, a cups-per-day "
                "number, or anything that reads as advice about sleep.</strong> Caffeine is the one subject in this "
                "series where a dosage number feels natural to add, and a dosage number is the fastest way to turn "
                "a physiology video into medical advice."),
    caption_words="“esophagus”, “caffeine”, “receptor” and “villi”",
    hook_step=("Copy the first second of clip 7 — the molecule seated in the receptor, glowing — to the "
               "very front of the timeline, then hard-cut to the mug at the lips. The image nobody has seen goes "
               "first. The voice-over does not move: it still starts at 0:00 and now plays over the receptor."),
    check_hook="The first second is the receptor, not the mug",
    kf_box_title="Four of these eight stills are already made",
    kf_box=("Clips 2, 5, 6 and 8 are anatomy, not coffee — the torso with the esophagus and stomach, the field "
            "of villi, the vessel network, the whole body. They are <strong>keyframes A, B, C and D</strong> from "
            "the egg video and they drop straight in as the start frames here; only what travels through them "
            "changes colour. This video needs four new stills: the mug at the lips, the stomach lining, the "
            "caffeine molecule and the brain barrier."),
    keep=("One new permanent asset — <strong>the blood–brain barrier still from clip 7</strong>, which no "
          "other video in the series reaches — plus a second use of keyframes A to D, which is what proves the "
          "library works. From here every video in the run costs four images and eight motion prompts."),
    hard_clips="clips 4, 6 and 7",
    prev=("egg", "Egg"),
    next=("water", "Water"),
)

CLIPS = [
    dict(
        n=1, name="The first mouthful", where="Mouth · head close-up",
        tc="0:00.000 → 0:08.000", kf=("new", "new still"),
        colour="#a9714a", palette="warm flesh + coffee brown · medium close-up",
        vo="Every morning when you drink coffee, the first warm mouthful spreads across your tongue and down your throat.",
        spoken=6.79,
        ends="Mouth closed, a thin dark film of coffee left on the surface of the tongue, and the last of the liquid moving back toward the opening of the throat. The steam has cleared from the frame.",
        img=[
            ("SHOT 1 OF 8 — THE FIRST MOUTHFUL.", "A hyper-realistic anatomical human head in three-quarter profile, taking the first sip from a mug of hot coffee."),
            ("SCENE", "An adult human head and shoulders turned three-quarters toward camera against a dark navy background. The skin is semi-transparent, so the skull, the jaw and cheek muscles, the tongue and the whole row of teeth read clearly through it — the look of a high-end medical visualisation figure. The face is calm and neutral, eyes open, no expression. A plain white ceramic mug is tilted at the lower lip and hot dark coffee is crossing that lip and spreading across the front of the tongue. Steam rises off the surface of the liquid and curls up past the cheek. Below the jaw, through the neck, the throat and the top of the esophagus are visible as a pale ribbed tube running down behind the windpipe."),
            ("CAMERA", "Medium close-up: the frame runs from the top of the skull down to the collarbones. Camera at mouth height, level with the face, 50 mm equivalent lens, shallow depth of field with the lips, tongue and liquid razor sharp and the back of the head falling soft."),
            ("SUBJECT — the coffee, stage 1 of 8", "Hot black coffee: deep roasted brown, almost black in the mass, translucent amber where it thins out at the edge, with a fine pale crema clinging to the rim of the mug. It must read instantly and unmistakably as coffee, not as any other dark liquid."),
            ("LIGHT", "One warm key light from the upper left catching every wet highlight on the lip, the tongue and the surface of the liquid, and lighting the steam from behind so it reads as fine bright vapour. A cool cyan rim light along the jawline and cheekbone separating the head from the background. Deep shadow behind the head."),
            ("CONTINUITY", "This is the opening shot and it locks the look for the whole video: this exact figure, this exact skin translucency, this exact dark coffee liquid, this warm-key-plus-cyan-rim lighting and this dark navy background appear in all eight shots. Nothing about the look changes after this frame."),
        ],
        real="the papillae covering the surface of the tongue, the pink gum margin around each tooth, the wet mucosa of the inner cheek and lip, the masseter and temporalis muscles under the skin, and the epiglottis and the opening of the esophagus sitting behind the base of the tongue.",
        cam="Push in, small amplitude, slow speed — the frame tightens by roughly 15% across the full eight seconds, travelling straight in toward the mouth and staying level at mouth height. Motorised smoothness, constant speed, no handheld shake, no rotation, no whip pan.",
        beats=[
            ("0.0 – 2.0 s", "The mug tilts a little further and the first coffee crosses the lower lip. Steam curls upward and drifts out of the top of frame."),
            ("2.0 – 4.0 s", "The liquid spreads across the front and sides of the tongue, darkening the surface and settling into the texture of it. The mug withdraws out of frame to the left."),
            ("4.0 – 6.0 s", "The lips close. The tongue rises and the liquid gathers into a shallow pool in the centre of the mouth, moving slightly as the jaw settles."),
            ("6.0 – 8.0 s", "The tongue presses up and back, and the pool moves toward the opening of the throat, leaving only a thin dark film behind it on the tongue."),
        ],
        light="Unchanged throughout — warm key upper left, cyan rim on the jaw. The steam thins across the eight seconds and is gone by the last frame. No other lighting change in this clip.",
        cons="One motion only: the sip. The head does not turn, nod, tilt, blink hard or speak. Nothing else in the frame moves. Slow and deliberate, continuous from the first frame to the last.",
        note=("Note", "The only shot in the video with an everyday object in it, and the one that tells the viewer what the video is about. If the still comes back and the liquid does not read as coffee at a glance — dark, hot, steaming, in a mug — re-roll it. Nothing later in the video re-establishes the subject."),
    ),
    dict(
        n=2, name="The swallow", where="Throat → stomach · torso wide",
        tc="0:08.000 → 0:16.000", kf=("reuse", "reuse keyframe A"),
        colour="#b9846f", palette="warm flesh + cyan rim · medium wide",
        vo="Your esophagus carries it down in one smooth wave, and it pools in your stomach.",
        spoken=5.34,
        ends="The whole upper body is in frame. The last of the dark liquid is passing the ring of muscle at the stomach entrance, and a shallow pool of coffee lies in the bottom of the stomach below.",
        img=[
            ("SHOT 2 OF 8 — THE SWALLOW.", "The same figure, one step wider: head, neck and upper chest, with the esophagus visible running down inside the body."),
            ("SCENE", "The same adult anatomical figure as shot 1, at the same three-quarter angle, now framed wider so the head, the whole neck and the upper chest are in view. Through the semi-transparent skin and the pale ribcage, the esophagus runs from the back of the throat down the centre of the chest, behind the heart, as a soft ribbed muscular tube. Dark coffee is entering the top of that tube as a narrow moving column, wetting the walls as it goes. The ring muscles of the esophagus read as evenly spaced bands along its length. A faint cool cyan glow runs down inside the tube ahead of the liquid, showing the direction of travel as a soft travelling light."),
            ("CAMERA", "Medium wide: the frame runs from just above the head down to the bottom of the ribcage. Camera level, 35 mm equivalent lens, moderate depth of field with the esophagus and the liquid sharp and the shoulders falling slightly soft."),
            ("SUBJECT — the coffee, stage 2 of 8", "A moving column of dark liquid rather than a lump: it runs faster, straighter and thinner than solid food would, and it leaves a wet dark trail on the wall behind it. That difference has to be visible — this is a drink, and it moves like one."),
            ("LIGHT", "Warm key from the upper left across the chest. Cool cyan rim down the left edge of the neck and shoulder. The esophagus glowing very faintly from within along its length."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is that same figure at that same angle, one step wider, with that same coffee now entering the top of the esophagus. Same skin, same light, same background, same liquid."),
        ],
        real="the esophagus as a muscular tube lying behind the trachea and in front of the spine, its wall built from an inner circular and an outer longitudinal muscle layer, the aortic arch and the left main bronchus crossing in front of it, the diaphragm it passes through, and the lower esophageal sphincter where it opens into the stomach.",
        cam="Pull out, large amplitude, front-loaded — the camera retreats quickly for the first three seconds, reaching the full upper-body frame by 3.0 s, then eases to a stop and holds there, almost motionless, for the last five. A drink outruns the camera; the move gets out of its way early and then watches. No shake, no rotation, no second move.",
        beats=[
            ("0.0 – 2.0 s", "The throat contracts once and the coffee drops into the top of the esophagus, already running. The camera retreats fast, the collarbones and ribcage arriving in frame within two seconds."),
            ("2.0 – 4.0 s", "The camera reaches the full upper body and eases to a stop. The liquid is already halfway down the tube, ahead of the muscle wave closing behind it."),
            ("4.0 – 6.0 s", "The camera is still. The column passes behind the heart, which beats steadily twice in this window, and the rings of muscle continue to close in sequence above it."),
            ("6.0 – 8.0 s", "The ring of muscle at the stomach entrance opens and the coffee pours through, gathering into a shallow pool at the bottom of the stomach. The camera never moves again."),
        ],
        light="The faint cyan glow inside the esophagus travels down the tube just ahead of the liquid, and fades out as the shot ends. Key and rim unchanged.",
        cons="One motion: the swallow, as a single continuous travelling squeeze that never stops or restarts. The figure does not move, turn or gesture; the only other movement in frame is the heartbeat.",
        note=("Note · reuse keyframe A", "This is <strong>keyframe A</strong> from the egg video — the torso with the esophagus and stomach visible. Use the same approved still as the start frame; only what travels down the tube is different, and the image prompt above is here for the case where you are generating this video first or want a fresh render. <strong>Re-run the motion prompt either way — never paste the egg video's rendered clip into this one.</strong>"),
    ),
    dict(
        n=3, name="Across the stomach lining", where="Stomach · cutaway → macro",
        tc="0:16.000 → 0:24.000", kf=("new", "new still"),
        colour="#c98452", palette="warm amber-brown · close → macro",
        vo="The warm liquid spreads across your stomach lining, and some of it already begins passing through.",
        spoken=6.35,
        ends="Extreme close on the stomach lining, with dark coffee lying in the valleys between the folds and fine dark threads of it moving down through the surface into the tissue below.",
        img=[
            ("SHOT 3 OF 8 — ACROSS THE STOMACH LINING.", "The stomach, seen close inside the body, its near wall cut away so the inside is visible."),
            ("SCENE", "The same figure, now framed on the abdomen. The stomach fills most of the frame, sitting under the ribs, with the lower ribcage and the outline of the torso still visible around the edges of frame so it stays obvious that we are inside a human body. The near wall of the stomach is opened in a clean medical cutaway, revealing the interior: deep folded ridges of stomach lining in wet red-brown, and a shallow pool of dark coffee lying across the floor of it, spreading out into the valleys between the folds and thinning to translucent amber at its edge. The whole surface glistens under a thin layer of mucus. Faint threads of colour are beginning to move downward out of the pool into the lining itself."),
            ("CAMERA", "Medium close-up on the stomach, slightly high angle looking down into the cutaway, 40 mm equivalent lens, shallow depth of field with the near folds and the edge of the pool sharp and the far wall of the stomach soft behind them."),
            ("SUBJECT — the coffee, stage 3 of 8", "The same dark liquid, now a spreading pool rather than a moving column: deep brown in the mass, amber and translucent where it runs thin over a fold, wetting everything it touches."),
            ("LIGHT", "Strong warm amber light coming up through the pool from below, turning it to glowing dark honey where it is thin. The folds of the lining lit from the upper left so their wet ridges catch a hard highlight. Cyan rim light along the cut edge of the stomach wall, tying this shot to the two before it."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame picks up from there: the same body, the camera now settled on the stomach that pool just landed in, with that same coffee lying across the lining. Same figure, same cyan rim, same background."),
        ],
        real="the gastric rugae as thick irregular folds of pink-red mucosa, a glistening mucus layer lying over them, gastric pits reading as fine dark openings across the surface, the dense submucosal capillary network faintly visible through the lining, and the greater curvature of the stomach holding the pool.",
        cam="Push in, large amplitude, slow steady speed — the camera moves from the medium shot of the stomach forward through the cutaway opening and down to the surface of the lining, ending in macro with a single fold and the edge of the pool filling the frame. One straight continuous move on a single axis, constant speed, no shake, no rotation, no stopping.",
        beats=[
            ("0.0 – 2.0 s", "The stomach wall contracts once and the pool slides across the floor of it, running further into the valleys between the folds. The camera begins pushing in."),
            ("2.0 – 4.0 s", "The push-in continues until the folds of the lining fill the frame, wet and glistening, with the edge of the dark liquid creeping across them."),
            ("4.0 – 6.0 s", "The surface darkens where the liquid rests on it, and the first fine threads begin to move downward out of the pool into the lining."),
            ("6.0 – 8.0 s", "More threads follow, reaching the fine capillaries visible just under the surface, which take on a faint dark tint as they arrive."),
        ],
        light="The amber underlight strengthens as the camera descends toward the lining, until by 6.0 s the whole frame is lit warmly from below and the background has gone to deep red-brown.",
        cons="One motion: the liquid spreading and beginning to soak in. It must not boil, bubble violently, foam or splash. Slow, wet, continuous across the full eight seconds, never restarting.",
        note=("Note · what makes this topic different", "Every other video in the series waits for the small intestine. Coffee does not — some of it crosses here, in the stomach, which is why it works so fast. That is the whole reason this shot exists, so <strong>the threads moving down into the lining are the thing that has to read clearly</strong>. If the still comes back with a pool and no absorption, re-roll it."),
    ),
    dict(
        n=4, name="Where we are now → the molecule", where="Whole body → macro",
        tc="0:24.000 → 0:32.000", kf=("new", "new still"),
        colour="#5fc4e8", palette="cold blue — colour break · wide → macro",
        vo="Inside it is caffeine, a molecule so small it can slip almost anywhere in your body.",
        spoken=5.84,
        ends="A single pale blue-white caffeine molecule alone in the centre of frame, turning slowly, adrift in dark fluid, with the soft out-of-focus wall of the stomach far behind it.",
        img=[
            ("SHOT 4 OF 8 — WHERE WE ARE NOW.", "The whole body seen at full length in cool blue, with the stomach and upper abdomen lit up inside it."),
            ("SCENE", "The same figure, now standing at full length facing camera in a dark navy void, rendered in cool blue X-ray tones: the skeleton, the organs and the outline of the muscles all visible through translucent blue skin. The stomach, high on the left of the abdomen, glows clear cyan-white and is the brightest thing in the body. Everything else is cool and dim. The figure stands still, arms slightly away from the sides, feet together."),
            ("CAMERA", "Wide: the whole figure from above the head to below the feet, filling about four-fifths of the frame height. Camera level at chest height, 50 mm equivalent lens, the whole figure in focus, the void behind it clean and empty."),
            ("SUBJECT — the coffee, stage 4 of 8", "Not visible as a drink any more. Its position in the body is what is visible: the cyan-white glow high in the abdomen is where it has reached."),
            ("LIGHT", "Cold: a cyan key from the front left and a deeper blue rim on both edges of the body. The stomach self-illuminated from within. No warm light anywhere in this frame."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This is the one deliberate step back in the video — the same figure seen whole, so the viewer re-anchors and remembers this is happening inside a body. The glowing point in the abdomen is exactly where the previous shot just was, and the camera dives straight back into it."),
        ],
        real="a correct skeleton — twelve pairs of ribs, the lumbar spine, the pelvis and the femoral heads — with the stomach high on the left under the diaphragm, the liver filling the space under the right ribs, and the coiled small intestine coiled below and behind them, all in true adult human proportion.",
        cam="Hold, then push in, very large amplitude, accelerating from slow to moderate and easing off at the end — the camera holds on the whole figure, then travels forward into the abdomen, through the body wall, and ends in macro on a single molecule adrift in fluid. One continuous move, no cut, no stop.",
        beats=[
            ("0.0 – 2.0 s", "The whole figure is held still in frame and the cyan-white glow in the abdomen pulses once, softly. Nothing else moves."),
            ("2.0 – 4.0 s", "The camera begins travelling forward. The figure grows until the torso fills the frame and the glow becomes the brightest part of the image."),
            ("4.0 – 6.0 s", "The camera passes through the abdominal wall into dark fluid. Countless small pale particles stream past the lens, out of focus and moving fast."),
            ("6.0 – 8.0 s", "The stream thins and the particles drift out of frame until one is left: a single pale blue-white molecule in the centre, turning slowly, in focus."),
        ],
        light="The whole clip is cold. As the camera enters the body the cyan key falls away and the only light left is the faint blue-white glow the molecule carries itself, with a dark blue ambient behind it.",
        cons="One motion: a single continuous forward travel from the whole body down to one molecule. No cut, no dissolve, no jump in scale, no rotation of the figure. The figure does not turn, move or gesture at any point.",
        note=("Note · the deliberate colour break", "Shot 3 is hot amber-brown and shot 4 opens ice blue, back to back on a hard cut. That jolt is doing retention work at the 24-second mark, which is roughly where a vertical video loses people — <strong>do not soften it and do not warm this shot up.</strong> It is also the shot that re-establishes the body, which is what stops the second half reading as abstract."),
    ),
    dict(
        n=5, name="Through the wall", where="Intestinal villi · macro",
        tc="0:32.000 → 0:40.000", kf=("reuse", "reuse keyframe B"),
        colour="#e8899d", palette="pink + pale blue · macro",
        vo="Most of it crosses the wall of your small intestine, through the tiny folds lining it.",
        spoken=5.54,
        ends="Inside the capillary within a single villus: red blood cells and pale blue-white molecules flowing along together, the vessel wall arcing around the frame.",
        img=[
            ("SHOT 5 OF 8 — THROUGH THE WALL.", "Extreme macro on the lining of the small intestine, so close that individual villi fill the frame."),
            ("SCENE", "The inner surface of the small intestine at extreme magnification: hundreds of soft finger-shaped villi rising toward camera, wet coral and rose pink, each faintly translucent with a fine red capillary network glowing just beneath its surface. Pale blue-white molecules drift down between them from the dark fluid above, settle against the villus surfaces, and pass through into the capillaries underneath, where they can be seen travelling away inside the vessel. The whole surface is wet, with a thin film of fluid moving slowly over it."),
            ("CAMERA", "Macro, camera low among the villi looking very slightly up, 85 mm macro equivalent, very shallow depth of field: one band of villi razor sharp, the field in front of and behind it melting into soft pink bokeh."),
            ("SUBJECT — the coffee, stage 5 of 8", "Single caffeine molecules: small, pale blue-white, faintly luminous, the same ones the camera found at the end of the previous shot."),
            ("LIGHT", "Warm pink light raking across from the right, catching every wet villus tip. Cool cyan fill from the left keeping the shadow side from going flat. The capillaries inside the villi glowing faintly red from within, and the molecules carrying a cold pale light of their own."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is that same molecule seen among many more of them, arriving at the lining they were drifting toward. Same intestine, same molecules, same pale blue light — the camera has simply arrived at the surface."),
        ],
        real="villi as finger-shaped projections of mucosa, each with a brush border of microvilli at its tip, a central lacteal running up its core, a capillary loop wrapped around that lacteal, goblet cells spaced between the absorptive cells, and the crypts sitting in the valleys at the base of each villus.",
        cam="Push in, moderate amplitude, one constant slow speed for the whole eight seconds — the camera travels straight forward through the field of villi toward one of them, and never stops, never drifts sideways and never rotates. A single-axis approach, from the field to one villus to the vessel inside it.",
        beats=[
            ("0.0 – 2.0 s", "The camera moves forward between the villi, which part visually as the perspective opens. Pale molecules drift down past the lens."),
            ("2.0 – 4.0 s", "One villus grows in the centre of frame. Molecules settle against its surface and the first of them pass through."),
            ("4.0 – 6.0 s", "The capillary network inside that villus becomes visible through the surface and brightens as pale points begin travelling along it."),
            ("6.0 – 8.0 s", "The camera arrives at the capillary and continues just inside it, ending with red cells and pale molecules flowing along together."),
        ],
        light="Warm pink key holds throughout. The capillaries brighten from within as the molecules enter them, so the last two seconds are noticeably warmer inside the villus than the first two.",
        cons="One motion: the drift and the crossing. The villi sway gently and continuously in the current — they never whip, wave, snap or pulse in unison. Nothing bursts, splits or explodes.",
        note=("Note · reuse keyframe B", "This is <strong>keyframe B</strong> from the egg video. It is the single most reusable image in the series — every video ends up at this wall and only the colour of what crosses it changes, gold for amino acids, pale blue-white here. Use the approved still as the start frame and re-run the motion prompt."),
    ),
    dict(
        n=6, name="Into the blood", where="Capillary → liver → whole body",
        tc="0:40.000 → 0:48.000", kf=("reuse", "reuse keyframe C"),
        colour="#cf6f70", palette="red + blue → whole body · macro → wide",
        vo="Your blood picks it up, carries it through your liver, and up along the vessels toward your head.",
        spoken=5.83,
        ends="The whole body seen at full length, its entire arterial and venous tree visible as a fine red-and-blue network, with pale blue points travelling up the vessels of the neck toward the head.",
        img=[
            ("SHOT 6 OF 8 — INTO THE BLOOD.", "Inside a blood vessel, with the branching vessel tree visible far beyond it."),
            ("SCENE", "Macro inside a blood vessel: glossy dark red biconcave red blood cells tumbling toward camera through translucent straw-coloured plasma, with pale blue-white molecules travelling among them and standing out clearly against the red. The vessel wall arcs around the edges of frame in translucent pink, lit with a cold rim so the shape of the tube is readable. Far beyond the cells, out of focus, the vessel branches away into a fine network."),
            ("CAMERA", "Macro inside the vessel, camera in the centre of the flow facing along it, 50 mm equivalent lens, sharp focal plane through the middle of frame with the cells at the frame edges softened by motion blur."),
            ("SUBJECT — the coffee, stage 6 of 8", "The same pale blue-white molecules, now travelling in blood among the red cells, distinct from them in both colour and size."),
            ("LIGHT", "Deep red ambient from the blood itself, a cold blue rim along the vessel wall, and the molecules carrying their own pale light. Strong red-and-blue contrast, warm centre and cool edges."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is that same capillary, one moment later, with the camera now inside the flow. Same molecules, same pale blue light, same blood."),
        ],
        real="red blood cells with their true biconcave dimpled shape and no nucleus, an endothelial lining one cell thick with the cell junctions faintly visible, vessels branching by real bifurcation into narrower ones — and at the wide end, an arterial tree in red and a venous tree in blue following real vascular anatomy, with the carotid arteries running up either side of the neck.",
        cam="Pull out, very large amplitude, then tilt up — the camera retreats at a constant slow speed from inside the capillary out to the whole standing figure, and from 5.0 s it also tilts gently upward, so the move finishes framed slightly high, with the head and neck in the upper third of frame. One continuous move, no stop between the retreat and the tilt, no shake, no rotation.",
        beats=[
            ("0.0 – 2.0 s", "Red cells and pale molecules stream past the lens as the camera begins to retreat along the vessel."),
            ("2.0 – 4.0 s", "The vessel widens and joins others. The camera passes through the dense red tissue of the liver, its vessels branching in every direction around the lens."),
            ("4.0 – 6.0 s", "The camera leaves the abdomen and the whole figure resolves, its vessel tree lighting up as a fine red-and-blue network. The tilt upward begins."),
            ("6.0 – 8.0 s", "The tilt finishes with the head and neck high in frame. Pale points travel up the vessels of the neck and are the brightest thing in the picture as the move stops."),
        ],
        light="Starts deep red from inside the blood and cools steadily as the camera retreats, ending on the cool blue-and-red network of the whole figure against the dark background.",
        cons="One motion: a single continuous pull-out from inside a vessel to the whole body. No cut, no dissolve, no jump in scale. The figure does not move, turn or gesture when it appears.",
        note=("Note · reuse keyframe C", "This is <strong>keyframe C</strong> from the egg video. The one thing to change in the render: in the egg video the gold spreads evenly to every limb, here <strong>the points heading up the neck are the brightest ones</strong>, because that is where this video is going. Same still, different motion."),
    ),
    dict(
        n=7, name="Past the wall of the brain", where="Brain capillary · extreme macro",
        tc="0:48.000 → 0:56.000", kf=("new", "new still"),
        colour="#7f8fe0", palette="violet-blue + pale glow · macro, near-still",
        vo="It slips past the wall that guards your brain, and settles into the receptor tiredness uses.",
        spoken=6.31,
        ends="The molecule seated in the receptor on the surface of the neuron, glowing pale blue, with everything else in frame completely still.",
        img=[
            ("SHOT 7 OF 8 — PAST THE WALL OF THE BRAIN.", "Extreme macro at the wall of a capillary inside the brain, with brain tissue on the far side of it."),
            ("SCENE", "Extreme macro inside the head: a fine capillary runs diagonally across the frame, its wall built from flat endothelial cells pressed edge to edge, wrapped closely by pale astrocyte end-feet like a sleeve. Red blood cells move through the vessel behind the wall, out of focus. On the far side of the wall lies brain tissue in cool violet-grey: the swollen body of a neuron with dendrites branching away from it, its surface textured and wet. A few pale blue-white molecules are pressed against the vessel wall, and one has already crossed and is drifting toward a small cup-shaped receptor sitting on the neuron's surface. The outline of the head is faintly visible at the very edge of frame, so the location stays readable."),
            ("CAMERA", "Extreme macro, camera close and level with the vessel wall, 100 mm macro equivalent, very shallow depth of field: the wall, the crossing molecule and the receptor razor sharp, the blood behind and the brain tissue beyond falling away soft."),
            ("SUBJECT — the coffee, stage 7 of 8", "One caffeine molecule, pale blue-white and faintly luminous, at the moment it crosses out of the blood and into the brain."),
            ("LIGHT", "Cool violet ambient from the brain tissue, a warm red glow from the blood behind the vessel wall, and the molecule carrying its own pale blue light — the brightest single point in the frame. Deep shadow between the dendrites."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is one of those points arriving, close up — the camera has followed the pale blue up the neck into a vessel in the brain. Same molecules, same pale blue light, same cool rim."),
        ],
        real="a brain capillary lined by endothelial cells joined edge to edge by tight junctions, sitting on a continuous basement membrane, with pericytes on the outside and astrocyte end-feet wrapping the vessel almost completely — and beyond it a neuron with a textured cell body, branching dendrites and small receptor structures on the membrane surface.",
        cam="Static shot, with the faintest push in — under 5% across the whole eight seconds, so slow it is barely perceptible. No pan, no tilt, no truck, no rotation, no shake. This is deliberately the stillest shot in the video.",
        beats=[
            ("0.0 – 2.0 s", "Almost nothing moves. Red cells drift past behind the vessel wall, out of focus. The molecule sits pressed against the wall."),
            ("2.0 – 4.0 s", "The molecule slips through the wall between the cells and emerges on the brain side, drifting slowly forward."),
            ("4.0 – 6.0 s", "It travels toward the receptor on the neuron's surface, turning slightly as it goes. The receptor brightens faintly as it approaches."),
            ("6.0 – 8.0 s", "The molecule settles into the receptor and stops. Its glow steadies. Everything in frame comes to rest."),
        ],
        light="The molecule's pale blue glow strengthens as it crosses and brightens again as it seats, so the frame is coolest and dimmest at 0 s and brightest at 8 s. Ambient light unchanged.",
        cons="One motion: one molecule crossing and seating. Nothing else in the frame moves except the out-of-focus blood behind the wall. No pulsing, no flashing, no energy effect, no burst of light when it seats.",
        note=("Note · the money shot of this video", "This is the image nobody has seen and the reason to make this video at all — it is also the shot that opens the finished cut. The stillness is the point: shot 6 has just travelled the length of a body, so shot 7 stops moving. <strong>Resist adding a camera move, and resist making the moment it seats into a flash of light.</strong> It has to look like something settling into place, not like a switch being thrown."),
    ),
    dict(
        n=8, name="The whole body, awake", where="Whole body · hero",
        tc="0:56.000 → 1:04.000", kf=("reuse", "reuse keyframe D"),
        colour="#f2b544", palette="warm gold — colour break 2 · full body",
        vo="That tired signal never arrives, so your brain stays alert and your body feels awake.",
        spoken=6.01,
        ends="The whole figure standing still with its vessel network lit steady warm gold and the head the brightest part of it, the camera stopped — a clean frame to hold under the end card.",
        img=[
            ("SHOT 8 OF 8 — THE WHOLE BODY, AWAKE.", "The same figure at full length, its vessel network glowing warm gold from within, brightest at the head."),
            ("SCENE", "The same adult anatomical figure standing at full length facing camera in a dark void, seen from the front. The body is translucent and smooth, the head without facial features and without hair. Its internal vessel network glows warm gold from within — brightest through the head and neck, falling away gently down the torso and into the arms and legs, so the eye is pulled upward. A soft warm haze surrounds the figure. The background is the same dark navy falling to black as every other shot."),
            ("CAMERA", "Wide: the whole figure from above the head to below the feet, filling about two-thirds of the frame height, centred, camera level at chest height, 50 mm equivalent lens, the whole figure in sharp focus."),
            ("SUBJECT — the coffee, stage 8 of 8", "No longer a separate object at all. It is the gold light in the network — everything that was one mug of coffee, now spread through the whole body and concentrated where it does its work."),
            ("LIGHT", "Warm gold from inside the body, brightest at the head, with a soft gold ambient haze around it and a cool blue rim on both edges. This is the warmest frame in the video and it is meant to be."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame matches on that light: the same glow, at the scale of the whole body. It reads as the camera stepping all the way back at the end of the journey. Same figure, same rim light, same background as shot 1."),
        ],
        real="a correct arterial and venous tree — the aorta arching out of the heart, the carotids running up the neck, the subclavians into the arms, the femorals down the legs — branching to fine peripheral vessels over a correct skeleton, with the dense vessel network of the head and brain readable as the brightest region, all in true adult human proportion.",
        cam="Tilt up, small amplitude, slow — the camera stays at the same distance and cranes gently upward across the first five seconds, from chest height to head height, so the frame arrives at the head rather than pushing into the body. It stops completely at 5.0 s and holds. No push in, no rotation, no orbit, no shake.",
        beats=[
            ("0.0 – 2.0 s", "The gold glow rises through the vessel network from the torso upward. The camera begins its slow tilt."),
            ("2.0 – 4.0 s", "The glow reaches the neck as the tilt continues, the head moving toward the centre of frame."),
            ("4.0 – 6.0 s", "The vessels of the head fill with light until they are the brightest part of the figure. The tilt stops at 5.0 s."),
            ("6.0 – 8.0 s", "Nothing moves. The figure stands still, lit steady, held for the end card."),
        ],
        light="A single continuous warm-up: from a dim network at 0 s to full steady gold at 6 s, then held without flicker to the end. No pulsing, no strobing, no beat.",
        cons="One motion: the glow rising and settling. The figure does not move, breathe visibly, turn, gesture or shift weight. No particles, no rays, no energy effects, no lens flare.",
        note=("Note · reuse keyframe D, and it opens the video too", "This is <strong>keyframe D</strong> from the egg video with one change: <strong>the head is the brightest part, not the torso</strong>. Specify <em>no facial features</em> again — a face here is uncanny and it pulls attention off the glow. The first second of the finished video is clip 7's receptor rather than this frame, which is the one place this video's cut differs from the egg's."),
    ),
]

TOPIC["clips"] = CLIPS
