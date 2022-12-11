#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of code day 11 - Monkey in the Middle"""

from functools import reduce
import operator


def read_monkeys(path: str, divby: int = 3) -> list[dict]:
    result = []
    with open(path, "r") as f:
        for monkey in f.read().split("\n\n"):
            monkey_data = [m.strip() for m in monkey.split("\n") if m.strip()]

            result.append(
                {
                    "monkey": int(monkey_data[0].replace(":", "").split()[-1]),
                    "stack": list(
                        map(
                            int,
                            monkey_data[1].replace("Starting items: ", "").split(","),
                        )
                    ),
                    "inspected": 0,
                    "mod": int(monkey_data[3].replace("Test: divisible by ", "")),
                    "operation": eval(
                        "lambda x: ("
                        + monkey_data[2]
                        .replace("Operation: new = ", "")
                        .replace("old", "x")
                        + ")"
                        + ("" if divby == 1 else f"//{divby}")
                    ),
                    "test": eval(
                        f"lambda x: ({int(monkey_data[4].split()[-1]), int(monkey_data[5].split()[-1])})"
                        f"[x % {int(monkey_data[3].replace('Test: divisible by ', ''))} != 0]"
                    ),
                }
            )
    return result


def run_monkeys(monkeys: list[dict], rounds=20, mod=1):
    for r in range(rounds):
        for m in monkeys:
            while m["stack"]:
                m["inspected"] += 1
                i = m["stack"].pop(0)
                x = m["operation"](i)
                monkeys[m["test"](x)]["stack"].append(x % mod)
    return monkeys


def prod(x):
    return reduce(operator.mul, x, 1)


def monkey_biz(monkeys: list[dict]):
    return prod(sorted([m["inspected"] for m in monkeys], reverse=True)[:2])


def part2(monkeys: list[dict], rounds=20):
    mod = prod([m["mod"] for m in monkeys])
    monkeys = run_monkeys(monkeys=monkeys, rounds=rounds, mod=mod)
    return monkey_biz(monkeys)


if __name__ == "__main__":
    ex_file = "day11_example.txt"
    in_file = "day11_input.txt"

    print("PART 1")
    divby = 3
    rounds = 20
    print(
        "example",
        monkey_biz(run_monkeys(read_monkeys(ex_file, divby=divby), rounds=rounds)),
    )
    print(
        "input",
        monkey_biz(run_monkeys(read_monkeys(in_file, divby=divby), rounds=rounds)),
    )

    print("PART 2")
    divby = 1
    rounds = 10000
    print("example", part2(read_monkeys(ex_file, divby=divby), rounds=rounds))
    print("input", part2(read_monkeys(in_file, divby=divby), rounds=rounds))
