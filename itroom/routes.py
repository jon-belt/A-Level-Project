from flask import Flask, render_template, url_for, flash, redirect, request
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
    form = LoginForm()
    if form.validate_on_submit():                   #runs when form is submitted and valid
        user = User.query.filter_by(userEmail=form.email.data).first()          #checks for login details
        if user and bcrypt.check_password_hash(user.userPassword, form.password.data):          #Bcrypt checks hashed password
            login_user(user, remember=form.remember.data)           #runs function to log user in
            return redirect(url_for('home'))        #redirects user to /home page
        else:
            flash('Login Unsucessful, Please check email and password', 'danger') 
    return render_template('login.html',form=form, title='Login')

@app.route("/adduser", methods=['GET', 'POST'])       #defines the HTML loaded for /adduser
def addUser():
    form = AddUserForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(userEmail=form.email.data, userPassword = hashed_password)
        db.session.add(user)
        db.session.commit()
        temptext = "Account created for ", form.email.data, "." 
        flash(temptext,'success')
        return redirect(url_for('addUser'))
    elif request.method == 'POST' and form.validate_on_submit()==False:
        flash('Account not created','danger')
    form = AddUserForm('/login')
    return render_template('addUser.html', title='Admin', form=form)

@app.route("/forum", methods=['GET', 'POST'])       #defines the HTML loaded for /forum
def forum():
    return render_template('forum.html', title='Forum')

@app.route("/ask", methods=['GET', 'POST'])       #defines the HTML loaded for /ask
def ask():
    return render_template('ask.html', title='Ask a Question')

@app.route("/profile", methods=['GET', 'POST'])       #defines the HTML loaded for /profile
def profile():
    return render_template('profile.html', title='My Profile')