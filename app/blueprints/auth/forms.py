from wtforms import StringField, SubmitField,PasswordField,EmailField, HiddenField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class PokemonSelect(FlaskForm):
    pokemon_name = StringField('Pokemon Name', validators=[DataRequired()])
    search_btn = SubmitField('Search', validators=[DataRequired()])
    pokemon_ability = HiddenField('Pokemon Ability')
    pokemon_base_exp = HiddenField('Pokemon Base Experience')
    pokemon_sprite = HiddenField('Pokemon Sprite')

class LoginForm(FlaskForm):
    identifier= StringField('Username or Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    login_btn = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    register_btn = SubmitField('Register', validators=[DataRequired()])

















































































"""
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    email = EmailField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_btn = SubmitField('Log In')

class SignUpForm(FlaskForm):
    first_name = StringField('First Name: ', validators=[DataRequired()])
    last_name = StringField('Last Name: ', validators=[DataRequired()])
    email = EmailField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit_btn = SubmitField('Sign Up')

"""