from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class AddAuthor(FlaskForm):
    author_name = StringField('Author name:', validators=[DataRequired(message="Author name cannot be left blank.")])
    submit = SubmitField('Add Author')

class AddBook(FlaskForm):
    book_title = StringField("Book title:", validators=[DataRequired(message="Book title cannot be left blank.")])
    author = SelectField("Add to author:", choices=[], validators=[DataRequired(message="You must add an author first.")])
    submit = SubmitField("Add Book")