                                        #Exercices 2

"""
COMMENTAIRES 
Les méthodes de ces classes représentent des tests unitaires pour des classes Book, Library et Client respectivement.

La classe TestBookMethods contient deux tests pour la classe Book. 
Le premier test, test_check_out, vérifie si un livre peut être emprunté avec succès en appelant la méthode check_out. 
Le deuxième test, test_check_in, vérifie si un livre peut être rendu avec succès en appelant la méthode check_in.

La classe TestLibraryMethods contient trois tests pour la classe Library. 
Le premier test, test_add_book, vérifie si un livre peut être ajouté à la bibliothèque avec succès en appelant la méthode add_book. 
Le deuxième test, test_check_out_book, vérifie si un livre peut être emprunté à la bibliothèque avec succès en appelant la méthode check_out_book. 
Le troisième test, test_check_in_book, vérifie si un livre peut être rendu à la bibliothèque avec succès en appelant la méthode check_in_book.

La classe TestClientMethods :
Ce test unitaire vérifie le comportement de la méthode check_out_book et check_in_book de la classe Client . 
Il instancie une bibliothèque et un livre, puis ajoute ce livre à la bibliothèque. 
Ensuite, il instancie un client et vérifie que la liste des livres empruntés par ce client est vide au départ. 
Ensuite, le client emprunte le livre en appelant check_out_book 
et vérifie que la liste des livres empruntés par ce client comporte désormais un seul élément, 
qui est le livre que le client a emprunté. 
Enfin, le client restitue le livre en appelant check_in_book 
et vérifie que la liste des livres empruntés par ce client est vide et que le livre n'est plus marqué comme emprunté.

Tous les tests utilisent l'assertion pour vérifier si les résultats obtenus correspondent à ce qui est attendu.
 
"""

#CODE BIBLIOTHEQUE

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        self.is_checked_out = True
        print(f"{self.title} by {self.author} has been checked out.")

    def check_in(self):
       self.is_checked_out = False
       print(f"{self.title} by {self.author} has been checked in.")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} by {book.author} has been added to the library.")

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_checked_out:
                book.check_out()
                return
        print(f"Sorry, {title} is not available.")

    def check_in_book(self, title):
       for book in self.books:
           if book.title == title and book.is_checked_out:
               book.check_in()
               return
       print(f"Sorry, {title} is not in the library.")




class Client:
    def __init__(self, name):
          self.name = name
          self.checked_out_books = []



    def check_out_book(self, library, title):
         for book in library.books:
             if book.title == title and not book.is_checked_out:
                 book.check_out()
                 self.checked_out_books.append(book)
                 return
         print(f"Sorry, {title} is not available.")

    def check_in_book(self, library, title):
         for book in self.checked_out_books:
             if book.title == title:
                 book.check_in()
                 self.checked_out_books.remove(book)
                 return
         print(f"Sorry, {title} is not checked out.")

library = Library()

book1 = Book("To Kill a Mockingbird", "Harper Lee")
library.add_book(book1)

book2 = Book("Pride and Prejudice", "Jane Austen")
library.add_book(book2)

client1 = Client("John Doe")
client1.check_out_book(library, "To Kill a Mockingbird")
client1.check_out_book(library, "Pride and Prejudice")

client2 = Client("Jane Doe")
client2.check_out_book(library, "To Kill a Mockingbird")

client1.check_in_book(library, "To Kill a Mockingbird")


#TESTS UNITAIRES
import unittest


class TestBookMethods(unittest.TestCase):
    def test_check_out(self):
        book = Book("To Kill a Mockingbird", "Harper Lee")
        self.assertFalse(book.is_checked_out)
        book.check_out()
        self.assertTrue(book.is_checked_out)


def test_check_in(self):
        book = Book("To Kill a Mockingbird", "Harper Lee")
        book.is_checked_out = True
        self.assertTrue(book.is_checked_out)
        book.check_in()
        self.assertFalse(book.is_checked_out)

class TestLibraryMethods(unittest.TestCase):

        def test_add_book(self):
                library = Library()
                book = Book("To Kill a Mockingbird", "Harper Lee")
                self.assertEqual(len(library.books), 0)
                library.add_book(book)
                self.assertEqual(len(library.books), 1)
                self.assertEqual(library.books[0].title, "To Kill a Mockingbird")
                self.assertEqual(library.books[0].author, "Harper Lee")

        def test_check_out_book(self):
                library = Library()
                book = Book("To Kill a Mockingbird", "Harper Lee")
                library.add_book(book)
                self.assertFalse(book.is_checked_out)
                library.check_out_book("To Kill a Mockingbird")
                self.assertTrue(book.is_checked_out)
                library.check_out_book("Pride and Prejudice")
                self.assertEqual(len(library.books), 1)


        def test_check_in_book(self):
                library = Library()
                book = Book("To Kill a Mockingbird", "Harper Lee")
                library.add_book(book)
                library.check_out_book("To Kill a Mockingbird")
                self.assertTrue(book.is_checked_out)
                library.check_in_book("To Kill a Mockingbird")
                self.assertFalse(book.is_checked_out)
                library.check_in_book("Pride and Prejudice")
                self.assertEqual(len(library.books), 1)


class TestClientMethods(unittest.TestCase):

        def test_check_out_book(self):
                library = Library()
                book = Book("To Kill a Mockingbird", "Harper Lee")
                library.add_book(book)
                client = Client("John Doe")
                self.assertEqual(len(client.checked_out_books), 0)
                client.check_out_book(library, "To Kill a Mockingbird")
                self.assertEqual(len(client.checked_out_books), 1)
                self.assertEqual(client.checked_out_books[0].title, "To Kill a Mockingbird")
                self.assertEqual(client.checked_out_books[0].author, "Harper Lee")

        def test_check_in_book(self):
                library = Library()
                book = Book("To Kill a Mockingbird", "Harper Lee")
                library.add_book(book)
                client = Client("John Doe")
                client.check_out_book(library, "To Kill a Mockingbird")
                self.assertEqual(len(client.checked_out_books), 1)
                client.check_in_book(library, "To Kill a Mockingbird")
                self.assertEqual(len(client.checked_out_books), 0)
                self.assertFalse(book.is_checked_out)

