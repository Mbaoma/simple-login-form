from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import (DataRequired, Email, EqualTo)
from wtforms.fields.html5 import EmailField

class SigninForm(FlaskForm):    
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me =  BooleanField('Remember me')
    submit = SubmitField('Sign In')

class SignUpForm(FlaskForm):    
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo(password)])
    submit = SubmitField('Sign Up')
