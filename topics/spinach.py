"""Video 5 — "What happens when you eat spinach."

Beats follow the map published in section 08 of the main teardown page.
Timings are measured from the rendered voice-over, not estimated.
"""

TOPIC = dict(
    slug="spinach",
    video_no=5,
    lane="circulation lane",
    emoji="🥬",
    accent="#7fd66a",
    glow="rgba(127,214,106,.13)",
    h1_plain="What happens when you eat spinach",
    title_html="What happens<br>when you eat<br><em>spinach.</em>",
    sub=("The strongest cold open in the series, because this journey starts before the swallow — the bacteria "
         "living on your tongue do the first step of the work. Full script, <strong>voice-over already rendered and "
         "measured</strong>, and all 16 prompts written out, every shot handing its last frame to the next one."),
    palette=("warm flesh pink and deep red tissue, deep green spinach leaf, a tiny pale blue-white gas molecule, "
             "cool cyan-teal rim light, dark navy background falling to black, with two or three very soft "
             "out-of-focus blue holographic panels far behind the subject blurred into pure glow"),
    vo_file="vo-spinach-64s.mp3",
    kf_chip="Reuses keyframes <b>A–D</b>",
    locks="the deep green leaf material",
    chain_break=("Two of the seven cuts are scale jumps rather than continuous handoffs: <strong>into shot 4</strong> "
                 "(the stomach fluid, out to the whole body) and <strong>into shot 8</strong> (one vessel, out to the "
                 "whole body). Both sit where the egg video puts them, and both are doing a job — shot 4 re-anchors "
                 "the viewer at the 24-second retention dip, shot 8 is the payoff. They are still matched: shot 4 "
                 "opens on the glow in the abdomen, exactly where shot 3 just was, and shot 8 matches on the pale "
                 "light coming out of shot 7."),
    compliance=("Sentences 1–7 describe only what happens. Sentence 8 says blood moves easily through a body that is "
                "holding its own vessels open — a description of a mechanism, and it stops there. <strong>Never "
                "write “lowers blood pressure”. That is a drug claim, not a nutrition one</strong>, and on this "
                "subject it is the hardest line in the whole series to resist, because it is the obvious payoff of "
                "everything the video just showed. No athletic-performance angle either, and no numbers. The vessel "
                "wall <em>relaxes</em>; end the sentence."),
    caption_words="“esophagus”, “compound”, “villi” and “vessel”",
    hook_step=("Copy the first second of clip 1's ending — the tongue surface at extreme macro with the bacteria "
               "alive on it — to the very front of the timeline, then hard-cut back to the mouth. “This starts "
               "before you swallow” is the whole hook. The voice-over does not move: it still starts at 0:00."),
    check_hook="The first second is the tongue at macro, not the mouth",
    kf_box_title="Four of these eight stills are already made",
    kf_box=("Clips 2, 5, 6 and 8 are anatomy, not spinach — the torso with the esophagus and stomach, the field of "
            "villi, the vessel network, the whole body. They are <strong>keyframes A, B, C and D</strong> from the "
            "egg video and they drop straight in as the start frames here. This video needs four new stills: the "
            "leaf on the tongue, the stomach, the gas molecule forming and the vessel wall opening."),
    keep=("One new permanent asset — <strong>the vessel-wall still from clip 7</strong>, a cross-section of a real "
          "artery that any future circulation topic starts from — and the fifth and final use of keyframes A to D, "
          "which by this point have paid for themselves four times over."),
    hard_clips="clips 1, 4 and 7",
    prev=("oats", "Oats"),
    next=None,
)

CLIPS = [
    dict(
        n=1, name="It starts on the tongue", where="Mouth → tongue surface · close-up → macro",
        tc="0:00.000 → 0:08.000", kf=("new", "new still"),
        colour="#6f9e5a", palette="warm flesh + deep green · close-up → macro",
        vo="When you eat spinach, the bacteria living on your tongue start changing the leaves immediately.",
        spoken=5.83,
        ends="Extreme macro on the surface of the tongue: papillae standing up like a dense soft forest, dark green leaf fragments pressed among them, and colonies of bacteria packed into the crevices between, already working on the leaf.",
        img=[
            ("SHOT 1 OF 8 — IT STARTS ON THE TONGUE.", "A hyper-realistic anatomical human head in three-quarter profile with spinach leaves in the mouth."),
            ("SCENE", "An adult human head and shoulders turned three-quarters toward camera against a dark navy background. The skin is semi-transparent, so the skull, the jaw and cheek muscles, the tongue and the whole row of teeth read clearly through it — the look of a high-end medical visualisation figure. The face is calm and neutral, eyes open, no expression. The mouth is open and dark green spinach leaves are on the tongue, torn and folded, their surfaces wet and glossy, the pale ribs of the leaves catching the light. Below the jaw, through the neck, the throat and the top of the esophagus are visible as a pale ribbed tube running down behind the windpipe."),
            ("CAMERA", "Medium close-up: the frame runs from the top of the skull down to the collarbones. Camera at mouth height, level with the face, 50 mm equivalent lens, shallow depth of field with the lips, tongue and leaves razor sharp and the back of the head falling soft."),
            ("SUBJECT — the spinach, stage 1 of 8", "Fresh spinach leaves: deep saturated green, slightly translucent where the light passes through them, with visible pale veins and a wet glossy surface. They must read instantly and unmistakably as leaves, not as any other green material."),
            ("LIGHT", "One warm key light from the upper left catching every wet highlight on the teeth, the tongue and the leaf surfaces. A cool cyan rim light along the jawline and cheekbone separating the head from the background. Deep shadow behind the head."),
            ("CONTINUITY", "This is the opening shot and it locks the look for the whole video: this exact figure, this exact skin translucency, this exact deep green leaf material, this warm-key-plus-cyan-rim lighting and this dark navy background appear in all eight shots. Nothing about the look changes after this frame."),
        ],
        real="the papillae covering the surface of the tongue — the fine pointed ones over most of the surface and the larger round ones toward the back — the pink gum margin around each tooth, the wet mucosa of the inner cheek, the masseter and temporalis muscles under the skin, and the deep crevices between papillae where the tongue's own bacterial colonies live.",
        cam="Push in, very large amplitude, accelerating from slow to moderate and easing off at the end — the camera travels straight in from the medium close-up on the head, past the lips, and down onto the surface of the tongue, ending in extreme macro among the papillae. One continuous move on a single axis, no cut, no stop, no rotation, no shake.",
        beats=[
            ("0.0 – 2.0 s", "The jaw closes once on the leaves and the leaves fold and tear between the teeth. The camera begins to travel forward."),
            ("2.0 – 4.0 s", "The camera passes the lips and the mouth fills the frame. The tongue surface resolves as texture rather than as a shape."),
            ("4.0 – 6.0 s", "Extreme macro: papillae stand up like a dense soft forest, with torn green leaf fragments pressed down among them."),
            ("6.0 – 8.0 s", "Colonies of bacteria come into focus in the crevices between the papillae, dense and alive, moving very slightly, already crowded onto the leaf fragments nearest them."),
        ],
        light="The warm key holds all the way in. As the camera reaches macro the light becomes softer and more enclosed, with a faint green bounce coming off the leaf fragments onto the papillae around them.",
        cons="One motion: a single continuous travel in from the whole head to the surface of the tongue. No cut, no dissolve, no jump in scale. The head does not turn, nod, tilt or speak. The bacteria move very slightly — they never swarm, boil or stream.",
        note=("Note · the cold open of the series", "This is the shot nobody expects and the reason this topic is worth making. It is also the only clip in the whole five-video run that <strong>travels from a whole head to a microscopic surface in one take</strong>, so it is the hardest single generation on this page — budget retries. The last second of it doubles as the video's opening hook."),
    ),
    dict(
        n=2, name="The swallow", where="Throat → stomach · torso wide",
        tc="0:08.000 → 0:16.000", kf=("reuse", "reuse keyframe A"),
        colour="#b9846f", palette="warm flesh + cyan rim · medium wide",
        vo="You swallow, and your esophagus carries that changed compound down toward your stomach.",
        spoken=5.74,
        ends="The whole upper body is in frame. The dark green mass has arrived at the lower end of the esophagus and the ring of muscle at the stomach entrance is opening in front of it. The stomach below is pink and empty.",
        img=[
            ("SHOT 2 OF 8 — THE SWALLOW.", "The same figure, one step wider: head, neck and upper chest, with the esophagus visible running down inside the body."),
            ("SCENE", "The same adult anatomical figure as shot 1, at the same three-quarter angle, now framed wider so the head, the whole neck and the upper chest are in view. Through the semi-transparent skin and the pale ribcage, the esophagus runs from the back of the throat down the centre of the chest, behind the heart, as a soft ribbed muscular tube. A dark green chewed mass sits at the very top of that tube, just entering it, with a faint pale glow spread through it where the tongue's bacteria have already changed it. The ring muscles of the esophagus read as evenly spaced bands along its length. A faint cool cyan glow runs down inside the tube ahead of the mass, showing the direction of travel as a soft travelling light."),
            ("CAMERA", "Medium wide: the frame runs from just above the head down to the bottom of the ribcage. Camera level, 35 mm equivalent lens, moderate depth of field with the esophagus and the mass sharp and the shoulders falling slightly soft."),
            ("SUBJECT — the spinach, stage 2 of 8", "No longer whole leaves: a soft dark green bolus roughly the size of a walnut, wet and folded, carrying a faint pale glow through it — the same green material as shot 1 in a new shape, plus the first sign of the change that started in the mouth."),
            ("LIGHT", "Warm key from the upper left across the chest. Cool cyan rim down the left edge of the neck and shoulder. The esophagus glowing very faintly from within along its length, and the pale glow inside the bolus reading clearly against the dark green."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is that same figure, pulled back out to the body, with that same leaf material — and the change those bacteria started — now formed into a bolus at the top of the esophagus. Same skin, same light, same background, same green."),
        ],
        real="the esophagus as a muscular tube lying behind the trachea and in front of the spine, its wall built from an inner circular and an outer longitudinal muscle layer, the aortic arch and the left main bronchus crossing in front of it, the diaphragm it passes through, and the lower esophageal sphincter where it opens into the stomach.",
        cam="Hold, then pull out, large amplitude — the camera holds on the head, neck and upper chest for the first three seconds, close enough that the pale glow inside the bolus is clearly readable, then retreats steadily to the whole upper body across the last five. One continuous move once it starts, no shake, no rotation.",
        beats=[
            ("0.0 – 2.0 s", "The camera is still. The throat contracts once and drives the bolus into the top of the esophagus, the pale glow inside it clearly visible at this distance."),
            ("2.0 – 4.0 s", "The retreat begins. Rings of muscle contract in sequence from the top downward, pushing the bolus about a third of the way down."),
            ("4.0 – 6.0 s", "The pull-out reveals the ribcage and the lungs. The bolus passes behind the heart, which beats steadily twice in this window."),
            ("6.0 – 8.0 s", "The stomach comes into frame below the ribs, pink and empty, and the ring of muscle at its entrance opens in front of the arriving bolus as the camera stops."),
        ],
        light="The faint cyan glow inside the esophagus travels down the tube just ahead of the bolus, and fades out as the shot ends. The pale glow inside the bolus strengthens very slightly across the eight seconds. Key and rim unchanged.",
        cons="One motion: the swallow, as a single continuous travelling squeeze that never stops or restarts. The figure does not move, turn or gesture; the only other movement in frame is the heartbeat.",
        note=("Note · reuse keyframe A", "This is <strong>keyframe A</strong> from the egg video — the torso with the esophagus and stomach visible. Use the same approved still as the start frame; only the colour of the bolus and the pale glow inside it change. <strong>Re-run the motion prompt — never paste the egg video's rendered clip into this one.</strong>"),
    ),
    dict(
        n=3, name="The acid finishes it", where="Stomach · cutaway → macro",
        tc="0:16.000 → 0:24.000", kf=("new", "new still"),
        colour="#c08f4a", palette="warm amber + green · close → macro",
        vo="Your stomach acid finishes the conversion your tongue started, in the warm fluid there.",
        spoken=5.49,
        ends="A drift of tiny pale blue-white points rising out of the dark green mass into the amber fluid above it, spreading slowly apart from one another.",
        img=[
            ("SHOT 3 OF 8 — THE ACID FINISHES IT.", "The stomach, seen close inside the body, its near wall cut away so the inside is visible."),
            ("SCENE", "The same figure, now framed on the abdomen. The stomach fills most of the frame, sitting under the ribs, with the lower ribcage and the outline of the torso still visible around the edges of frame so it stays obvious that we are inside a human body. The near wall of the stomach is opened in a clean medical cutaway, revealing the interior: deep folded ridges of stomach lining in wet red-brown, a churning pool of warm amber gastric fluid, and the dark green spinach mass lying in it, softening and fraying at its edges. The pale glow the mass carried in is brightening, and the first tiny pale blue-white points are lifting off it into the fluid."),
            ("CAMERA", "Medium close-up on the stomach, slightly high angle looking down into the cutaway, 40 mm equivalent lens, shallow depth of field with the green mass sharp in the foreground and the folded stomach lining soft behind it."),
            ("SUBJECT — the spinach, stage 3 of 8", "The green mass giving up what it was carrying: dark green and fraying, with pale blue-white points separating out of it and rising. The green stays green — it is not dissolving away, it is releasing something."),
            ("LIGHT", "Strong warm amber light coming up through the gastric fluid from below, turning it to glowing honey. The green mass lit hard from the upper left so its wet folds catch a highlight and read clearly against the amber. Cyan rim light along the cut edge of the stomach wall, tying this shot to the two before it."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame picks up from there: the same body, the camera now settled on the stomach the bolus was entering, with that same green mass lying in the acid. Same figure, same cyan rim, same background."),
        ],
        real="the gastric rugae as thick irregular folds of pink-red mucosa, a glistening mucus layer lying over them, gastric pits reading as fine dark openings across the surface, the submucosal capillary network faintly visible through the lining, and the greater curvature of the stomach holding the pool.",
        cam="Push in, large amplitude, slow steady speed — the camera moves from the medium shot of the stomach forward through the cutaway opening and into the fluid, ending in macro just above the surface of the green mass with the rising points filling the centre of frame. One straight continuous move on a single axis, constant speed, no shake, no rotation, no stopping.",
        beats=[
            ("0.0 – 2.0 s", "The stomach wall contracts once and the amber fluid swirls around the green mass, which rolls slightly and frays further at its edges. The camera begins pushing in."),
            ("2.0 – 4.0 s", "The push-in continues until the mass fills the lower half of frame. The pale glow inside it strengthens along the torn edges."),
            ("4.0 – 6.0 s", "The first tiny pale blue-white points lift off the surface and rise slowly into the fluid, tumbling as they go."),
            ("6.0 – 8.0 s", "More follow, spreading apart from one another as they rise, until a loose drift of them fills the fluid above the green mass."),
        ],
        light="The amber underlight strengthens as the camera descends into the fluid, until by 6.0 s the whole frame is lit from below and the pale rising points are the coolest, brightest things in it.",
        cons="One motion: the release. It must read as something <strong>coming out of</strong> the green mass and rising — not as the mass dissolving, melting, exploding or disappearing. The green stays. One continuous transformation across the full eight seconds, never restarting.",
        note=("Note", "The distinction that matters: <strong>the spinach is not being destroyed here, it is handing something over.</strong> If the generation dissolves the leaf mass away to nothing, the shot contradicts the sentence — re-roll it with the green holding its shape while the pale points leave it."),
    ),
    dict(
        n=4, name="Where we are now → the molecule", where="Whole body → macro",
        tc="0:24.000 → 0:32.000", kf=("new", "new still"),
        colour="#5fc4e8", palette="cold blue — colour break · wide → macro",
        vo="A tiny gas molecule forms, one of the smallest signals your body uses.",
        spoken=5.46,
        ends="Looking straight down at one tiny pale blue-white gas molecule alone below the lens, far smaller than anything else drifting in the fluid around it, turning very slowly.",
        img=[
            ("SHOT 4 OF 8 — WHERE WE ARE NOW.", "The whole body seen at full length in cool blue, with the stomach and upper abdomen lit up inside it."),
            ("SCENE", "The same figure, now standing at full length facing camera in a dark navy void, rendered in cool blue X-ray tones: the skeleton, the organs and the outline of the muscles all visible through translucent blue skin. The stomach and the upper abdomen glow clear cyan-white and are the brightest part of the body. Everything else is cool and dim. The figure stands still, arms slightly away from the sides, feet together."),
            ("CAMERA", "Wide: the whole figure from above the head to below the feet, filling about four-fifths of the frame height. Camera level at chest height, 50 mm equivalent lens, the whole figure in focus, the void behind it clean and empty."),
            ("SUBJECT — the spinach, stage 4 of 8", "Not visible as a leaf any more. Its position in the body is what is visible: the cyan-white glow in the abdomen is where it has reached."),
            ("LIGHT", "Cold: a cyan key from the front left and a deeper blue rim on both edges of the body. The abdomen self-illuminated from within. No warm light anywhere in this frame."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This is the one deliberate step back in the video — the same figure seen whole, so the viewer re-anchors and remembers this is happening inside a body. The glowing point in the abdomen is exactly where the previous shot just was, and the camera dives straight back into it."),
        ],
        real="a correct skeleton — twelve pairs of ribs, the lumbar spine, the pelvis and the femoral heads — with the stomach high on the left under the diaphragm, the liver filling the space under the right ribs, and the coiled small intestine below them, all in true adult human proportion.",
        cam="Descend, very large amplitude, accelerating then easing — the camera starts wide on the standing figure and cranes downward and forward at the same time, entering the body from above rather than head-on, so the shot travels down the front of the torso and into the abdomen. It ends looking straight down at a single molecule in the fluid below. One continuous move, no cut, no stop, no rotation.",
        beats=[
            ("0.0 – 2.0 s", "The whole figure is held in frame and the cyan-white glow in the abdomen pulses once, softly. The camera begins to crane down from above."),
            ("2.0 – 4.0 s", "The descent steepens. The head passes out of the top of frame and the torso fills the picture, the glow rising toward the lens."),
            ("4.0 – 6.0 s", "The camera drops through the body wall into dark fluid, now looking straight down. Pale points at every scale stream up past the lens as it falls."),
            ("6.0 – 8.0 s", "The fall slows to a stop. One very small pale blue-white molecule is left directly below the lens, in focus, turning slowly — noticeably smaller than everything drifting past it."),
        ],
        light="The whole clip is cold. As the camera enters the body the cyan key falls away and the only light left is the faint blue-white glow the molecule carries itself, against a dark blue ambient.",
        cons="One motion: a single continuous forward travel from the whole body down to one molecule. No cut, no dissolve, no jump in scale, no rotation of the figure. The figure does not turn, move or gesture at any point.",
        note=("Note · the deliberate colour break, and one thing to check", "Shot 3 is hot amber and shot 4 opens ice blue, back to back on a hard cut. That jolt is doing retention work at the 24-second mark — <strong>do not soften it.</strong> The other thing to check in the render: <strong>the molecule must be visibly tiny</strong> next to everything else in the fluid. The sentence says “one of the smallest signals your body uses”, and scale is the only way the picture can say it."),
    ),
    dict(
        n=5, name="Through the wall", where="Intestinal villi · macro",
        tc="0:32.000 → 0:40.000", kf=("reuse", "reuse keyframe B"),
        colour="#e8899d", palette="pink + pale blue · macro",
        vo="It crosses the wall of your small intestine, through the folds, into the vessels below.",
        spoken=5.49,
        ends="Inside the capillary within a single villus: red blood cells and tiny pale blue-white points flowing along together, the vessel wall arcing around the frame.",
        img=[
            ("SHOT 5 OF 8 — THROUGH THE WALL.", "Extreme macro on the lining of the small intestine, so close that individual villi fill the frame."),
            ("SCENE", "The inner surface of the small intestine at extreme magnification: hundreds of soft finger-shaped villi rising toward camera, wet coral and rose pink, each faintly translucent with a fine red capillary network glowing just beneath its surface. Tiny pale blue-white points drift down between them from the fluid above, reach the villus surfaces and pass straight through into the capillaries underneath, where they can be seen travelling away inside the vessel. They are small enough to cross without effort and the picture should show that — no gathering, no queueing, no pushing through."),
            ("CAMERA", "Macro, camera low among the villi looking very slightly up, 85 mm macro equivalent, very shallow depth of field: one band of villi razor sharp, the field in front of and behind it melting into soft pink bokeh."),
            ("SUBJECT — the spinach, stage 5 of 8", "The same tiny pale blue-white points, crossing a living surface as if it were not there. Their smallness is the whole characteristic — they are the smallest thing in every frame they appear in."),
            ("LIGHT", "Warm pink light raking across from the right, catching every wet villus tip. Cool cyan fill from the left keeping the shadow side from going flat. The capillaries inside the villi glowing faintly red from within, and the points carrying a cold pale light of their own."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is that same molecule among many more like it, arriving at the lining. Same fluid, same pale blue light, same scale — the camera has simply arrived at the surface."),
        ],
        real="villi as finger-shaped projections of mucosa, each with a brush border of microvilli at its tip, a central lacteal running up its core, a capillary loop wrapped around that lacteal, goblet cells spaced between the absorptive cells, and the crypts sitting in the valleys at the base of each villus.",
        cam="Truck left, moderate amplitude, decelerating to a complete stop — the camera drifts sideways across the field of villi, slowing continuously, and is completely still from 6.0 s to the end. The direction is the opposite of the egg video's move on this same still, and the stop is what marks how easily this subject crosses: the camera stops, and it has already gone through.",
        beats=[
            ("0.0 – 2.0 s", "The camera drifts left past the field of villi, which sway very slightly in the moving fluid. Tiny pale points drift down from above."),
            ("2.0 – 4.0 s", "The points reach the villus surfaces and pass straight through them without pausing. The drift begins to slow."),
            ("4.0 – 6.0 s", "Inside the villi, the capillary networks show pale points already travelling along them. The camera comes to rest on one villus."),
            ("6.0 – 8.0 s", "Completely still. The frame holds on that villus and its capillary, red cells and pale points flowing along together inside it."),
        ],
        light="Warm pink key holds throughout. The capillaries brighten from within as the points enter them, so the last two seconds are slightly cooler and brighter inside the villus than the first two.",
        cons="One motion: the drift and the crossing. The villi sway gently and continuously in the current — they never whip, wave, snap or pulse in unison. Nothing bursts, splits or explodes.",
        note=("Note · reuse keyframe B", "This is <strong>keyframe B</strong> from the egg video, and this is its fourth use — at which point the still has paid for itself several times over. Only the colour and size of what crosses changes: gold beads for the egg, pale blue-white for coffee, amber for oats, and here the smallest points in the series. Re-run the motion prompt."),
    ),
    dict(
        n=6, name="Into the blood", where="Capillary → whole body",
        tc="0:40.000 → 0:48.000", kf=("reuse", "reuse keyframe C"),
        colour="#cf6f70", palette="red + blue → whole body · macro → wide",
        vo="Your blood carries it out through the whole network, all the way to your vessel walls.",
        spoken=4.99,
        ends="The whole body seen at full length at a slight three-quarter angle, its entire arterial and venous tree visible as a fine red-and-blue network with real depth, and pale points spread out along it and gathering at the vessel walls themselves.",
        img=[
            ("SHOT 6 OF 8 — INTO THE BLOOD.", "Inside a blood vessel, with the branching vessel tree visible far beyond it."),
            ("SCENE", "Macro inside a blood vessel: glossy dark red biconcave red blood cells tumbling toward camera through translucent straw-coloured plasma, with tiny pale blue-white points travelling among them — much smaller than the cells and standing out cold against the red. The vessel wall arcs around the edges of frame in translucent pink, lit with a cold rim so the shape of the tube is readable. Some of the points are drifting toward that wall rather than staying in the middle of the flow. Far beyond the cells, out of focus, the vessel branches away into a fine network."),
            ("CAMERA", "Macro inside the vessel, camera in the centre of the flow facing along it, 50 mm equivalent lens, sharp focal plane through the middle of frame with the cells at the frame edges softened by motion blur."),
            ("SUBJECT — the spinach, stage 6 of 8", "The same tiny pale points, now travelling in blood — and beginning to move outward toward the wall of the vessel, which is where the next shot happens."),
            ("LIGHT", "Deep red ambient from the blood itself, a cold blue rim along the vessel wall, and the points carrying their own pale light. Strong red-and-blue contrast, warm centre and cool edges."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is that same capillary, one moment later, with the camera now inside the flow. Same points, same pale blue light, same blood."),
        ],
        real="red blood cells with their true biconcave dimpled shape and no nucleus, an endothelial lining one cell thick with the cell junctions faintly visible, vessels branching by real bifurcation into narrower ones — and at the wide end, an arterial tree in red and a venous tree in blue following real vascular anatomy out to the hands and feet.",
        cam="Pull out with a slow arc, very large amplitude — the camera retreats from inside the capillary to the whole standing figure while also drifting slowly around to one side, so the body is revealed at a slight three-quarter angle rather than straight on, and the depth of the vessel network is readable. One continuous move, constant speed, no shake, no spin — the arc is gentle and never becomes an orbit.",
        beats=[
            ("0.0 – 2.0 s", "Red cells and tiny pale points stream past the lens. The camera begins to retreat and, at the same time, to drift very slowly to one side."),
            ("2.0 – 4.0 s", "The vessel widens and joins others. Points drift outward toward the walls as they travel."),
            ("4.0 – 6.0 s", "The camera leaves the abdomen. The torso resolves, then the whole figure, now seen at a slight angle so the vessel tree reads with depth rather than flat."),
            ("6.0 – 8.0 s", "The move eases to a stop. The pale points are spread the length of the network, brightest right at the vessel walls rather than in the middle of the flow."),
        ],
        light="Starts deep red from inside the blood and cools steadily as the camera retreats, ending on the cool blue-and-red network of the whole figure against the dark background.",
        cons="One motion: a single continuous pull-out from inside a vessel to the whole body. No cut, no dissolve, no jump in scale. The figure does not move, turn or gesture when it appears.",
        note=("Note · reuse keyframe C", "This is <strong>keyframe C</strong> from the egg video. The difference in the motion is small but it sets up the payoff: <strong>the points move to the vessel walls</strong> instead of spreading evenly to the tissues, because the wall is this video's destination. Same still, different motion."),
    ),
    dict(
        n=7, name="The vessel opens", where="Artery wall · macro, near-still",
        tc="0:48.000 → 0:56.000", kf=("new", "new still"),
        colour="#d06a7a", palette="deep red + pale blue · macro, near-still",
        vo="The muscle in that vessel wall relaxes, and the passage through it opens wider.",
        spoken=5.14,
        ends="The vessel seen from inside with its muscular wall relaxed, the passage through it visibly wider than at the start of the shot, and blood moving through it more freely and evenly. Everything is still.",
        img=[
            ("SHOT 7 OF 8 — THE VESSEL OPENS.", "Extreme macro at the wall of an artery, cut so the layers of the wall are visible, with blood flowing through the passage inside."),
            ("SCENE", "Extreme macro inside the body at a small artery, cut open along its length so both the inside of the tube and the thickness of its wall are visible in one frame. The inner surface is a smooth glistening lining of flat cells, and behind it lies a thick band of muscle wrapped in rings around the tube, deep red and fibrous, with a looser outer sheath of pale connective tissue and fine nerves and vessels running through it. Blood moves through the passage — dark red cells in straw-coloured plasma — and tiny pale blue-white points are gathered at the inner lining, passing through it into the muscle layer behind. The muscle is tight at the start, and the passage through the tube is narrow. The outline of the limb it sits in is faintly visible at the very edge of frame."),
            ("CAMERA", "Extreme macro, camera close and level with the cut wall, 100 mm macro equivalent, very shallow depth of field: the lining, the muscle band and the pale points razor sharp, the far side of the vessel and the tissue beyond falling away soft."),
            ("SUBJECT — the spinach, stage 7 of 8", "The last of the pale points, arriving at the tissue that responds to them. This is where everything the video has followed for fifty seconds actually does something."),
            ("LIGHT", "Deep red ambient from the blood, a warm key raking across the cut face of the wall from the upper left so the muscle fibres read as fibres, and a cool blue rim along the outer sheath. The pale points carrying their own cold light against all of it."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is one of those walls, close up — the camera has followed the pale points out of the flow and to the wall they were gathering at. Same points, same pale blue light, same blood.",),
        ],
        real="an artery wall in its three true layers: the intima, a single smooth layer of endothelial cells over an internal elastic lamina; the media, a thick band of smooth muscle wound circumferentially around the vessel with elastic fibres between the cells; and the adventitia outside it, loose connective tissue carrying fine nerves and its own tiny vessels — with red blood cells moving through the lumen inside.",
        cam="Static shot, with the faintest push in — under 5% across the whole eight seconds, so slow it is barely perceptible. No pan, no tilt, no truck, no rotation, no shake. This is deliberately the stillest shot in the video.",
        beats=[
            ("0.0 – 2.0 s", "Almost nothing moves. Blood runs through the narrow passage. Pale points sit gathered against the inner lining."),
            ("2.0 – 4.0 s", "The points pass through the lining into the muscle layer behind it. The muscle fibres there begin, very slowly, to lengthen."),
            ("4.0 – 6.0 s", "The ring of muscle eases. The wall thins slightly and the passage inside the vessel widens — slowly and smoothly, over seconds, not in a jump."),
            ("6.0 – 8.0 s", "The widening stops. Blood runs through the larger passage more freely and more evenly. Everything comes to rest."),
        ],
        light="Unchanged in colour, but the frame brightens very slightly as the passage widens and more blood moves through it. No flash, no pulse, no bloom at the moment the muscle relaxes.",
        cons="One motion: a slow, smooth widening. <strong>It must not snap open, pop, throb, pulse or dilate in a single frame</strong> — the whole point is that this is gradual. Nothing else in the frame moves except the blood.",
        note=("Note · the money shot, and the compliance line", "This is the payoff of the entire video and it is also the most dangerous shot on the page. The picture is about to make the viewer think of blood pressure, and <strong>the script must not say it</strong> — the sentence describes the muscle relaxing and the passage opening, and it stops. Let the picture do the rest. Keep the widening slow: a fast dilation reads as a drug working, which is exactly the wrong impression."),
    ),
    dict(
        n=8, name="A body holding itself open", where="Whole body · hero",
        tc="0:56.000 → 1:04.000", kf=("reuse", "reuse keyframe D"),
        colour="#86e0b0", palette="pale green-gold — colour break 2 · full body",
        vo="Now blood moves easily through a body that is holding its own vessels open.",
        spoken=4.70,
        ends="The whole figure standing still, its vessel network lit an even pale green-gold and visibly open along its whole length, the camera stopped — a clean frame to hold under the end card.",
        img=[
            ("SHOT 8 OF 8 — A BODY HOLDING ITSELF OPEN.", "The same figure at full length, its vessel network glowing an even pale green-gold from within."),
            ("SCENE", "The same adult anatomical figure standing at full length facing camera in a dark void, seen from the front. The body is translucent and smooth, the head without facial features and without hair. Its internal vessel network glows a soft pale green-gold from within, even from the torso out to the fingers and toes, and the vessels themselves read as open and full rather than thin and tight. A faint warm haze surrounds the figure. The background is the same dark navy falling to black as every other shot."),
            ("CAMERA", "Wide: the whole figure from above the head to below the feet, filling about two-thirds of the frame height, centred, camera level at chest height, 50 mm equivalent lens, the whole figure in sharp focus."),
            ("SUBJECT — the spinach, stage 8 of 8", "No longer a separate object at all. It is the pale green-gold light in the vessel network — one plate of leaves, now readable only as the state of the whole system."),
            ("LIGHT", "Soft pale green-gold from inside the body, even throughout, with a faint warm ambient haze around it and a cool blue rim on both edges. Calm and open rather than bright and hot — this is the gentlest hero frame in the series."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame matches on that light and on that openness: the same pale glow and the same relaxed vessels, at the scale of the whole body. It reads as the camera stepping all the way back at the end of the journey. Same figure, same rim light, same background as shot 1."),
        ],
        real="a correct arterial and venous tree — the aorta arching out of the heart, the carotids up the neck, the subclavians into the arms, the femorals down the legs — branching to fine peripheral vessels over a correct skeleton, with true adult human proportion.",
        cam="Pull back, very small amplitude, slow — the camera retreats by about 8% over the first six seconds, so the figure grows slightly smaller and more space opens around it, then stops completely at 6.0 s and holds. It is the only hero shot in the series that moves away rather than in, because this video's subject is something opening. No rotation, no orbit, no shake.",
        beats=[
            ("0.0 – 2.0 s", "The pale green-gold glow rises through the vessel network from the torso outward. The camera begins to retreat, very slightly."),
            ("2.0 – 4.0 s", "The glow reaches the hands and the feet, and the fine vessels there fill and widen a little as it arrives. More dark space opens around the figure."),
            ("4.0 – 6.0 s", "The network settles to a steady, even pale green-gold. The retreat eases to a stop."),
            ("6.0 – 8.0 s", "Nothing moves. The figure stands still and open, lit steady, held for the end card."),
        ],
        light="A single continuous warm-up: from a dim network at 0 s to full steady pale green-gold at 6 s, then held without flicker to the end. No pulsing, no strobing, no heartbeat rhythm.",
        cons="One motion: the glow rising and settling. The figure does not move, breathe visibly, turn, gesture or shift weight. No particles, no rays, no energy effects, no lens flare.",
        note=("Note · reuse keyframe D", "This is <strong>keyframe D</strong> from the egg video with the colour shifted to a pale green-gold and the vessels rendered slightly wider than in the other four videos. That small difference — <strong>open vessels rather than bright ones</strong> — is the argument of this whole video made in a single frame. Specify <em>no facial features</em> again."),
    ),
]

TOPIC["clips"] = CLIPS
