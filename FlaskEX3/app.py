from flask import Flask, redirect, render_template, request
from sqlalchemy import null

app = Flask(__name__)
theList = {}

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/registered')
def registered():
    return render_template('registered.html',theList=theList)


@app.route('/registered', methods=['POST'])
def home():
    errormessage = ''
    if request.method == 'POST':
        name = request.form['name']
        club = request.form['club']
        theList.update({name: club})

        if len(name) == 0:

            errormessage = 'please enter a valid name'
            return render_template('index.html', errormessage=errormessage)

    return render_template('registered.html', theList=theList)



if __name__ == "__main__":
    app.run(debug=True)
