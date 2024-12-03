from Library.library import Library


def run_cli() -> None:
    library = Library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        try:
            if choice == "1":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = int(input("Введите год издания: "))
                library.add_book(title, author, year)
            elif choice == "2":
                book_id = int(input("Введите ID книги: "))
                library.delete_book(book_id)
            elif choice == "3":
                field = input("Введите поле для поиска (title, author, year): ")
                query = input("Введите запрос для поиска: ")
                results = library.search_books(query, field)
                if results:
                    library.display_books()
                else:
                    print("Книги не найдены.")
            elif choice == "4":
                library.display_books()
            elif choice == "5":
                book_id = int(input("Введите ID книги: "))
                status = input("Введите новый статус (в наличии/выдана): ")
                library.update_status(book_id, status)
            elif choice == "6":
                print("Выход из программы...")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Попробуйте снова.")
