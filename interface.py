from flask import Flask, render_template, request, flash, redirect, url_for, session
from datetime import timedelta
from hashlock import hash_pass, verify_pass
from password_strength_checker import check_password_strength
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))  # Use environment variable or generate random key

# Configure session cookie for production
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    PREFERRED_URL_SCHEME='https'  # Force HTTPS
)

# Ensure session data persists in production
app.config['SESSION_TYPE'] = 'filesystem'
if os.environ.get('FLASK_ENV') == 'production':
    app.config['SESSION_PERMANENT'] = True
    app.permanent_session_lifetime = timedelta(days=1)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form.get('password')
        strength, tips = check_password_strength(password)
        
        if tips:  # Password is not strong enough
            return render_template('index.html', strength=strength, tips=tips)
        
        # Store the hash in session
        session['password_hash'] = hash_pass(password).decode()
        flash('Password registered successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('index.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        if 'password_hash' not in session:
            flash('No password registered!', 'error')
            return redirect(url_for('index'))
            
        password = request.form.get('password')
        stored_hash = session['password_hash'].encode()
        
        if verify_pass(password, stored_hash):
            flash('Password verified successfully! ✅', 'success')
        else:
            flash('Invalid password! ❌', 'error')
    
    return render_template('verify.html')

@app.route('/view-hash', methods=['GET', 'POST'])
def view_hash():
    if request.method == 'POST':
        if 'password_hash' not in session:
            flash('No password registered!', 'error')
            return redirect(url_for('index'))
            
        password = request.form.get('password')
        stored_hash = session['password_hash'].encode()
        
        if verify_pass(password, stored_hash):
            return render_template('view_hash.html', hash_value=session['password_hash'])
        else:
            flash('Invalid password! Access denied.', 'error')
    
    return render_template('view_hash.html')

if __name__ == '__main__':
    app.run(debug=True)

# This is for Vercel deployment
app.debug = False
