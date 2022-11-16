from application import db, app
from application.categories import categories
from application.models import Category

with app.app_context():
    db.drop_all()
    db.create_all()

    # Puts the categories in alphabetical order
    categories.sort()
    # Populates the Category table from the categories file
    for i in categories:
        newcat = Category(cat_name = i)
        db.session.add(newcat)
        db.session.commit()