from flask import Flask, render_template, url_for, flash, redirect
from itroom import app, db, bcrypt
from itroom.forms import LoginForm, AddUserForm
from itroom.models import User, Post
from flask_login import login_user

@app.route("/")
@app.route("/home")     #defines the HTML loaded for /home
def home():
    return render_template('home.html', title='Home')


@app.route("/login", methods=['GET', 'POST'])       #defines the HTML loaded for /login
def login():
    form = LoginForm('')
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.userEmail.data).first()
        if user and bcrypt.check_password_hash(user.userPassword, form.password):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsucessful, Please check email and password') 
    return render_template('login.html',form=form, title='Login')

@app.route("/adduser", methods=['GET', 'POST'])       #defines the HTML loaded for /adduser
def addUser():
    form = AddUserForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode ('utf-8')
        user = User(userEmail=form.email.data, userPassword = hashed_password)
        db.session.add(user)
        db.session.commit()
        temptext = ("Account created for '", form.email.data, "'." )
        flash(temptext)

    else:
        flash('Account not created')
    form = AddUserForm('/login')
    return render_template('addUser.html', title='Admin', form=form)