from application import app, db
from application.forms import AddAuthor, AddBook, UpdateBook
from application.models import Author, Book, Category
from flask import request, render_template, redirect, url_for

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add-author', methods=['GET', 'POST'])
def add_author():
    form = AddAuthor()
    if request.method == 'POST':
        name = form.author_name.data
        # Checks if author already exists in database
        duplicate = Author.query.filter_by(author_name=name).first()
        # If they don't, the author is added
        if not duplicate:
            author = Author(author_name = name)
            db.session.add(author)
            db.session.commit()
        # This part may need to be changed, but the basic functionality works
        else:
            return f"That author already exists in the database."
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
        category_id = form.category.data
        # value = dict(form.category.choices).get(form.category.data)
        # cat_name = value
        # Checks if the book already exists in database
        duplicate = Book.query.filter_by(author_id=author_id, book_title=title).first()
        # If it doesn't, the book is added
        if not duplicate:
            book = Book(book_title = title, author_id = author_id, category_id = category_id)
            db.session.add(book)
            db.session.commit()
        # This part may need to be changed, but the basic functionality works
        else:
            return f"That book already exists in the database."
    return render_template('add_book.html', form=form)

@app.route('/view-books', methods=['GET'])
def view_books():
    authors = Author.query.all()
    books = Book.query.all()
    return render_template('view_books.html', authors=authors, books=books)

@app.route('/book-<int:bid>')
def book(bid):
    book = Book.query.filter_by(id=bid).first()
    maxid = Book.query.order_by(Book.id.desc()).first().id
    return render_template('books.html', book=book, maxid=maxid)

@app.route('/update-book/<int:bid>', methods=['GET','POST'])
def update_book(bid):
    form = UpdateBook()
    categories = Category.query.all()
    if request.method == 'POST':
        title = form.book_title.data
        # Category.id = form.category.data
        book = Book.query.filter_by(id=bid).first()
        book.book_title = title
        # book.category = Category
        db.session.commit()
        # # Not sure whether to redirect or not
        # return redirect(url_for('home'))
    return render_template('update_book.html', form=form)

@app.route('/delete-book/<int:bid>')
def delete_book(bid):
    book = Book.query.filter_by(id=bid).first()
    # Probably delete below
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('view_books'))

@app.route('/view-authors', methods=['GET'])
def view_authors():
    authors = Author.query.all()
    return render_template('view_authors.html', authors=authors)