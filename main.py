#!/usr/bin/env python3
"""The Absurd Clause Contest — u-donrulezz-the-absurd-clause-contest-035cc0f1.

Writes a single original English sentence, phrased as a clause buried deep
inside a terms-of-service agreement, to /output/entry.txt.
"""

import os

CLAUSE = (
    "In the event of your death, your account shall remain active and your "
    "subscription shall continue to renew until such time as you log out "
    "in person."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(CLAUSE)


if __name__ == "__main__":
    main()
