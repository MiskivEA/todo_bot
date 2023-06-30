def _get_part_text(text: str, start: int, page_size: int):
    D = ',', '.', '!', ':', ';', '?'
    left = start
    right = start + page_size - 1
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


book: dict[int, str] = {}
PAGE_SIZE = 1050


def prepare_book(path):
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
