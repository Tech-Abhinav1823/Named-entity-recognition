from flask import Flask, render_template, request, redirect, url_for, session
from db import Database
from api import extract_entities
import os

app = Flask(__name__)

# A secret key is required for session management.
# In a production environment, use a more complex, securely stored key.
app.secret_key = os.urandom(24)

dbo = Database()

@app.route('/')
def index():
    # If user is already logged in, redirect to profile
    if 'user_email' in session:
        return redirect(url_for('profile'))
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/perform_registration', methods=['POST'])
def perform_registration():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    response = dbo.insert(name, email, password)

    if response:
        return render_template('login.html', message='Registration complete. Kindly login to proceed.')
    else:
        return render_template('registration.html', message='Email already exists.')

@app.route('/perform_login', methods=['POST'])
def perform_login():
    email = request.form.get('email')
    password = request.form.get('password')

    user_name = dbo.search(email, password)

    if user_name:
        # Store user's email in the session to mark them as logged in
        session['user_email'] = email
        session['user_name'] = user_name
        return redirect(url_for('profile'))
    else:
        return render_template('login.html', message='Incorrect email or password.')

@app.route('/profile')
def profile():
    # Protect this route: only logged-in users can see it
    if 'user_email' in session:
        return render_template('profile.html', user_name=session.get('user_name'))
    else:
        return redirect(url_for('login'))

@app.route('/ner')
def ner():
    # Protect this route
    if 'user_email' in session:
        return render_template('ner.html')
    else:
        return redirect(url_for('login'))

@app.route('/perform_ner', methods=['POST'])
def perform_ner():
    # Protect this route
    if 'user_email' not in session:
        return redirect(url_for('login'))
        
    text = request.form.get('nertext')
    if not text:
        return render_template('ner.html', message="Please enter some text to analyze.")
        
    result = extract_entities(text)
    return render_template('ner.html', entities=result, original_text=text)

@app.route('/logout')
def logout():
    # Clear the session to log the user out
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)