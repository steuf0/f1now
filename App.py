from flask import Flask, render_template
from utils import *
from datetime import date

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/drivers")
def drivers():
    return render_template('drivers.html', data=getDrivers())

@app.route("/constructors")
def constructors():
    return render_template('constructors.html', data=getConstructors())


if __name__ == "__main__":
    app.run(debug=True)
