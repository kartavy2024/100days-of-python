class library:
    no_of_books = 3
    books = ["clash of clains","how to win friends","rich dad poor dad"]

    def add_book(self,bookName):
        self.no_of_books +=1
        self.books.append(bookName)

    def how_many_books(self):
        print("total books available is ",self.no_of_books)

book = library()

book.add_book("psychology of money")
book.how_many_books()


