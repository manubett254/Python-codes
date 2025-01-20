# Code 4: Library Management System

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        if title in self.books:
            return "Book already exists."
        self.books[title] = author
        return f"Book '{title}' by {author} added."

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            return f"Book '{title}' removed."
        return "Book not found."

    def view_books(self):
        if not self.books:
            return "No books available."
        return "\n".join([f"{title} by {author}" for title, author in self.books.items()])

if __name__ == "__main__":
    # Test Library Management
    library = Library()
    library.add_book("1984", "George Orwell")
    print(library.view_books())