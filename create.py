from application import db, app
# get rid of this line I think, or change if you want to pre-populate with categories or something
from application.models import Author, Book

with app.app_context():
    db.drop_all()
    db.create_all()