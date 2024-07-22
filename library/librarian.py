from database import DataManager
from library.book import Book


class Librarian:

    def __init__(self, operator: DataManager):
        self.operator = operator
        self.command_menu = {
            "1": ("Просмотреть список книг", self.display_books),
            "2": ("Добавить книгу", self.add_book),
            "3": ("Найти книгу", self.search_book),
            "4": ("Удалить книгу", self.delete_book),
            "5": ("Изменить статус книги", self.book_issuance),
        }

    def print_command_menu(self):
        print("\nДобро пожаловать в систему управления библиотекой!")
        print(
            "Вы можете использовать это приложение для добавления, удаления, поиска и отображения книг:\n"
        )

        for key, value in self.command_menu.items():
            print(f"{key}: {value[0]}\n")

    def display_books(self) -> None:
        books = self.operator.load_data()
        if not books:
            print("Библиотека пуста.")
        for book in books:
            print(
                f"""
                ID: {book['id']}
                Название: {book['title']}
                Автор: {book['author']}
                Год: {book['year']}
                Статус: {book['status']}
            """
            )

    def add_book(self) -> None:

        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = int(input("Введите год издания книги: \n"))

        books = self.operator.load_data()
        new_book = Book(title, author, year)
        books.append(new_book.to_dict())
        self.operator.save_data(books)
        print(f"Книга '{title}' добавлена с ID {new_book.id}.\n")

    def delete_book(self) -> None:
        books = self.operator.load_data()
        book_id = int(input("Введите номер книги: "))
        for book in books:
            if book["id"] == book_id:
                books.remove(book)
                self.operator.save_data(books)
                break
            else:
                print(f"Книга с ID {book_id} не найдена\n")
                return
        print(f"Книга с ID {book_id} удалена.\n")

    # Функция для поиска книг
    def search_book(self):
        query = input("Введите поисковый запрос: ")
        books = self.operator.load_data()
        find_books = [book for book in books if query.lower() in str(book).lower()]
        if not find_books:
            print("Книги не найдены")
        else:
            for book in find_books:
                print(
                    f"""
                    Найдены книги:\n
                    ID: {book['id']}
                    Название: {book['title']}
                    Автор: {book['author']}
                    Год: {book['year']}
                    Статус: {book['status']}
                """
                )

    def book_issuance(self) -> None:
        books = self.operator.load_data()
        book_id = int(input("Введите номер книги: "))
        for book in books:
            if book["id"] == book_id:
                print(f"{book['title']}\n{book['status']}")
                status = input("Введите новый статус (в наличии/выдана): ")
                book["status"] = status
                break
        self.operator.save_data(books)
        print(f"Статус книги с ID {book_id} изменен на '{status}'.")
