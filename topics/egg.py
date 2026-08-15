"""Video 1 — "What happens when you eat an egg."

Ported from build-egg-page.py (11 Aug 2026) and extended with the per-shot
REAL ANATOMY blocks. Timings are measured from the rendered voice-over.
"""

TOPIC = dict(
    slug="egg",
    video_no=1,
    lane="protein lane",
    emoji="\U0001F95A",
    accent="#ffe23d",
    glow="rgba(255,226,61,.13)",
    h1_plain="What happens when you eat an egg",
    title_html="What happens<br>when you eat<br><em>an egg.</em>",
    sub=("Everything needed to make the finished 64-second short: the full script, <strong>the voice-over already "
         "rendered and measured</strong>, and all 16 prompts written out — <strong>one unbroken journey through one "
         "body</strong>, every shot handing its last frame to the next one."),
    palette=("warm flesh pink and deep red tissue, cream-yellow egg, cool cyan-teal rim light, dark navy background "
             "falling to black, with two or three very soft out-of-focus blue holographic panels far behind the "
             "subject blurred into pure glow"),
    vo_file="vo-egg-64s.mp3",
    kf_chip="Mints keyframes <b>A\u2013D</b>",
    locks="the cream-yellow egg material",
    chain_break=("Two of the seven cuts are scale jumps rather than continuous handoffs: <strong>into shot 4</strong> "
                 "(deep inside the stomach, out to the whole body) and <strong>into shot 8</strong> (a muscle fibre, "
                 "out to the whole body). Both are in the reference video at the same points, and both are doing a "
                 "job \u2014 shot 4 re-anchors the viewer at the 24-second retention dip, shot 8 is the payoff. They "
                 "are still matched: shot 4 matches on the glowing point in the abdomen \u2014 the place shot 3 just "
                 "was \u2014 and shot 8 matches on the warm gold light coming out of shot 7."),
    compliance=("Sentences 1\u20137 describe only what happens. Sentence 8 says your body <em>\u201cnow holds "
                "everything it needs to keep repairing and rebuilding itself\u201d</em> \u2014 a description of "
                "supply, not a promise of a result. <strong>Do not rewrite clip 8 into \u201cbuilds muscle\u201d, "
                "\u201cspeeds up recovery\u201d or \u201cburns fat\u201d.</strong> That is the sentence the "
                "pressure will always land on, because an outcome makes a better ending. It is also the one that "
                "turns a physiology video into a health claim."),
    caption_words="\u201cesophagus\u201d, \u201cvilli\u201d and \u201camino\u201d",
    hook_step=("Copy the first second of clip 8 to the very front of the timeline, so the video opens on the glowing "
               "body, then hard-cuts to the mouth. The voice-over does not move \u2014 it still starts at 0:00 and "
               "now plays over the hero frame."),
    check_hook="The first second is the glowing hero body, not the mouth",
    kf_box_title="Four of these eight stills are permanent assets",
    kf_box=("Clips 2, 5, 6 and 8 are anatomy, not egg \u2014 a torso with an esophagus and a stomach, a field of "
            "villi, a vessel network, a whole body. They look the same whatever the subject is. Generate them "
            "properly here, save them as <strong>keyframes A, B, C and D</strong>, and every later video in the "
            "series starts from four finished stills and needs only four new ones. That is why this video is first: "
            "it is the one that pays for the library."),
    keep=("Four finished stills \u2014 <strong>A torso and esophagus, B villi, C bloodstream, D hero body</strong> "
          "\u2014 a voice-over builder that guarantees the timing, a prompt layout that holds the compliance line, "
          "and the continuity chain itself, which is the part that transfers to every video in the series. The next "
          "one needs four new images and eight motion prompts, and the whole thing gets faster from here."),
    hard_clips="clips 3, 4 and 6",
    prev=None,
    next=("coffee", "Coffee"),
)

CLIPS = [{'n': 1,
  'name': 'The mouth',
  'where': 'Mouth · head close-up',
  'tc': '0:00.000 → 0:08.000',
  'kf': ('new', 'new still'),
  'colour': '#c98f6a',
  'palette': 'warm flesh + cyan rim · medium close-up',
  'vo': 'Every day when you eat an egg, the journey starts in your mouth, where your teeth break the white apart.',
  'spoken': 6.26,
  'ends': 'Mouth closed. A pale cream mass of chewed egg is sitting at the back of the tongue, at the entrance to '
          'the throat. The jaw is relaxed.',
  'img': [('SHOT 1 OF 8 — THE MOUTH.',
           'A hyper-realistic anatomical human head in three-quarter profile, taking a bite of boiled egg.'),
          ('SCENE',
           'An adult human head and shoulders turned three-quarters toward camera against a dark navy background. '
           'The skin is semi-transparent, so the skull, the jaw and cheek muscles, the tongue and the whole row of '
           'teeth read clearly through it — the look of a high-end medical visualisation figure. The face is calm '
           'and neutral, eyes open, no expression. The mouth is open and a stainless steel fork holds a piece of '
           'boiled egg between the front teeth, which have just closed on it. Fine clear strands of saliva stretch '
           'between the food and the tooth surfaces. Below the jaw, through the neck, the throat and the top of the '
           'esophagus are visible as a pale ribbed tube running down behind the windpipe.'),
          ('CAMERA',
           'Medium close-up: the frame runs from the top of the skull down to the collarbones. Camera at mouth '
           'height, level with the face, 50 mm equivalent lens, shallow depth of field with the lips, teeth and food '
           'razor sharp and the back of the head falling soft.'),
          ('SUBJECT — the egg, stage 1 of 8',
           'A firm piece of boiled egg white: pale cream, slightly translucent along its cut edge, with a band of '
           'deep yellow yolk running through it. It must read instantly and unmistakably as egg.'),
          ('LIGHT',
           'One warm key light from the upper left catching every wet highlight on teeth, tongue and food. A cool '
           'cyan rim light along the jawline and cheekbone separating the head from the background. Deep shadow '
           'behind the head.'),
          ('CONTINUITY',
           'This is the opening shot and it locks the look for the whole video: this exact figure, this exact skin '
           'translucency, this exact cream-yellow egg material, this warm-key-plus-cyan-rim lighting and this dark '
           'navy background appear in all eight shots. Nothing about the look changes after this frame.')],
  'real': 'the enamel crowns in their true irregular shapes, the pink gum margin running around each tooth, the '
          'papillae covering the surface of the tongue, the wet mucosa lining the inner cheek, the masseter and '
          'temporalis muscles bunching under the skin as the jaw closes, and the epiglottis and the opening of the '
          'esophagus behind the tongue.',
  'cam': 'Push in, small amplitude, slow speed — the frame tightens by roughly 15% across the full eight seconds, '
         'travelling straight in toward the mouth and staying level at mouth height. Motorised smoothness, constant '
         'speed, no handheld shake, no rotation, no whip pan.',
  'beats': [('0.0 – 2.0 s',
             'The fork slides back out of frame to the left. The lips close over the food. The jaw begins to rise.'),
            ('2.0 – 4.0 s',
             'The molars press down through the piece of egg: it compresses, dents, then splits into two. One saliva '
             'strand stretches thin and breaks. Under the transparent skin, the jaw and cheek muscles visibly bunch '
             'and release.'),
            ('4.0 – 6.0 s',
             'Two more chewing cycles, each breaking the pieces smaller, until the egg is a pale, wet, granular '
             'paste. The tongue rolls the paste to the centre of the mouth.'),
            ('6.0 – 8.0 s',
             'The tongue lifts and presses the paste back toward the throat. The mass starts moving to the back of '
             'the mouth as the shot ends.')],
  'light': 'Unchanged throughout — warm key upper left, cyan rim on the jaw. No lighting change in this clip.',
  'cons': 'One motion only: chewing. The head does not turn, nod, tilt, blink hard or speak. Nothing else in the '
          'frame moves. Slow, deliberate and mechanical, continuous from the first frame to the last.',
  'note': ('Note',
           'The only shot in the video with an everyday object in it, and the one that tells the viewer what the '
           'video is about. If the still comes back and the food does not read as egg at a glance, re-roll it — '
           'nothing later in the video re-establishes the subject.')},
 {'n': 2,
  'name': 'The swallow',
  'where': 'Throat → stomach · torso wide',
  'tc': '0:08.000 → 0:16.000',
  'kf': ('mint', 'mints keyframe A'),
  'colour': '#b9846f',
  'palette': 'warm flesh + cyan rim · medium wide',
  'vo': 'You swallow, and your esophagus squeezes in slow waves, pushing the mouthful down toward your stomach.',
  'spoken': 6.8,
  'ends': 'The whole upper body is in frame. The pale bolus has arrived at the lower end of the esophagus and the '
          'ring of muscle at the stomach entrance is opening in front of it. The stomach below is pink and empty.',
  'img': [('SHOT 2 OF 8 — THE SWALLOW.',
           'The same figure, one step wider: head, neck and upper chest, with the esophagus visible running down '
           'inside the body.'),
          ('SCENE',
           'The same adult anatomical figure as shot 1, at the same three-quarter angle, now framed wider so the '
           'head, the whole neck and the upper chest are in view. Through the semi-transparent skin and the pale '
           'ribcage, the esophagus runs from the back of the throat down the centre of the chest, behind the heart, '
           'as a soft ribbed muscular tube. A pale cream mass of chewed egg sits at the very top of that tube, just '
           'entering it. The ring muscles of the esophagus read as evenly spaced bands along its length. A faint '
           'cool cyan glow runs down inside the tube ahead of the mass, showing the direction of travel as a soft '
           'travelling light.'),
          ('CAMERA',
           'Medium wide: the frame runs from just above the head down to the bottom of the ribcage. Camera level, 35 '
           'mm equivalent lens, moderate depth of field with the esophagus and the mass sharp and the shoulders '
           'falling slightly soft.'),
          ('SUBJECT — the egg, stage 2 of 8',
           'No longer a piece: a smooth pale cream bolus roughly the size of a grape, wet and rounded, the same '
           'material as shot 1 in a new shape.'),
          ('LIGHT',
           'Warm key from the upper left across the chest. Cool cyan rim down the left edge of the neck and '
           'shoulder. The esophagus glowing very faintly from within along its length.'),
          ('CONTINUITY',
           'PREVIOUS SHOT ENDED: {prev}. This frame is that same figure at that same angle, one step wider, with '
           'that same chewed mass now formed into a bolus at the top of the esophagus. Same skin, same light, same '
           'background, same egg material.')],
  'real': 'the esophagus as a muscular tube lying behind the trachea and in front of the spine, its wall built from '
          'an inner circular and an outer longitudinal muscle layer, the aortic arch and the left main bronchus '
          'crossing in front of it, the diaphragm it passes through, and the lower esophageal sphincter where it '
          'meets the stomach.',
  'cam': 'Pull out, large amplitude, slow constant speed — the camera retreats and cranes down very slightly, so '
         'that by 8.0 s the frame holds the whole upper body from the top of the head to just below the stomach. One '
         'continuous move, never stopping, never speeding up. No shake, no rotation.',
  'beats': [('0.0 – 2.0 s',
             'The throat contracts once and drives the bolus into the top of the esophagus. The camera begins its '
             'pull-out.'),
            ('2.0 – 4.0 s',
             'Rings of muscle contract in sequence from the top downward, squeezing the tube shut behind the bolus '
             'and pushing it about a third of the way down. The pull-out reveals the collarbones and the top of the '
             'ribcage.'),
            ('4.0 – 6.0 s',
             'The wave continues down the tube. The bolus passes behind the heart, which beats steadily twice in '
             'this window. The pull-out reveals the whole ribcage and the lungs.'),
            ('6.0 – 8.0 s',
             'The stomach comes into frame below the ribs, pink and empty. The bolus reaches the lower end of the '
             'esophagus and the ring of muscle at the stomach entrance opens in front of it.')],
  'light': 'The faint cyan glow inside the esophagus travels down the tube just ahead of the bolus, and fades out as '
           'the shot ends. Key and rim unchanged.',
  'cons': 'One motion: the swallow, as a single continuous travelling squeeze that never stops or restarts. The '
          'figure does not move, turn or gesture; the only other movement in frame is the heartbeat.',
  'note': ('Note · save this one — keyframe A',
           'This still becomes <strong>keyframe A</strong> and it is the most valuable asset in the video. A torso '
           'with a visible esophagus and stomach is identical whatever the food is, so every later video in the '
           'series starts from this exact file — only the colour and shape of the bolus changes. Re-roll it until '
           'the ribcage is clean and the esophagus reads clearly as a tube, not a shadow.')},
 {'n': 3,
  'name': 'Inside the stomach',
  'where': 'Stomach · cutaway → macro',
  'tc': '0:16.000 → 0:24.000',
  'kf': ('new', 'new still'),
  'colour': '#d99a3f',
  'palette': 'warm amber · close → macro',
  'vo': 'Inside your stomach, acid unwinds each folded protein and enzymes cut the strands apart.',
  'spoken': 6.6,
  'ends': 'A long, almost completely straightened golden protein ribbon drifting in amber fluid, with two blunt '
          'translucent enzyme forms closed on it but not yet cutting.',
  'img': [('SHOT 3 OF 8 — INSIDE THE STOMACH.',
           'The stomach, seen close inside the body, its near wall cut away so the inside is visible.'),
          ('SCENE',
           'The same figure, now framed on the abdomen. The stomach fills most of the frame, sitting under the ribs, '
           'with the lower ribcage and the outline of the torso still visible around the edges of frame so it stays '
           'obvious that we are inside a human body. The near wall of the stomach is opened in a clean medical '
           'cutaway, revealing the interior: deep folded ridges of stomach lining in wet red-brown, a churning pool '
           'of warm amber gastric fluid, and the pale cream egg bolus lying in it, already softening and fraying at '
           'the edges. Rising out of the fluid in the near foreground, close to camera and sharp, is a single '
           'tightly coiled protein — a dense golden helix knotted on itself, its surface faceted and faintly '
           'metallic.'),
          ('CAMERA',
           'Medium close-up on the stomach, slightly high angle looking down into the cutaway, 40 mm equivalent '
           'lens, shallow depth of field with the coiled protein sharp in the foreground and the folded stomach '
           'lining soft behind it.'),
          ('SUBJECT — the egg, stage 3 of 8',
           'The bolus breaking apart in acid, and one protein released from it isolated in the foreground, still '
           'tightly coiled and wound on itself.'),
          ('LIGHT',
           'Strong warm amber light coming up through the gastric fluid from below, turning it to glowing honey. The '
           'coiled protein lit hard from the upper left. Cyan rim light along the cut edge of the stomach wall, '
           'tying this shot to the two before it.'),
          ('CONTINUITY',
           'PREVIOUS SHOT ENDED: {prev}. This frame picks up from there: the same body, the camera now settled on '
           'the stomach the bolus was entering, with that same bolus lying in the acid. Same figure, same cyan rim, '
           'same background.')],
  'real': 'the gastric rugae as thick irregular folds of pink-red mucosa, a glistening mucus layer lying over them, '
          'gastric pits reading as fine dark openings across the surface, the submucosal capillary network faintly '
          'visible through the lining, and the greater curvature of the stomach carrying the pool of fluid.',
  'cam': 'Push in, large amplitude, slow steady speed — the camera moves from the medium shot of the stomach forward '
         'through the cutaway opening and into the fluid, ending in macro with the coiled protein filling the centre '
         'of frame. One straight continuous move on a single axis, constant speed, no shake, no rotation, no '
         'stopping.',
  'beats': [('0.0 – 2.0 s',
             'The stomach wall contracts once and the amber fluid swirls; the bolus rolls over and starts to break '
             'apart. The camera begins pushing in toward the coiled protein in the foreground.'),
            ('2.0 – 4.0 s',
             'The push-in continues until the coiled golden protein fills the centre of frame and the stomach lining '
             'behind it becomes a soft wall of red-brown texture. The coil begins to loosen: the outermost turn '
             'lifts away from the body of the knot.'),
            ('4.0 – 6.0 s',
             'The helix unwinds steadily, turn by turn, opening out into a long loose golden ribbon that waves '
             'slowly in the current. Bubbles rise past it continuously.'),
            ('6.0 – 8.0 s',
             'The ribbon straightens almost completely. Two blunt translucent enzyme forms drift in from the edges '
             'of frame and close onto it, gripping it without cutting yet.')],
  'light': 'The amber underlight strengthens as the camera descends into the fluid, until by 6.0 s the whole frame '
           'is lit from below and the background has gone to deep red-brown.',
  'cons': 'One motion: the unwinding. It must read as a coil opening out — tight at 0 s, loose and long at 8 s — not '
          'as something dissolving, exploding, melting or shattering. One continuous transformation across the full '
          'eight seconds, never restarting.',
  'note': ('Note · the money shot',
           'This is the image the video gets remembered for and the one to spend re-rolls on. Two failure modes to '
           'watch: the coil <em>dissolving</em> instead of unwinding, and the camera arriving so early that the '
           'unwinding has nowhere left to go. If the still is right and the motion is wrong, re-run the motion '
           'prompt on the same still rather than regenerating the image.')},
 {'n': 4,
  'name': 'Where we are now → the cut',
  'where': 'Whole body → small intestine',
  'tc': '0:24.000 → 0:32.000',
  'kf': ('new', 'new still'),
  'colour': '#5fc4e8',
  'palette': 'cold blue — colour break · wide → macro',
  'vo': 'In your small intestine, more enzymes arrive and cut those strands down into single amino acids.',
  'spoken': 6.9,
  'ends': 'A loose cloud of small glowing gold beads drifting apart from one another just above the ridged inner '
          'lining of the small intestine.',
  'img': [('SHOT 4 OF 8 — WHERE WE ARE NOW.',
           'The whole body seen at full length in cool blue, with the small intestine lit up inside the abdomen.'),
          ('SCENE',
           'The same figure, now standing at full length facing camera in a dark navy void, rendered in cool blue '
           'X-ray tones: the skeleton, the organs and the outline of the muscles all visible through translucent '
           'blue skin. The small intestine, coiled in the centre of the abdomen, glows clear cyan-white and is by '
           'far the brightest thing in the body. A faint cool trail runs down from the stomach into it. The head, '
           'arms and legs are dim and cool, so the eye goes straight to the abdomen.'),
          ('CAMERA',
           'Wide: the whole figure from above the head to below the feet, filling about four-fifths of the frame '
           'height. Camera level at chest height, 50 mm equivalent lens, the whole figure in focus, the void behind '
           'it clean and empty.'),
          ('SUBJECT — the egg, stage 4 of 8',
           'Not visible as food any more. Its position in the body is what is visible: the cyan-white glow in the '
           'small intestine is where it has reached.'),
          ('LIGHT',
           'Cold: a cyan key from the front left and a deeper blue rim on both edges of the body. The abdomen '
           'self-illuminated from within. No warm light anywhere in this frame.'),
          ('CONTINUITY',
           'PREVIOUS SHOT ENDED: {prev}. This is the one deliberate step back in the video — the same figure seen '
           'whole, so the viewer re-anchors and remembers this is happening inside a body. The glowing point in the '
           'abdomen is exactly where the previous shot just was, and the camera dives straight back into it, so the '
           'step back lasts under two seconds.')],
  'real': 'the jejunum and ileum coiled through the centre of the abdomen with the frame of the colon around them, '
          'the liver sitting under the right ribs, the stomach high on the left, and a correct skeleton — twelve '
          'pairs of ribs, the lumbar spine, the pelvis and the femoral heads.',
  'cam': 'Hold, then push in, very large amplitude, accelerating from slow to moderate and easing off at the end — '
         'the camera holds on the whole figure, then travels forward into the abdomen, through the body wall, and '
         'into the small intestine, ending inside the tunnel. One straight continuous move, no cuts, no rotation, no '
         'shake.',
  'beats': [('0.0 – 1.5 s',
             'The whole body holds still. The cyan glow in the abdomen pulses once, brightening and settling.'),
            ('1.5 – 4.0 s',
             'The camera pushes in toward the abdomen. The figure grows and passes out of frame at the edges; the '
             'camera travels through the translucent body wall and up to the outer surface of the coiled small '
             'intestine.'),
            ('4.0 – 6.0 s',
             'Through the wall and inside: a wet ridged tunnel of coral-pink lining, lit cool blue. The straightened '
             'golden ribbon runs across the frame. Translucent crystalline enzyme forms close along it in sequence '
             'and snip it apart at several points at once.'),
            ('6.0 – 8.0 s',
             'The ribbon separates into a row of small glowing gold beads. They drift apart from one another and '
             'spread out through the frame as the camera slows to a stop.')],
  'light': 'Cold blue throughout the first half. As the camera enters the intestine at 4.0 s, a warm gold glow from '
           'the beads begins to build inside the cold blue and grows to the end of the shot — the first warmth '
           'returning.',
  'cons': 'One motion: the dive in. Everything else follows from it. The cutting happens steadily across the second '
          'half, not all in one frame. The figure at the start does not move, turn or gesture.',
  'note': ('Note · the deliberate colour break',
           'Shot 3 is hot amber and shot 4 opens ice blue, back to back on a hard cut. That jolt is doing retention '
           'work at the 24-second mark, which is roughly where a vertical video loses people — <strong>do not warm '
           'it toward the amber of the shot before it.</strong> The reference video does exactly this at exactly '
           'this point. The gold beads that appear at the end here are the thread that carries through shots 5, 6 '
           'and 7.')},
 {'n': 5,
  'name': 'Through the wall',
  'where': 'Intestinal villi · macro',
  'tc': '0:32.000 → 0:40.000',
  'kf': ('mint', 'mints keyframe B'),
  'colour': '#e8899d',
  'palette': 'pink + gold · macro',
  'vo': 'Your intestinal wall is covered in tiny folds, and the amino acids pass through them into your blood.',
  'spoken': 6.67,
  'ends': 'Inside the capillary within a single villus: red blood cells and glowing gold beads flowing along '
          'together, the vessel wall arcing around the frame.',
  'img': [('SHOT 5 OF 8 — THROUGH THE WALL.',
           'Extreme macro on the lining of the small intestine, so close that individual villi fill the frame.'),
          ('SCENE',
           'The inner surface of the small intestine at extreme magnification: hundreds of soft finger-shaped villi '
           'rising toward camera, wet coral and rose pink, each faintly translucent with a fine red capillary '
           'network glowing just beneath its surface. Small glowing gold beads drift down between them from the top '
           'of frame and rest against their surfaces. Far behind, well out of focus, the tunnel of the intestine '
           'curves away into darkness, so it stays clear we are inside the gut and not in an empty void.'),
          ('CAMERA',
           'Macro, camera low among the villi looking very slightly up, 85 mm macro equivalent, very shallow depth '
           'of field: one band of villi razor sharp, the field in front of and behind it melting into soft pink '
           'bokeh.'),
          ('SUBJECT — the egg, stage 5 of 8',
           'Single amino acids: small, smooth, glowing warm gold beads, the same beads the enzymes released at the '
           'end of the previous shot.'),
          ('LIGHT',
           'Warm gold light raking across from the right, catching every wet villus tip. Cool cyan fill from the '
           'left keeping the shadow side from going flat. The capillaries inside the villi glowing faintly red from '
           'within.'),
          ('CONTINUITY',
           'PREVIOUS SHOT ENDED: {prev}. This frame is those same beads seen closer, resting on the lining they were '
           'drifting above. Same intestine, same beads, same gold — the camera has simply arrived at the surface.')],
  'real': 'villi as finger-shaped projections of mucosa, each with a brush border of microvilli at its tip, a '
          'central lacteal running up its core, a capillary loop wrapped around that lacteal, goblet cells spaced '
          'between the absorptive cells, and the crypts sitting in the valleys at the base of each villus.',
  'cam': 'Truck right, small amplitude, slow speed for the first six seconds, then push in, small amplitude, slow '
         'speed on one villus for the last two. Two linked moves in one continuous take — the sideways drift eases '
         'into the push. No shake, no rotation, no cut.',
  'beats': [('0.0 – 2.0 s',
             'The villi sway gently in a slow current, all together, like a field of grass under water. More gold '
             'beads drift down between them from the top of frame.'),
            ('2.0 – 4.0 s',
             'The camera trucks slowly right across the field. The beads settle down onto the villus surfaces and '
             'stop moving.'),
            ('4.0 – 6.0 s',
             'The beads press into the surface and pass through it, the tissue closing softly behind them. They '
             'reappear inside the villus as glowing points in the capillary loop just beneath the skin of it.'),
            ('6.0 – 8.0 s',
             'The camera pushes in on that one villus until the capillary inside it fills the frame; its wall turns '
             'translucent and we are looking into flowing blood.')],
  'light': 'Constant warm gold rake throughout. The only change is the light from the beads themselves, which is '
           'hidden as they sink and then reappears from inside the villus.',
  'cons': 'One motion: the beads crossing the wall. The villi sway continuously and gently the whole time and never '
          'stop; nothing jerks, snaps or pops. The transfer is a soft absorption, not an impact.',
  'note': ('Note · save this one — keyframe B',
           'This still becomes <strong>keyframe B</strong>. It is the single most reusable image in the series: '
           'every video in the run ends up at this wall, and only the colour of the beads changes. Get the depth of '
           'field right here — one sharp band with soft bokeh in front and behind — and this file will carry five '
           'videos.')},
 {'n': 6,
  'name': 'Into the blood',
  'where': 'Capillary → liver → whole body',
  'tc': '0:40.000 → 0:48.000',
  'kf': ('mint', 'mints keyframe C'),
  'colour': '#cf6f70',
  'palette': 'red + blue → whole body · macro → wide',
  'vo': 'Your blood carries them through your liver, then out along your vessels toward every tissue in your body.',
  'spoken': 6.08,
  'ends': 'The whole body seen at full length, its entire arterial and venous tree visible as a fine red-and-blue '
          'network, with gold points travelling outward along it toward the arms and legs.',
  'img': [('SHOT 6 OF 8 — INTO THE BLOOD.',
           'Inside a blood vessel, with the branching vessel tree visible far beyond it.'),
          ('SCENE',
           'Macro inside a blood vessel: glossy dark red biconcave red blood cells tumbling toward camera through '
           'translucent straw-coloured plasma, with glowing gold beads travelling among them and standing out '
           'clearly against the red. The vessel wall arcs around the edges of frame in translucent pink, lit with a '
           'cold blue rim. Far away in the depth beyond the vessel, faintly visible through the tissue, the '
           'branching silhouette of a much larger vessel tree glows dim red — so the shot reads as one small place '
           'inside a much bigger system.'),
          ('CAMERA',
           'Macro inside the vessel, camera in the centre of the flow facing along it, 50 mm equivalent lens, sharp '
           'focal plane through the middle of frame with the cells at the frame edges softened by motion blur.'),
          ('SUBJECT — the egg, stage 6 of 8',
           'The same warm gold beads, now travelling in blood among the red cells.'),
          ('LIGHT',
           'Deep red ambient from the blood itself, a cold blue rim along the vessel wall, and the gold beads '
           'carrying their own light. Strong red-and-blue contrast, warm centre and cool edges.'),
          ('CONTINUITY',
           'PREVIOUS SHOT ENDED: {prev}. This frame is that same capillary, one moment later, with the camera now '
           'inside the flow. Same beads, same gold, same blood.')],
  'real': 'red blood cells with their true biconcave dimpled shape and no nucleus, an endothelial lining one cell '
          'thick with the cell junctions faintly visible, and vessels branching by real bifurcation into narrower '
          'ones — and at the wide end, an arterial tree in red and a venous tree in blue that follow real vascular '
          'anatomy.',
  'cam': 'Pull out, very large amplitude, one constant slow speed all the way — the camera retreats continuously '
         'from inside the capillary out through the liver, out of the abdomen, and back until the whole standing '
         'figure is in frame. A single unbroken move, never accelerating, never stopping, no rotation, no shake. '
         'This is the longest camera move in the video.',
  'beats': [('0.0 – 2.0 s',
             'Red cells and gold beads stream past camera toward the foreground in a steady current. The camera '
             'begins to pull back along the vessel.'),
            ('2.0 – 4.0 s',
             'The vessel widens as the camera retreats; it exits into a larger vessel and the dark red mass of the '
             'liver forms around it. Gold beads pass through the liver tissue and continue on.'),
            ('4.0 – 6.0 s',
             'The pull-out continues without pause: the liver shrinks, the abdomen forms around it, the ribcage and '
             'the heart come into frame. The heart beats twice in this window.'),
            ('6.0 – 8.0 s',
             'The move completes on the whole figure at full length, its entire arterial and venous network visible '
             'as a fine red-and-blue tree, with gold points travelling outward along it toward the hands and the '
             'feet.')],
  'light': 'Deep red at the start, opening out to a cool dark navy as the camera leaves the body, with the vessel '
           'network self-illuminated and the gold points the brightest thing in frame by the end.',
  'cons': 'One motion: the pull-out, at one constant speed. The flow of blood past camera never changes pace and '
          'never reverses. The figure that resolves at the end is standing still and does not move, turn or gesture.',
  'note': ('Note · save this one — keyframe C',
           'This still becomes <strong>keyframe C</strong>. The pull-out is the only camera move in the video that '
           'travels any real distance, and it is what makes the scale feel like it is opening out — it earns the '
           'whole-body shot that follows. If the generation cuts or stutters part-way through the move, re-roll it; '
           'a broken pull-out here reads as two shots joined.')},
 {'n': 7,
  'name': 'The muscle fibre',
  'where': 'Thigh muscle · extreme macro',
  'tc': '0:48.000 → 0:56.000',
  'kf': ('new', 'new still'),
  'colour': '#d97a5f',
  'palette': 'saturated red + gold · macro, near-still',
  'vo': 'Your muscle fibres pull them in, and use them as the raw material to rebuild their own structure.',
  'spoken': 6.37,
  'ends': 'The muscle fibre lit warmly from within, its cross-banding crisp, everything at rest and completely '
          'still.',
  'img': [('SHOT 7 OF 8 — THE MUSCLE FIBRE.',
           'Extreme macro inside a thigh muscle, with the outline of the leg still faintly visible at the edge of '
           'frame.'),
          ('SCENE',
           'Extreme macro inside the muscle of a thigh: a bundle of skeletal muscle fibres running diagonally across '
           'the frame, deep saturated red, wet and faintly iridescent, with clear pale cross-banding along every '
           'fibre, wrapped in a translucent sheath threaded with fine capillaries. Glowing gold beads travel along '
           'the nearest capillary and rest against the surface of the closest fibre. At the very edge of frame, soft '
           'and far out of focus, the outline of the thigh and the skin surface is still faintly visible against the '
           'dark background, so it stays clear where in the body this is.'),
          ('CAMERA',
           'Extreme macro, camera close and level with the fibre bundle, 100 mm macro equivalent, very shallow depth '
           'of field: the nearest fibre and the beads on it razor sharp, the rest of the bundle falling away soft, '
           'the leg outline at the edge reduced to a suggestion.'),
          ('SUBJECT — the egg, stage 7 of 8',
           'The last of the gold beads, arriving at the tissue that will use them.'),
          ('LIGHT',
           'Warm key from the upper right along the length of the fibres. Cool blue rim along the top edge of the '
           'bundle. Deep black in the gaps between fibres. The beads carrying their own warm light.'),
          ('CONTINUITY',
           'PREVIOUS SHOT ENDED: {prev}. This frame is one of those destinations, close up — the camera has followed '
           'the gold along the network out to a muscle in the thigh. Same beads, same gold, same warm-and-cool '
           'light.')],
  'real': 'skeletal muscle fibres with true sarcomere cross-banding — regular light and dark bands repeating along '
          'every fibre — each fibre sheathed in endomysium, bundles wrapped in perimysium, capillaries running in '
          'the grooves between the fibres, and nuclei sitting just beneath the surface of each fibre.',
  'cam': 'Static shot, with the faintest push in — under 5% across the whole eight seconds, so slow it is barely '
         'perceptible. No pan, no tilt, no truck, no rotation, no shake. This is deliberately the stillest shot in '
         'the video.',
  'beats': [('0.0 – 2.0 s', 'The frame settles. Gold beads travel along the capillary toward the nearest fibre.'),
            ('2.0 – 4.0 s',
             'The first beads touch the fibre surface and sink into it. The fibre brightens softly from within at '
             'each point where one enters.'),
            ('4.0 – 6.0 s',
             'More beads follow and are absorbed. The pale cross-banding along the fibre becomes crisper and more '
             'defined, and the fibre thickens very slightly.'),
            ('6.0 – 8.0 s',
             'The last beads disappear into the fibre. The internal glow settles to a steady warm gold and '
             'everything comes to rest.')],
  'light': "The only change in the frame: the fibre's internal glow rises from nothing to a steady warm gold as the "
           'beads are absorbed. Key and rim unchanged.',
  'cons': 'One motion: absorption. The muscle does not contract, twitch, flex or pulse — it is receiving material, '
          'not working. Nothing swings, nothing snaps. If in doubt, less movement.',
  'note': ('Note',
           'The stillest shot in the video, on purpose. Shot 6 has just travelled a very long way; shot 7 stops '
           'moving so the last shot has somewhere to go. Resist the urge to add a camera move here. This is also the '
           'shot the compliance line lives on — it shows material arriving, not a result being produced.')},
 {'n': 8,
  'name': 'The whole body',
  'where': 'Whole body · hero',
  'tc': '0:56.000 → 1:04.000',
  'kf': ('mint', 'mints keyframe D'),
  'colour': '#efc24d',
  'palette': 'warm gold — colour break 2 · full body',
  'vo': 'From one egg, your body now holds everything it needs to keep repairing and rebuilding itself.',
  'spoken': 6.35,
  'ends': 'The whole vessel network lit steady warm gold, the figure standing still, the camera stopped — a clean '
          'frame to hold under the end card.',
  'img': [('SHOT 8 OF 8 — THE WHOLE BODY.',
           'The same figure at full length, its vessel network glowing warm gold from within.'),
          ('SCENE',
           'The same adult anatomical figure standing at full length facing camera in a dark void, seen from the '
           'front. The body is translucent and smooth, the head without facial features and without hair. Its '
           'internal vessel network glows warm gold from within, brightest through the torso and falling away toward '
           'the hands and the feet. A soft gold haze radiates outward into the darkness around the silhouette. A '
           'cool blue rim light runs down both edges of the body, separating it from the black and tying it back to '
           'the cool shots earlier in the video.'),
          ('CAMERA',
           'Wide: the whole figure from above the head to below the feet, filling about two-thirds of the frame '
           'height, centred, camera level at chest height, 50 mm equivalent lens, the whole figure in sharp focus.'),
          ('SUBJECT — the egg, stage 8 of 8',
           'No longer a separate object at all. It is the gold light in the vessel network — everything that was one '
           'piece of egg, now distributed through the whole body.'),
          ('LIGHT',
           'Warm gold from inside the body, a soft gold ambient haze around it, and a cool blue rim on both edges. '
           'This is the warmest frame in the video and it is meant to be.'),
          ('CONTINUITY',
           'PREVIOUS SHOT ENDED: {prev}. This frame matches on that warm gold light: the same glow, at the scale of '
           'the whole body. It reads as the camera stepping all the way back at the end of the journey. Same figure, '
           'same rim light, same background as shot 1.')],
  'real': 'a correct arterial and venous tree — the aorta arching out of the heart, the carotids up the neck, the '
          'subclavians into the arms, the femorals down the legs — branching down to fine peripheral vessels over a '
          'correct skeleton, with true adult human proportion.',
  'cam': 'Push in, very small amplitude — about 8% over the first six seconds, slowing to a complete stop at 6.0 s '
         'and holding perfectly still to the end. No rotation, no orbit, no shake. The figure never turns.',
  'beats': [('0.0 – 2.0 s', 'The figure stands still. The gold glow in the torso brightens gently.'),
            ('2.0 – 4.0 s',
             'The glow spreads outward from the torso along the vessel network into the shoulders and the hips.'),
            ('4.0 – 6.0 s',
             'It reaches the hands and the feet until the whole network is lit. A soft gold haze builds in the air '
             'around the silhouette.'),
            ('6.0 – 8.0 s',
             'The glow settles and holds steady. The camera stops. The final two seconds are completely still.')],
  'light': 'One continuous lift: gold rising from the torso outward until the whole network is lit, then holding. '
           'Nothing dims, nothing flickers, nothing pulses.',
  'cons': 'The figure stays standing and completely still — it does not turn, rotate, walk, flex, breathe visibly or '
          'gesture. One motion only: light spreading. The head has no facial features at any point.',
  'note': ('Note · save this one, and it opens the video too',
           'This still becomes <strong>keyframe D</strong>, and it does double duty: the first second of the '
           'finished video is this frame, before the hard cut back to the mouth. Specify <em>no facial features</em> '
           'and check the result — a generated face at this scale reads as uncanny and pulls attention off the glow, '
           'which is the entire subject of the shot.')}]

TOPIC["clips"] = CLIPS
