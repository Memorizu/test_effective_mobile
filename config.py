from pathlib import Path


class Settings:

    DATA_FILE: Path = Path("library/library_data.json").resolve()
    TEST_DATA_FILE = Path("tests/test_library_data.json").resolve()


settings = Settings()
