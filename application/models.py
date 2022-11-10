from application import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(50), nullable=False)
    books = db.relationship("Book", backref="author")

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(50), nullable=False)
    available = db.Column(db.Boolean, default=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))