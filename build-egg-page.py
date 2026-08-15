#!/usr/bin/env python3
"""
SUPERSEDED 15 Aug 2026 — kept so the old command still works.

This file used to hold both the egg video's data and its page template. Both now
live elsewhere, because there are five videos in the series rather than one:

    topics/egg.py    the egg's script, prompts and continuity chain
    pagegen.py       the shared page template and prompt assembly
    build_pages.py   the builder for every topic

Running this file rebuilds the egg page through the new builder, so it can no
longer overwrite the page with the older, weaker prompt set.

    python3 build_pages.py            # all five
    python3 build_pages.py egg        # identical to running this file
"""
import subprocess
import sys
import pathlib

print(__doc__.strip(), "\n")
sys.exit(subprocess.call([sys.executable, str(pathlib.Path(__file__).parent / "build_pages.py"), "egg"]))
