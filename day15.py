#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of code day 15 - Beacon Exclusion Zone"""

import re


def distance(x):
    return abs(x[0] - x[2]) + abs(x[1] - x[3])


def read_beacons(path: str) -> list[tuple[int, int], int]:
    with open(path, "r") as f:
        return list(
            map(
                lambda x: (x[0:2], x[2:4], distance(x)),
                (
                    tuple(
                        int(i)
                        for i in re.split("; |, |=|:", line.strip())
                        if i.replace("-", "").isdigit()
                    )
                    for line in f.readlines()
                ),
            )
        )


def cover(row, beacons):
    covered = set()
    for s, b, d in beacons:
        dd = d - abs(s[1] - row)
        if dd < 0:
            continue
        covered.update(range(s[0] - dd, s[0] + dd + 1))
        if b[1] == row:
            covered.remove(b[0])
    return len(covered)


def calc_covers(row, beacons, lim):
    covers = []
    for s, b, d in beacons:
        dd = d - abs(s[1] - row)
        if dd < 0:
            continue
        x = max(0, s[0] - dd), min(lim, s[0] + dd + 1)
        covers.append([x[0], x[1]])
        if len(covers) == 1:
            continue

        # Now remove covers
        covers.sort(key=lambda x: x[0])
        idx = 0
        for a in covers:
            if covers[idx][1] >= a[0]:
                covers[idx][1] = max(covers[idx][1], a[1])
            else:
                idx += 1
                covers[idx] = a
        covers = covers[: idx + 1]

        if covers[0][0] == 0 and covers[0][0] == lim:
            return covers
    return covers


def part2(lim: int, beacons):
    for row in range(lim):
        overlap = calc_covers(row, beacons, lim)
        if len(overlap) != 1:
            return 4000000 * overlap[0][1] + row


if __name__ == "__main__":
    DAY = "15"
    exdata = read_beacons(f"day{DAY}_example.txt")
    indata = read_beacons(f"day{DAY}_input.txt")

    print("PART 1")
    print("\texample", cover(10, exdata))
    print("\tinput", cover(2000000, indata))

    print("PART 2")
    print("\texample", part2(20, exdata))
    print("\tinput", part2(4000000, indata))
