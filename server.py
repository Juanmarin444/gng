from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)

app.secret_key = 'Habudu'

@app.route('/')
def index():
    random_num = random.randrange(0,101)
    session['rando'] = random_num
    print(session['rando'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    print(session['rando'],'random num')
    guess = int(request.form['gnum'])
    print(guess,'guess num')

    if session['rando'] == guess:
        print('that was legitness')
        return render_template('success.html')
    elif session['rando'] < guess:
        print('Number to high!')
        return render_template('high.html')
    elif session['rando'] > guess:
        print('Number to low!')
        return render_template('low.html')

app.run(debug=True)