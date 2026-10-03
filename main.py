"""Wallpaper Cycle — Set the desktop wallpaper from a folder, sequentially or random."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='wallpaper_cycle',
        description='Set the desktop wallpaper from a folder, sequentially or random.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Wallpaper Cycle')
    print('A wallpaper folder you actually cycle.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
