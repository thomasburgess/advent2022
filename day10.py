#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of code day 10 - Cathode-Ray Tube"""


def read_program(path: str) -> list[tuple[int, int]]:
    with open(path, "r") as f:
        return [
            (1 if "noop" in l else 2, 0 if "noop" in l else int(l.split()[1]))
            for l in f.readlines()
        ]


def run_program(prog: list[tuple[int, int]], x: int = 1) -> list[tuple[int, int]]:
    y = [[0, x]]
    for dt, dx in prog:
        y.append((y[-1][0] + dt, y[-1][1] + dx))
    return y


def part1(out: list[tuple[int, int]]):
    result = 0
    for q in range(20, out[-1][0], 40):
        *_, x = (q * v for (t, v) in out if t < q)
        result += x
    return result


def part2(prog: list[tuple[int, int]]):
    idx = 0
    result = [" "] * 240
    for s in range(240):
        r, c = divmod(s, 40)
        if prog[idx][1] - 1 <= c <= prog[idx][1] + 1:
            result[s] = "█"
        if s > prog[idx][0]:
            idx += 1
    return "\n".join("".join(result[i * 40 : (i + 1) * 40]) for i in range(6))


if __name__ == "__main__":
    exdata = run_program(read_program("day10_example.txt"))
    indata = run_program(read_program("day10_input.txt"))

    print("PART 1")
    print("example", part1(exdata))
    print("input", part1(indata))

    print("PART 2")
    print("example\n", part2(exdata))
    print("input\n", part2(indata))
