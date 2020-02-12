from flask import Flask, render_template, url_for, flash, redirect
from itroom import app, db, bcrypt
from itroom.forms import LoginForm, AddUserForm
from itroom.models import User, Post

@app.route("/")
@app.route("/home")     #defines the HTML loaded for /home
def home():
    return render_template('home.html', title='Home')


@app.route("/login", methods=['GET', 'POST'])       #defines the HTML loaded for /login
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "test" and form.password.data == "password":
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/adduser", methods=['GET', 'POST'])       #defines the HTML loaded for /login
def addUser():
    form = AddUserForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode ('utf-8')
        user = User(userEmail=form.email.data, userPassword = hashed_password)
        db.session.add(user)
        db.session.commit()
        print("Account Created")
        temptext = ("Account created for '", form.email.data, "'." )
        flash(temptext)
    else:
        flash('Account not created')
    return render_template('addUser.html', title='Login', form=form)