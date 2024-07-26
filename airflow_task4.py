# -*- coding: utf-8 -*-
# Copyright (c) 2023 by WenHuan Yang-Zhang.
# Date: 2023-03.01
# Ich und google :)
import time
import random
import logging


def print_random_num():
    for num in range(100):
        logger = logging.getLogger(__name__)
        logger.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        logger.info(f"give you a random number, it's {random.randint(-999, 999)}")
        time.sleep(1)
    logger.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


if __name__ == "__main__":
    print_random_num()