# advent2022

These are my contributions to [AdventOfCode2022](https://adventofcode.com). Read more about them on my [blog](https://thomasburgess.github.io/blog/2022/12/01/aoc22.html).


## Template

```python

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of code day XX - """

def read_data(path: str) -> list:
    result = []
    with open(path, "r") as f:
        for line in f.readlines():
            result.append(line)
    return result

if __name__ == "__main__":
    exdata = read_data("dayXX_example.txt")
    indata = read_data("dayXX_input.txt")

    print("PART 1")
    print("example", part1(exdata))
    print("input", part1(indata))

    print("PART 2")
    print("example", part2(exdata))
    print("input", part2(indata))

```
