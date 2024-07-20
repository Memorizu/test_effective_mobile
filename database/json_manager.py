import json
import os


from database.data_manager import DataManager
from config import settings


class JsonManager(DataManager):

    def __chek_file(self):
        return os.path.exists(settings.DATA_FILE)

    def __create_file(self):
        with open(settings.DATA_FILE, "w") as file:
            json.dump([], file)

    def load_data(self) -> list:
        if not self.__chek_file():
            self.__create_file()

        try:
            with open(settings.DATA_FILE, "r") as file:
                return json.load(file)
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

    def save_data(self, data: list) -> None:
        if not self.__chek_file():
            self.__create_file()

        try:
            with open(settings.DATA_FILE, "w") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except json.decoder.JsonDecodeError:
            print("Некорректный формат данных.")
