from model import BookModel
from view import BookView

class BookController:
    def __init__(self):
        self.model = BookModel()
        self.view = BookView()

    def main(self):
        choice = self.view.get_user_input()

        #Search for book
        if choice == '0':
            name, author, language, genre = self.view.get_search_input()
            book = self.model.get_books(name, author, language, genre)
            self.view.display_book_info(book.title, book.author, book.languages, book.copyright)
        
        #Tags
        elif choice == '1':
            db = input('\n0 - Add to tag\n1 - View tag\n')
            
            #Add to tag
            if db == "0":
                name, author, tag = self.view.get_add_to_tag_input()
                self.model.create_tables()
                self.model.add_to_tag(name, author, tag)
            
            #Print tag contents
            elif db == "1":
                tag = input('\nTag (shelf, favourites, tbr): ')
                rows = self.model.access_table(tag)
                self.view.display_tag_entries(rows)
            
            else:
                print('Please choose an option from the list')
        
        else:
            print('Please choose an option from the list')

if __name__ == "__main__":
    controller = BookController()
    controller.main()
