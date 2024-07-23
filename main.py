from library.librarian import Librarian
from library import library


def main():

    lib = Librarian(library=library)
    lib.print_command_menu()

    while True:

        choice = input("Введите номер команды: ")

        if choice in lib.command_menu:
            lib.command_menu[choice][1]()
        else:
            print("Выберите номер из списка.\n")
            continue


if __name__ == "__main__":
    main()
