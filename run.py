from flask import Flask, render_template, url_for
from forms import LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'd0f59ff548e889290c6bf21f05d52afc'

@app.route("/")
@app.route("/home")     #defines the HTML loaded for /home
def home():
    return render_template('home.html', title='Home')


@app.route("/login")    #defines the HTML loaded for /login
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':      #always sets debug to be true
    app.run(debug=True)