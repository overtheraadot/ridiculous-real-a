"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Writes one sentence (at most 200 characters) pitching a bizarre startup
idea that sounds absurd until you realise it would actually sell, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

LINE = (
    "We sell an AI that invents fake citations, then cites itself as proof "
    "\u2014 universities pay $99 a month, because the only way to catch "
    "students faking references is a machine that fakes them better."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
