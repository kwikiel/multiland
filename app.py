from flask import Flask
from flask import render_template

app = Flask(__name__)

#Yolo2

@app.route("/")
def hello():
    return render_template("index.html")
