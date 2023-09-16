from application import db
from werkzeug.security import generate_password_hash, check_password_hash


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(50), nullable=False)
    books = db.relationship("Book", backref="author")


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(50), nullable=False)
    available = db.Column(db.Boolean, default=True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(50))
    books = db.relationship("Book", backref="category")


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.id)
