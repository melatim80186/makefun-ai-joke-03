"""ai-joke-03 entry: writes one one-liner about AI coding agents.

The joke is fixed text: the judge reads exactly the bytes written, so the
program writes them byte for byte, deterministically, with no trailing
newline and no network.
"""

import os
from pathlib import Path

JOKE = "I told my agent to handle errors gracefully. Now it apologizes to every exception before re-raising it."

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
(output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")
