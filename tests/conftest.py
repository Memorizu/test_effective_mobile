import json
import os
import pytest

from library import Library
from library.book import Book
from database import JsonManager
from config import settings


class MockDataManager(JsonManager):
    DATA_FILE = settings.TEST_DATA_FILE

    def load_data(self):
        return super().load_data()

    def save_data(self, books):
        super().save_data(books)


@pytest.fixture(autouse=True)
def setup():
    initial_books = [
        {
            "id": 1,
            "title": "Test Book 1",
            "author": "Author 1",
            "year": 2001,
            "status": "в наличии",
        },
        {
            "id": 2,
            "title": "Test Book 2",
            "author": "Author 2",
            "year": 2002,
            "status": "выдана",
        },
    ]
    with open(MockDataManager.DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(initial_books, file, ensure_ascii=False, indent=4)

    yield

    # Teardown: Remove the test data file
    if os.path.exists(MockDataManager.DATA_FILE):
        os.remove(MockDataManager.DATA_FILE)


@pytest.fixture
def library():
    return Library(item=Book, operator=MockDataManager())


@pytest.fixture
def book():
    return Book(title="Test Book 3", author="Author 3", year=2003)
