from flask import Flask, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("registration.html")


@app.route("/store")
def dashboard():
    return render_template("store.html")


@app.route("/cli_store")
def addcli():
    return render_template("cli_store.html")


@app.route("/adm_store")
def addadm():
    return render_template("adm_store.html")


if __name__ == "__main__":
    app.run(debug=True)
