
from hw_6_madash.university.library import Library
from hw_6_madash.university.student import Student

s = Student("Loksli")
d = Student("Artur")

print(list(Library.book_list()))

s.get_book(Library, "Страна радости")
d.get_book(Library, "Девять нигретят")

s.return_book("Страна радости")

print(list(Library.book_list()))

d.get_book(Library, "Девять нигретят")

print(list(Library.book_list()))

#cowsay.tux("Well Done")