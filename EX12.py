class Library:
    instance = None
    books = {}

       
    def __new__(cls, books=None):
        if cls.instance is None:
            cls.instance = super(Library, cls).__new__(cls)
            # Initialize the books array    
            cls.instance.books = {} if books is None else books
        return cls.instance

    def requestBook(self, bookName):
        if((bookName in self.instance.books) and self.instance.books[bookName] > 0):
            self.instance.books[bookName]=self.instance.books[bookName] - 1
        else:
            print("book does not exist on library")

    def returnBook(self, bookName):
        if((bookName in self.instance.books)):
            self.instance.books[bookName]=self.instance.books[bookName] + 1
        else:
            self.instance.books[bookName] = 1
   
    def setBooks(self, fillbooks):
        self.instance.books = fillbooks
       
    def getBooks(self):
        return self.instance.books

def main():
    logger_instance_1 = Library({"Harry Potter" : 0, "Disney" : 0, "Taitanic" : 2})
    logger_instance_2 = Library()
    logger_instance_2.returnBook("Harry")
    logger_instance_2.requestBook("Harry")
    logger_instance_2.setBooks({"Harry Potter" : 0, "Disney" : 0, "Taitanic" : 2})
    print(logger_instance_1.getBooks())
    print(logger_instance_2.getBooks())
   
if __name__ == "__main__":
    main()