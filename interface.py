from flask import Flask, render_template, request, flash, redirect, url_for, session
from hashlock import hash_pass, verify_pass
from password_strength_checker import check_password_strength
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))  # Use environment variable or generate random key

# Configure session cookie for production
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax'
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        strength, tips = check_password_strength(password)
        
        if tips:  # Password is not strong enough
            return render_template('index.html', strength=strength, tips=tips)
        
        if confirm_password:  # Confirmation phase
            if password != confirm_password:
                flash('Passwords do not match!', 'error')
                return render_template('index.html', show_confirm=True)
            
            # Store the hash in session
            session['password_hash'] = hash_pass(password).decode()
            flash('Password set successfully!', 'success')
            return redirect(url_for('verify'))
        
        # Show confirmation field if password is strong
        return render_template('index.html', show_confirm=True)
    
    return render_template('index.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if 'password_hash' not in session:
        flash('Please set a password first!', 'warning')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        password = request.form.get('password')
        stored_hash = session['password_hash'].encode()
        
        if verify_pass(password, stored_hash):
            flash('Password verified successfully!', 'success')
        else:
            flash('Invalid password!', 'error')
    
    return render_template('verify.html')

@app.route('/view-hash', methods=['GET', 'POST'])
def view_hash():
    if 'password_hash' not in session:
        flash('Please set a password first!', 'warning')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        password = request.form.get('password')
        stored_hash = session['password_hash'].encode()
        
        if verify_pass(password, stored_hash):
            return render_template('view_hash.html', hash_value=session['password_hash'])
        else:
            flash('Invalid password!', 'error')
    
    return render_template('view_hash.html')

if __name__ == '__main__':
    app.run(debug=True)

# This is for Vercel deployment
app.debug = False
