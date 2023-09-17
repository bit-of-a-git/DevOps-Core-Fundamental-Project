from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, PasswordField
from wtforms.validators import DataRequired


class AddAuthor(FlaskForm):
    author_name = StringField(
        "Author name:",
        validators=[DataRequired(message="Author name cannot be left blank.")],
    )
    submit = SubmitField("Add Author")


class AddBook(FlaskForm):
    book_title = StringField(
        "Book title:",
        validators=[DataRequired(message="Book title cannot be left blank.")],
    )
    author = SelectField(
        "Add to author:",
        choices=[],
        validators=[DataRequired(message="You must add an author first.")],
    )
    category = SelectField("Category:", choices=[])
    submit = SubmitField("Add Book")


class UpdateBook(FlaskForm):
    book_title = StringField("New title")
    available = BooleanField("Currently available?", default=True)
    submit = SubmitField("Update Book")
    category = SelectField("Category:", choices=[])


class UpdateAuthor(FlaskForm):
    author_name = StringField("New name:")
    submit = SubmitField("Update Author")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")
