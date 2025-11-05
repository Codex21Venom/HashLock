from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, make_response
from hashlock import hash_pass, verify_pass
from password_strength_checker import check_password_strength
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Just for flash messages

# Configure to never save cookies
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    PERMANENT_SESSION_LIFETIME=0,  # Sessions die immediately
    SESSION_REFRESH_EACH_REQUEST=False,  # Don't refresh sessions
)

# In-memory storage (cleared when app restarts)
current_hash = None

@app.before_request
def clear_cookies():
    global current_hash
    # Clear the current hash on every new browser session
    if not request.cookies.get('session_started'):
        current_hash = None

@app.after_request
def clear_session(response):
    # Clear all cookies except the bare minimum needed for flash messages
    if not request.path == '/':  # Don't clear on main page to allow flash messages
        response.delete_cookie('session')
    response.set_cookie('session_started', 'true', max_age=0)  # Expires when browser closes
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    global current_hash
    
    if request.args.get('new') == '1':
        current_hash = None
    
    if request.method == 'POST':
        password = request.form.get('password')
        strength, tips = check_password_strength(password)
        
        if tips:  # Password is not strong enough
            return render_template('index.html', strength=strength, tips=tips)
        
        # Store the hash in memory
        current_hash = hash_pass(password).decode()
        flash('Password registered successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('index.html', has_password=bool(current_hash))

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    global current_hash
    
    if not current_hash:
        flash('No password registered!', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        password = request.form.get('password')
        stored_hash = current_hash.encode()
        
        if verify_pass(password, stored_hash):
            flash('Password verified successfully! ✅', 'success')
        else:
            flash('Invalid password! ❌', 'error')
        return redirect(url_for('index'))  # Return to menu after verification
    
    return render_template('verify.html')

@app.route('/view-hash', methods=['GET', 'POST'])
def view_hash():
    global current_hash
    
    if not current_hash:
        flash('No password registered!', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        password = request.form.get('password')
        stored_hash = current_hash.encode()
        
        if verify_pass(password, stored_hash):
            flash('Hash displayed successfully!', 'success')
            # Show hash and redirect back to menu after a delay
            return render_template('view_hash.html', hash_value=current_hash, redirect_after=True)
        else:
            flash('Invalid password! Access denied.', 'error')
            return redirect(url_for('index'))
    
    return render_template('view_hash.html')

if __name__ == '__main__':
    app.run(debug=True)

# This is for Vercel deployment
app.debug = False
