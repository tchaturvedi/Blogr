from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class RegisterationForm(Form):
    username = StringField( 'username', validators=[InputRequired(), Length(min=5, max=25)] )
    email = StringField( 'email', validators=[InputRequired(), Email(), Length(min=6, max=30)] )
    password = PasswordField( 'password', validators=[InputRequired(),
                                                            EqualTo('confirm_password', message='Passwords must match'),
                                                            Length(min=8)] )
    confirm_password = PasswordField( 'confirm password', validators=[EqualTo('password', message='Passwords must match')] )


class LoginForm(Form):
    username = StringField( 'username', validators=[InputRequired(), Length(min=5, max=25)] )
    password = PasswordField( 'password', validators=[InputRequired(), Length(min=5)] )
