from pathlib import Path


class Settings:

    DATA_FILE: Path = Path("library/library_data.json").resolve()


settings = Settings()
