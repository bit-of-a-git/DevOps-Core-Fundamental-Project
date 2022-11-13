from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired

class AddAuthor(FlaskForm):
    author_name = StringField('Author name:', validators=[DataRequired(message="Author name cannot be left blank.")])
    submit = SubmitField('Add Author')

class AddBook(FlaskForm):
    book_title = StringField("Book title:", validators=[DataRequired(message="Book title cannot be left blank.")])
    author = SelectField("Add to author:", choices=[], validators=[DataRequired(message="You must add an author first.")])
    category = SelectField("Category:", choices=[])
    submit = SubmitField("Add Book")

class UpdateBook(FlaskForm):
    # Just trying to get changing the name working for now
    # after this I will make it so it can be marked unavailable
    book_title = StringField('New title', validators=[DataRequired(message="Book title cannot be left blank.")])
    available = BooleanField("Currently available?", default=True)
    submit = SubmitField('Update Book')
    category = SelectField("Category:", choices=[])

class UpdateAuthor(FlaskForm):
    # Just trying to get changing the name working for now
    # after this I will make it so it can be marked unavailable
    author_name = StringField('New name:', validators=[DataRequired(message="Author name cannot be left blank.")])
    submit = SubmitField('Update Author')