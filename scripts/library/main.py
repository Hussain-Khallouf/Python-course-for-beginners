from books_handler import *


def instructions():
    print("Welocme to your automated library ♥_♥")
    print("You have these options:")
    print("D: to Dispaly your library")
    print("A: to add a new book")
    print("R: to remove a book")
    print("S: to save changes")
    print("Q: to quit")

def main():

    instructions()
    load_books()

    while True:
        user_input = input("\nEnter your option: ").lower()
        try:
            if user_input == "d":
                display_books()
            elif user_input == "a":
                title = input("The book title: ")
                pages = int(input("number of pages: "))
                page_size = input("page size: (small, midum, lagre)")
                price = int(input("book price: "))
                add_book(title, pages, page_size, price)
            elif user_input == "r":
                id = int(input("Enter book's id: "))
                delete_book(id)
            elif user_input == "s":
                save()
            elif user_input == "q":
                break
            else:
                print("Sorry, it is an incorrect option *_*")
        except ValueError:
            print("Bad input, try again")

if __name__ == "__main__":
    main()