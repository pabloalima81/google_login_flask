import os
import pathlib

import requests
from flask import Flask, session, abort, redirect, request
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

app = Flask("Google Login App")
app.secret_key = "testedesenha"

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return "Protegido" #abort(401)  # Authorization required
        else:
            return function()

    return wrapper

@app.route("/login")
def login():
    session["google_id"] = "Test"
    return redirect("/protected_area")

@app.route("/callback")
def callback():
    pass

@app.route("/logout")
def logout():
    session.clear()
    return redirect ("/")

@app.route("/")
def index():
    return("Hello World <a href='/login'><button>Login</button></a> ")
 
@app.route("/protected_area")
@login_is_required
def protected_area():
    return("Protected <a href='/logout'><button>Logout</button></a>")


if __name__ == "__main__":
    app.run(debug=True)
index()