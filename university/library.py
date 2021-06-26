import os
import re


class Library:
    __secret_key = os.environ.get('SECRET_LIB_KEY', default=None)
    __book_list = ['Убийство в восточном экспрессе', 'Девять нигретят', 'Страна радости', 'Шесть циферблат']

    @classmethod
    def book_list(cls):
        if cls.__secret_key is not None:
            return cls.__book_list
        else:
            return 'Forbidden action'

    @classmethod
    def give_book(cls, book_name):
        if cls.__secret_key is not None and book_name in cls.__book_list:
            cls.__book_list.remove(book_name)
            return cls.__book_list
        else:
            print(f"Can't give this book {book_name} to you")
            return False

    @classmethod
    def return_book(cls, book_name):
        if cls.__secret_key is not None and book_name not in cls.__book_list:
            cls.__book_list.append(book_name)
            return cls.__book_list
        else:
            return False

    @staticmethod
    def check_student_key(public_key):
        pattern = r"\b([a-zA-z0-9]{4})-([a-zA-z0-9]{4})-([a-zA-z0-9]{6})$"
        try:
            found = re.match(pattern, public_key)
            print("Public key Success", found.group()[:8]+"***")
            return True
        except Exception:
            print("Wrong Public Key")
            return False