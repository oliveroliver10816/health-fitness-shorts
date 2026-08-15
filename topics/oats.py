"""Video 4 — "What happens when you eat oats."

Beats follow the map published in section 08 of the main teardown page.
Timings are measured from the rendered voice-over, not estimated.
"""

TOPIC = dict(
    slug="oats",
    video_no=4,
    lane="carbohydrate lane",
    emoji="🥣",
    accent="#e0b774",
    glow="rgba(224,183,116,.14)",
    h1_plain="What happens when you eat oats",
    title_html="What happens<br>when you eat<br><em>oats.</em>",
    sub=("The most visually distinctive of the five: the subject physically changes state inside the body — dry "
         "flakes become a thick gel. Full script, <strong>voice-over already rendered and measured</strong>, and all "
         "16 prompts written out — one unbroken journey through one body, every shot handing its last frame to the "
         "next one."),
    palette=("warm flesh pink and deep red tissue, cream-beige oat flakes turning to pale honey-coloured gel, cool "
             "cyan-teal rim light, dark navy background falling to black, with two or three very soft out-of-focus "
             "blue holographic panels far behind the subject blurred into pure glow"),
    vo_file="vo-oats-64s.mp3",
    kf_chip="Reuses keyframes <b>A–D</b>",
    locks="the cream-beige oat material and the honey-coloured gel it becomes",
    chain_break=("Two of the seven cuts are scale jumps rather than continuous handoffs: <strong>into shot 4</strong> "
                 "(the thickening gel in the stomach, out to the whole body) and <strong>into shot 8</strong> (the "
                 "colon, out to the whole body). Both sit where the egg video puts them, and both are doing a job — "
                 "shot 4 re-anchors the viewer at the 24-second retention dip, shot 8 is the payoff. They are still "
                 "matched: shot 4 opens on the glow in the abdomen, exactly where shot 3 just was, and shot 8 "
                 "matches on the warm light coming out of shot 7."),
    compliance=("Sentences 1–7 describe only what happens. Sentence 8 says the body is running on a steady supply — "
                "a description of a pattern, not a promise. <strong>Never write “lowers cholesterol”, “prevents "
                "diabetes”, “blood sugar crash”, or a glycaemic-index number.</strong> A cholesterol line is legally "
                "permitted for oats in some countries, and it still does not belong in this format: it is an outcome "
                "claim, it invites a comment section full of medical argument, and it is the one sentence that would "
                "make this video worth reporting. Describe the gel and let the viewer draw the conclusion."),
    caption_words="“esophagus”, “fibre”, “villi” and “bacteria”",
    hook_step=("Copy one second of clip 3 — the flakes swelling into gel — to the very front of the timeline, then "
               "hard-cut to the spoon at the mouth. The state change is the hook, so lead with it. The voice-over "
               "does not move: it still starts at 0:00 and now plays over the gel."),
    check_hook="The first second is the gel forming, not the spoon",
    kf_box_title="Four of these eight stills are already made",
    kf_box=("Clips 2, 5, 6 and 8 are anatomy, not oats — the torso with the esophagus and stomach, the field of "
            "villi, the vessel network, the whole body. They are <strong>keyframes A, B, C and D</strong> from the "
            "egg video and they drop straight in as the start frames here. This video needs four new stills: the "
            "spoonful at the mouth, the gel forming, the coated intestinal wall and the colon."),
    keep=("One new permanent asset — <strong>the colon still from clip 7</strong>, which is where any future "
          "gut-bacteria video in this series will start — and a fourth use of keyframes A to D. This is also the "
          "video with the best pure motion in the run: a real state change, on camera, in one continuous shot."),
    hard_clips="clips 3, 4 and 6",
    prev=("water", "Water"),
    next=("spinach", "Spinach"),
)

CLIPS = [
    dict(
        n=1, name="The spoonful", where="Mouth · head close-up",
        tc="0:00.000 → 0:08.000", kf=("new", "new still"),
        colour="#cbb083", palette="warm flesh + oat cream · medium close-up",
        vo="Every morning when you eat oats, your teeth break the soft flakes apart in your mouth.",
        spoken=5.31,
        ends="Mouth closed. A soft cream-coloured mass of broken oat flakes is sitting at the back of the tongue, at the entrance to the throat. The jaw is relaxed.",
        img=[
            ("SHOT 1 OF 8 — THE SPOONFUL.", "A hyper-realistic anatomical human head in three-quarter profile, taking a spoonful of cooked oats."),
            ("SCENE", "An adult human head and shoulders turned three-quarters toward camera against a dark navy background. The skin is semi-transparent, so the skull, the jaw and cheek muscles, the tongue and the whole row of teeth read clearly through it — the look of a high-end medical visualisation figure. The face is calm and neutral, eyes open, no expression. The mouth is open and a stainless steel spoon is delivering a mound of cooked oats onto the tongue: individual soft flakes, cream and pale beige, swollen with milk or water and clinging together in a loose mass. Faint steam rises off it. Below the jaw, through the neck, the throat and the top of the esophagus are visible as a pale ribbed tube running down behind the windpipe."),
            ("CAMERA", "Medium close-up: the frame runs from the top of the skull down to the collarbones. Camera at mouth height, level with the face, 50 mm equivalent lens, shallow depth of field with the lips, teeth and oats razor sharp and the back of the head falling soft."),
            ("SUBJECT — the oats, stage 1 of 8", "Cooked porridge oats: individual flat flakes, cream to pale beige, each one visibly swollen and soft at the edges, glistening with the liquid they were cooked in and holding together loosely as a mound. Individual flakes must be identifiable — this must not read as a smooth paste at the start, because the whole video is about it becoming one."),
            ("LIGHT", "One warm key light from the upper left catching every wet highlight on teeth, tongue and food, and lighting the steam from behind. A cool cyan rim light along the jawline and cheekbone separating the head from the background. Deep shadow behind the head."),
            ("CONTINUITY", "This is the opening shot and it locks the look for the whole video: this exact figure, this exact skin translucency, this exact cream-beige oat material, this warm-key-plus-cyan-rim lighting and this dark navy background appear in all eight shots. Nothing about the look changes after this frame."),
        ],
        real="the papillae covering the surface of the tongue, the pink gum margin around each tooth, the wet mucosa of the inner cheek, the flat grinding surfaces of the molars, the masseter and temporalis muscles bunching under the skin as the jaw closes, and the epiglottis and the opening of the esophagus behind the base of the tongue.",
        cam="Push in, small amplitude, slow speed — the frame tightens by roughly 15% across the full eight seconds, travelling straight in toward the mouth and staying level at mouth height. Motorised smoothness, constant speed, no handheld shake, no rotation, no whip pan.",
        beats=[
            ("0.0 – 2.0 s", "The spoon slides back out of frame to the left, leaving the mound of oats on the tongue. The lips close over it and the jaw begins to rise."),
            ("2.0 – 4.0 s", "The molars press down through the mass: the flakes flatten and break apart, the mound losing its shape. Under the transparent skin, the jaw and cheek muscles visibly bunch and release."),
            ("4.0 – 6.0 s", "Two more chewing cycles. The flakes break smaller and mix with saliva, the whole mass turning softer and wetter and beginning to hold together."),
            ("6.0 – 8.0 s", "The tongue lifts and presses the mass back toward the throat. It starts moving to the back of the mouth as the shot ends."),
        ],
        light="Unchanged throughout — warm key upper left, cyan rim on the jaw. The steam thins across the eight seconds. No other lighting change in this clip.",
        cons="One motion only: chewing. The head does not turn, nod, tilt, blink hard or speak. Nothing else in the frame moves. Slow, deliberate and mechanical, continuous from the first frame to the last.",
        note=("Note", "The only shot in the video with an everyday object in it, and the one that tells the viewer what the video is about. <strong>Individual flakes have to be visible in this still</strong> — the entire point of shot 3 is that this loose, dry-looking mass becomes a single thick gel, and that only reads if the starting state is clearly separate flakes."),
    ),
    dict(
        n=2, name="The swallow", where="Throat → stomach · torso wide",
        tc="0:08.000 → 0:16.000", kf=("reuse", "reuse keyframe A"),
        colour="#b9846f", palette="warm flesh + cyan rim · medium wide",
        vo="Your esophagus moves the warm spoonful down in slow waves, into your stomach below.",
        spoken=5.92,
        ends="The frame has tightened onto the lower chest and stomach. The pale cream mass has arrived at the lower end of the esophagus and the ring of muscle at the stomach entrance is opening in front of it. The stomach below is pink and empty.",
        img=[
            ("SHOT 2 OF 8 — THE SWALLOW.", "The same figure, one step wider: head, neck and upper chest, with the esophagus visible running down inside the body."),
            ("SCENE", "The same adult anatomical figure as shot 1, at the same three-quarter angle, now framed wider so the head, the whole neck and the upper chest are in view. Through the semi-transparent skin and the pale ribcage, the esophagus runs from the back of the throat down the centre of the chest, behind the heart, as a soft ribbed muscular tube. A soft cream-coloured mass of chewed oats sits at the very top of that tube, just entering it, thick and slow-moving. The ring muscles of the esophagus read as evenly spaced bands along its length. A faint cool cyan glow runs down inside the tube ahead of the mass, showing the direction of travel as a soft travelling light."),
            ("CAMERA", "Medium wide: the frame runs from just above the head down to the bottom of the ribcage. Camera level, 35 mm equivalent lens, moderate depth of field with the esophagus and the mass sharp and the shoulders falling slightly soft."),
            ("SUBJECT — the oats, stage 2 of 8", "A soft, thick, cream-coloured bolus roughly the size of a walnut, holding its shape as it is squeezed along. It moves more slowly and more reluctantly than a liquid would, and it deforms around each contraction rather than running ahead of it."),
            ("LIGHT", "Warm key from the upper left across the chest. Cool cyan rim down the left edge of the neck and shoulder. The esophagus glowing very faintly from within along its length."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is that same figure at that same angle, one step wider, with that same chewed mass now formed into a bolus at the top of the esophagus. Same skin, same light, same background, same oat material."),
        ],
        real="the esophagus as a muscular tube lying behind the trachea and in front of the spine, its wall built from an inner circular and an outer longitudinal muscle layer, the aortic arch and the left main bronchus crossing in front of it, the diaphragm it passes through, and the lower esophageal sphincter where it opens into the stomach.",
        cam="Push in, moderate amplitude, slow and decelerating — the camera starts on the whole upper body and moves steadily forward and slightly down, tightening onto the lower chest and the stomach, and easing almost to a stop by 7.0 s. It closes in rather than opening out, because this subject travels slowly and the shot stays with it. No shake, no rotation, no second move.",
        beats=[
            ("0.0 – 2.0 s", "The throat contracts once and drives the thick bolus into the top of the esophagus. The camera begins moving forward."),
            ("2.0 – 4.0 s", "Rings of muscle squeeze the tube shut behind the mass, which deforms around each contraction rather than running ahead of it. The head leaves the top of frame."),
            ("4.0 – 6.0 s", "The mass passes behind the heart, which beats steadily twice in this window. The frame tightens onto the lower ribs."),
            ("6.0 – 8.0 s", "The stomach fills the lower half of frame, pink and empty, and the ring of muscle at its entrance opens in front of the arriving mass as the camera eases to a stop."),
        ],
        light="The faint cyan glow inside the esophagus travels down the tube just ahead of the bolus, and fades out as the shot ends. Key and rim unchanged.",
        cons="One motion: the swallow, as a single continuous travelling squeeze that never stops or restarts. The figure does not move, turn or gesture; the only other movement in frame is the heartbeat.",
        note=("Note · reuse keyframe A", "This is <strong>keyframe A</strong> from the egg video — the torso with the esophagus and stomach visible. Use the same approved still as the start frame; only the colour and thickness of the bolus changes. <strong>Re-run the motion prompt — never paste the egg video's rendered clip into this one.</strong>"),
    ),
    dict(
        n=3, name="The gel forms", where="Stomach · cutaway → macro",
        tc="0:16.000 → 0:24.000", kf=("new", "new still"),
        colour="#c9a06a", palette="warm honey · close → macro",
        vo="The fibre soaks up water, and the whole mass thickens into a slow, heavy gel.",
        spoken=5.64,
        ends="A thick pale honey-coloured gel filling the lower half of the frame, its surface slumping very slowly under its own weight, with a single strand drawing out and settling back into it.",
        img=[
            ("SHOT 3 OF 8 — THE GEL FORMS.", "The stomach, seen close inside the body, its near wall cut away, with the oat mass swelling in the fluid inside it."),
            ("SCENE", "The same figure, now framed on the abdomen. The stomach fills most of the frame, sitting under the ribs, with the lower ribcage and the outline of the torso still visible around the edges of frame so it stays obvious that we are inside a human body. The near wall of the stomach is opened in a clean medical cutaway, revealing the interior: deep folded ridges of stomach lining in wet red-brown, a pool of warm fluid, and the pale cream oat mass lying in it. The flakes at the surface of the mass are visibly swelling, their edges softening and blurring into the liquid around them, and the whole mass is beginning to thicken and pull together into one body of pale honey-coloured gel that is denser and more translucent than the fluid around it."),
            ("CAMERA", "Medium close-up on the stomach, slightly high angle looking down into the cutaway, 40 mm equivalent lens, shallow depth of field with the swelling mass sharp in the foreground and the folded stomach lining soft behind it."),
            ("SUBJECT — the oats, stage 3 of 8", "The moment of change: separate soft flakes at 0 s, one thick continuous translucent gel by 8 s. The gel must look heavy — it slumps rather than pours, strands draw out of it and settle back, and it holds a shape for a moment before giving way."),
            ("LIGHT", "Strong warm amber light coming up through the fluid from below, turning the thickening gel to glowing pale honey. The mass lit hard from the upper left so its wet surface catches a highlight. Cyan rim light along the cut edge of the stomach wall, tying this shot to the two before it."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame picks up from there: the same body, the camera now settled on the stomach the bolus was entering, with that same mass lying in the fluid. Same figure, same cyan rim, same background."),
        ],
        real="the gastric rugae as thick irregular folds of pink-red mucosa, a glistening mucus layer lying over them, gastric pits reading as fine dark openings across the surface, the submucosal capillary network faintly visible through the lining, and the greater curvature of the stomach holding the mass.",
        cam="Push in, large amplitude, slow steady speed — the camera moves from the medium shot of the stomach forward through the cutaway opening and down to the surface of the mass, ending in macro with the gel filling the lower half of the frame. One straight continuous move on a single axis, constant speed, no shake, no rotation, no stopping.",
        beats=[
            ("0.0 – 2.0 s", "The stomach wall contracts once and the fluid moves around the mass. The flakes at its surface begin to swell, their edges softening. The camera starts pushing in."),
            ("2.0 – 4.0 s", "The push-in continues until the mass fills the frame. The gaps between the flakes close as each one swells into the next; the outline of individual flakes starts to disappear."),
            ("4.0 – 6.0 s", "The whole mass draws together into one continuous body of pale honey gel. The fluid around it visibly thins as the gel takes it up."),
            ("6.0 – 8.0 s", "The gel slumps slowly under its own weight, a single thick strand drawing out of the surface and settling back into it. It has stopped looking like food and started looking like a substance."),
        ],
        light="The amber underlight strengthens as the camera descends toward the mass, until by 6.0 s the whole frame is lit warmly from below and the gel is glowing from within.",
        cons="One motion: the thickening. It must read as <strong>swelling and drawing together</strong> — separate at 0 s, one continuous heavy gel at 8 s — never as melting, dissolving, boiling or foaming. One continuous transformation across the full eight seconds, never restarting.",
        note=("Note · the money shot", "This is the best single piece of motion in the whole five-video series and the reason to make this one. It is also the shot that opens the finished cut. <strong>The test is the last two seconds: does it slump like something heavy, or does it flow like a liquid?</strong> If it flows, the gel is too thin and the shot has not landed — re-roll it with the slumping emphasised."),
    ),
    dict(
        n=4, name="Where we are now → the coated wall", where="Whole body → small intestine",
        tc="0:24.000 → 0:32.000", kf=("new", "new still"),
        colour="#5fc4e8", palette="cold blue — colour break · wide → macro",
        vo="That gel coats the wall of your small intestine, and everything moving through it slows down.",
        spoken=5.92,
        ends="The ridged inner surface of the small intestine seen close, with a smooth translucent layer of gel lying over it, and small pale particles drifting slowly through that layer rather than freely past it.",
        img=[
            ("SHOT 4 OF 8 — WHERE WE ARE NOW.", "The whole body seen at full length in cool blue, with the small intestine lit up inside the abdomen."),
            ("SCENE", "The same figure, now standing at full length facing camera in a dark navy void, rendered in cool blue X-ray tones: the skeleton, the organs and the outline of the muscles all visible through translucent blue skin. The small intestine, coiled in the centre of the abdomen, glows clear cyan-white and is the brightest thing in the body. Everything else is cool and dim. The figure stands still, arms slightly away from the sides, feet together."),
            ("CAMERA", "Wide: the whole figure from above the head to below the feet, filling about four-fifths of the frame height. Camera level at chest height, 50 mm equivalent lens, the whole figure in focus, the void behind it clean and empty."),
            ("SUBJECT — the oats, stage 4 of 8", "Not visible as food any more. Its position in the body is what is visible: the cyan-white glow in the abdomen is where it has reached."),
            ("LIGHT", "Cold: a cyan key from the front left and a deeper blue rim on both edges of the body. The abdomen self-illuminated from within. No warm light anywhere in this frame."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This is the one deliberate step back in the video — the same figure seen whole, so the viewer re-anchors and remembers this is happening inside a body. The glowing point in the abdomen is exactly where the previous shot just was, and the camera dives straight back into it."),
        ],
        real="the jejunum and ileum coiled through the centre of the abdomen with the frame of the colon around them, the liver under the right ribs, the stomach high on the left, and a correct skeleton — twelve pairs of ribs, the lumbar spine, the pelvis and the femoral heads.",
        cam="Push in, very large amplitude, decelerating hard — the camera leaves the wide figure quickly, then slows continuously the deeper it goes, as if the medium itself were thickening around the lens. By 6.0 s it is barely moving and by 7.0 s it has stopped, resting just above the coated lining. One continuous move, no cut, no rotation, and no point at which it speeds up again.",
        beats=[
            ("0.0 – 2.0 s", "The whole figure is held for a moment, the cyan-white glow in the abdomen pulsing once, then the camera moves in quickly and the torso fills the frame."),
            ("2.0 – 4.0 s", "The camera passes through the body wall into the intestine — and immediately begins to slow, as if it had entered something thicker than fluid."),
            ("4.0 – 6.0 s", "The ridged inner surface resolves ahead, with a smooth translucent layer lying over it. The approach is now crawling."),
            ("6.0 – 8.0 s", "The camera comes to rest just above the lining. Small pale particles drift through the gel layer above it, visibly slower and more reluctantly than they would through open fluid."),
        ],
        light="The whole clip is cold. As the camera enters the intestine the cyan key falls away and the light becomes a soft even blue-white coming through the gel itself, which glows faintly where it is thickest.",
        cons="One motion: a single continuous forward travel from the whole body down to the coated lining. No cut, no dissolve, no jump in scale, no rotation of the figure. The figure does not turn, move or gesture at any point.",
        note=("Note · the deliberate colour break", "Shot 3 is hot honey-amber and shot 4 opens ice blue, back to back on a hard cut. That jolt is doing retention work at the 24-second mark, which is roughly where a vertical video loses people — <strong>do not soften it and do not warm this shot up.</strong> The particles moving <em>slowly</em> in the last two seconds are the whole sentence; if they move freely, the shot has not landed."),
    ),
    dict(
        n=5, name="Through the wall, slowly", where="Intestinal villi · macro",
        tc="0:32.000 → 0:40.000", kf=("reuse", "reuse keyframe B"),
        colour="#e8899d", palette="pink + amber · macro",
        vo="Sugars cross the lining gradually now, a few at a time, through the tiny folds.",
        spoken=5.85,
        ends="Inside the capillary within a single villus: red blood cells flowing along with a few warm amber beads travelling among them, well spaced apart, the vessel wall arcing around the frame.",
        img=[
            ("SHOT 5 OF 8 — THROUGH THE WALL, SLOWLY.", "Extreme macro on the lining of the small intestine, so close that individual villi fill the frame, with a translucent gel layer lying over them."),
            ("SCENE", "The inner surface of the small intestine at extreme magnification: hundreds of soft finger-shaped villi rising toward camera, wet coral and rose pink, each faintly translucent with a fine red capillary network glowing just beneath its surface. A smooth translucent layer of pale honey gel lies over the whole field, softening the tips of the villi seen through it. Small warm amber beads move down through that gel toward the villus surfaces — clearly fewer and further apart than they would be in open fluid — and pass through into the capillaries underneath, where they can be seen travelling away inside the vessel."),
            ("CAMERA", "Macro, camera low among the villi looking very slightly up, 85 mm macro equivalent, very shallow depth of field: one band of villi razor sharp, the field in front of and behind it melting into soft pink bokeh."),
            ("SUBJECT — the oats, stage 5 of 8", "Single sugars: small, smooth, glowing warm amber beads. What matters is the <em>rate</em> — they arrive spaced out, a few at a time, never as a crowd or a flood."),
            ("LIGHT", "Warm amber light raking across from the right, catching every wet villus tip and the surface of the gel layer. Cool cyan fill from the left keeping the shadow side from going flat. The capillaries inside the villi glowing faintly red from within."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is that same gel layer and those same particles seen closer, at the surface they were drifting toward. Same intestine, same gel, same amber — the camera has simply arrived at the lining."),
        ],
        real="villi as finger-shaped projections of mucosa, each with a brush border of microvilli at its tip, a central lacteal running up its core, a capillary loop wrapped around that lacteal, goblet cells spaced between the absorptive cells, and the crypts sitting in the valleys at the base of each villus.",
        cam="Descend, small amplitude, very slow — the camera starts above the gel layer and sinks straight down through it onto the villus tips across the full eight seconds, so the shot passes through the coating rather than moving along it. Constant speed, no sideways drift, no rotation, no stop. The heaviness of the move is the subject.",
        beats=[
            ("0.0 – 2.0 s", "The camera sinks toward the translucent gel layer, which softens and blurs the villus tips seen through it."),
            ("2.0 – 4.0 s", "The lens passes into the gel. A few amber beads work their way down through it alongside the camera, slowly, while others stay held up above."),
            ("4.0 – 6.0 s", "The camera emerges just above the villus tips. Those few beads settle against the surface and pass through the wall."),
            ("6.0 – 8.0 s", "The descent stops at one villus and its capillary fills the frame, red cells and a few well-spaced amber beads flowing along together."),
        ],
        light="Warm amber key holds throughout. The capillaries brighten from within as the beads enter them, but gently — this shot never gets bright, because nothing here arrives all at once.",
        cons="One motion: the drift and the slow crossing. The villi sway gently and continuously — they never whip, wave, snap or pulse in unison. <strong>Beads must arrive spaced out, never as a surge or a swarm</strong>; the rate is the subject of the sentence.",
        note=("Note · reuse keyframe B, with one addition", "This is <strong>keyframe B</strong> from the egg video with a translucent gel layer added over it. It is the one reuse in the series that needs a small change to the still itself — everywhere else the keyframe drops in untouched. Generate it once with the gel and it becomes a second reusable asset for any future fibre topic."),
    ),
    dict(
        n=6, name="Into the blood", where="Capillary → liver → whole body",
        tc="0:40.000 → 0:48.000", kf=("reuse", "reuse keyframe C"),
        colour="#cf6f70", palette="red + blue → whole body · macro → wide",
        vo="Your blood receives them as a slow, steady rise instead of one sudden surge.",
        spoken=5.36,
        ends="The whole body seen at full length, its entire arterial and venous tree visible as a fine red-and-blue network, with amber points spread evenly along it and the whole network brightening very slowly and steadily.",
        img=[
            ("SHOT 6 OF 8 — INTO THE BLOOD.", "Inside a blood vessel, with the branching vessel tree visible far beyond it."),
            ("SCENE", "Macro inside a blood vessel: glossy dark red biconcave red blood cells tumbling toward camera through translucent straw-coloured plasma, with warm amber beads travelling among them, well spaced apart and evenly distributed rather than clustered. The vessel wall arcs around the edges of frame in translucent pink, lit with a cold rim so the shape of the tube is readable. Far beyond the cells, out of focus, the vessel branches away into a fine network."),
            ("CAMERA", "Macro inside the vessel, camera in the centre of the flow facing along it, 50 mm equivalent lens, sharp focal plane through the middle of frame with the cells at the frame edges softened by motion blur."),
            ("SUBJECT — the oats, stage 6 of 8", "The same warm amber beads, now travelling in blood among the red cells — evenly spaced, arriving at a steady rate, never bunched."),
            ("LIGHT", "Deep red ambient from the blood itself, a cold blue rim along the vessel wall, and the amber beads carrying their own light. Strong red-and-blue contrast, warm centre and cool edges."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is that same capillary, one moment later, with the camera now inside the flow. Same beads, same amber, same blood."),
        ],
        real="red blood cells with their true biconcave dimpled shape and no nucleus, an endothelial lining one cell thick with the cell junctions faintly visible, vessels branching by real bifurcation into narrower ones — and at the wide end, an arterial tree in red and a venous tree in blue following real vascular anatomy.",
        cam="Hold, then pull out, very large amplitude at one unvarying speed — the camera stays completely still for the first two seconds, then begins retreating and continues at exactly the same rate to the end, stopping only in the last quarter second. Nothing about this move accelerates at any point, because nothing about this video surges. No rotation, no shake.",
        beats=[
            ("0.0 – 2.0 s", "The camera is still. Red cells and evenly spaced amber beads move past the lens at a steady rate, none of them bunched."),
            ("2.0 – 4.0 s", "The retreat begins and the vessel widens and joins others. The camera passes through the dense red tissue of the liver."),
            ("4.0 – 6.0 s", "The camera leaves the abdomen. The torso resolves, then the whole figure, its vessel tree lighting up as a fine red-and-blue network."),
            ("6.0 – 8.0 s", "The move stops on the whole standing figure. The amber points are spread evenly through the network and the whole thing brightens by a small, steady amount — no spike, no wave, no flare."),
        ],
        light="Starts deep red from inside the blood and cools steadily as the camera retreats, ending on the cool blue-and-red network of the whole figure. The final brightening is slow and small — it must never read as a surge.",
        cons="One motion: a single continuous pull-out from inside a vessel to the whole body. No cut, no dissolve, no jump in scale. <strong>Nothing floods, spikes, pulses or flashes at any point</strong> — this is the one video in the series whose subject is a rate, and a burst of light would say the opposite of the sentence.",
        note=("Note · reuse keyframe C", "This is <strong>keyframe C</strong> from the egg video. The difference is entirely in the motion: the egg sends a wave of gold outward, and here <strong>the rise is slow, small and even</strong>. If the render produces a surge of light at the end, it has contradicted the narration — re-run it with the last beat emphasised."),
    ),
    dict(
        n=7, name="What the fibre feeds", where="Colon · macro",
        tc="0:48.000 → 0:56.000", kf=("new", "new still"),
        colour="#8f9d6a", palette="olive + warm pink · macro, near-still",
        vo="Further along, the fibre that survived becomes food for the bacteria living in your gut.",
        spoken=5.92,
        ends="The colon lining lit warmly from within, dense with bacteria working over the last strands of fibre, everything settled and moving only very slightly.",
        img=[
            ("SHOT 7 OF 8 — WHAT THE FIBRE FEEDS.", "Extreme macro on the inner lining of the colon, with the outline of the lower abdomen still faintly visible at the edge of frame."),
            ("SCENE", "Extreme macro inside the large intestine: the lining here is flat and smooth compared with the small intestine — no finger-shaped villi, just a gently rolling surface of wet pink-red mucosa with fine dark pit openings across it, covered by a thick translucent mucus layer. Lying on and in that layer are the remains of the oat fibre — pale honey-coloured strands and fragments, softened and frayed. Living over them is a dense, varied community of bacteria: countless tiny rods, spheres and short chains in pale cream, olive and soft green, packed close together, moving very slightly, clustered thickest where the fibre is. The outline of the lower abdomen is faintly visible at the very edge of frame."),
            ("CAMERA", "Extreme macro, camera close and level with the lining, 100 mm macro equivalent, very shallow depth of field: the nearest cluster of bacteria and the fibre they sit on razor sharp, the rest of the field falling away soft, the body outline at the edge reduced to a suggestion."),
            ("SUBJECT — the oats, stage 7 of 8", "The last of it: the fibre that was never broken down, frayed and softened, now being worked over. This is the only shot in the series where the subject ends up feeding something other than the body itself."),
            ("LIGHT", "Warm key from the upper right raking across the lining and catching the wet mucus layer. Cool blue rim along the top edge. Deep shadow in the low places between folds. The bacteria pale against the darker tissue."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is further down the same journey — the camera has followed what was not absorbed into the large intestine. Same body, same warm-and-cool light, same honey-coloured fibre material."),
        ],
        real="the colon lining, which unlike the small intestine has <em>no villi</em> — a flat mucosal surface with straight tubular crypts opening onto it, abundant goblet cells and a thick two-layer mucus blanket over the top, haustral folds bulging the wall at intervals, and a dense mixed microbial community sitting in the outer mucus layer.",
        cam="Static shot, with the faintest push in — under 5% across the whole eight seconds, so slow it is barely perceptible. No pan, no tilt, no truck, no rotation, no shake. This is deliberately the stillest shot in the video.",
        beats=[
            ("0.0 – 2.0 s", "Almost nothing moves. The mucus layer shifts very slightly. Bacteria sit clustered on the fibre strands."),
            ("2.0 – 4.0 s", "The clusters thicken as more bacteria gather along the strands. Individual cells divide slowly here and there."),
            ("4.0 – 6.0 s", "The fibre strands soften and fray further where the bacteria are densest, their edges going indistinct."),
            ("6.0 – 8.0 s", "The lining beneath brightens very slightly and warmly, and everything settles. Only the faintest drift remains."),
        ],
        light="A slow, small warm-up over the eight seconds: the lining is dim at 0 s and gently warm by 8 s. No flash, no pulse, no bloom.",
        cons="One motion: bacteria gathering and fibre softening, both very slow. Nothing swarms, boils, explodes or moves fast. This is the calm shot before the last one and the stillness is deliberate.",
        note=("Note · the shot to get anatomically right", "The easiest mistake here is villi — <strong>the colon has none</strong>, and a generator that has learned “intestine” will put them in. The REAL ANATOMY line in the prompt says so explicitly; check the still before rendering. Get this one right and it becomes the permanent asset for any gut-bacteria video later."),
    ),
    dict(
        n=8, name="A steady supply", where="Whole body · hero",
        tc="0:56.000 → 1:04.000", kf=("reuse", "reuse keyframe D"),
        colour="#e8c87f", palette="steady warm gold — colour break 2 · full body",
        vo="Your body is running on a steady supply instead of a spike, hour after hour.",
        spoken=5.19,
        ends="The whole figure standing still, its vessel network lit an even, steady warm gold that does not waver, the camera stopped — a clean frame to hold under the end card.",
        img=[
            ("SHOT 8 OF 8 — A STEADY SUPPLY.", "The same figure at full length, its vessel network glowing an even, steady warm gold from within."),
            ("SCENE", "The same adult anatomical figure standing at full length facing camera in a dark void, seen from the front. The body is translucent and smooth, the head without facial features and without hair. Its internal vessel network glows warm gold from within, even and unwavering from the torso out to the fingers and toes, with no brighter centre and no hot spots anywhere. A soft warm haze surrounds the figure. The background is the same dark navy falling to black as every other shot."),
            ("CAMERA", "Wide: the whole figure from above the head to below the feet, filling about two-thirds of the frame height, centred, camera level at chest height, 50 mm equivalent lens, the whole figure in sharp focus."),
            ("SUBJECT — the oats, stage 8 of 8", "No longer a separate object at all. It is the steady gold light in the vessel network — one bowl of oats, released slowly, and still arriving."),
            ("LIGHT", "Warm gold from inside the body, even throughout, with a soft gold ambient haze around it and a cool blue rim on both edges. Steady is the word that matters: nothing in this frame flares, spikes or pulses."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame matches on that warm light: the same glow, at the scale of the whole body. It reads as the camera stepping all the way back at the end of the journey. Same figure, same rim light, same background as shot 1."),
        ],
        real="a correct arterial and venous tree — the aorta arching out of the heart, the carotids up the neck, the subclavians into the arms, the femorals down the legs — branching to fine peripheral vessels over a correct skeleton, with true adult human proportion.",
        cam="Push in, very small amplitude, stopping early — about 6% over the first four seconds, then a complete stop at 4.0 s and a full four seconds of absolute stillness. Half the shot is motionless, which is twice as long as any other hero shot in the series holds. No rotation, no orbit, no shake. The figure never turns.",
        beats=[
            ("0.0 – 2.0 s", "The gold glow rises evenly through the whole vessel network, slowly. The camera begins its very small push in."),
            ("2.0 – 4.0 s", "The rise continues at exactly the same rate until the network is fully lit. The camera stops at 4.0 s."),
            ("4.0 – 6.0 s", "Nothing moves and nothing changes. The glow holds absolutely steady."),
            ("6.0 – 8.0 s", "Still nothing moves. The figure stands lit and even, held for the end card."),
        ],
        light="A single continuous, perfectly even rise from dim to full over six seconds, then held without any flicker or variation. <strong>No pulsing, no strobing, no beat, no travelling wave</strong> — the steadiness is the message of the whole video.",
        cons="One motion: the glow rising evenly and then holding. The figure does not move, breathe visibly, turn, gesture or shift weight. No particles, no rays, no energy effects, no lens flare.",
        note=("Note · reuse keyframe D", "This is <strong>keyframe D</strong> from the egg video, and the difference is entirely in how it is lit over time: the egg glow rises and settles, this one <strong>rises at a constant rate and then does not move at all</strong>. That difference is the video's argument, made in light rather than in words. Specify <em>no facial features</em> again."),
    ),
]

TOPIC["clips"] = CLIPS
