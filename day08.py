#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of code day 08 - Treetop Tree House"""

from itertools import takewhile


def read_map(path: str) -> tuple[tuple[int]]:
    """Read in data into 2D int array"""
    with open(path, "r") as f:
        return tuple(tuple(map(int, i.strip())) for i in f.readlines())


def T(data: tuple[tuple[int]]) -> tuple[tuple[int]]:
    """Transpose list of lists"""
    return tuple(zip(*data))


# PART 1


def vor(x: list[bool], y: list[bool]) -> list[bool]:
    """Elementwise or of lists x and y"""
    return tuple(i or j for i, j in zip(x, y))


def vx(x: tuple[int]) -> tuple[bool]:
    """Visibility for each element in row x"""
    return [True] + [all(j < x[i] for j in x[:i]) for i in range(1, len(x))]


def vis(data: tuple[tuple[int]]) -> tuple[tuple[bool]]:
    """Visibilities for both directions in each row in data"""
    return tuple(vor(vx(x), vx(x[::-1])[::-1]) for x in data)


def visibility(data: tuple[tuple[int]]) -> tuple[tuple[bool]]:
    """Visibility ORed for rows and columns in data"""
    return tuple(vor(i, j) for i, j in zip(vis(data), T(vis(T(data)))))


def sum_visibility(data: tuple[tuple[int]]) -> int:
    """Sum visibilities"""
    return sum(sum(i) for i in visibility(data))


# PART 2


def count(v0: int, v: list[int]) -> int:
    """Count trees"""
    n = 0
    for x in v:
        n += 1
        if v0 <= x:
            break
    return n


def scenic(data: tuple[tuple[int]]) -> int:
    """Compute scenic score for each tree"""
    scenic_scores = dict()
    data_t = T(data)
    r = len(data)
    c = len(data[0])
    maxx = 0
    for i in range(r):
        for j in range(c):
            x = data[i][j]
            maxx = max(
                maxx,
                count(x, data[i][:j][::-1])
                * count(x, data[i][j + 1 : c])
                * count(x, data_t[j][:i][::-1])
                * count(x, data_t[j][i + 1 : r]),
            )
    return maxx


if __name__ == "__main__":
    exdata = read_map("day08_example.txt")
    indata = read_map("day08_input.txt")

    print("PART 1")
    print("example", sum_visibility(exdata))
    print("input", sum_visibility(indata))

    print("PART 2")
    print("example", scenic(exdata))
    print("input", scenic(indata))
