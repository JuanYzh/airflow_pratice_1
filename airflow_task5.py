# -*- coding: utf-8 -*-
# Copyright (c) 2023 by WenHuan Yang-Zhang.
# Date: 2023-03.01
# Ich und google :)
import time
import logging
from datetime import datetime


def print_time_now():
    for num in range(100):
        logger = logging.getLogger(__name__)
        logger.info("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
        current_time = datetime.now()
        time_now = current_time.strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"现在是北京时间: {time_now}!")
        time.sleep(1)
    logger.info("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")


if __name__ == "__main__":
    print_time_now()