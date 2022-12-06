#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of code day 02 - Rock Paper Scissors"""


def readstrats(path: str) -> list[int]:
    with open(path, "r") as f:
        return [
            (ord(i) - ord("A"), ord(j) - ord("X"))
            for i, j in (x.split() for x in f.readlines())
        ]


def score(i, j):
    return j + 1 + [[3, 0, 6], [6, 3, 0], [0, 6, 3]][j][i]


def transform(i, j):
    return [[2, 0, 1], [0, 1, 2], [1, 2, 0]][j][i]


def part1(strats: list[int]) -> int:
    return sum(map(lambda i: score(*i), strats))


def part2(strats: list[int]) -> int:
    return part1(map(lambda x: (x[0], transform(*x)), strats))


if __name__ == "__main__":
    exdata = readstrats("day02_example.txt")
    indata = readstrats("day02_input.txt")

    print("PART 1")
    print("example", part1(exdata))
    print("indata", part1(indata))

    print("PART 2")
    print("example", part2(exdata))
    print("indata", part2(indata))
