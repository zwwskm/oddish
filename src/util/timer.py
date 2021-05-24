import datetime
import random
import time
import asyncio

from src.config.definitions import config
from src.util.logger import log

# 爬buff使用长间隔，steam使用短间隔
def sleep_awhile(is_steam_request = 0, takeout= 0):
    low = max(config.FREQUENCY_INTERVAL_LOW, 10)
    high = max(10, config.FREQUENCY_INTERVAL_HIGH)
    if is_steam_request == 1:
        interval = 1/(random.randint(5, 10))
    else:
        interval = random.randint(low, high)
    interval = interval - takeout
    if interval > 0:
        log.info("sleep {}s at {}".format(interval, datetime.datetime.now()))
        time.sleep(interval)

async def async_sleep_awhile():
    low = max(config.FREQUENCY_INTERVAL_LOW, 2)
    high = max(2, config.FREQUENCY_INTERVAL_HIGH)
    interval = random.randint(low, high)
    log.info("sleep {}s at {}".format(interval, datetime.datetime.now()))
    await asyncio.sleep(interval)
