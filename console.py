import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Robin", "Hobb")
author_repository.save(author1)
author2 = Author("Philip", "Pullman")
author_repository.save(author2)
author3 = Author("Isaac", "Asimov")
author_repository.save(author3)
author4 = Author("Markus", "Zusak")
author_repository.save(author4)
author5 = Author("Peter", "May")
author_repository.save(author5)

book_1 = Book("Ship of Magic", "Fantasy", "HarperCollins", author1)
book_repository.save(book_1)
book_2 = Book("The Mad Ship", "Fantasy", "HarperCollins", author1)
book_repository.save(book_2)
book_3 = Book("Ship of Destiny", "Fantasy", "HarperCollins", author1)
book_repository.save(book_3)
book_4 = Book("Northern Lights", "Fantasy", "Scholastic", author2)
book_repository.save(book_4)
book_5 = Book("The Subtle Knife", "Fantasy", "Scholastic", author2)
book_repository.save(book_5)
book_6 = Book("The Amber Spyglass", "Fantasy", "Scholastic", author2)
book_repository.save(book_6)


pdb.set_trace()