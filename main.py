from library.librarian import Librarian
from database import json_manager


def main():
    librarian = Librarian(operator=json_manager)


if __name__ == "__main__":
    main()
