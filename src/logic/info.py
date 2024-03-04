import dataclasses

import aiohttp
from bs4 import BeautifulSoup


@dataclasses.dataclass
class Info:
    sent: int | None
    will_accept: int


async def get_info() -> dict[str, Info]:
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://www.ssps.cz/zajemci/kriteria-prijimaciho-rizeni-2/prijimaci-rizeni/"
        ) as response:
            response.raise_for_status()
            soup = BeautifulSoup(await response.text(), "html.parser")

    result: dict[str, Info] = {}
    for table in soup.find(name="tbody").find_all(name="tr"):
        table_values = table.find_all(name="td")
        table_values = [value.text for value in table_values]
        result[table_values[0]] = Info(
            int(table_values[1]) if table_values[1] != " " else None,
            int(table_values[2]),
        )

    return result
