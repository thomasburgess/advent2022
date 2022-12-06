#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of code  06 - Tuning Trouble"""
from itertools import takewhile


def read_messages(path: str) -> list[str]:
    with open(path, "r") as f:
        return f.readlines()


def find_start(message: str, n: int) -> int:
    return n + sum(
        1
        for _ in takewhile(
            lambda x: x != n,
            map(lambda x: len(set(message[x - n : x])), range(n, len(message))),
        )
    )


if __name__ == "__main__":
    exdata = read_messages("day06_example.txt")
    indata = read_messages("day06_input.txt")

    print("PART 1")
    for i, message in enumerate(exdata):
        print(f"example {i}: {find_start(message, 4)}")
    print("input", find_start(indata[0], 4))

    print("PART 2")
    for i, message in enumerate(exdata):
        print(f"example {i}: {find_start(message, 14)}")
    print("input", find_start(indata[0], 14))
