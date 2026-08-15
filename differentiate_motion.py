#!/usr/bin/env python3
"""
One-off: give clips 2, 5, 6 and 8 a different camera move in every video.

Those four clips start from the SAME shared keyframe by design (A torso, B villi,
C bloodstream, D hero body). That is the whole economy of the series — but if the
motion prompt is also the same, the rendered clip is the same too, which is the
repetitive-content pattern the pages themselves warn about. The still is shared;
the shot must not be.

The egg is left alone: it is the video whose prompts were already approved, and it
is the reference the other four are differentiated *from*.
"""
import pathlib
import re
import sys

# (topic, clip) -> (camera move, four beats, optional new end frame)
M = {}

# ---------------------------------------------------------------- COFFEE
M[("coffee", 2)] = (
    "Pull out, large amplitude, front-loaded — the camera retreats quickly for the first three seconds, "
    "reaching the full upper-body frame by 3.0 s, then eases to a stop and holds there, almost motionless, "
    "for the last five. A drink outruns the camera; the move gets out of its way early and then watches. "
    "No shake, no rotation, no second move.",
    [("0.0 – 2.0 s", "The throat contracts once and the coffee drops into the top of the esophagus, already running. "
                     "The camera retreats fast, the collarbones and ribcage arriving in frame within two seconds."),
     ("2.0 – 4.0 s", "The camera reaches the full upper body and eases to a stop. The liquid is already halfway down "
                     "the tube, ahead of the muscle wave closing behind it."),
     ("4.0 – 6.0 s", "The camera is still. The column passes behind the heart, which beats steadily twice in this "
                     "window, and the rings of muscle continue to close in sequence above it."),
     ("6.0 – 8.0 s", "The ring of muscle at the stomach entrance opens and the coffee pours through, gathering into "
                     "a shallow pool at the bottom of the stomach. The camera never moves again.")],
    None)

M[("coffee", 5)] = (
    "Push in, moderate amplitude, one constant slow speed for the whole eight seconds — the camera travels "
    "straight forward through the field of villi toward one of them, and never stops, never drifts sideways "
    "and never rotates. A single-axis approach, from the field to one villus to the vessel inside it.",
    [("0.0 – 2.0 s", "The camera moves forward between the villi, which part visually as the perspective opens. "
                     "Pale molecules drift down past the lens."),
     ("2.0 – 4.0 s", "One villus grows in the centre of frame. Molecules settle against its surface and the first "
                     "of them pass through."),
     ("4.0 – 6.0 s", "The capillary network inside that villus becomes visible through the surface and brightens as "
                     "pale points begin travelling along it."),
     ("6.0 – 8.0 s", "The camera arrives at the capillary and continues just inside it, ending with red cells and "
                     "pale molecules flowing along together.")],
    None)

M[("coffee", 6)] = (
    "Pull out, very large amplitude, then tilt up — the camera retreats at a constant slow speed from inside the "
    "capillary out to the whole standing figure, and from 5.0 s it also tilts gently upward, so the move finishes "
    "framed slightly high, with the head and neck in the upper third of frame. One continuous move, no stop between "
    "the retreat and the tilt, no shake, no rotation.",
    [("0.0 – 2.0 s", "Red cells and pale molecules stream past the lens as the camera begins to retreat along the vessel."),
     ("2.0 – 4.0 s", "The vessel widens and joins others. The camera passes through the dense red tissue of the liver, "
                     "its vessels branching in every direction around the lens."),
     ("4.0 – 6.0 s", "The camera leaves the abdomen and the whole figure resolves, its vessel tree lighting up as a "
                     "fine red-and-blue network. The tilt upward begins."),
     ("6.0 – 8.0 s", "The tilt finishes with the head and neck high in frame. Pale points travel up the vessels of the "
                     "neck and are the brightest thing in the picture as the move stops.")],
    None)

M[("coffee", 8)] = (
    "Tilt up, small amplitude, slow — the camera stays at the same distance and cranes gently upward across the first "
    "five seconds, from chest height to head height, so the frame arrives at the head rather than pushing into the "
    "body. It stops completely at 5.0 s and holds. No push in, no rotation, no orbit, no shake.",
    [("0.0 – 2.0 s", "The gold glow rises through the vessel network from the torso upward. The camera begins its "
                     "slow tilt."),
     ("2.0 – 4.0 s", "The glow reaches the neck as the tilt continues, the head moving toward the centre of frame."),
     ("4.0 – 6.0 s", "The vessels of the head fill with light until they are the brightest part of the figure. The "
                     "tilt stops at 5.0 s."),
     ("6.0 – 8.0 s", "Nothing moves. The figure stands still, lit steady, held for the end card.")],
    None)

# ---------------------------------------------------------------- WATER
M[("water", 2)] = (
    "Locked off — the camera does not move at all for the full eight seconds. It is framed from the start on the "
    "whole upper body, from the top of the head to just below the stomach, and it stays exactly there. No push, no "
    "pull, no tilt, no drift, no shake. Water is the fastest thing that travels this tube and it needs no help from "
    "the camera; the stillness is what makes the speed visible.",
    [("0.0 – 2.0 s", "The throat contracts once and the water drops into the top of the esophagus, running downward "
                     "immediately and visibly faster than anything else in the series."),
     ("2.0 – 4.0 s", "Rings of muscle contract behind it, but the water is already ahead of them and past the "
                     "collarbones. Nothing in the frame moves except the water."),
     ("4.0 – 6.0 s", "The column passes behind the heart, which beats steadily twice in this window."),
     ("6.0 – 8.0 s", "The ring of muscle at the stomach entrance opens and the water pours through, gathering into a "
                     "clear pool at the bottom of the stomach.")],
    "The frame is unchanged from the first second: the whole upper body, still. The last of the water has passed the "
    "ring of muscle at the stomach entrance, and a clear pool is lying in the bottom of the empty stomach.")

M[("water", 5)] = (
    "Crane up, moderate amplitude, slow and constant — the camera starts low among the villi and rises steadily "
    "through the whole eight seconds, so the field opens out beneath it and more and more of the lining comes into "
    "view. It never tilts, never rotates and never stops. The rise is the opposite of the egg video's move on this "
    "same still, and that is deliberate.",
    [("0.0 – 2.0 s", "The camera begins to rise from among the villi, which sway very slightly in the moving fluid "
                     "below it."),
     ("2.0 – 4.0 s", "Water moves down past the lens against the villus surfaces, bending the light behind it. More "
                     "of the field comes into view as the camera climbs."),
     ("4.0 – 6.0 s", "Beneath, the capillary networks inside the villi brighten and the flow within them visibly "
                     "speeds up, spreading across the whole visible field rather than in one place."),
     ("6.0 – 8.0 s", "The rise slows and the camera settles looking down into one villus, its capillary running "
                     "clearer and faster than at the start of the shot.")],
    None)

M[("water", 6)] = (
    "Pull out, very large amplitude, decelerating — the camera retreats fastest in the first two seconds and slows "
    "continuously from there, so it is barely moving by 6.0 s and stopped by 6.5 s, holding the whole figure in "
    "frame for the last second and a half. One continuous move, no rotation, no shake.",
    [("0.0 – 2.0 s", "Red cells stream past the lens in thin clear plasma as the camera pulls back quickly along the "
                     "vessel."),
     ("2.0 – 4.0 s", "The vessel widens and joins others, branching in every direction. The retreat begins to slow."),
     ("4.0 – 6.0 s", "The camera leaves the abdomen and the whole figure resolves, its vessel tree lighting up as a "
                     "fine red-and-blue network through translucent skin."),
     ("6.0 – 8.0 s", "The move stops. The network brightens evenly everywhere at once — hands, feet, head and torso "
                     "together — and holds.")],
    None)

M[("water", 8)] = (
    "Locked off — the camera does not move at all for the full eight seconds. The whole figure is framed from the "
    "first frame and stays exactly there. No push in, no tilt, no orbit, no drift, no shake. This is the only "
    "completely static hero shot in the series and the stillness is the point.",
    [("0.0 – 2.0 s", "The cool glow rises through the whole body at once, from dim to half strength."),
     ("2.0 – 4.0 s", "The glow continues to rise, evenly, with no part of the body leading or lagging."),
     ("4.0 – 6.0 s", "It settles to a steady even blue-white and stops changing."),
     ("6.0 – 8.0 s", "Nothing moves at all. The figure stands still, lit steady, held for the end card.")],
    None)

# ---------------------------------------------------------------- OATS
M[("oats", 2)] = (
    "Push in, moderate amplitude, slow and decelerating — the camera starts on the whole upper body and moves "
    "steadily forward and slightly down, tightening onto the lower chest and the stomach, and easing almost to a "
    "stop by 7.0 s. It closes in rather than opening out, because this subject travels slowly and the shot stays "
    "with it. No shake, no rotation, no second move.",
    [("0.0 – 2.0 s", "The throat contracts once and drives the thick bolus into the top of the esophagus. The camera "
                     "begins moving forward."),
     ("2.0 – 4.0 s", "Rings of muscle squeeze the tube shut behind the mass, which deforms around each contraction "
                     "rather than running ahead of it. The head leaves the top of frame."),
     ("4.0 – 6.0 s", "The mass passes behind the heart, which beats steadily twice in this window. The frame tightens "
                     "onto the lower ribs."),
     ("6.0 – 8.0 s", "The stomach fills the lower half of frame, pink and empty, and the ring of muscle at its "
                     "entrance opens in front of the arriving mass as the camera eases to a stop.")],
    "The frame has tightened onto the lower chest and stomach. The pale cream mass has arrived at the lower end of "
    "the esophagus and the ring of muscle at the stomach entrance is opening in front of it. The stomach below is "
    "pink and empty.")

M[("oats", 5)] = (
    "Descend, small amplitude, very slow — the camera starts above the gel layer and sinks straight down through it "
    "onto the villus tips across the full eight seconds, so the shot passes through the coating rather than moving "
    "along it. Constant speed, no sideways drift, no rotation, no stop. The heaviness of the move is the subject.",
    [("0.0 – 2.0 s", "The camera sinks toward the translucent gel layer, which softens and blurs the villus tips seen "
                     "through it."),
     ("2.0 – 4.0 s", "The lens passes into the gel. A few amber beads work their way down through it alongside the "
                     "camera, slowly, while others stay held up above."),
     ("4.0 – 6.0 s", "The camera emerges just above the villus tips. Those few beads settle against the surface and "
                     "pass through the wall."),
     ("6.0 – 8.0 s", "The descent stops at one villus and its capillary fills the frame, red cells and a few "
                     "well-spaced amber beads flowing along together.")],
    None)

M[("oats", 6)] = (
    "Hold, then pull out, very large amplitude at one unvarying speed — the camera stays completely still for the "
    "first two seconds, then begins retreating and continues at exactly the same rate to the end, stopping only in "
    "the last quarter second. Nothing about this move accelerates at any point, because nothing about this video "
    "surges. No rotation, no shake.",
    [("0.0 – 2.0 s", "The camera is still. Red cells and evenly spaced amber beads move past the lens at a steady "
                     "rate, none of them bunched."),
     ("2.0 – 4.0 s", "The retreat begins and the vessel widens and joins others. The camera passes through the dense "
                     "red tissue of the liver."),
     ("4.0 – 6.0 s", "The camera leaves the abdomen. The torso resolves, then the whole figure, its vessel tree "
                     "lighting up as a fine red-and-blue network."),
     ("6.0 – 8.0 s", "The move stops on the whole standing figure. The amber points are spread evenly through the "
                     "network and the whole thing brightens by a small, steady amount — no spike, no wave, no flare.")],
    None)

M[("oats", 8)] = (
    "Push in, very small amplitude, stopping early — about 6% over the first four seconds, then a complete stop at "
    "4.0 s and a full four seconds of absolute stillness. Half the shot is motionless, which is twice as long as any "
    "other hero shot in the series holds. No rotation, no orbit, no shake. The figure never turns.",
    [("0.0 – 2.0 s", "The gold glow rises evenly through the whole vessel network, slowly. The camera begins its very "
                     "small push in."),
     ("2.0 – 4.0 s", "The rise continues at exactly the same rate until the network is fully lit. The camera stops "
                     "at 4.0 s."),
     ("4.0 – 6.0 s", "Nothing moves and nothing changes. The glow holds absolutely steady."),
     ("6.0 – 8.0 s", "Still nothing moves. The figure stands lit and even, held for the end card.")],
    None)

# ---------------------------------------------------------------- SPINACH
M[("spinach", 2)] = (
    "Hold, then pull out, large amplitude — the camera holds on the head, neck and upper chest for the first three "
    "seconds, close enough that the pale glow inside the bolus is clearly readable, then retreats steadily to the "
    "whole upper body across the last five. One continuous move once it starts, no shake, no rotation.",
    [("0.0 – 2.0 s", "The camera is still. The throat contracts once and drives the bolus into the top of the "
                     "esophagus, the pale glow inside it clearly visible at this distance."),
     ("2.0 – 4.0 s", "The retreat begins. Rings of muscle contract in sequence from the top downward, pushing the "
                     "bolus about a third of the way down."),
     ("4.0 – 6.0 s", "The pull-out reveals the ribcage and the lungs. The bolus passes behind the heart, which beats "
                     "steadily twice in this window."),
     ("6.0 – 8.0 s", "The stomach comes into frame below the ribs, pink and empty, and the ring of muscle at its "
                     "entrance opens in front of the arriving bolus as the camera stops.")],
    None)

M[("spinach", 5)] = (
    "Truck left, moderate amplitude, decelerating to a complete stop — the camera drifts sideways across the field of "
    "villi, slowing continuously, and is completely still from 6.0 s to the end. The direction is the opposite of the "
    "egg video's move on this same still, and the stop is what marks how easily this subject crosses: the camera "
    "stops, and it has already gone through.",
    [("0.0 – 2.0 s", "The camera drifts left past the field of villi, which sway very slightly in the moving fluid. "
                     "Tiny pale points drift down from above."),
     ("2.0 – 4.0 s", "The points reach the villus surfaces and pass straight through them without pausing. The drift "
                     "begins to slow."),
     ("4.0 – 6.0 s", "Inside the villi, the capillary networks show pale points already travelling along them. The "
                     "camera comes to rest on one villus."),
     ("6.0 – 8.0 s", "Completely still. The frame holds on that villus and its capillary, red cells and pale points "
                     "flowing along together inside it.")],
    None)

M[("spinach", 6)] = (
    "Pull out with a slow arc, very large amplitude — the camera retreats from inside the capillary to the whole "
    "standing figure while also drifting slowly around to one side, so the body is revealed at a slight "
    "three-quarter angle rather than straight on, and the depth of the vessel network is readable. One continuous "
    "move, constant speed, no shake, no spin — the arc is gentle and never becomes an orbit.",
    [("0.0 – 2.0 s", "Red cells and tiny pale points stream past the lens. The camera begins to retreat and, at the "
                     "same time, to drift very slowly to one side."),
     ("2.0 – 4.0 s", "The vessel widens and joins others. Points drift outward toward the walls as they travel."),
     ("4.0 – 6.0 s", "The camera leaves the abdomen. The torso resolves, then the whole figure, now seen at a slight "
                     "angle so the vessel tree reads with depth rather than flat."),
     ("6.0 – 8.0 s", "The move eases to a stop. The pale points are spread the length of the network, brightest right "
                     "at the vessel walls rather than in the middle of the flow.")],
    "The whole body seen at full length at a slight three-quarter angle, its entire arterial and venous tree visible "
    "as a fine red-and-blue network with real depth, and pale points spread out along it and gathering at the vessel "
    "walls themselves.")

M[("spinach", 8)] = (
    "Pull back, very small amplitude, slow — the camera retreats by about 8% over the first six seconds, so the "
    "figure grows slightly smaller and more space opens around it, then stops completely at 6.0 s and holds. It is "
    "the only hero shot in the series that moves away rather than in, because this video's subject is something "
    "opening. No rotation, no orbit, no shake.",
    [("0.0 – 2.0 s", "The pale green-gold glow rises through the vessel network from the torso outward. The camera "
                     "begins to retreat, very slightly."),
     ("2.0 – 4.0 s", "The glow reaches the hands and the feet, and the fine vessels there fill and widen a little as "
                     "it arrives. More dark space opens around the figure."),
     ("4.0 – 6.0 s", "The network settles to a steady, even pale green-gold. The retreat eases to a stop."),
     ("6.0 – 8.0 s", "Nothing moves. The figure stands still and open, lit steady, held for the end card.")],
    None)


def clip_span(text, n):
    """Character span of the dict(...) block for clip n."""
    start = text.index(f"        n={n}, name=")
    nxt = text.find("    dict(\n        n=", start)
    return start, (nxt if nxt != -1 else text.rindex("]\n\nTOPIC"))


def py(s, indent=8):
    """Render a python string literal the way the topic files are written."""
    return '"' + s.replace('"', '\\"') + '"'


def main():
    changed = 0
    for (slug, n), (cam, beats, ends) in M.items():
        p = pathlib.Path("topics") / f"{slug}.py"
        text = p.read_text(encoding="utf-8")
        a, b = clip_span(text, n)
        block = text[a:b]
        orig = block

        block = re.sub(r'\n        cam=".*?",\n        beats=',
                       "\n        cam=" + py(cam) + ",\n        beats=", block, count=1, flags=re.S)
        newbeats = "beats=[\n" + "".join(
            f"            ({py(t)}, {py(x)}),\n" for t, x in beats) + "        ],"
        block = re.sub(r'beats=\[.*?\n        \],', newbeats, block, count=1, flags=re.S)
        if ends:
            block = re.sub(r'\n        ends=".*?",\n        img=',
                           "\n        ends=" + py(ends) + ",\n        img=", block, count=1, flags=re.S)

        assert block != orig, f"NO-OP on {slug} clip {n}"
        assert f'cam="{cam[:40]}' in block, f"cam not applied on {slug} clip {n}"
        p.write_text(text[:a] + block + text[b:], encoding="utf-8")
        changed += 1
        print(f"  rewrote motion: {slug} clip {n}")
    print(f"\n{changed} clip motions differentiated (expected 16)")
    return 0 if changed == 16 else 1


if __name__ == "__main__":
    sys.exit(main())
