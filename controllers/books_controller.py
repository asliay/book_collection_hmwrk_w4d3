from flask import Flask, render_template, Blueprint
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint("books", __name__)

# INDEX
# GET '/books'
@books_blueprint.route("/books")
def books():
    all_books = book_repository.select_all()
    return render_template("books/index.html", all_books = all_books)


# NEW
# GET '/books/new'
@books_blueprint.route("/books/new")
def new_book():
    pass



# CREATE
# POST '/books'


# SHOW
# GET '/books/<id>'


# EDIT
# GET '/books/<id>/edit'


# UPDATE
# PUT '/books/<id>'



# DELETE
# DELETE '/books/<id>'