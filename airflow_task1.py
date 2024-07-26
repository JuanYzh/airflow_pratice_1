# -*- coding: utf-8 -*-
# Copyright (c) 2023 by WenHuan Yang-Zhang.
# Date: 2023-03.01
# Ich und google :)
import time
import logging


def print_numbers():
    for num in range(100):
        logger = logging.getLogger(__name__)
        logger.info("####################################################################")
        logger.info(f"I am number {num}!")
        time.sleep(1)
    logger.info("####################################################################")


if __name__ == "__main__":
    print_numbers()