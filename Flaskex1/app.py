from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    timeNow = datetime.now()
    time = timeNow.strftime("%m/%d/%Y, %H:%M:%S")
    return  render_template('index.html', time=time) ##"the current date time is: " + time.strftime("%m/%d/%Y, %H:%M:%S")

if __name__ == "__main__":
    app.run(debug=True)