import urllib.parse
import urllib.request
import json
import sqlite3
from book import BookFactory

class BookModel:
    def __init__(self):
        self.base_url = 'http://gutendex.com/books'
        self.db_name = 'bookshelf.db'

    def get_books(self, name, author, language, genre):
        base_url = self.base_url
        url = []

        # Check which parameters are given
        if name != '0':
            query_param_name = f"{name}"
            query_string_name = urllib.parse.quote(query_param_name)
            url.append(f'search={query_string_name}')

        if author != '0':
            query_param_author = f"{author}"
            query_string_author = urllib.parse.quote(query_param_author)
            url.append(f'search={query_string_author}')

        if language != '0':
            query_param_lang = f"{language}"
            query_string_lang = urllib.parse.quote(query_param_lang)
            url.append(f'languages={query_string_lang}')

        if genre != '0':
            query_param_genre = f"{genre}"
            query_string_genre = urllib.parse.quote(query_param_genre)
            url.append(f'topic={query_string_genre}')

        try:
            final_url = f'{base_url}?'

            # Put together final url
            for x in url:
                final_url = final_url + x + '&'

            # Get data from API and parse the json data
            with urllib.request.urlopen(final_url) as response:
                data = json.loads(response.read().decode())

                if data and 'results' in data and len(data['results']) > 0:
                    book = data['results'][0]
                    title = book['title']
                    author = book['authors'][0]['name'] if 'authors' in book else 'Author information not available'
                    languages = book['languages'][0]
                    copyright = book['copyright']

                    return BookFactory.create_book(title, author, languages, copyright)

                else:
                    return None, 'Book not found'

        except Exception as e:
            return None, f'Error occurred: {str(e)}'

    def add_to_tag(self, title, author, tag):
        # Connect to the SQLite database
        con = sqlite3.connect(self.db_name)

        cur = con.cursor()

        # Insert data
        cur.execute(f"INSERT INTO {tag} VALUES (?,?)", (title, author))

        # Commit the changes
        con.commit()

        # Close the cursor and the database connection
        cur.close()
        con.close()

    def create_tables(self):
        # Connect to the SQLite database
        con = sqlite3.connect(self.db_name)

        cur = con.cursor()

        # Create tables
        cur.execute("""CREATE TABLE IF NOT EXISTS shelf(name, author)""")
        cur.execute("""CREATE TABLE IF NOT EXISTS favourites(name, author)""")
        cur.execute("""CREATE TABLE IF NOT EXISTS tbr(name, author)""")

        # Commit the changes
        con.commit()

        # Close the cursor and the database connection
        cur.close()
        con.close()

    def access_table(self, tag):
        # Connect to the SQLite database
        con = sqlite3.connect(self.db_name)

        # Create a cursor object
        cur = con.cursor()

        # Get all the table entries
        cur.execute(f"SELECT * FROM {tag}")

        rows = cur.fetchall()

        # Close the cursor and the database connection
        cur.close()
        con.close()

        return rows
