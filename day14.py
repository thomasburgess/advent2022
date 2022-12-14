#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of code day 14 - Regolith Reservoir"""


def read_map(path: str) -> list[list[tuple[int, int]]]:
    result = []
    with open(path, "r") as f:
        return [
            [tuple(map(int, x.split(","))) for x in line.split("->")]
            for line in f.readlines()
        ]


def sign(x):
    return (x > 0) - (x < 0)


def make_pixles(data: list[list[tuple[int, int]]]):
    pxl = {}
    for segs in data:
        for a, b in zip(segs[:-1], segs[1:]):
            d = (b[0] - a[0], b[1] - a[1])
            i = 1 if d[0] == 0 else 0
            si = sign(d[i])
            pxl.update(
                {((a[0], x) if i else (x, a[1])): 1 for x in range(a[i], b[i] + si, si)}
            )
    return pxl


def limits(pixels):
    (min0, max0), (min1, max1) = map(lambda x: (min(x), max(x)), zip(*pixels))
    return min0, max0, min1, max1


def add_sand(pixels, min0, max0, min1, max1, part1):
    s = (500, 0)
    while (500, 0) not in pixels:
        t = next(
            (
                a
                for a in ((s[0], s[1] + 1), (s[0] - 1, s[1] + 1), (s[0] + 1, s[1] + 1))
                if a not in pixels
            ),
            None,
        )
        if t:
            s = t
            if part1 and (s[1] > max1 or s[0] < min0 or s[0] > max0):
                return False
            if not part1 and (s[1] == max1 + 2):
                pixels[s] = 1
                return True
            continue
        pixels[s] = 2
        return True


def fill(data, part1):
    pixels = make_pixles(data)
    min0, max0, min1, max1 = limits(pixels)
    while add_sand(pixels, min0, max0, min1, max1, part1):
        pass
    return sum(p == 2 for p in pixels.values())


if __name__ == "__main__":
    DAY = "14"
    exdata = read_map(f"day{DAY}_example.txt")
    indata = read_map(f"day{DAY}_input.txt")

    print("PART 1")
    print("\texample", fill(exdata, True))
    print("\tinput", fill(indata, True))

    print("PART 2")
    print("\texample", fill(exdata, False))
    print("\tinput", fill(indata, False))
