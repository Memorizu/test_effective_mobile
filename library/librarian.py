from database import DataManager
from library.book import Book


class Librarian:

    def __init__(self, operator: DataManager):
        self.operator = operator

    def add_book(self, title: str, author: str, year: int) -> None:
        books = self.operator.load_data()
        new_book = Book(title, author, year)
        books.append(new_book.to_dict())
        self.operator.save_data(books)
        print(f"Книга '{title}' добавлена с ID {new_book.id}.")

    # Функция для удаления книги
    def delete_book(self, book_id: int) -> None:
        books = self.load_books()
        for book in books:
            if book["id"] == book_id:
                books.remove(book)
                break
            else:
                print(f"Книга с ID {book_id} не найдена")
        print(f"Книга с ID {book_id} удалена.")

    # Функция для поиска книг
    def search_books(self, query: str, field: str) -> list:
        books = self.operator.load_data()
        return [book for book in books if query.lower() in str(book[field]).lower()]

    # Функция для отображения всех книг
    def display_books(self) -> None:
        books = self.operator.load_data()
        if not books:
            print("Библиотека пуста.")
        for book in books:
            print(
                f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}"
            )

    # Функция для изменения статуса книги
    def change_status(self, book_id: int, status: str) -> None:
        books = self.operator.load_data()
        for book in books:
            if book["id"] == book_id:
                book["status"] = status
                break
        self.operator.save_data(books)
        print(f"Статус книги с ID {book_id} изменен на '{status}'.")
