# -------------------------------
# 📚 Online Bookstore System
# -------------------------------

# Initialize BookStore
BookStore = [
    ("Rich Dad Poor Dad","Robert T. Kiyosaki",1997,"Business"),
    ("The Alchemist","Paulo Coelho",1988,"Fiction"),
    ("The Da Vinci Code","Dan Brown",2003,"Mystery"),
    ("The Hunger Games","Suzanne Collins",2008,"Dystopian"),
    ("The Lord of the Rings","J.R.R. Tolkien",1954,"Fantasy"),
]

print("\n📚 List of all books")
if not BookStore:
  print("BookStore is empty")
else:
  print("BookStore contains the following books:")
  for title,auther,year,genre in BookStore:
    print(f"title: {title}, auther: {auther}, year: {year}, genre: {genre}")

# Adding new book
print("\nAdding new book")

title = input("Enter title of book: ")
auther = input("Enter auther of book: ")
year = int(input("Enter year of book:"))
genre = input("Enter genre of book: ")

existing_book = {book[0] for book in BookStore}
if title in existing_book:
  print("❌ Book already exists")
else:
  BookStore.append((title,auther,year,genre))
  print("✅ Book is added to BookStore")

print("\nList of all books")
if not BookStore:
  print("BookStore is empty")
else:
  print("BookStore contains the following books:")
  for title,auther,year,genre in BookStore:
    print(f"title: {title}, auther: {auther}, year: {year}, genre: {genre}")

# Removing    

print("\nRemoving the book")

title_2_remove = input("Enter title of book to remove: ")
for book in BookStore:
  if book[0] == title_2_remove:
    BookStore.remove(book)
    print("✅ Book is removed from BookStore")
    break
else:
    print("❌ Book not found")


print("\nList of all books")
if not BookStore:
  print("BookStore is empty")
else:
  print("BookStore contains the following books:")
  for title,auther,year,genre in BookStore:
    print(f"title: {title}, auther: {auther}, year: {year}, genre: {genre}")


# Unique Value Display

Unique_Book = {book[3] for book in BookStore}
print("\n🎭 Unique genre Book")
for genre in Unique_Book:
  print(genre)


print("\nList of all books")
if not BookStore:
  print("BookStore is empty")
else:
  print("BookStore contains the following books:")
  for title,auther,year,genre in BookStore:
    print(f"title: {title}, auther: {auther}, year: {year}, genre: {genre}")

# Update 


title_update = input("Enter title of book to update: ")
detail_to_update = input("Enter detail to update (title,auther,year,genre): ")
new_value = input("Enter new value: ")

for index,book in enumerate(BookStore):
  if book[0] == title_update:
    book_list = list(book)
    if detail_to_update == "title":
      book_list[0] = new_value
    elif detail_to_update == "auther":
      book_list[1] = new_value
    elif detail_to_update == "year":
      book_list[2] = int(new_value)
    elif detail_to_update == "genre":
      book_list[3] = new_value
    else:
      print("❌ Invalid detail to update")
      break
    BookStore[index] = tuple(book_list)
    print(f"✅ Book is updated {title_update} with {detail_to_update} : {new_value}")
    break
  else:
    print(f"❌{title_update} is not found in BookStore")

print("\nList of all books")
if not BookStore:
  print("BookStore is empty")
else:
  print("BookStore contains the following books:")
  for title,auther,year,genre in BookStore:
    print(f"title: {title}, auther: {auther}, year: {year}, genre: {genre}")

    
 
