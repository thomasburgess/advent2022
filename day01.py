#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of code day 01"""


def readsums(path: str) -> list[int]:
    """Return list of sums between empty lines."""
    result = [0]  # Start with single empty sum
    with open(path, "r") as f:
        for line in f.readlines():
            if not line.strip():
                result.append(0)  # Add new empty sum
                continue
            result[-1] = result[-1] + int(line)
    return result


def part1(sums: list[int]) -> int:
    """Find maximal sum."""
    return max(sums)


def part2(sums: list[int]) -> int:
    """Find sum of the 3 largest sums."""
    return sum(sorted(sums)[-3:])


if __name__ == "__main__":
    exdata = readstrats("day01_example.txt")
    indata = readstrats("day01_input.txt")

    print("PART 1")
    print("example", part1(exdata))
    print("input", part1(indata))

    print("PART 2")
    print("example", part2(exdata))
    print("input", part2(indata))
