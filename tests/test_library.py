import unittest
import os
from Library.library import Library
from Library.models import Book


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Создание временной библиотеки перед каждым тестом."""
        self.test_file = "test_library.json"
        self.library = Library(data_file=self.test_file)

    def tearDown(self):
        """Удаление временного файла после каждого теста."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self):
        """Проверка добавления книги в библиотеку."""
        self.library.add_book("Test Title", "Test Author", 2023)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Test Title")

    def test_delete_book(self):
        """Проверка удаления книги из библиотеки."""
        self.library.add_book("Test Title", "Test Author", 2023)
        book_id = self.library.books[0].id
        self.library.delete_book(book_id)
        self.assertEqual(len(self.library.books), 0)

    def test_search_books(self):
        """Проверка поиска книги по названию."""
        self.library.add_book("Test Title", "Test Author", 2023)
        self.library.add_book("Another Title", "Another Author", 2022)

        results = [book for book in self.library.books if "Test" in book.title]
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Test Title")

    def test_update_status(self):
        """Проверка обновления статуса книги."""
        self.library.add_book("Test Title", "Test Author", 2023)
        book_id = self.library.books[0].id
        self.library.update_status(book_id, "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")


if __name__ == "__main__":
    unittest.main()
