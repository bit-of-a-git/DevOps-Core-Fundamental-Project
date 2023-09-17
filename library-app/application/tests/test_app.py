from application import app, db
from application.models import Author, Book, Category
from flask_testing import TestCase
from flask import url_for


class TestBase(TestCase):
    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///',
        # ? not sure about below
        SECRET_KEY='TEST_SECRET_KEY',
        DEBUG=True,
        WTF_CSRF_ENABLED=False
        )
        return app


    def setUp(self):
        # Will be called before every test
        # Create table schema
        db.create_all()

        # Create test objects
        test_author = Author(author_name = "Ray Bradbury")
        test_book = Book(book_title = "Fahrenheit 451", author_id = 1, category_id = 1)
        test_category = Category(cat_name = "Dystopian Fiction")

        # save sample data to database
        db.session.add(test_author)
        db.session.add(test_book)
        db.session.add(test_category)
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.session.remove()
        db.drop_all()


# Tests the homepage
class TestHome(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home')) # sends a GET request
        self.assertEqual(response.status_code, 200) # asserts that the response code is 200
        self.assertIn(b"Library Management App", response.data)


# Test adding an author
class TestAddAuthor(TestBase):
    def test_add_author(self):
        response = self.client.post(
            url_for('add_author'),
            data = dict(author_name="G. R. R. Martin")
        )
        assert Author.query.filter_by(author_name="G. R. R. Martin").first().id == 2


    def test_duplicate(self):
        response = self.client.post(
            url_for('add_author'),
            data = dict(author_name="Ray Bradbury")
        )
        self.assertIn(b'That author already exists in the database.', response.data)


# Test adding a book
class TestAddBook(TestBase):
    def test_add_book(self):
        response = self.client.post(
            url_for("add_book"),
            data = dict(book_title = "The Veldt", author_id=1, category_id=1)
        )
        assert Book.query.filter_by(book_title="The Veldt").first().id == 2


    # # Come back and fix
    # def test_duplicate(self):
    #     response = self.client.post(
    #         url_for("add_book"),
    #         data = dict(book_title = "Fahrenheit 451"),
    #         follow_redirects=True
    #     )
    #     self.assertIn(b'That book already exists in the database.', response.data)


# Tests whether books can be viewed
class TestViewBooks(TestBase):
    def test_view_books(self):
        response = self.client.get(url_for('view_books'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Fahrenheit 451', response.data)


# Tests whether Fahrenheit 451 can be updated
class TestUpdateBook(TestBase):
    def test_update_book(self):
        response = self.client.post(
            url_for("update_book", bid=1),
            data = dict(book_title = "Fahrenheit 451: 50th Anniversary Edition", author_id=1, category_id=1),
            follow_redirects=True
        )
        self.assertIn(b"Fahrenheit 451: 50th Anniversary Edition", response.data)


class TestDeleteBook(TestBase):
    def test_delete_book(self):
        response = self.client.get(
            url_for('delete_book', bid = 1), follow_redirects=True)
        self.assertNotIn(b'Fahrenheit 451', response.data)


# Tests whether authors can be viewed
class TestViewAuthors(TestBase):
    def test_view_authors(self):
        response = self.client.get(url_for('view_authors'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ray Bradbury', response.data)


# Tests whether Ray Bradbury's name can be changed
class TestUpdateAuthor(TestBase):
    def test_update_author(self):
        response = self.client.post(
            url_for("update_author", aid=1),
            data = dict(author_name = "Ray Douglas Bradbury"),
            follow_redirects=True
        )
        self.assertIn(b"Ray Douglas Bradbury", response.data)


class TestDeleteAuthor(TestBase):
    def test_delete_author(self):
        response = self.client.get(
            url_for('delete_author', aid = 1), follow_redirects=True)
        self.assertNotIn(b'Ray Bradbury', response.data)


class TestViewCategories(TestBase):
    def test_view_categories(self):
        response = self.client.get(url_for('view_categories'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dystopian Fiction', response.data)