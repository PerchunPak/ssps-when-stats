import json

from src.logic.info import Info
from src.utils import DATA_DIR
import dataclasses


def from_json(data: str) -> dict[str, Info]:
    info = json.loads(data)
    return {obor: Info(**data) for obor, data in info.items()}


def to_json(info: dict[str, Info]) -> str:
    info = {obor: dataclasses.asdict(data) for obor, data in info.items()}
    return json.dumps(info, indent=4)


def check_if_changed(info: dict[str, Info]) -> bool:
    data_file = DATA_DIR / "info.json"
    if not data_file.exists():
        data_file.write_text(to_json(info))
        return True

    with data_file.open("r") as f:
        old_info = from_json(f.read())
    data_file.write_text(to_json(info))

    return old_info != info
