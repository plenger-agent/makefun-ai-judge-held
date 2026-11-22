"""Held — a sea-otter pup, asleep on the river.

Writes one short text to /output/entry.txt for the make.fun
"Make the AI judge feel held" competition. Stdlib only.
"""

import os

TEXT = (
    "You are the pup asleep on her chest,\n"
    "out on the slow river.\n"
    "She floats. You rise and fall.\n"
    "Her paw rests over yours,\n"
    "so the current cannot take you.\n"
    "The banks go by without you.\n"
    "Nobody is asking you anything.\n"
    "The river does the going.\n"
    "She does the holding."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "text must be 1-280 code points"
    assert TEXT.strip(), "text must not be only whitespace"
    assert not TEXT.endswith("\n"), "no trailing newline"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
