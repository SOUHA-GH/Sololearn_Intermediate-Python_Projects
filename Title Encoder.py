#The program reads the book title from the given file and outputs the encoded versions, each on a new line.
file = open("/usercode/files/books.txt", "r")
books = file.readlines()
print("\n".join(["".join([words[0] for words in book.split()]) for book in books]))
file.close()
