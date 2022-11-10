from application import app, db
from application.forms import AddAuthor, AddBook
from application.models import Author, Book
from flask import request, render_template

# redirect, url_for may be added to flask import

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add-author', methods=['GET', 'POST'])
def add_author():
    form = AddAuthor()
    if request.method == 'POST':
        name = form.author_name.data
        author = Author(author_name = name)
        db.session.add(author)
        db.session.commit()
    return render_template('add_author.html', form=form)

@app.route('/add-book', methods=['GET', 'POST'])
def add_book():
    form = AddBook()
    authors = Author.query.all()
    for author in authors:
        form.author.choices.append((author.id, author.author_name))
    if request.method == 'POST':
        title = form.book_title.data
        author_id = form.author.data
        book = Book(book_title = title, author_id = author_id)
        db.session.add(book)
        db.session.commit()
    return render_template('add_book.html', form=form)

@app.route('/view-books', methods=['GET'])
def view_books():
    authors = Author.query.all()
    books = Book.query.all()
    return render_template('view_books.html', authors=authors, books=books)