import asyncio

from loguru import logger

from src import utils, logic
from src.config import Config


async def main() -> None:
    utils.setup_logging()
    logger.info("Hello World!")

    Config()
    utils.start_sentry()
    await utils.start_apykuma()
    await logic.start_loop()


if __name__ == "__main__":
    asyncio.run(main())
