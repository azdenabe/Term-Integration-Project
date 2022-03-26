from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    render_template("/home/january.html")


app.run(port=8000)