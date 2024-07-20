from dataclasses import dataclass
from enum import Enum
import json
import os

from config import settings


class BookEnum(Enum):
    in_stock = "в наличии"
    issued = "выдана"


@dataclass
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.id = self.generate_id()
        self.title = title
        self.author = author
        self.year = year
        self.status = BookEnum(BookEnum.in_stock)

    @staticmethod
    def generate_id() -> int:
        if not os.path.exists(settings.DATA_FILE):
            return 1
        with open(settings.DATA_FILE, "r") as file:
            books = json.load(file)
            if not books:
                return 1
            last_book = books[-1]
            return last_book["id"] + 1

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status.value,
        }
