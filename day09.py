#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of code day 09 - """


def read_moves(path: str) -> list[tuple[str, int]]:
    with open(path, "r") as f:
        return list(
            map(lambda x: (x[0], int(x[1])), (line.split() for line in f.readlines()))
        )


def sign(x: int) -> int:
    return (x > 0) - (x < 0)


def printer(x: list[list[int]], hashes: bool = False):
    c = ["#" if hashes else str(i) for i in range(len(x))]
    if not hashes:
        c[0] = "H"
    sx = [s[0] for s in x]
    minx, maxx = min(sx), max(sx)
    sy = [s[1] for s in x]
    miny, maxy = min(sy), max(sy)
    for j in list(range(miny, maxy + 1))[::-1]:
        print(
            "".join(
                [
                    c[x.index([i, j])] if [i, j] in x else "."
                    for i in list(range(minx, maxx + 1))[::-1]
                ]
            )
        )


def simulate(data, n=9, show=False):
    x = [[0, 0] for i in range(n + 1)]
    DELTA = {"U": (0, 1), "D": (0, -1), "R": (-1, 0), "L": (1, 0)}
    visited = {(0, 0)}
    for direction, steps in data:
        if show:
            print(f"=== {direction} {steps} ===")
        d = DELTA[direction]
        for step in range(steps):
            # Update head
            x[0] = [x[0][0] + d[0], x[0][1] + d[1]]
            # Update tail
            for i in range(1, len(x)):
                dt = [x[i - 1][0] - x[i][0], x[i - 1][1] - x[i][1]]
                if abs(dt[0]) > 1 or abs(dt[1]) > 1:
                    x[i][0] += sign(dt[0])
                    x[i][1] += sign(dt[1])
            visited.add(tuple(x[-1]))
        if show:
            printer(x)
    if show:
        print("VISITED")
        printer(list(list(x) for x in visited), hashes=True)
    return len(visited)


if __name__ == "__main__":
    exdata = read_moves("day09_example.txt")
    exdata2 = read_moves("day09_example2.txt")
    indata = read_moves("day09_input.txt")

    print("PART 1")
    print("example", simulate(exdata, 1))
    print("input", simulate(indata, 1))
    print()
    print("PART 2")
    print("example 2", simulate(exdata2, 9, show=True))
    print("input", simulate(indata, 9))
