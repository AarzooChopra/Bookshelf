class BookView:

    #Main Menu
    def get_user_input(self):
        choice = input('\n0 - Search\n1 - Tags\n')
        
        return choice

    #Search Menu
    def get_search_input(self):
        print('\nPlease fill in the following fields. If you do not want to use a field, type 0.\n')
        name = input('Title: ')
        author = input('Author: ')
        language = input('Language: ')
        genre = input('Genre: ')
        
        return name, author, language, genre

    #Tag Menu
    def get_add_to_tag_input(self):
        name = input('Title: ')
        author = input('Author: ')
        tag = input('Tag (shelf, favourites, tbr): ')
        
        return name, author, tag

    #Display Book Info
    def display_book_info(self, title, author, languages, copyright):
        if title and author and languages:
            print(f"\nBook: {title}")
            print(f"Author: {author}")
            print(f"Languages: {languages}")
            print(f"Copyright: {copyright}\n")
        
        else:
            print(f"\nError: Book not found\n")

    #Display Tag Contents
    def display_tag_entries(self, rows):
        for row in rows:
            print(row)
