from flask import Flask, session, render_template, redirect, url_for, request

import random

app = Flask(__name__)
app.secret_key = 'replace-this-with-a-secret-value'

choices = ['rock', 'paper', 'scissors']

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "user wins!"
    else:
        return "computer wins!"

@app.route('/home')
def home():
    if 'wins' not in session:
        session["wins"] = 0
        session["loses"] = 0
        session["ties"] = 0

    return render_template('index.html', session=session)

@app.route('/')
def index():
    return home()

@app.route('/play',methods=['POST'])
def play():
    user_choice = request.form['choice']
    computer_choice = random.choice(choices)
    winner = get_winner(user_choice, computer_choice)

    if winner == 'computer wins!':
        session['loses'] += 1
    elif winner == 'user wins!':
        session['wins'] += 1
    else:
        session['ties'] += 1
    return render_template('index.html',
        user_choices=user_choice,
        computer_choices=computer_choice,
        winner=winner,
        session=session
    )

@app.route('/reset')
def reset():
    session['wins'] = 0
    session['loses'] = 0
    session['ties'] = 0
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)