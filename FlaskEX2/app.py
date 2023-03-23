from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')
@app.get('/')
def calcpage():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        task_content = request.form['number'] 
        evenOrOdd = "doodles"
        try:
            task_content=int(task_content)
            x = (task_content%2)
            evenOrOdd = ''
            if x == 1:
                evenOrOdd = "your number is odd"
            if x == 0:
                evenOrOdd = "your number is even"
        except:
            evenOrOdd = "please enter an integer"
    
        return render_template('calculate.html', evenOrOdd=evenOrOdd)
    pass

@app.route('/calculate',methods=['GET', 'POST'])
def rethome():
    if request.method == 'POST':
        return redirect('/')
    return render_template('calculate.html')

if __name__ == "__main__":
    app.run(debug=True)
