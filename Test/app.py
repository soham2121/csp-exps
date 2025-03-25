from flask import Flask, render_template, Request
import sqlite3

app = Flask(__name__)
connection = sqlite3.connect('test.db')
cursor = connection.cursor()

def once():
    cursor.execute("DROP TABLE movie")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/Signup")
def signup():
    return render_template("signup.html")

@app.route("/Login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)