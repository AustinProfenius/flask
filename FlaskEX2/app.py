from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST','GET'])
def calculate():
    if request.method == 'GET':
        task_content = request.form['number'] 
        evenOrOdd = "doodles"
        try:
            x = 1##(task_content%2)
            evenOrOdd = ''
            if x == 1:
                evenOrOdd = "your number is odd"
            if x == 0:
                evenOrOdd = "your number is even"
        except:
            evenOrOdd = "please enter an integer"
    
    return redirect('calculate.html', evenOrOdd=evenOrOdd)

@app.route('/calculate',methods=['GET', 'POST'])
def rethome():
    return render_template('calculate.html')

if __name__ == "__main__":
    app.run(debug=True)
