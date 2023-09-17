from application import db, app
from application.categories import categories
from application.models import Category, User
from flask_bcrypt import Bcrypt
import os
from sqlalchemy import inspect

bcrypt = Bcrypt(app)

with app.app_context():
    inspector = inspect(db.engine)
    # This uses inspect to check if the tables exist. If not, they are created.
    if "category" not in inspector.get_table_names():
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
        user.password_hash = hashed_password

        # Checks to see if the user already exists in the database
        existing_user = User.query.filter_by(username=username).first()
        if not existing_user:
            db.session.add(user)
            db.session.commit()

            print(f"User '{username}' created.")
        else:
            print(f"User '{username}' already exists.")
