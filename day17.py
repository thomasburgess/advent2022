#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of code day 17 - Pyroclastic Flow"""

import itertools
import functools


def make_rocks():
    ROCKS = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##"""
    return tuple(
        set(
            (col, row)
            for row, z in enumerate(r.split()[::-1])
            for col, c in enumerate(z)
            if c != "."
        )
        for r in ROCKS.split("\n\n")
    )


def read_moves(path: str) -> list[int]:
    with open(path, "r") as f:
        return [{"<": -1, ">": 1}[i] for i in f.read()]


@functools.cache
def rock_wh(rock):
    return max(rock)[0] - min(rock)[0] + 1, max(rock, key=lambda x: x[1])[1] + 1


def read_moves(path: str) -> list[int]:
    with open(path, "r") as f:
        return [{"<": -1, ">": 1}[i] for i in f.read()]


def move_rock(rock, w, dx, dy):
    if not any(0 <= x + dx < 8 - w for x, _ in rock):
        return rock
    return set((c + dx, r + dy) for c, r in rock)


def sim(moves: list[bool], rocks, nmax: int):
    irocks = enumerate(itertools.cycle(rocks))
    moves = itertools.cycle(moves)
    n = 0
    x = 2
    y = 0
    height = 0
    rock = None
    board = set((i, 0) for i in range(7))
    while n < nmax:
        if not rock:
            n, rock = next(irocks)
            w, h = rock_wh(tuple(rock))
            y = height + 4
            rock = move_rock(
                rock,
                w,
                2,
                y,
            )
        move = next(moves)
        rock = move_rock(rock, w, move, 0)
        vert = move_rock(rock, w, 0, -1)
        if vert & board:
            board |= rock
            height = max(height, y + h - 1)
            rock = None
            continue
        rock = vert
        y -= 1
    return max(board, key=lambda x: x[1])[1]


def show(R):
    for y in range(max(R, key=lambda x: x[1])[1], -1, -1):
        row = ""
        for x in range(7):
            if (x, y) in R:
                row += "#"
            else:
                row += "."
        print(row)


if __name__ == "__main__":
    DAY = "17"
    exdata = read_moves(f"day{DAY}_example.txt")
    indata = read_moves(f"day{DAY}_input.txt")
    rocks = make_rocks()

    print("PART 1")
    n = 2022
    print("\texample", sim(exdata, rocks, n))
    print("\tinput", sim(indata, rocks, n))
    print("PART 2")
    # n = 1000000000000
    # print("\texample", sim(exdata, rocks, n))
    # print("\tinput", sim(indata, rocks, n))
