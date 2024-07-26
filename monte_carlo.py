# -*- coding: utf-8 -*-
# Copyright (c) 2023 by WenHuan Yang-Zhang.
# Date: 2023-03.01
# Ich und google :)
import time
import random


def monte_carlo(sample):
    inner = int()
    time_1 = time.time()
    for i in range(sample):
        a = random.uniform(0, 1)
        b = random.uniform(0, 1)
        if a ** 2 + b ** 2 <= 1:
            inner += 1
    time_2 = time.time()
    print(f"run once coast time: {round(time_2 - time_1, 2)}s")
    return inner


def get_pi(sample):
    num = 4
    inner = sum([monte_carlo(sample) for i in range(num)]) / num
    print(f"Monte Carlo Pi >> {inner / sample * 4}")


if __name__ == '__main__':
    time_1 = time.time()
    samjple_test = int(10e8)
    get_pi(samjple_test)
    time_2 = time.time()
    print(f"total_time: {round(time_2 - time_1, 2)}s")
