import asyncio
import typing as t

import sentry_sdk
from loguru import logger

from src.config import Config
from src.logic.check_if_changed import check_if_changed
from src.logic.info import get_info
from src.logic.send_info import send_info


async def start_loop() -> t.Never:  # type: ignore[misc] # Implicit return in function which does not return (on KeyboardInterrupt)
    config = Config()
    while True:
        try:
            info = await get_info()

            if not check_if_changed(info):
                logger.info("No changes")
                await asyncio.sleep(config.interval)
                continue

            await send_info(info)
        except KeyboardInterrupt:
            break
        except Exception as e:
            sentry_sdk.capture_exception(e)
            logger.exception(e)
        else:
            await asyncio.sleep(config.interval)
