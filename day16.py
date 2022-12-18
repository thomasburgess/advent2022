#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of code day 16 - Proboscidea Volcanium"""

import re
import collections
from typing import Iterator


VALVES_T = dict[str : tuple[int, list[int]]]


def read_valves(path: str) -> VALVES_T:
    valves = {}
    with open(path, "r") as f:
        return {
            v.split()[1]: (
                int(re.split("rate=|; ", v)[1]),
                re.split("valves|valve", v)[1].replace(",", "").split(),
            )
            for v in f.readlines()
            if v.strip()
        }


def generate_steps(valves: VALVES_T, c: str, opened) -> Iterator[tuple[str, set[str]]]:
    # Explore tunnels
    for v in valves[c][1]:
        yield v, opened
    # Open valve
    if valves[c][0] > 0 and c not in opened:
        yield c, opened | set((c,))


def search(valves: VALVES_T, start: str, steps: int, opened: set[str] = set()) -> int:
    seen = {start: 0}
    queue = collections.deque([(1, [start], 0, opened)])
    paths = []
    while queue:
        t, path, pressure, opened = queue.pop()
        c = path[-1]
        if t == steps:
            paths.append((pressure, path, opened))
            continue
        if seen.get((t, c), -1) >= pressure:
            continue
        seen[(t, c)] = pressure
        pressure += sum(valves[o][0] for o in opened)
        queue.extend(
            (t + 1, path + [i], pressure + (valves[c][0] if i == c else 0), o)
            for i, o in generate_steps(valves, c, opened)
        )
    return max(paths)[0]


def search_elephant(valves: VALVES_T, start: str = "AA", steps: int = 26) -> int:
    frontier = [(0, (start, start), set())]
    for i in range(0, steps):
        if i > 5:
            # it _works_ with my data...
            # A priority queue would have been a little nicer
            frontier.sort(reverse=True)
            frontier = frontier[:5000]
        update = []
        for pressure, (a, b), opened in frontier:
            pressure += sum(valves[o][0] for o in opened)
            update.extend(
                (pressure, (ia, ib), ob)
                for ia, oa in generate_steps(valves, a, opened)
                for ib, ob in generate_steps(valves, b, oa)
            )
        frontier = update
    return max(frontier)[0]


if __name__ == "__main__":
    DAY = "16"
    exdata = read_valves(f"day{DAY}_example.txt")
    indata = read_valves(f"day{DAY}_input.txt")

    start = "AA"
    steps = 30
    print("PART 1")
    print("\texample", search(valves=exdata, start=start, steps=steps))
    print("\tinput", search(valves=indata, start=start, steps=steps))

    print("PART 2")
    steps = 26
    print("\texample", search_elephant(valves=exdata, start=start, steps=steps))
    print("\tinput", search_elephant(valves=indata, start=start, steps=steps))
