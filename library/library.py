from library.library_item import LibraryItem
from database import DataManager


class Library:
    def __init__(self, item: LibraryItem, operator: DataManager):
        self.item = item
        self.operator = operator

    def get_items(self):
        return self.operator.load_data()

    def save_item(self, item: dict) -> None:
        items = self.operator.load_data()
        items.append(item)
        self.operator.save_data(items)

    def add_item(self, item: LibraryItem):
        items = self.operator.load_data()
        items.append(item.to_dict())
        self.operator.save_data(items)

    def delete_item(self, item_id):
        items = self.operator.load_data()
        self.operator.save_data([item for item in items if item["id"] != item_id])

    def get_books_by_query(self, query: str) -> LibraryItem:
        items = self.operator.load_data()
        find_items = [item for item in items if query.lower() in str(item).lower()]
        return find_items

    def get_book(self, item_id: int) -> dict:
        items = self.operator.load_data()
        for item in items:
            if item["id"] == item_id:
                return item
