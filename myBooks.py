print('Organizing my bookshelf\n')

books = ["The Prince", "Meditations", "The Art of War", "Think Python"]

print("Books on the shelf:")
print(books)

print("\nNew books have arrived!")
books.extend(["Wuthering Heights", "Maze Runner"])
print(books)

print("\nI'm going to feature a book.")
books.insert(0, "The Little Prince")
print(books)

print("\nI bought another book.")
books.append("Introduction to SQL Language")
print(books)

print("\nI lent 'Meditations'.")
books.remove("Meditations")
print(books)

print("\nThe last book went to another shelf.")
book = books.pop()
print("Removed book:", book)
print(books)

print("\nI'm going to remove an old book.")
del books[2]
print(books)

print("\nBooks in alphabetical order:")
books.sort()
print(books)

print("\nBooks in reverse alphabetical order:")
books.sort(reverse=True)
print(books)

print("\nReversing the shelf order:")
books.reverse()
print(books)

print("\nNow I have", len(books), "books on the shelf.")