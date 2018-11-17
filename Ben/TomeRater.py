class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        print ("User Email changed from {email_old} to {email_new}".format(email_old=self.email,email_new=address))
        self.email=address

    def __repr__(self):
        print("User {name}, email: {email}, books read: {num_book}".format(name=self.name, email=self.email, num_book=len(self.books)))

    def __eq__(self, other_user):
        if self.name==other_user and self.email==other_user:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book]=rating

    def get_average_rating(self):
        rating_total=0
        counter=0
        for book in self.books.keys():
            counter+=1
            if self.books[book] is not None:
                rating_total+=self.books[book]
        avg_rating=rating_total/counter
        return avg_rating



    
class Book:
    def __init__(self, title, isbn):
        self.title=title
        self.isbn=isbn
        self.ratings=[]

    def __repr__(self):
        return "{title} with ISBN {isbn}".format(title=self.title, isbn=self.isbn)
    
    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        print ("Set {book_name} ISBN number from {number_old} to {number_new}".format(book_name=self.title,number_old=self.isbn,number_new=new_isbn))

    def add_rating(self, rating):
        if rating>=0 and rating<=4:
            self.ratings.append(rating)

        else:
            print ("Invalid Rating")

    def __eq__(self, compare):
        if self.title==compare and self.isbn==compare:
            return True
        else:
            return False

    def get_average_rating(self):
        rating_total=0
        for rating in self.ratings:
            rating_total+=rating
        if len(self.ratings)==0 or rating_total==0:
            avg_rating=0
        else:
            avg_rating=rating_total/len(self.ratings)
            
        return avg_rating
        
    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title,isbn)
        self.author=author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title,author=self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title,isbn)
        self.subject=subject
        self.level=level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)



    
class TomeRater:
    def __init__(self):
        self.users={}
        self.books={}

    def create_book(self, title, isbn):
        book_entry=Book(title, isbn)
        return book_entry

    def create_novel(self, title, author, isbn):
        novel_entry=Fiction(title, author, isbn)
        return novel_entry

    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction_entry=Non_Fiction(title, subject, level, isbn)
        return non_fiction_entry

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book,rating)
            if rating is not None:
                book.add_rating(rating)
            if book in self.books.keys():
                self.books[book]+=1
            else:
                self.books[book]=1
        else:
            print ("No user with email {email}!".format(email=email))


    def add_user(self, name, email, user_books=None):
        user_entry = User(name, email)
        self.users[email] = user_entry
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.keys():
            print (user)

    def most_read_book(self):
        book_name=" "
        book_count=0
        for book in self.books.keys():
            if self.books[book] > book_count:
                book_name=book.title
                book_count=self.books[book]
        return "The Most Read Book: {title}  Read Count: {count}".format(title=book_name,count=book_count)

    def highest_rated_book(self):
        book_name=""
        book_rate=0
        for book in self.books.keys():
            if book.get_average_rating() > book_rate:
                book_name=book.title
                book_count=book.get_average_rating()
        return "The Highest Rating Book: {title}  Average Rating: {count}".format(title=book_name,count=book_count)

    def most_positive_user(self):
        user_name=""
        user_rate=0
        for user in self.users.values():
            avg=user.get_average_rating()
            if  avg > user_rate:
                 user_name=user.name
                 user_rate=avg
        return "The Most Positive User: {user}  Rating: {rate}".format(user=user_name,rate=str(user_rate))
    
  
