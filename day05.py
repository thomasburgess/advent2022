#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of code day 05 - Supply Stacks"""
import re
from collections import defaultdict


def read_stacks(path: str) -> tuple[dict[int, list[chr]], list[list[int]]]:
    stacks = defaultdict(list)
    moves = []
    with open(path, "r") as f:
        lines = f.readlines()

        # Read stacks
        for j, line in enumerate(lines):
            if line == "\n":
                break
            for i in range(len(line) // 4):
                stacks[i].append(re.sub("[^A-Za-z]+", "", line[i * 4 : i * 4 + 4]))

        # Read moves
        for line in lines[j + 1 :]:
            moves.append([int(i) for i in re.sub("[^0-9]+", " ", line).split()])

    return {k + 1: [i for i in v if i] for k, v in stacks.items()}, moves


def apply_moves(
    stacks: dict[int, list[chr]], moves: list[list[int]], reverse: bool
) -> str:
    for n, s, d in moves:
        sub = stacks[s][:n]
        stacks[d] = (sub[::-1] if reverse else sub) + stacks[d]
        stacks[s] = stacks[s][n:]
    return "".join([v[0] for k, v in stacks.items()])


if __name__ == "__main__":
    ex_stacks, ex_moves = read_stacks("day05_example.txt")
    in_stacks, in_moves = read_stacks("day05_input.txt")

    print("PART 1")
    print("example", apply_moves(ex_stacks.copy(), ex_moves, True))
    print("input", apply_moves(in_stacks.copy(), in_moves, True))

    print("PART 2")
    print("example", apply_moves(ex_stacks.copy(), ex_moves, False))
    print("input", apply_moves(in_stacks.copy(), in_moves, False))
