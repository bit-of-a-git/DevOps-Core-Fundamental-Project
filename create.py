from application import db, app
from application.categories import categories
from application.models import Category, User
from flask_bcrypt import Bcrypt
import os

bcrypt = Bcrypt(app)

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

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        # Set the password for the user (remember to hash it)
        user.password_hash = hashed_password

    # Add the user to the database
    db.session.add(user)
    db.session.commit()

    print(f"User '{username}' created.")
