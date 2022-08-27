from book import Book

path = "my_books.txt"

my_books = []


def load_books():
    books_file = open(path, "r")
    books_file_list = books_file.read().split("\n")
    for line in books_file_list:
        if len(line) == 0:
            continue
        attributes_list = line.split(",")
        id, title, pages, page_size, price, is_readed = attributes_list
        id = int(id)
        pages = int(pages)
        price = int(price)
        is_readed = is_readed == "True"
        book = Book(title, pages, page_size, price, id, is_readed)
        my_books.append(book)
    books_file.close()


def save():
    books_file = open(path, "w")
    for book in my_books:
        books_file.write(book.form_to_file())
    print("Saving is done")
    books_file.close()


def add_book(title, pages, page_size, price):
    book = Book(title, pages, page_size, price)
    my_books.append(book)


def display_books():
    if len(my_books) == 0:
        print("There is no books")
        return
    print(f"You have {len(my_books)} books")
    for book in my_books:
        print(f"_____{book.title}_____")
        book.display()


def delete_book(id):
    for book in my_books:
        if book.id == id:
            my_books.remove(book)
            print("the book is removed")
            return
    else:
        print(f"There is no book has an id {id}")
