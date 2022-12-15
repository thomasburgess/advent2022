#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of code day 15 - Beacon Exclusion Zone"""

import re


def distance(x):
    d = abs(x[0] - x[2]) + abs(x[1] - x[3])
    return d, x[1] - d, x[1] + d


def read_beacons(path: str) -> dict[tuple[int, int], str]:
    result = []
    with open(path, "r") as f:
        return sorted(
            list(
                map(
                    lambda x: (x[0:2], x[2:4], *distance(x)),
                    (
                        tuple(
                            int(i)
                            for i in re.split("; |, |=|:", line.strip())
                            if i.replace("-", "").isdigit()
                        )
                        for line in f.readlines()
                    ),
                )
            ),
            key=lambda x: x[4],
        )


def cover(row, beacons):
    overlap = set()
    for s, b, d, ylo, yup in beacons:
        if ylo < row > yup:
            continue
        dd = d - abs(s[1] - row)
        if dd < 0:
            continue
        overlap.update(range(s[0] - dd, s[0] + dd + 1))
        if b[1] == row:
            overlap.remove(b[0])
    return overlap


def merge(arr):
    arr.sort(key=lambda x: x[0])
    idx = 0
    for a in arr[1:]:
        if arr[idx][1] >= a[0]:
            arr[idx][1] = max(arr[idx][1], a[1])
        else:
            idx += 1
            arr[idx] = a
    return arr[: idx + 1]


def cover2(row, beacons, lim):
    overlaps = []
    for s, b, d, ylo, yup in beacons:
        if ylo < row > yup:
            continue
        dd = d - abs(s[1] - row)
        if dd < 0:
            continue
        x = max(0, s[0] - dd), min(lim, s[0] + dd + 1)
        overlaps.append([x[0], x[1]])
        overlaps = merge(overlaps)
        if overlaps[0][0] == 0 and overlaps[0][0] == lim:
            return overlaps
    return overlaps


def part2(lim: int, beacons):
    for row in range(lim):
        overlap = cover2(row, beacons, lim)
        if len(overlap) != 1:
            return 4000000 * overlap[0][1] + row


if __name__ == "__main__":
    DAY = "15"
    exdata = read_beacons(f"day{DAY}_example.txt")
    indata = read_beacons(f"day{DAY}_input.txt")

    print("PART 1")
    print("\texample", len(cover(10, exdata)))
    print("\tinput", len(cover(2000000, indata)))

    print("PART 2")
    print("\texample", part2(20, exdata))
    print("\tinput", part2(4000000, indata))
