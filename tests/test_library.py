class TestLibrary:

    def test_get_items(self, library):
        items = library.get_items()
        assert len(items) == 2
        assert items[0]["title"] == "Test Book 1"

    def test_save_item(self, library, book):
        library.save_item(book.to_dict())
        items = library.get_items()
        assert len(items) == 3
        assert items[-1]["title"] == "Test Book 3"

    def test_delete_item(self, library):
        library.delete_item(1)
        items = library.get_items()
        assert len(items) == 1
        assert items[0]["id"] == 2

    def test_get_books_by_query(self, library):
        books = library.get_books_by_query("Test Book")
        assert len(books) == 2
        assert books[0]["title"] == "Test Book 1"
        assert books[1]["title"] == "Test Book 2"
