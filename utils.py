from typing import Any
import os
import orjson


def get_data_from_file(path: str) -> dict[str, Any]:
    if not os.path.exists(path):
        print("No data found")
        exit(1)

    with open(path, "r", encoding="utf-8") as file:
        return orjson.loads(file.read())


def save_data(path: str, data: dict[str, Any]) -> None:
    if not os.path.exists(path):
        print("No data file found")
        exit(1)

    with open(path, "w", encoding="utf-8") as file:
        file.write(orjson.dumps(data).decode())
