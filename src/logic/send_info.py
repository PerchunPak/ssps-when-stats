import aiohttp
from loguru import logger

from src.config import Config
from src.logic.info import Info


async def send_info(info: dict[str, Info]) -> None:
    config = Config()

    msg = f"<@{config.user_id_to_ping}>\n"
    for obor, data in info.items():
        msg += f"{obor}: {data.sent}/{data.will_accept}\n"

    async with aiohttp.ClientSession() as session:
        async with session.post(config.webhook_url, json={"content": msg}) as response:
            response.raise_for_status()

    logger.success("Sent")
