from application import db, app
from application.categories import categories
from application.models import Category, User
import os

with app.app_context():
    db.drop_all()
    db.create_all()

    # Puts the categories in alphabetical order
    categories.sort()
    # Populates the Category table from the categories file
    for i in categories:
        newcat = Category(cat_name=i)
        db.session.add(newcat)
        db.session.commit()

    username = os.getenv("LIBRARIAN_USERNAME")
    password = os.getenv("LIBRARIAN_PASSWORD")

    if username and password:
        user = User(username=username)
        # Set the password for the user (remember to hash it)
        user.set_password(password)

    # Add the user to the database
    db.session.add(user)
    db.session.commit()

    print("User 'Librarian' created.")
