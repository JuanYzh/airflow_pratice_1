# -*- coding: utf-8 -*-
# Copyright (c) 2023 by WenHuan Yang-Zhang.
# Date: 2023-03.01
# Ich und google :)
import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
