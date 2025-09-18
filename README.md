# 📚 Online Bookstore System

A simple **Python-based Online Bookstore Management System** that allows users to manage a collection of books.  
This project demonstrates the use of **lists, tuples, sets, and CRUD operations** with error handling in Python.  

---

## 🚀 Features

- **Initialize Book Collection** – Start with a pre-loaded list of books stored as tuples `(title, author, year, genre)`.  
- **Display All Books** – View all books in a clean, user-friendly format.  
- **Add a New Book** – Add new books with duplicate title checking.  
- **Remove a Book** – Delete a book by its title with error handling.  
- **Display Unique Genres** – Show all unique genres using a Python `set`.  
- **Update Book Information** – Update book details like title, author, year, or genre.  
- **Error Handling** – Handles cases where a book is not found during update or removal.  
- **Final Display** – After every operation, the updated list of books is displayed.  

---

## 🛠️ Tech Stack
- **Language:** Python 3  
- **Concepts Used:** Lists, Tuples, Sets, Loops, Conditional Statements, Functions  

---

## 📂 Project Structure



---

## 💻 Sample Code Snippet

```python
# Initialize Book Collection
BookStore = [
    ("Rich Dad Poor Dad", "Robert T. Kiyosaki", 1997, "Finance"),
    ("Sapiens", "Yuval Noah Harari", 2011, "Intellectual"),
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("Into the Wild", "Jon Krakauer", 1996, "Adventure"),
    ("The Alchemist", "Paulo Coelho", 1988, "Fiction")
]

# Display All Books
def display_books():
    print("\n📚 Current Books in Store:")
    for book in BookStore:
        print(f"- {book[0]} by {book[1]} ({book[2]}) [{book[3]}]")







