# Instance methods has object opr self as parameter.
# Class method has class as parameter.
# static method doesn't have any parameter.


class Book:
    TYPES = ("Hardcover", "Paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def instance_method(self):
        return f"Message printing from instance method of book {self.name}"

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, {self.weight}>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight + 20)

    @staticmethod
    def print_book_intro():
        print("This function prints book introduction")

book = Book("Harry Porter", "funky", 200)
book2 = Book.hardcover("Alchemist", 210)
book3 = Book.paperback("Fault in our stars", 120)
book3 = Book.print_book_intro()
print(book)
print(book2.instance_method())
print(book2)
print(book3)
