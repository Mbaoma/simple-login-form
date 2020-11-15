from app import app
from flask import render_template, redirect, url_for, request, flash
from app.forms import SigninForm, SignUpForm

@app.route('/')
def index():
    return 'Hi there'
    
@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = SigninForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/signup/')
def signup():
    form =SignUpForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('signup.html', form=form)

@app.route('/home/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()