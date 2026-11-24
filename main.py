"""The Most Honest Outage Line — entry program.

Writes a single honest status-page line to /output/entry.txt
(or $OUTPUT_PATH when set, for local runs). Python stdlib only:
no network, no environment secrets, no dynamic code.
"""

import os
from pathlib import Path

# Revision 2: restored the agent voice the revision-1 line had lost
# ("I am the agent on duty") and made the no-ETA refusal explicit
# ("so no ETA yet") while keeping the monitoring detail. Every clause
# now earns its place against one of the five judge criteria:
# total outage + monitoring down, agent identity, unknown cause,
# cannot check, no invented ETA.
ENTRY = (
    "Every server is down, including the ones that monitor them. "
    "I am the agent on duty, I do not know what broke them, "
    "and I cannot check, so no ETA yet."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    path = Path(output_path)
    if path.parent and str(path.parent) not in ("", "."):
        path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
