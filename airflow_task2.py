# -*- coding: utf-8 -*-
# Copyright (c) 2023 by WenHuan Yang-Zhang.
# Date: 2023-03.01
# Ich und google :)
import time
import logging


def print_time():
    for num in range(100):
        logger = logging.getLogger(__name__)
        logger.info("====================================================================")
        logger.info(f"time now is {round(time.time() * 1000, 3)}!")
        time.sleep(1)
    logger.info("====================================================================")


if __name__ == "__main__":
    print_time()