class User(object):
    def __init__(self,user_id):
        self.user_id = user_id
        self.author_list = []
        self.shelf = []

class Book(object):
    def __init__(self,Author,book_id,ratings_5,popularity,image_url):
        self.Author = Author
        self.Author_id = Author.Author_id
        self.book_id = book_id
        self.ratings_5 = ratings_5
        self.popularity = popularity
        self.image_url = image_url
        self.reader_list = []
        def add_reader(self,User):
            if User not in self.reader_list:
                self.reader_list.append(User)

class Author:
    def __init__(self,Author_id):
        self.Author_id = Author_id
        self.reader_list = []
        def add_reader(self,User):
            if User not in self.reader_list:
                self.reader_list.append(User)
        