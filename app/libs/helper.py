import isbnlib

def is_isbn_or_key(word):
    isbn_or_key = 'key'
    if isbnlib.is_isbn13(word) or isbnlib.is_isbn10(word):
        isbn_or_key = 'isbn'
    return isbn_or_key


def is_isbn_or_key2(word):
    """
        判断word是isbn号还是查询关键字key
        isbn isbn13 由13个0-9在数字组成
        isbn10 由10表0-9表数字组组成，中间可能包含' - '
    :param word:
    :return: key or isbn
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key