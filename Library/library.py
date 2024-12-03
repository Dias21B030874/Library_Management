from typing import List
from .models import Book
from .storage import load_books, save_books


class Library:
    """
        Класс для управления библиотекой книг.

        Атрибуты:
            data_file (str): Путь к файлу для хранения данных библиотеки.
            books (List[Book]): Список книг в библиотеке.
        """
    def __init__(self, data_file: str = "data/library.json") -> None:
        self.data_file = data_file
        self.books: List[Book] = load_books(data_file)

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавляет новую книгу в библиотеку."""
        new_id = max((book.id for book in self.books), default=0) + 1
        new_book = Book(new_id, title, author, year)
        self.books.append(new_book)
        save_books(self.data_file, self.books)
        print(f"Книга '{title}' успешно добавлена с ID {new_id}.")

    def delete_book(self, book_id: int) -> None:
        """Удаляет книгу из библиотеки по ID."""
        book = next((book for book in self.books if book.id == book_id), None)
        if not book:
            print("Книга с указанным ID не найдена.")
            return
        self.books.remove(book)
        save_books(self.data_file, self.books)
        print(f"Книга с ID {book_id} успешно удалена.")

    def search_books(self, query: str, field: str) -> None:
        """
        Ищет книги по заданному полю и запросу.

        Параметры:
            query (str): Запрос для поиска.
            field (str): Поле для поиска (title, author, year).
        """
        if field not in {"title", "author", "year"}:
            print("Недопустимое поле для поиска. Используйте 'title', 'author' или 'year'.")
            return

        results = [
            book for book in self.books if query.lower() in str(getattr(book, field)).lower()
        ]
        if results:
            self._display_books(results)
        else:
            print("Книги не найдены.")

    def display_books(self) -> None:
        """Выводит список всех книг."""
        if not self.books:
            print("Библиотека пуста.")
        else:
            print("\nСписок книг:")
            for book in self.books:
                print(
                    f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}"
                )

    def update_status(self, book_id: int, status: str) -> None:
        """Обновлаяет статус книги."""
        if status not in {"в наличии", "выдана"}:
            print("Недопустимый статус. Используйте 'в наличии' или 'выдана'.")
            return

        book = next((book for book in self.books if book.id == book_id), None)
        if not book:
            print("Книга с указанным ID не найдена.")
            return

        book.status = status
        save_books(self.data_file, self.books)
        print(f"Статус книги с ID {book_id} успешно обновлен на '{status}'.")

    @staticmethod
    def _display_books(books: List[Book]) -> None:
        """Выводит список книг."""
        print("\nСписок книг:")
        for book in books:
            print(
                f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}"
            )
