from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")     #defines the HTML loaded for /home
def home():
    return render_template('home.html', title='Home')


@app.route("/login")    #defines the HTML loaded for /login
def about():
    return render_template('login.html', title='Login')


if __name__ == '__main__':      #always sets debug to be true
    app.run(debug=True)