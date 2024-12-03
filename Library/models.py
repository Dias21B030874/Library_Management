from typing import Dict


class Book:
    """
      Класс для представления книги.

      Атрибуты:
          id (int): Уникальный идентификатор книги.
          title (str): Название книги.
          author (str): Автор книги.
          year (int): Год издания.
          status (str): Статус книги ("в наличии" или "выдана").
      """

    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "в наличии") -> None:
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> Dict[str, str | int]:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: Dict[str, str | int]) -> "Book":
        return Book(data["id"], data["title"], data["author"], data["year"], data["status"])
