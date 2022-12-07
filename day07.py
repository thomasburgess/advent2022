#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of code day 07 - """


def read_tree(path: str) -> dict:
    tree = {}
    cwd = []
    with open(path, "r") as f:
        t = tree
        for line in f.readlines()[1:]:
            split = line.split()
            if split[0] != "$":
                t[split[1]] = {} if split[0] == "dir" else int(split[0])
            elif split[1] == "cd":
                dest = line.split()[-1]
                cwd = cwd[:-1] if dest == ".." else (cwd + [dest])
                t = tree
                for c in cwd:
                    t = t[c]
    return tree


def dir_size(tree: dict, base: str = "/") -> dict:
    result = {base: 0}
    for k, v in tree.items():
        if isinstance(v, int):
            result[base] += v
            continue
        key = base + "/" + k
        t = dir_size(v, base=key)
        result.update(t)
        result[base] += t[key]
    return result


def part1(data: dict, thresh=100000) -> int:
    return sum(v for k, v in data.items() if v < 100000)


def part2(data, total=70000000, req=30000000) -> int:
    return min(v for k, v in data.items() if total - data["/"] + v > req)


if __name__ == "__main__":
    exdata = dir_size(read_tree("day07_example.txt"))
    indata = dir_size(read_tree("day07_input.txt"))

    print("PART 1")
    print("example", part1(exdata.copy()))
    print("input", part1(indata.copy()))

    print("PART 2")
    print("example", part2(exdata.copy()))
    print("input", part2(indata.copy()))
