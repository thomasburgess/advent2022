#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of code day 13 - Distress Signal"""

import json
import functools
import operator


def read_pairs(path: str) -> list:
    with open(path, "r") as f:
        lines = f.readlines()
        return [
            list(map(json.loads, (lines[i], lines[i + 1])))
            for i in range(0, len(lines), 3)
        ]


def compare(left, right):
    for l, r in zip(left, right):
        ints = tuple(map(lambda x: isinstance(x, int), (l, r)))
        if all(ints):
            if l < r:
                return 1
            elif r < l:
                return 0
            else:
                continue
        result = compare([l] if ints[0] else l, [r] if ints[1] else r)
        if result is not None:
            return result
    if len(left) > len(right):
        return 0
    if len(right) > len(left):
        return 1


def prod(x):
    return functools.reduce(operator.mul, x, 1)


def part1(pairs):
    return sum(i for i, pair in enumerate(pairs, 1) if compare(pair[0], pair[1]))


def part2(pairs):
    q = sorted(
        [i for p in pairs for i in p] + [[[2]], [[6]]],
        key=functools.cmp_to_key(lambda left, right: -compare(left, right)),
    )
    return prod([i for i, c in enumerate(q, 1) if c in ([[2]], [[6]])])


if __name__ == "__main__":
    ex_pairs = read_pairs("day13_example.txt")
    in_pairs = read_pairs("day13_input.txt")

    print("PART 1")
    print("\texample:", part1(ex_pairs))
    print("\tinput:", part1(in_pairs))
    print("\nPART 2")
    print("\texample:", part2(ex_pairs))
    print("\tinput:", part2(in_pairs))
