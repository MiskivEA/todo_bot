import os

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    D = ',', '.', '!', ':', ';', '?'
    left = start
    right = start + size - 1
    end_flag = False
    if right > len(text):
        end_flag = True
        right = len(text) - 1
    if not end_flag:
        while text[right + 1] in D and text[right] in D:
            right -= 1

    while text[right] not in D:
        right -= 1

    page = text[left: right + 1]
    return page, len(page)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='UTF-8') as t:
        text = t.read()
    idx = 1
    start = 0
    text_ln = len(text)

    while start < text_ln:
        page_text, page_ln = _get_part_text(text, start, PAGE_SIZE)
        book[idx] = page_text.lstrip()
        idx += 1
        start += page_ln

    return book


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))