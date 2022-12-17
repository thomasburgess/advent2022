#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of code day 16 - Proboscidea Volcanium"""

import heapq

import re
import pprint
import collections


def read_valves(path: str) -> dict[dict]:
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


def generate_steps(data, c, opened):
    # Explore tunnels
    for v in data[c][1]:
        yield v, opened
    # Open valve
    if data[c][0] > 0 and c not in opened:
        yield c, opened | set((c,))


def bfs(data):
    seen = {"AA": 0}
    queue = collections.deque([(1, "AA", 0, set())])
    best = 0
    while queue:
        t, c, pressure, opened = queue.pop()
        if t == 30:
            best = max(best, pressure)
            continue
        if seen.get((t, c), -1) >= pressure:
            continue
        seen[(t, c)] = pressure
        pressure += sum(data[o][0] for o in opened)
        queue.extend(
            (t + 1, i, pressure + (data[c][0] if i == c else 0), o)
            for i, o in generate_steps(data, c, opened)
        )
    return best


def find_elephant(data, start="AA", steps=26):
    frontier = [(0, (start, start), set())]
    for i in range(0, steps):
        if i > 5:
            # it _works_ with my data...
            # A priority queue would have been a little nicer
            frontier.sort(reverse=True)
            frontier = frontier[:5000]
        update = []
        for pressure, (a, b), opened in frontier:
            pressure += sum(data[o][0] for o in opened)
            update.extend(
                (pressure, (ia, ib), ob)
                for ia, oa in generate_steps(data, a, opened)
                for ib, ob in generate_steps(data, b, oa)
            )
        frontier = update
    return max(frontier)[0]


if __name__ == "__main__":
    DAY = "16"
    exdata = read_valves(f"day{DAY}_example.txt")
    indata = read_valves(f"day{DAY}_input.txt")
    print("PART 1")
    print("\texample", bfs(exdata))
    print("\tinput", bfs(indata))

    print("PART 2")
    steps = 26
    print("\texample", find_elephant(exdata, steps=steps))
    print("\tinput", find_elephant(indata, steps=steps))
