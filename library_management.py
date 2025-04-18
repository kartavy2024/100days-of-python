class library:
    books = ["clash of clains","how to win friends","rich dad poor dad"]
    assigned_books = {
        "Kartavy":["brave new world","Moby","The alchemist"],
        "Vibhuti":["War and peace","Expectations"]
    }
    def add_book(self,bookName):
        self.books.append(bookName)

    def how_many_books(self):
        print("total books available is ",len(self.books))
    
    def show_assigned_books(self,person):
        print(f"Currenty assigned books to {person} is: ",self.assigned_books[person])

    def unassign_book(self,person,bookname):
        self.assigned_books[person].remove(bookname)
        self.books.append(bookname)
    def total_available_books(self):
        print("Total available books are",self.books)

book = library()

book.add_book("psychology of money")
book.how_many_books()
book.total_available_books()
book.show_assigned_books("Kartavy")
book.unassign_book("Kartavy","Moby")
book.show_assigned_books("Kartavy")
book.total_available_books()
book.how_many_books()


