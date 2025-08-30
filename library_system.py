import json
import os

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.borrowed_books = {}
        self.load_data()

    
    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.books = data.get("books", [])
                self.borrowed_books = data.get("borrowed_books", {})
        else:
            self.books = []
            self.borrowed_books = {}

    
    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump({"books": self.books, "borrowed_books": self.borrowed_books}, f, indent=4)

    def add_book(self, title, author, subject):
        self.books.append({"title": title, "author": author, "subject": subject})
        self.save_data()
        print(f" Book '{title}' by {author} ({subject}) added to library.\n")

    def show_books(self):
        if not self.books:
            print(" No books in the library.\n")
            return
        print("\n Available Books:")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book['title']} by {book['author']} ({book['subject']})")
        print()

    def borrow_book(self, title, user):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                self.borrowed_books[title] = {"user": user, "author": book["author"], "subject": book["subject"]}
                self.save_data()
                print(f" {user} borrowed '{title}'.\n")
                return
        print(" Book not available.\n")

    def return_book(self, title):
        if title in self.borrowed_books:
            info = self.borrowed_books.pop(title)
            self.books.append({"title": title, "author": info["author"], "subject": info["subject"]})
            self.save_data()
            print(f" {info['user']} returned '{title}'.\n")
        else:
            print(" This book was not borrowed from here.\n")


def main():
    library = Library()

    while True:
        print("==== Library Menu ====")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            while True:
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                subject = input("Enter subject (Math, English, Physics, Chemistry): ")
                library.add_book(title, author, subject)

                more = input("Add another book? (y/n): ").lower()
                if more != "y":
                    break

        elif choice == "2":
            library.show_books()

        elif choice == "3":
            while True:
                title = input("Enter book title to borrow: ")
                user = input("Enter your name: ")
                library.borrow_book(title, user)

                more = input("Borrow another book? (y/n): ").lower()
                if more != "y":
                    break

        elif choice == "4":
            while True:
                title = input("Enter book title to return: ")
                library.return_book(title)

                more = input("Return another book? (y/n): ").lower()
                if more != "y":
                    break

        elif choice == "5":
            print(" Exiting Library System. Goodbye!")
            break

        else:
            print(" Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
