class Book:
    def __init__(self, title, author, languages, copyright):
        self.title = title
        self.author = author
        self.languages = languages
        self.copyright = copyright

class BookFactory:
    @staticmethod
    def create_book(title, author, languages, copyright):
        return Book(title, author, languages, copyright)
