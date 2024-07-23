__all__ = [
    "Library",
    "Book",
    "Librarian",
]

from library.library import Library
from library.book import Book
from database import json_manager


library = Library(item=Book, operator=json_manager)
