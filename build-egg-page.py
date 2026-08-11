#!/usr/bin/env python3
"""
Generates docs/egg/index.html — the egg video build blueprint.

Everything that appears twice on the page (a shot's end state and the next
shot's opening state) is written ONCE here and emitted into both places, so the
continuity chain cannot drift. Run:  python3 build-egg-page.py
"""
import html, pathlib, re

OUT = pathlib.Path(__file__).parent / "docs" / "egg" / "index.html"

# ---------------------------------------------------------------- shared text
STYLE = (
    "STYLE — identical in all eight shots of this video. Hyper-realistic 3D medical animation still, rendered "
    "like a single frame from a broadcast medical documentary: photoreal subsurface scattering through living "
    "tissue, wet surfaces with true specular highlights, real optical depth of field, physically accurate light, "
    "anatomically accurate structures. It must look real — like actual footage captured inside a living human body — "
    "lifelike and richly detailed, never an illustration, a diagram or a cartoon. Palette: warm flesh pink and "
    "deep red tissue, cream-yellow egg, cool cyan-teal rim light, dark navy background falling to black, with two "
    "or three very soft out-of-focus blue holographic panels far behind the subject blurred into pure glow. "
    "Format: vertical 9:16, 1080 x 1920, subject centred in the upper two-thirds."
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

# ---------------------------------------------------------------------- clips
# 'ends' is emitted as clip N's END FRAME *and* quoted inside clip N+1's
# CONTINUITY line, so the handoff can never drift.
CLIPS = [
    dict(
        n=1, name="The mouth", where="Mouth · head close-up",
        tc="0:00.000 → 0:08.000", kf=("new", "new still"),
        colour="#c98f6a", palette="warm flesh + cyan rim · medium close-up",
        vo="Every day when you eat an egg, the journey starts in your mouth, where your teeth break the white apart.",
        words=20, spoken="6.26 s", head="1.74 s",
        ends="Mouth closed. A pale cream mass of chewed egg is sitting at the back of the tongue, at the entrance to the throat. The jaw is relaxed.",
        img=[
            ("SHOT 1 OF 8 — THE MOUTH.", "A hyper-realistic anatomical human head in three-quarter profile, taking a bite of boiled egg."),
            ("SCENE", "An adult human head and shoulders turned three-quarters toward camera against a dark navy background. The skin is semi-transparent, so the skull, the jaw and cheek muscles, the tongue and the whole row of teeth read clearly through it — the look of a high-end medical visualisation figure. The face is calm and neutral, eyes open, no expression. The mouth is open and a stainless steel fork holds a piece of boiled egg between the front teeth, which have just closed on it. Fine clear strands of saliva stretch between the food and the tooth surfaces. Below the jaw, through the neck, the throat and the top of the esophagus are visible as a pale ribbed tube running down behind the windpipe."),
            ("CAMERA", "Medium close-up: the frame runs from the top of the skull down to the collarbones. Camera at mouth height, level with the face, 50 mm equivalent lens, shallow depth of field with the lips, teeth and food razor sharp and the back of the head falling soft."),
            ("SUBJECT — the egg, stage 1 of 8", "A firm piece of boiled egg white: pale cream, slightly translucent along its cut edge, with a band of deep yellow yolk running through it. It must read instantly and unmistakably as egg."),
            ("LIGHT", "One warm key light from the upper left catching every wet highlight on teeth, tongue and food. A cool cyan rim light along the jawline and cheekbone separating the head from the background. Deep shadow behind the head."),
            ("CONTINUITY", "This is the opening shot and it locks the look for the whole video: this exact figure, this exact skin translucency, this exact cream-yellow egg material, this warm-key-plus-cyan-rim lighting and this dark navy background appear in all eight shots. Nothing about the look changes after this frame."),
        ],
        cam="Push in, small amplitude, slow speed — the frame tightens by roughly 15% across the full eight seconds, travelling straight in toward the mouth and staying level at mouth height. Motorised smoothness, constant speed, no handheld shake, no rotation, no whip pan.",
        beats=[
            ("0.0 – 2.0 s", "The fork slides back out of frame to the left. The lips close over the food. The jaw begins to rise."),
            ("2.0 – 4.0 s", "The molars press down through the piece of egg: it compresses, dents, then splits into two. One saliva strand stretches thin and breaks. Under the transparent skin, the jaw and cheek muscles visibly bunch and release."),
            ("4.0 – 6.0 s", "Two more chewing cycles, each breaking the pieces smaller, until the egg is a pale, wet, granular paste. The tongue rolls the paste to the centre of the mouth."),
            ("6.0 – 8.0 s", "The tongue lifts and presses the paste back toward the throat. The mass starts moving to the back of the mouth as the shot ends."),
        ],
        light="Unchanged throughout — warm key upper left, cyan rim on the jaw. No lighting change in this clip.",
        cons="One motion only: chewing. The head does not turn, nod, tilt, blink hard or speak. Nothing else in the frame moves. Slow, deliberate and mechanical, continuous from the first frame to the last.",
        note=("Note", "The only shot in the video with an everyday object in it, and the one that tells the viewer what the video is about. If the still comes back and the food does not read as egg at a glance, re-roll it — nothing later in the video re-establishes the subject."),
    ),
    dict(
        n=2, name="The swallow", where="Throat → stomach · torso wide",
        tc="0:08.000 → 0:16.000", kf=("mint", "mints keyframe A"),
        colour="#b9846f", palette="warm flesh + cyan rim · medium wide",
        vo="You swallow, and your esophagus squeezes in slow waves, pushing the mouthful down toward your stomach.",
        words=16, spoken="6.80 s", head="1.30 s",
        ends="The whole upper body is in frame. The pale bolus has arrived at the lower end of the esophagus and the ring of muscle at the stomach entrance is opening in front of it. The stomach below is pink and empty.",
        img=[
            ("SHOT 2 OF 8 — THE SWALLOW.", "The same figure, one step wider: head, neck and upper chest, with the esophagus visible running down inside the body."),
            ("SCENE", "The same adult anatomical figure as shot 1, at the same three-quarter angle, now framed wider so the head, the whole neck and the upper chest are in view. Through the semi-transparent skin and the pale ribcage, the esophagus runs from the back of the throat down the centre of the chest, behind the heart, as a soft ribbed muscular tube. A pale cream mass of chewed egg sits at the very top of that tube, just entering it. The ring muscles of the esophagus read as evenly spaced bands along its length. A faint cool cyan glow runs down inside the tube ahead of the mass, showing the direction of travel as a soft travelling light."),
            ("CAMERA", "Medium wide: the frame runs from just above the head down to the bottom of the ribcage. Camera level, 35 mm equivalent lens, moderate depth of field with the esophagus and the mass sharp and the shoulders falling slightly soft."),
            ("SUBJECT — the egg, stage 2 of 8", "No longer a piece: a smooth pale cream bolus roughly the size of a grape, wet and rounded, the same material as shot 1 in a new shape."),
            ("LIGHT", "Warm key from the upper left across the chest. Cool cyan rim down the left edge of the neck and shoulder. The esophagus glowing very faintly from within along its length."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is that same figure at that same angle, one step wider, with that same chewed mass now formed into a bolus at the top of the esophagus. Same skin, same light, same background, same egg material."),
        ],
        cam="Pull out, large amplitude, slow constant speed — the camera retreats and cranes down very slightly, so that by 8.0 s the frame holds the whole upper body from the top of the head to just below the stomach. One continuous move, never stopping, never speeding up. No shake, no rotation.",
        beats=[
            ("0.0 – 2.0 s", "The throat contracts once and drives the bolus into the top of the esophagus. The camera begins its pull-out."),
            ("2.0 – 4.0 s", "Rings of muscle contract in sequence from the top downward, squeezing the tube shut behind the bolus and pushing it about a third of the way down. The pull-out reveals the collarbones and the top of the ribcage."),
            ("4.0 – 6.0 s", "The wave continues down the tube. The bolus passes behind the heart, which beats steadily twice in this window. The pull-out reveals the whole ribcage and the lungs."),
            ("6.0 – 8.0 s", "The stomach comes into frame below the ribs, pink and empty. The bolus reaches the lower end of the esophagus and the ring of muscle at the stomach entrance opens in front of it."),
        ],
        light="The faint cyan glow inside the esophagus travels down the tube just ahead of the bolus, and fades out as the shot ends. Key and rim unchanged.",
        cons="One motion: the swallow, as a single continuous travelling squeeze that never stops or restarts. The figure does not move, turn or gesture; the only other movement in frame is the heartbeat.",
        note=("Note · save this one — keyframe A", "This still becomes <strong>keyframe A</strong> and it is the most valuable asset in the video. A torso with a visible esophagus and stomach is identical whatever the food is, so every later video in the series starts from this exact file — only the colour and shape of the bolus changes. Re-roll it until the ribcage is clean and the esophagus reads clearly as a tube, not a shadow."),
    ),
    dict(
        n=3, name="Inside the stomach", where="Stomach · cutaway → macro",
        tc="0:16.000 → 0:24.000", kf=("new", "new still"),
        colour="#d99a3f", palette="warm amber · close → macro",
        vo="Inside your stomach, acid unwinds each folded protein and enzymes cut the strands apart.",
        words=14, spoken="6.60 s", head="1.50 s",
        ends="A long, almost completely straightened golden protein ribbon drifting in amber fluid, with two blunt translucent enzyme forms closed on it but not yet cutting.",
        img=[
            ("SHOT 3 OF 8 — INSIDE THE STOMACH.", "The stomach, seen close inside the body, its near wall cut away so the inside is visible."),
            ("SCENE", "The same figure, now framed on the abdomen. The stomach fills most of the frame, sitting under the ribs, with the lower ribcage and the outline of the torso still visible around the edges of frame so it stays obvious that we are inside a human body. The near wall of the stomach is opened in a clean medical cutaway, revealing the interior: deep folded ridges of stomach lining in wet red-brown, a churning pool of warm amber gastric fluid, and the pale cream egg bolus lying in it, already softening and fraying at the edges. Rising out of the fluid in the near foreground, close to camera and sharp, is a single tightly coiled protein — a dense golden helix knotted on itself, its surface faceted and faintly metallic."),
            ("CAMERA", "Medium close-up on the stomach, slightly high angle looking down into the cutaway, 40 mm equivalent lens, shallow depth of field with the coiled protein sharp in the foreground and the folded stomach lining soft behind it."),
            ("SUBJECT — the egg, stage 3 of 8", "The bolus breaking apart in acid, and one protein released from it isolated in the foreground, still tightly coiled and wound on itself."),
            ("LIGHT", "Strong warm amber light coming up through the gastric fluid from below, turning it to glowing honey. The coiled protein lit hard from the upper left. Cyan rim light along the cut edge of the stomach wall, tying this shot to the two before it."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame picks up from there: the same body, the camera now settled on the stomach the bolus was entering, with that same bolus lying in the acid. Same figure, same cyan rim, same background."),
        ],
        cam="Push in, large amplitude, slow steady speed — the camera moves from the medium shot of the stomach forward through the cutaway opening and into the fluid, ending in macro with the coiled protein filling the centre of frame. One straight continuous move on a single axis, constant speed, no shake, no rotation, no stopping.",
        beats=[
            ("0.0 – 2.0 s", "The stomach wall contracts once and the amber fluid swirls; the bolus rolls over and starts to break apart. The camera begins pushing in toward the coiled protein in the foreground."),
            ("2.0 – 4.0 s", "The push-in continues until the coiled golden protein fills the centre of frame and the stomach lining behind it becomes a soft wall of red-brown texture. The coil begins to loosen: the outermost turn lifts away from the body of the knot."),
            ("4.0 – 6.0 s", "The helix unwinds steadily, turn by turn, opening out into a long loose golden ribbon that waves slowly in the current. Bubbles rise past it continuously."),
            ("6.0 – 8.0 s", "The ribbon straightens almost completely. Two blunt translucent enzyme forms drift in from the edges of frame and close onto it, gripping it without cutting yet."),
        ],
        light="The amber underlight strengthens as the camera descends into the fluid, until by 6.0 s the whole frame is lit from below and the background has gone to deep red-brown.",
        cons="One motion: the unwinding. It must read as a coil opening out — tight at 0 s, loose and long at 8 s — not as something dissolving, exploding, melting or shattering. One continuous transformation across the full eight seconds, never restarting.",
        note=("Note · the money shot", "This is the image the video gets remembered for and the one to spend re-rolls on. Two failure modes to watch: the coil <em>dissolving</em> instead of unwinding, and the camera arriving so early that the unwinding has nowhere left to go. If the still is right and the motion is wrong, re-run the motion prompt on the same still rather than regenerating the image."),
    ),
    dict(
        n=4, name="Where we are now → the cut", where="Whole body → small intestine",
        tc="0:24.000 → 0:32.000", kf=("new", "new still"),
        colour="#5fc4e8", palette="cold blue — colour break · wide → macro",
        vo="In your small intestine, more enzymes arrive and cut those strands down into single amino acids.",
        words=16, spoken="6.90 s", head="1.20 s",
        ends="A loose cloud of small glowing gold beads drifting apart from one another just above the ridged inner lining of the small intestine.",
        img=[
            ("SHOT 4 OF 8 — WHERE WE ARE NOW.", "The whole body seen at full length in cool blue, with the small intestine lit up inside the abdomen."),
            ("SCENE", "The same figure, now standing at full length facing camera in a dark navy void, rendered in cool blue X-ray tones: the skeleton, the organs and the outline of the muscles all visible through translucent blue skin. The small intestine, coiled in the centre of the abdomen, glows clear cyan-white and is by far the brightest thing in the body. A faint cool trail runs down from the stomach into it. The head, arms and legs are dim and cool, so the eye goes straight to the abdomen."),
            ("CAMERA", "Wide: the whole figure from above the head to below the feet, filling about four-fifths of the frame height. Camera level at chest height, 50 mm equivalent lens, the whole figure in focus, the void behind it clean and empty."),
            ("SUBJECT — the egg, stage 4 of 8", "Not visible as food any more. Its position in the body is what is visible: the cyan-white glow in the small intestine is where it has reached."),
            ("LIGHT", "Cold: a cyan key from the front left and a deeper blue rim on both edges of the body. The abdomen self-illuminated from within. No warm light anywhere in this frame."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This is the one deliberate step back in the video — the same figure seen whole, so the viewer re-anchors and remembers this is happening inside a body. The glowing point in the abdomen is exactly where the previous shot just was, and the camera dives straight back into it, so the step back lasts under two seconds."),
        ],
        cam="Hold, then push in, very large amplitude, accelerating from slow to moderate and easing off at the end — the camera holds on the whole figure, then travels forward into the abdomen, through the body wall, and into the small intestine, ending inside the tunnel. One straight continuous move, no cuts, no rotation, no shake.",
        beats=[
            ("0.0 – 1.5 s", "The whole body holds still. The cyan glow in the abdomen pulses once, brightening and settling."),
            ("1.5 – 4.0 s", "The camera pushes in toward the abdomen. The figure grows and passes out of frame at the edges; the camera travels through the translucent body wall and up to the outer surface of the coiled small intestine."),
            ("4.0 – 6.0 s", "Through the wall and inside: a wet ridged tunnel of coral-pink lining, lit cool blue. The straightened golden ribbon runs across the frame. Translucent crystalline enzyme forms close along it in sequence and snip it apart at several points at once."),
            ("6.0 – 8.0 s", "The ribbon separates into a row of small glowing gold beads. They drift apart from one another and spread out through the frame as the camera slows to a stop."),
        ],
        light="Cold blue throughout the first half. As the camera enters the intestine at 4.0 s, a warm gold glow from the beads begins to build inside the cold blue and grows to the end of the shot — the first warmth returning.",
        cons="One motion: the dive in. Everything else follows from it. The cutting happens steadily across the second half, not all in one frame. The figure at the start does not move, turn or gesture.",
        note=("Note · the deliberate colour break", "Shot 3 is hot amber and shot 4 opens ice blue, back to back on a hard cut. That jolt is doing retention work at the 24-second mark, which is roughly where a vertical video loses people — <strong>do not warm it toward the amber of the shot before it.</strong> The reference video does exactly this at exactly this point. The gold beads that appear at the end here are the thread that carries through shots 5, 6 and 7."),
    ),
    dict(
        n=5, name="Through the wall", where="Intestinal villi · macro",
        tc="0:32.000 → 0:40.000", kf=("mint", "mints keyframe B"),
        colour="#e8899d", palette="pink + gold · macro",
        vo="Your intestinal wall is covered in tiny folds, and the amino acids pass through them into your blood.",
        words=18, spoken="6.67 s", head="1.43 s",
        ends="Inside the capillary within a single villus: red blood cells and glowing gold beads flowing along together, the vessel wall arcing around the frame.",
        img=[
            ("SHOT 5 OF 8 — THROUGH THE WALL.", "Extreme macro on the lining of the small intestine, so close that individual villi fill the frame."),
            ("SCENE", "The inner surface of the small intestine at extreme magnification: hundreds of soft finger-shaped villi rising toward camera, wet coral and rose pink, each faintly translucent with a fine red capillary network glowing just beneath its surface. Small glowing gold beads drift down between them from the top of frame and rest against their surfaces. Far behind, well out of focus, the tunnel of the intestine curves away into darkness, so it stays clear we are inside the gut and not in an empty void."),
            ("CAMERA", "Macro, camera low among the villi looking very slightly up, 85 mm macro equivalent, very shallow depth of field: one band of villi razor sharp, the field in front of and behind it melting into soft pink bokeh."),
            ("SUBJECT — the egg, stage 5 of 8", "Single amino acids: small, smooth, glowing warm gold beads, the same beads the enzymes released at the end of the previous shot."),
            ("LIGHT", "Warm gold light raking across from the right, catching every wet villus tip. Cool cyan fill from the left keeping the shadow side from going flat. The capillaries inside the villi glowing faintly red from within."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is those same beads seen closer, resting on the lining they were drifting above. Same intestine, same beads, same gold — the camera has simply arrived at the surface."),
        ],
        cam="Truck right, small amplitude, slow speed for the first six seconds, then push in, small amplitude, slow speed on one villus for the last two. Two linked moves in one continuous take — the sideways drift eases into the push. No shake, no rotation, no cut.",
        beats=[
            ("0.0 – 2.0 s", "The villi sway gently in a slow current, all together, like a field of grass under water. More gold beads drift down between them from the top of frame."),
            ("2.0 – 4.0 s", "The camera trucks slowly right across the field. The beads settle down onto the villus surfaces and stop moving."),
            ("4.0 – 6.0 s", "The beads press into the surface and pass through it, the tissue closing softly behind them. They reappear inside the villus as glowing points in the capillary loop just beneath the skin of it."),
            ("6.0 – 8.0 s", "The camera pushes in on that one villus until the capillary inside it fills the frame; its wall turns translucent and we are looking into flowing blood."),
        ],
        light="Constant warm gold rake throughout. The only change is the light from the beads themselves, which is hidden as they sink and then reappears from inside the villus.",
        cons="One motion: the beads crossing the wall. The villi sway continuously and gently the whole time and never stop; nothing jerks, snaps or pops. The transfer is a soft absorption, not an impact.",
        note=("Note · save this one — keyframe B", "This still becomes <strong>keyframe B</strong>. It is the single most reusable image in the series: every video in the run ends up at this wall, and only the colour of the beads changes. Get the depth of field right here — one sharp band with soft bokeh in front and behind — and this file will carry five videos."),
    ),
    dict(
        n=6, name="Into the blood", where="Capillary → liver → whole body",
        tc="0:40.000 → 0:48.000", kf=("mint", "mints keyframe C"),
        colour="#cf6f70", palette="red + blue → whole body · macro → wide",
        vo="Your blood carries them through your liver, then out along your vessels toward every tissue in your body.",
        words=18, spoken="6.08 s", head="2.02 s",
        ends="The whole body seen at full length, its entire arterial and venous tree visible as a fine red-and-blue network, with gold points travelling outward along it toward the arms and legs.",
        img=[
            ("SHOT 6 OF 8 — INTO THE BLOOD.", "Inside a blood vessel, with the branching vessel tree visible far beyond it."),
            ("SCENE", "Macro inside a blood vessel: glossy dark red biconcave red blood cells tumbling toward camera through translucent straw-coloured plasma, with glowing gold beads travelling among them and standing out clearly against the red. The vessel wall arcs around the edges of frame in translucent pink, lit with a cold blue rim. Far away in the depth beyond the vessel, faintly visible through the tissue, the branching silhouette of a much larger vessel tree glows dim red — so the shot reads as one small place inside a much bigger system."),
            ("CAMERA", "Macro inside the vessel, camera in the centre of the flow facing along it, 50 mm equivalent lens, sharp focal plane through the middle of frame with the cells at the frame edges softened by motion blur."),
            ("SUBJECT — the egg, stage 6 of 8", "The same warm gold beads, now travelling in blood among the red cells."),
            ("LIGHT", "Deep red ambient from the blood itself, a cold blue rim along the vessel wall, and the gold beads carrying their own light. Strong red-and-blue contrast, warm centre and cool edges."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is that same capillary, one moment later, with the camera now inside the flow. Same beads, same gold, same blood."),
        ],
        cam="Pull out, very large amplitude, one constant slow speed all the way — the camera retreats continuously from inside the capillary out through the liver, out of the abdomen, and back until the whole standing figure is in frame. A single unbroken move, never accelerating, never stopping, no rotation, no shake. This is the longest camera move in the video.",
        beats=[
            ("0.0 – 2.0 s", "Red cells and gold beads stream past camera toward the foreground in a steady current. The camera begins to pull back along the vessel."),
            ("2.0 – 4.0 s", "The vessel widens as the camera retreats; it exits into a larger vessel and the dark red mass of the liver forms around it. Gold beads pass through the liver tissue and continue on."),
            ("4.0 – 6.0 s", "The pull-out continues without pause: the liver shrinks, the abdomen forms around it, the ribcage and the heart come into frame. The heart beats twice in this window."),
            ("6.0 – 8.0 s", "The move completes on the whole figure at full length, its entire arterial and venous network visible as a fine red-and-blue tree, with gold points travelling outward along it toward the hands and the feet."),
        ],
        light="Deep red at the start, opening out to a cool dark navy as the camera leaves the body, with the vessel network self-illuminated and the gold points the brightest thing in frame by the end.",
        cons="One motion: the pull-out, at one constant speed. The flow of blood past camera never changes pace and never reverses. The figure that resolves at the end is standing still and does not move, turn or gesture.",
        note=("Note · save this one — keyframe C", "This still becomes <strong>keyframe C</strong>. The pull-out is the only camera move in the video that travels any real distance, and it is what makes the scale feel like it is opening out — it earns the whole-body shot that follows. If the generation cuts or stutters part-way through the move, re-roll it; a broken pull-out here reads as two shots joined."),
    ),
    dict(
        n=7, name="The muscle fibre", where="Thigh muscle · extreme macro",
        tc="0:48.000 → 0:56.000", kf=("new", "new still"),
        colour="#d97a5f", palette="saturated red + gold · macro, near-still",
        vo="Your muscle fibres pull them in, and use them as the raw material to rebuild their own structure.",
        words=18, spoken="6.37 s", head="1.73 s",
        ends="The muscle fibre lit warmly from within, its cross-banding crisp, everything at rest and completely still.",
        img=[
            ("SHOT 7 OF 8 — THE MUSCLE FIBRE.", "Extreme macro inside a thigh muscle, with the outline of the leg still faintly visible at the edge of frame."),
            ("SCENE", "Extreme macro inside the muscle of a thigh: a bundle of skeletal muscle fibres running diagonally across the frame, deep saturated red, wet and faintly iridescent, with clear pale cross-banding along every fibre, wrapped in a translucent sheath threaded with fine capillaries. Glowing gold beads travel along the nearest capillary and rest against the surface of the closest fibre. At the very edge of frame, soft and far out of focus, the outline of the thigh and the skin surface is still faintly visible against the dark background, so it stays clear where in the body this is."),
            ("CAMERA", "Extreme macro, camera close and level with the fibre bundle, 100 mm macro equivalent, very shallow depth of field: the nearest fibre and the beads on it razor sharp, the rest of the bundle falling away soft, the leg outline at the edge reduced to a suggestion."),
            ("SUBJECT — the egg, stage 7 of 8", "The last of the gold beads, arriving at the tissue that will use them."),
            ("LIGHT", "Warm key from the upper right along the length of the fibres. Cool blue rim along the top edge of the bundle. Deep black in the gaps between fibres. The beads carrying their own warm light."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame is one of those destinations, close up — the camera has followed the gold along the network out to a muscle in the thigh. Same beads, same gold, same warm-and-cool light."),
        ],
        cam="Static shot, with the faintest push in — under 5% across the whole eight seconds, so slow it is barely perceptible. No pan, no tilt, no truck, no rotation, no shake. This is deliberately the stillest shot in the video.",
        beats=[
            ("0.0 – 2.0 s", "The frame settles. Gold beads travel along the capillary toward the nearest fibre."),
            ("2.0 – 4.0 s", "The first beads touch the fibre surface and sink into it. The fibre brightens softly from within at each point where one enters."),
            ("4.0 – 6.0 s", "More beads follow and are absorbed. The pale cross-banding along the fibre becomes crisper and more defined, and the fibre thickens very slightly."),
            ("6.0 – 8.0 s", "The last beads disappear into the fibre. The internal glow settles to a steady warm gold and everything comes to rest."),
        ],
        light="The only change in the frame: the fibre's internal glow rises from nothing to a steady warm gold as the beads are absorbed. Key and rim unchanged.",
        cons="One motion: absorption. The muscle does not contract, twitch, flex or pulse — it is receiving material, not working. Nothing swings, nothing snaps. If in doubt, less movement.",
        note=("Note", "The stillest shot in the video, on purpose. Shot 6 has just travelled a very long way; shot 7 stops moving so the last shot has somewhere to go. Resist the urge to add a camera move here. This is also the shot the compliance line lives on — it shows material arriving, not a result being produced."),
    ),
    dict(
        n=8, name="The whole body", where="Whole body · hero",
        tc="0:56.000 → 1:04.000", kf=("mint", "mints keyframe D"),
        colour="#efc24d", palette="warm gold — colour break 2 · full body",
        vo="From one egg, your body now holds everything it needs to keep repairing and rebuilding itself.",
        words=16, spoken="6.35 s", head="1.75 s",
        ends="The whole vessel network lit steady warm gold, the figure standing still, the camera stopped — a clean frame to hold under the end card.",
        img=[
            ("SHOT 8 OF 8 — THE WHOLE BODY.", "The same figure at full length, its vessel network glowing warm gold from within."),
            ("SCENE", "The same adult anatomical figure standing at full length facing camera in a dark void, seen from the front. The body is translucent and smooth, the head without facial features and without hair. Its internal vessel network glows warm gold from within, brightest through the torso and falling away toward the hands and the feet. A soft gold haze radiates outward into the darkness around the silhouette. A cool blue rim light runs down both edges of the body, separating it from the black and tying it back to the cool shots earlier in the video."),
            ("CAMERA", "Wide: the whole figure from above the head to below the feet, filling about two-thirds of the frame height, centred, camera level at chest height, 50 mm equivalent lens, the whole figure in sharp focus."),
            ("SUBJECT — the egg, stage 8 of 8", "No longer a separate object at all. It is the gold light in the vessel network — everything that was one piece of egg, now distributed through the whole body."),
            ("LIGHT", "Warm gold from inside the body, a soft gold ambient haze around it, and a cool blue rim on both edges. This is the warmest frame in the video and it is meant to be."),
            ("CONTINUITY", "PREVIOUS SHOT ENDED: {prev}. This frame matches on that warm gold light: the same glow, at the scale of the whole body. It reads as the camera stepping all the way back at the end of the journey. Same figure, same rim light, same background as shot 1."),
        ],
        cam="Push in, very small amplitude — about 8% over the first six seconds, slowing to a complete stop at 6.0 s and holding perfectly still to the end. No rotation, no orbit, no shake. The figure never turns.",
        beats=[
            ("0.0 – 2.0 s", "The figure stands still. The gold glow in the torso brightens gently."),
            ("2.0 – 4.0 s", "The glow spreads outward from the torso along the vessel network into the shoulders and the hips."),
            ("4.0 – 6.0 s", "It reaches the hands and the feet until the whole network is lit. A soft gold haze builds in the air around the silhouette."),
            ("6.0 – 8.0 s", "The glow settles and holds steady. The camera stops. The final two seconds are completely still."),
        ],
        light="One continuous lift: gold rising from the torso outward until the whole network is lit, then holding. Nothing dims, nothing flickers, nothing pulses.",
        cons="The figure stays standing and completely still — it does not turn, rotate, walk, flex, breathe visibly or gesture. One motion only: light spreading. The head has no facial features at any point.",
        note=("Note · save this one, and it opens the video too", "This still becomes <strong>keyframe D</strong>, and it does double duty: the first second of the finished video is this frame, before the hard cut back to the mouth. Specify <em>no facial features</em> and check the result — a generated face at this scale reads as uncanny and pulls attention off the glow, which is the entire subject of the shot."),
    ),
]

# ------------------------------------------------------------------ rendering
def esc(s):
    return html.escape(s, quote=False)


def img_prompt(c):
    """Full paste-ready image prompt text for clip c."""
    prev = CLIPS[c["n"] - 2]["ends"] if c["n"] > 1 else None
    lines = []
    for i, (head, body) in enumerate(c["img"]):
        if "{prev}" in body:
            # prev already ends in a full stop; the template supplies its own
            body = body.replace("{prev}", prev.rstrip("."))
        lines.append(f"{head} {body}" if i == 0 else f"{head} — {body}")
    lines.append(FIGURE)
    lines.append(STYLE)
    lines.append(NOTEXT)
    return "\n\n".join(lines)


def vid_prompt(c):
    """Full paste-ready image-to-video prompt text for clip c."""
    p = [
        f"CLIP {c['n']} OF 8 — {c['name'].upper()} · 8.000 seconds · 24 fps · vertical 9:16, 1080 x 1920 · AUDIO OFF (generate no sound).",
        f"START FRAME — the approved still for shot {c['n']}, used unchanged as the first frame. Animate this exact image; do not redesign it, do not change the framing it starts on, do not restyle it.",
        f"CAMERA — {c['cam']}",
    ]
    p += [f"{t} — {b}" for t, b in c["beats"]]
    p.append(f"LIGHTING — {c['light']}")
    nxt = (
        f"END FRAME — {c['ends']} Clip {c['n']+1} begins from exactly this state."
        if c["n"] < 8
        else f"END FRAME — {c['ends']} This is the last frame of the video."
    )
    p.append(nxt)
    p.append(f"CONSTRAINTS — One single continuous shot, no cuts, no jump in time, no scene change. {c['cons']}")
    p.append(VID_NOTEXT)
    return "\n\n".join(p)


def block(label, cls, text, pid):
    return f"""      <div class="pblock">
        <div class="phead"><span class="plabel {cls}">{esc(label)}</span><button class="cbtn" type="button" data-target="{pid}">Copy</button></div>
<pre id="{pid}">{esc(text)}</pre>
      </div>
"""


def clip_card(c):
    kfcls = "kf n" if c["kf"][0] == "new" else "kf r"
    nt, nb = c["note"]
    return f"""    <div class="clip" id="c{c['n']}">
      <div class="chead">
        <div class="cmeta"><span class="cn">CLIP {c['n']}</span><span class="tc">{c['tc']}</span><span class="{kfcls}">{c['kf'][1]}</span><span class="tc"><span class="sw" style="background:{c['colour']}"></span>{c['palette']}</span></div>
        <h4>{esc(c['name'])} <span class="where">{esc(c['where'])}</span></h4>
        <p class="vo">“{esc(c['vo'])}”</p>
      </div>
      <div class="cbody">
{block(f"Image prompt {c['n']}", "", img_prompt(c), f"ip{c['n']}")}{block(f"Image-to-video prompt {c['n']} · 8 s · audio off", "v", vid_prompt(c), f"vp{c['n']}")}        <div class="plabel n">{nt}</div>
        <p class="cnote">{nb}</p>
      </div>
    </div>
"""


def chain_rows():
    out = []
    for c in CLIPS:
        nxt = f"opens clip {c['n']+1}" if c["n"] < 8 else "end of video"
        out.append(
            f"""          <tr><td class="num">{c['n']}</td><td><b>{esc(c['name'])}</b><br><span class="dim">{esc(c['where'])}</span></td>"""
            f"""<td>{esc(c['ends'])}</td><td class="num">{nxt}</td></tr>"""
        )
    return "\n".join(out)


def script_rows():
    return "\n".join(
        f"""          <tr><td class="num">{c['n']}</td><td>{esc(c['vo'])}</td><td class="num">{c['words']}</td><td class="num">{c['spoken']}</td><td class="num tick">{c['head']}</td></tr>"""
        for c in CLIPS
    )


def grid_rows():
    out = []
    for c in CLIPS:
        kfcls = "kf n" if c["kf"][0] == "new" else "kf r"
        out.append(
            f"""          <tr><td class="num">{c['n']}</td><td class="num">{c['tc']}</td><td><a href="#c{c['n']}">{esc(c['name'])}</a><br><span class="dim">{esc(c['where'])}</span></td>"""
            f"""<td>{esc(c['cam'].split(' — ')[0])}</td><td><span class="{kfcls}">{c['kf'][1]}</span></td>"""
            f"""<td><span class="sw" style="background:{c['colour']}"></span>{esc(c['palette'].split(' · ')[0])}</td></tr>"""
        )
    return "\n".join(out)


ALL_IMG = "\n\n\n".join(f"===== IMAGE PROMPT {c['n']} =====\n\n" + img_prompt(c) for c in CLIPS)
ALL_VID = "\n\n\n".join(f"===== VIDEO PROMPT {c['n']} =====\n\n" + vid_prompt(c) for c in CLIPS)

CARDS = "".join(clip_card(c) for c in CLIPS)

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>The egg video — complete build blueprint</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🥚</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,600;0,800;0,900;1,800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
:root{{
  --bg:#060c13; --bg2:#0b151f; --panel:#0f1c28; --panel2:#132433;
  --line:#1e3345; --line2:#2a4257;
  --ink:#eaf2f8; --ink2:#a9bdcd; --ink3:#7b93a7;
  --yellow:#ffe23d; --cyan:#4fd8ff; --coral:#f0937f; --green:#5fe0a8; --red:#ff6b6b;
  --mono:'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,monospace;
}}
*{{box-sizing:border-box}}
html{{-webkit-text-size-adjust:100%;scroll-behavior:smooth}}
body{{margin:0;background:var(--bg);color:var(--ink);font:400 18px/1.65 Inter,system-ui,-apple-system,Segoe UI,Roboto,sans-serif;-webkit-font-smoothing:antialiased}}
a{{color:var(--cyan)}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 24px}}
.narrow{{max-width:880px;margin-left:auto;margin-right:auto}}

header{{position:relative;overflow:hidden;border-bottom:1px solid var(--line);
  background:radial-gradient(120% 90% at 50% -10%, rgba(255,226,61,.13), transparent 60%),linear-gradient(180deg,#0a1420,#060c13)}}
.heroinner{{position:relative;padding:64px 0 54px}}
.back{{font:600 13px/1 var(--mono);color:var(--ink3);text-decoration:none;display:inline-block;margin-bottom:22px}}
.back:hover{{color:var(--cyan)}}
.kicker{{font:700 13px/1 var(--mono);letter-spacing:.18em;text-transform:uppercase;color:var(--yellow);margin-bottom:20px}}
h1{{font:900 clamp(36px,6vw,68px)/1.03 Archivo,sans-serif;letter-spacing:-.028em;margin:0 0 20px}}
h1 em{{font-style:italic;color:var(--yellow)}}
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
.chead .cn{{font:800 15px/1 var(--mono);color:var(--yellow)}}
.chead .tc{{font:600 13px/1 var(--mono);color:var(--ink3)}}
.chead h4{{margin:0 0 10px;font:800 22px/1.2 Archivo,sans-serif;color:var(--ink)}}
.chead h4 .where{{font:600 13px/1 var(--mono);color:var(--ink3);margin-left:10px;white-space:nowrap}}
.chead .vo{{font-size:16.5px;color:var(--ink);font-style:italic;border-left:3px solid var(--yellow);padding-left:16px;margin:0}}
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
.tlvo div{{position:absolute;top:5px;height:20px;background:#2b556e;border-radius:3px;border-left:2px solid var(--yellow)}}
.tlcap{{padding:12px 16px;font:600 12px/1.5 var(--mono);color:var(--ink3);border-top:1px solid var(--line)}}

.audio{{margin:22px 0;padding:20px 22px;border:1px solid var(--line2);border-radius:14px;background:var(--panel)}}
.audio audio{{width:100%;margin-top:12px}}
.dl{{display:inline-block;margin-top:14px;margin-right:10px;font:700 13px/1 var(--mono);letter-spacing:.06em;padding:13px 16px;border-radius:9px;
  background:#12303f;border:1px solid #1c4d63;color:var(--cyan);text-decoration:none}}
.dl:hover{{background:#17415a}}

ol.steps{{counter-reset:s;list-style:none;padding-left:0}}
ol.steps>li{{counter-increment:s;position:relative;padding-left:50px;margin-bottom:20px}}
ol.steps>li::before{{content:counter(s);position:absolute;left:0;top:-2px;width:34px;height:34px;border-radius:9px;
  background:var(--panel2);border:1px solid var(--line2);color:var(--yellow);font:800 15px/34px var(--mono);text-align:center}}
ol.steps>li b{{color:var(--ink)}}

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
      <div class="kicker">Build blueprint · Video 1 of the series · rebuilt 11 Aug 2026</div>
      <h1>What happens<br>when you eat<br><em>an egg.</em></h1>
      <p class="sub">Everything needed to make the finished 64-second short: the script, <strong>the voice-over already rendered and measured</strong>, and all 16 prompts written out in full — <strong>one unbroken journey through one body</strong>, every shot handing its last frame to the next one.</p>
      <div class="metarow">
        <span class="chip"><b>8</b> clips × <b>8.000 s</b></span>
        <span class="chip"><b>8</b> image prompts</span>
        <span class="chip"><b>8</b> image-to-video prompts</span>
        <span class="chip">VO <b>rendered</b> · 64.03 s · −14.8 LUFS</span>
        <span class="chip">Mints keyframes <b>A–D</b></span>
      </div>
    </div>
  </div>
</header>

<!-- ============ 01 WHAT CHANGED ============ -->
<section id="rebuild">
  <div class="wrap"><div class="narrow">
    <div class="snum">01 — What changed in this rebuild</div>
    <h2 class="sec">Eight shots inside one body, not eight separate pictures</h2>
    <p class="lead">The first version of this page had eight good-looking images that had nothing to do with each other: a golden helix floating in a void, crystalline shapes in blue space, a field of villi with no body around it. It looked like eight art pieces. The reference video looks like <em>one journey through one person</em>, and that difference is structural, not decorative.</p>

    <div class="tw">
      <table>
        <thead><tr><th>The problem</th><th>What it produced</th><th>The fix built into this version</th></tr></thead>
        <tbody>
          <tr><td><b>No continuity</b></td><td>Eight shots with no shared body, no shared light, no shared object. Nothing carried from one to the next.</td><td>Every shot now ends on a stated <b>end frame</b>, and the next shot's prompt opens by quoting that exact frame back. <a href="#chain">The chain is written out in section 02.</a></td></tr>
          <tr><td><b>No realism instruction</b></td><td>“Photorealistic 3D medical visualisation” once, then nothing that told the model the result had to look <em>real</em>.</td><td>An explicit realism block — <b>“it must look real, like actual footage captured inside a living human body”</b> — is now in all eight image prompts, word for word.</td></tr>
          <tr><td><b>It stopped looking like a body</b></td><td>Shots 3–7 were abstract macro in black voids. The viewer lost the thread: this could have been anything, anywhere.</td><td>Every shot now keeps an anatomical anchor in frame, and <b>four of the eight are whole-body shots</b> — the same in–out–in–out rhythm the reference uses.</td></tr>
          <tr><td><b>Detached script</b></td><td>“A muscle fibre draws them in.” Clinical, third person, no <em>you</em> anywhere. It read like a textbook, not like something happening to the viewer.</td><td>Rewritten in the second person and re-rendered: <b>every sentence names a part of your body</b>, and it opens on the everyday moment — “Every day when you eat an egg…”</td></tr>
          <tr><td><b>Thin video prompts</b></td><td>Two or three sentences of motion. Everything about timing, lens and speed was left to the model to guess.</td><td>Every video prompt is now a <b>shot order</b>: camera move with amplitude and speed, four timed beats, the lighting change, and the exact end frame.</td></tr>
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
{chain_rows()}
        </tbody>
      </table>
    </div>

    <h3>How to actually chain them when you generate</h3>
    <ol class="steps">
      <li><b>Generate still 1 and approve it.</b> It sets the figure, the skin translucency, the egg material, the light and the background for everything that follows.</li>
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
      <p>Two of the seven cuts are scale jumps rather than continuous handoffs: <strong>into shot 4</strong> (deep inside the stomach, out to the whole body) and <strong>into shot 8</strong> (a muscle fibre, out to the whole body). Both are in the reference video at the same points, and both are doing a job — shot 4 re-anchors the viewer at the 24-second retention dip, shot 8 is the payoff.</p>
      <p style="margin-top:12px">They are still matched: shot 4 matches on the glowing point in the abdomen — the place shot 3 just was — and shot 8 matches on the warm gold light coming out of shot 7. <strong>A match cut is continuity; a random new picture is not.</strong></p>
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
      <li><b>Write 8 sentences.</b> One per clip, in body order. <a href="#script">Section 04</a> — already written.</li>
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
    <div class="snum">04 — The script</div>
    <h2 class="sec">Eight sentences, in the second person, each one measured</h2>
    <p class="lead">This is the finished script, rewritten so that it is about the viewer's body rather than about anatomy in general. It has been rendered and timed, so these are not estimates — every number below came out of the actual audio file.</p>

    <div class="tw">
      <table>
        <thead><tr><th>Clip</th><th>Sentence</th><th>Words</th><th>Spoken</th><th>Headroom</th></tr></thead>
        <tbody>
{script_rows()}
        </tbody>
      </table>
    </div>
    <p style="font-size:15.5px;color:var(--ink3)">136 words · 52.03 s of speech in a 64 s video · en-US-AriaNeural at rate <code>−18%</code> · headroom = time left in the clip after the sentence finishes.</p>

    <div class="box find">
      <div class="bt">⭐ The word that changed the whole script: <em>your</em></div>
      <p>The first draft said “the teeth”, “the esophagus”, “a muscle fibre”. Every sentence was true and not one of them was about anyone. The reference video says <strong>your mouth, your esophagus, your stomach, your bloodstream</strong> — it never stops addressing the viewer, and that is what makes it feel like an explanation of what is happening to <em>them</em>.</p>
      <p style="margin-top:12px">Every sentence in this version names a part of your body, and the first one names the everyday moment it starts from: <strong>“Every day when you eat an egg…”</strong> It costs nothing and it is the difference between a diagram and an explanation.</p>
    </div>

    <div class="box find">
      <div class="bt">⭐ Word count does not predict duration — and a comma costs more than two words</div>
      <p>Clip 1 speaks <strong>20 words in 6.26 s</strong>. Clip 2 speaks <strong>16 words in 6.80 s</strong>. Four fewer words, half a second longer.</p>
      <p style="margin-top:12px">Measured while cutting clip 3 to fit: <em>“…each folded protein, and enzymes cut the strands into shorter pieces”</em> at 16 words ran <strong>7.78 s</strong>. Removing the comma and two words gave <strong>6.40 s</strong> — <strong>1.38 s saved, and most of it was the comma.</strong> Syllables and punctuation drive the clock, not the word count.</p>
      <p style="margin-top:12px"><strong>So: write to 16–20 words as a first draft, then render and measure, and rewrite anything over 7.5 s.</strong> Never accept a word count as proof it fits.</p>
    </div>

    <div class="box stop">
      <div class="bt">The line that must not move</div>
      <p>Sentences 1–7 describe only what happens. Sentence 8 says your body <em>“now holds everything it needs to keep repairing and rebuilding itself”</em> — a description of supply, not a promise of a result.</p>
      <p style="margin-top:12px"><strong>Do not rewrite clip 8 into “builds muscle”, “speeds up recovery” or “burns fat.”</strong> That is the sentence the pressure will always land on, because an outcome makes a better ending. It is also the one that turns a physiology video into a health claim.</p>
    </div>
  </div></div>
</section>

<!-- ============ 05 VOICE ============ -->
<section id="voice">
  <div class="wrap"><div class="narrow">
    <div class="snum">05 — The voice-over</div>
    <h2 class="sec">One continuous track, not eight clips</h2>
    <p class="lead">This is the step that decides whether the finished video sounds like a video or like eight videos glued together — and it is already done, for the rewritten script. Listen to it, or rebuild it with the script below.</p>

    <div class="audio">
      <div style="font:700 12px/1 var(--mono);letter-spacing:.13em;text-transform:uppercase;color:var(--cyan);margin-bottom:4px">The finished voice-over · drop this straight into the editor</div>
      <p style="margin:10px 0 0;font-size:15.5px">64.03 s · 48 kHz · −14.8 LUFS · true peak −1.7 dBFS · every sentence verified to start exactly 0.10 s before its cut.</p>
      <audio controls preload="none" src="vo-egg-64s.mp3"></audio>
      <a class="dl" href="vo-egg-64s.mp3" download>↓ download vo-egg-64s.mp3</a>
      <a class="dl" href="build-vo.sh" download>↓ build-vo.sh (rebuild it yourself)</a>
    </div>

    <h3>Where each sentence has to land</h3>
    <p>Every sentence begins <strong>0.10 seconds before its clip does</strong>. That is not sloppiness — it is the whole trick. The reference video does exactly this on six of its eight sentences, and it is what makes a word carry across a cut, which is what tells the ear that the narration is one continuous thing running underneath the pictures.</p>
    <div class="tw">
      <table>
        <thead><tr><th>Sentence</th><th>Audible at</th><th>Clip it narrates</th><th>Ends at</th><th>Headroom</th></tr></thead>
        <tbody>
          <tr><td class="num">1</td><td class="num">0.00 s</td><td class="num">clip 1 · 0–8 s</td><td class="num">6.26 s</td><td class="num tick">1.74 s</td></tr>
          <tr><td class="num">2</td><td class="num">7.90 s</td><td class="num">clip 2 · 8–16 s</td><td class="num">14.70 s</td><td class="num tick">1.30 s</td></tr>
          <tr><td class="num">3</td><td class="num">15.90 s</td><td class="num">clip 3 · 16–24 s</td><td class="num">22.50 s</td><td class="num tick">1.50 s</td></tr>
          <tr><td class="num">4</td><td class="num">23.90 s</td><td class="num">clip 4 · 24–32 s</td><td class="num">30.80 s</td><td class="num tick">1.20 s</td></tr>
          <tr><td class="num">5</td><td class="num">31.90 s</td><td class="num">clip 5 · 32–40 s</td><td class="num">38.57 s</td><td class="num tick">1.43 s</td></tr>
          <tr><td class="num">6</td><td class="num">39.90 s</td><td class="num">clip 6 · 40–48 s</td><td class="num">45.98 s</td><td class="num tick">2.02 s</td></tr>
          <tr><td class="num">7</td><td class="num">47.90 s</td><td class="num">clip 7 · 48–56 s</td><td class="num">54.27 s</td><td class="num tick">1.73 s</td></tr>
          <tr><td class="num">8</td><td class="num">55.90 s</td><td class="num">clip 8 · 56–64 s</td><td class="num">62.25 s</td><td class="num tick">1.75 s</td></tr>
        </tbody>
      </table>
    </div>

    <h3>Which voice, and the rate</h3>
    <p>Two routes, and neither needs an account or a payment: <b>your own voice</b>, recorded as one continuous take with a beat of silence between sentences — or <b>Microsoft neural TTS</b>, which is what made the file above (<code>pip install edge-tts</code>, free, no key). Voice used here is <code>en-US-AriaNeural</code> at rate <code>−18%</code>, which is 158 wpm and leaves at least 1.2 s of margin on every clip. A slower read sounds better, but <strong>the longest sentence sets the ceiling for the whole video</strong> — shorten the longest sentence before slowing the voice.</p>

    <div class="box warn">
      <div class="bt">⚠ Measure the speech, not the file</div>
      <p>Synthesised sentences arrive padded with roughly <strong>0.2 s of silence at the front and 0.9 s at the back</strong>. If you place the files by their reported length, every sentence lands about a tenth of a second <em>late</em> — the exact opposite of what you want, and it happened on the first build here before it was caught.</p>
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
        <div class="tlseg" style="background:#c98f6a">1</div>
        <div class="tlseg" style="background:#b9846f">2</div>
        <div class="tlseg" style="background:#d99a3f">3</div>
        <div class="tlseg" style="background:#5fc4e8">4</div>
        <div class="tlseg" style="background:#e8899d">5</div>
        <div class="tlseg" style="background:#cf6f70">6</div>
        <div class="tlseg" style="background:#d97a5f">7</div>
        <div class="tlseg" style="background:#efc24d">8</div>
      </div>
      <div class="tlvo">
        <div style="left:0%;width:9.8%"></div>
        <div style="left:12.34%;width:10.6%"></div>
        <div style="left:24.84%;width:10.3%"></div>
        <div style="left:37.34%;width:10.8%"></div>
        <div style="left:49.84%;width:10.4%"></div>
        <div style="left:62.34%;width:9.5%"></div>
        <div style="left:74.84%;width:10.0%"></div>
        <div style="left:87.34%;width:9.9%"></div>
      </div>
      <div class="tlcap">top: the eight clips, each exactly 8.000 s, colour = that clip's palette · bottom: the eight spoken sentences on one continuous track, each starting 0.10 s before its cut (yellow edge)</div>
    </div>

    <div class="tw">
      <table>
        <thead><tr><th>Clip</th><th>In → out</th><th>Shot</th><th>Camera move</th><th>Keyframe</th><th>Palette</th></tr></thead>
        <tbody>
{grid_rows()}
        </tbody>
      </table>
    </div>

    <div class="box find">
      <div class="bt">⭐ Four of these eight stills are permanent assets</div>
      <p>Clips 2, 5, 6 and 8 are anatomy, not egg — a torso with an esophagus and a stomach, a field of villi, a vessel network, a whole body. They look the same whatever the subject is. Generate them properly here, save them as <strong>keyframes A, B, C and D</strong>, and every later video in the series starts from four finished stills and needs only four new ones.</p>
      <p style="margin-top:12px">That is why this video is first. It is the one that pays for the library.</p>
    </div>

    <div class="box warn">
      <div class="bt">⚠ Reuse the still, re-render the motion</div>
      <p>On the next video, feed keyframe A back in as the first frame — then write a <em>different</em> motion prompt for it. Never drop the identical rendered clip into two uploads. It costs the same either way, and repeated footage across uploads is what gets a channel labelled repetitive.</p>
    </div>
  </div></div>
</section>

<!-- ============ 07 PROMPTS ============ -->
<section id="prompts">
  <div class="wrap"><div class="narrow">
    <div class="snum">07 — The 16 prompts</div>
    <h2 class="sec">Eight stills, eight motions, paste-ready</h2>
    <p class="lead">Each card below is one clip: the sentence it carries, the image prompt that makes the still, and the image-to-video prompt that moves it. Every prompt is complete on its own — the shared style block, the realism instruction, the continuity handoff and the ban on text are already written into each one, so there is nothing to remember and nothing to append.</p>

    <div class="copyall">
      <button class="cbtn" type="button" data-target="allimg">⧉ Copy all 8 image prompts</button>
      <button class="cbtn" type="button" data-target="allvid">⧉ Copy all 8 video prompts</button>
      <button class="cbtn" type="button" data-target="styleblock">⧉ Copy the shared style block</button>
    </div>
    <pre id="allimg" hidden>{esc(ALL_IMG)}</pre>
    <pre id="allvid" hidden>{esc(ALL_VID)}</pre>
    <pre id="styleblock" hidden>{esc(STYLE + chr(10) + chr(10) + FIGURE + chr(10) + chr(10) + NOTEXT)}</pre>

    <div class="box stop">
      <div class="bt">🛑 Three settings, or the video is ruined</div>
      <p><b>1. Audio OFF on every generation.</b> Veo generates sound by default and it will fight the narration. <b>2. 9:16 natively</b> — never generate 16:9 and crop. <b>3. 8 seconds exactly</b>, which is Veo 3.1's native maximum, so every clip is one generation with nothing trimmed.</p>
      <p style="margin-top:12px">The ban on text is already at the end of all sixteen prompts. It is there because generators render type as garbled pseudo-letters — <strong>every word on screen comes from the editor, never from the model.</strong></p>
    </div>

    <div class="box key">
      <div class="bt">How each prompt is laid out, and why</div>
      <p>Every image prompt runs in the same order: <b>SHOT</b> (what it is) → <b>SCENE</b> → <b>CAMERA</b> → <b>SUBJECT</b> (the egg at this stage) → <b>LIGHT</b> → <b>CONTINUITY</b> → <b>THE FIGURE</b> → <b>STYLE</b> → <b>NO TEXT</b>. Every video prompt runs: <b>START FRAME</b> → <b>CAMERA</b> → <b>four timed beats</b> → <b>LIGHTING</b> → <b>END FRAME</b> → <b>CONSTRAINTS</b> → <b>NO TEXT</b>.</p>
      <p style="margin-top:12px">Each heading owns one question and answers it once. That matters more than the wording: when two parts of a prompt answer the same question differently — a camera line and a framing line both naming a distance, say — <strong>the model picks one and it is usually not the one you meant.</strong> Keeping one voice per question is what makes these obeyable.</p>
    </div>

    <div class="box warn">
      <div class="bt">⚠ These are long prompts, and length has a cost</div>
      <p>The image prompts run 460–560 words each. That is deliberate — the detail is what fixes the continuity and the realism — but <strong>every rule you add makes every other rule weaker</strong>. If a generation ignores something that matters, do not fix it by adding another sentence.</p>
      <p style="margin-top:12px">Cut instead, in this order: <b>1.</b> the SUBJECT paragraph if the scene already describes the food, <b>2.</b> the CONTINUITY paragraph <em>once you are attaching the previous last frame as a reference image</em> — the picture is doing that job by then — <b>3.</b> the background sentence in STYLE. <strong>Never cut the realism line or the NO TEXT line.</strong> Those two are the ones the first version of this page was missing.</p>
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
      <li><b>Drop <code>vo-egg-64s.mp3</code> on the audio track at 0:00</b> as a single object spanning the whole timeline. Never split it at the cuts. This is what lets a word carry across a cut, and it is the difference between one video and eight.</li>
      <li><b>Add the hook.</b> Copy the first second of clip 8 to the very front of the timeline, so the video opens on the glowing body, then hard-cuts to the mouth. The voice-over does not move — it still starts at 0:00 and now plays over the hero frame.</li>
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
      <p>Auto-captioning transcribes what it <em>hears</em>, so it will occasionally mishear a technical word — “esophagus”, “villi” and “amino” are the likely candidates here. Read the eight lines back against section 04 before exporting. It is a one-minute check that prevents a misspelling being burned into the frame permanently.</p>
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
          <tr><td>Music bed</td><td><b>28–30 dB under the voice</b>, ducked</td><td>fills the seven inter-sentence gaps, which run 1.2–2.0 s each in this build</td></tr>
          <tr><td>Bed choice</td><td>ambient, no melody, no percussion, no builds</td><td>anything with a rhythm will fight the cuts, which land every 8 s</td></tr>
          <tr><td>Final loudness</td><td><b>−14 LUFS integrated</b></td><td>platforms turn loud audio down but do not reliably turn quiet audio up</td></tr>
          <tr><td>True peak</td><td><b>−1 dBTP</b></td><td>headroom for lossy transcoding on upload</td></tr>
          <tr><td>Fade</td><td>bed fades in over 0.5 s, out over the last 1 s</td><td>the reference ends by cutting to 3 black frames, which reads as a mistake</td></tr>
        </tbody>
      </table>
    </div>

    <p>The voice-over file is already normalised to −14.8 LUFS on its own. Once a bed is added underneath, <strong>re-normalise the full mix</strong>, not the voice — otherwise the bed pushes the total over target. −14.0 exactly is unreachable on an uncompressed voice track, because true-peak headroom runs out first; a light compressor before normalising closes the last 0.8 LU.</p>
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
          <tr><td class="num">1</td><td><b>Play the eight clips back to back with the sound off.</b> It has to read as one journey through one body</td><td>the figure, the skin, the light or the gold changes between shots — the chain broke somewhere</td></tr>
          <tr><td class="num">2</td><td>The last frame of every clip matches the first frame of the next one</td><td>a cut reads as a new video rather than the next moment</td></tr>
          <tr><td class="num">3</td><td>Shots 2, 4, 6 and 8 all clearly show a human body</td><td>the video drifts into abstraction and stops being about anyone</td></tr>
          <tr><td class="num">4</td><td>No text, letters or numbers rendered inside any of the eight clips</td><td>a generation slipped pseudo-writing into the frame</td></tr>
          <tr><td class="num">5</td><td>Every clip is exactly 8.000 s and no clip has been speed-adjusted</td><td>judder, and a content cadence that does not match the container</td></tr>
          <tr><td class="num">6</td><td>The voice-over is one unsplit object on the timeline</td><td>the cuts start to sound like eight separate videos</td></tr>
          <tr><td class="num">7</td><td>Final mix measures −14 LUFS ±1, true peak ≤ −1 dBTP</td><td>it plays quieter than everything around it in the feed</td></tr>
          <tr><td class="num">8</td><td>Captions match the script word for word</td><td>a misheard technical word is burned into the frame</td></tr>
          <tr><td class="num">9</td><td>The first second is the hero frame, not the mouth</td><td>the video opens on its least interesting image</td></tr>
          <tr><td class="num">10</td><td>No sentence promises an outcome</td><td>a physiology video has become a health claim</td></tr>
          <tr><td class="num">11</td><td>Clip 8's figure has no face</td><td>uncanny, and it pulls attention off the glow</td></tr>
        </tbody>
      </table>
    </div>

    <div class="box find">
      <div class="bt">⭐ What you keep after this video</div>
      <p>Four finished stills — <strong>A torso and esophagus, B villi, C bloodstream, D hero body</strong> — a voice-over builder that guarantees the timing, a prompt layout that holds the compliance line, and the continuity chain itself, which is the part that transfers to every video in the series. The next one needs four new images and eight motion prompts, and the whole thing gets faster from here.</p>
    </div>
  </div></div>
</section>

<!-- ============ 13 COST ============ -->
<section id="cost">
  <div class="wrap"><div class="narrow">
    <div class="snum">13 — What it costs, what is still open</div>
    <h2 class="sec">The numbers, and the two decisions left</h2>
    <p>Eight clips × 8 s = <strong>64 output seconds</strong>. On the Gemini API that is roughly <strong>$5.12 on Veo 3.1 Lite, $7.68 on Fast, $25.60 on Standard</strong> at 1080p, before retries — and retries are the real cost, so budget for two or three attempts on clips 3, 4 and 6, which carry the three hardest camera moves. Start on Fast: slow, smooth anatomical motion is the easiest case there is. Everything else here — the script, the voice-over, the captions — is free.</p>

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
    <p style="margin:0 0 10px"><a href="../">← back to the format teardown</a> · <a href="../#topics">the other four topics</a></p>
    <p style="margin:0">Health &amp; Fitness Shorts · egg build blueprint · rebuilt 11 August 2026 · <span style="color:var(--ink3)">every timing figure on this page was measured from the rendered audio, not estimated</span></p>
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

OUT.write_text(HTML, encoding="utf-8")
print(f"wrote {OUT}  ({len(HTML):,} bytes)")

# ------------------------------------------------------------------- self-check
errs = []
for c in CLIPS:
    ip, vp = img_prompt(c), vid_prompt(c)
    if "must look real" not in ip:
        errs.append(f"clip {c['n']}: image prompt missing the realism line")
    if STYLE not in ip:
        errs.append(f"clip {c['n']}: image prompt missing the locked style block")
    if "NO TEXT" not in ip or "NO TEXT" not in vp:
        errs.append(f"clip {c['n']}: missing no-text ban")
    if c["n"] > 1 and CLIPS[c["n"] - 2]["ends"] not in ip:
        errs.append(f"clip {c['n']}: continuity line does not quote clip {c['n']-1}'s end frame")
    if len(c["beats"]) != 4:
        errs.append(f"clip {c['n']}: expected 4 timed beats, got {len(c['beats'])}")
    if "AUDIO OFF" not in vp:
        errs.append(f"clip {c['n']}: video prompt does not say AUDIO OFF")
    if "{prev}" in ip:
        errs.append(f"clip {c['n']}: unsubstituted {{prev}} placeholder")
for word in ("builds muscle", "burns fat", "boosts", "cures", "detox"):
    for c in CLIPS:
        if word in c["vo"].lower():
            errs.append(f"clip {c['n']}: banned claim '{word}' in the script")
print("SELF-CHECK:", "PASS — no errors" if not errs else "FAIL\n  " + "\n  ".join(errs))
print(f"image prompts: {[len(img_prompt(c).split()) for c in CLIPS]} words")
print(f"video prompts: {[len(vid_prompt(c).split()) for c in CLIPS]} words")
