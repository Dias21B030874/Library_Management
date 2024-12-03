import json
import os
from typing import List
from .models import Book


def load_books(data_file: str) -> List[Book]:
    """Загружает данные книг из файла."""
    if os.path.exists(data_file):
        try:
            with open(data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Book.from_dict(book) for book in data]
        except (json.JSONDecodeError, IOError) as e:
            print(f"Ошибка загрузки данных: {e}")
    return []


def save_books(data_file: str, books: List[Book]) -> None:
    """Сохраняет данные книг в файл."""
    try:
        with open(data_file, "w", encoding="utf-8") as f:
            json.dump([book.to_dict() for book in books], f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка сохранения данных: {e}")
