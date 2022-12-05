#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of code day 04"""


def readpairs(path: str) -> list[list[int]]:
    result = []
    with open(path, "r") as f:
        for line in f.readlines():
            result.append(list(map(int, line.replace("-", ",").split(","))))
    return result


def count_contained(pairs: list[list[int]]) -> int:
    return sum(
        map(
            lambda x: (x[2] >= x[0] and x[3] <= x[1])
            or (x[0] >= x[2] and x[1] <= x[3]),
            pairs,
        )
    )


def count_overlaps(pairs: list[list[int]]) -> int:
    return sum(
        map(
            lambda x: (x[1] >= x[2] and x[1] <= x[3])
            or (x[3] >= x[0] and x[3] <= x[1]),
            pairs,
        )
    )


if __name__ == "__main__":
    exdata = readpairs("day04_example.txt")
    indata = readpairs("day04_input.txt")

    print("PART 1")
    print("example", count_contained(exdata))
    print("input", count_contained(indata))

    print("PART 2")
    print("example", count_overlaps(exdata))
    print("input", count_overlaps(indata))
