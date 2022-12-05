#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of code day 03"""


def priority(c: chr) -> int:
    return (ord(c) - ord("A") + 27) if c.isupper() else (ord(c) - ord("a") + 1)


def readsacks(path: str):
    result = []
    with open(path, "r") as f:
        for line in f.readlines():
            result.append(list(map(priority, line.strip())))
    return result


def part1(sacks: list[list[int]]) -> int:
    return sum(
        map(lambda x: sum(set(x[: len(x) // 2]).intersection(x[len(x) // 2 :])), sacks)
    )


def part2(sacks: list[list[int]]) -> int:
    return sum(
        map(
            lambda x: sum(
                set(sacks[x]).intersection(sacks[x + 1]).intersection(sacks[x + 2])
            ),
            range(0, len(sacks), 3),
        )
    )


if __name__ == "__main__":
    exdata = readsacks("day03_example.txt")
    indata = readsacks("day03_input.txt")

    print("PART 1")
    print(f"example: {part1(exdata)}")
    print(f"example: {part1(indata)}")

    print("PART 2")
    print(f"example: {part2(exdata)}")
    print(f"example: {part2(indata)}")
