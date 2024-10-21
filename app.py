from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/home")

@app.route("/test")
def render_test():
    return render_template("./admin/base.html")

@app.route("/home")
def render_home():
    return render_template("index.html")