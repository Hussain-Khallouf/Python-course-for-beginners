import random

random.seed(42)


class Book:
    def __init__(self, title, pages, page_size, price, id=None, is_readed=False):
        if id == None:
            id = random.randint(1000, 9999)
        self.id = id
        self.title = title
        self.pages = pages
        self.page_size = page_size
        self.price = price
        self.is_readed = is_readed

    def display(self):
        print(f"The book: {self.id}: {self.title}")
        print(f"has {self.pages} at {self.page_size} page size")
        print(f"his price is: {self.price}")
        if self.is_readed == True:
            print("You have readed this book")
        else:
            print("You did not read this book")

    def make_as_read(self):
        if self.is_readed == True:
            print("You already have readed this book")
        else:
            self.is_readed = True

    def form_to_file(self):
        book = f"{self.id},{self.title},{self.pages},{self.page_size},{self.price},{self.is_readed}\n"
        return book


print("class")
