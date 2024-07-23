from library.library import Library
from library.book import Book


class Librarian:

    def __init__(self, library: Library):
        self.library = library
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
        books = self.library.get_items()
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
        try:
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания книги: \n"))

            book = Book(title=title, author=author, year=year)
            self.library.add_item(book)
            print(f"Книга '{title}' добавлена.\n")
        except ValueError:
            print("Не верный формат данных")

    def delete_book(self) -> None:
        try:
            book_id = int(input("Введите номер книги: "))
            self.library.delete_item(book_id)
            print(f"Книга с ID {book_id} удалена.\n")
        except ValueError:
            print("Не верный формат данных")

    # Функция для поиска книг
    def search_book(self):
        query = input("Введите поисковый запрос: ")
        books = self.library.get_books_by_query(query=query)
        if not books:
            print("Книги не найдены")
        else:
            for book in books:
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
        try:
            book_id = int(input("Введите номер книги: "))
        except ValueError:
            print("Необходимо ввести номер книги.")
            return

        book = self.library.get_book(item_id=book_id)
        print(f"{book['title']}\n{book['status']}")

        new_status = input("Введите новый статус (в наличии/выдана): ")
        book["status"] = new_status
        self.library.save_item(book)
        print(f"Статус книги {book['title']} с ID {book_id} изменен на '{new_status}'.")
