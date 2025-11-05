from flask import Flask, render_template, request, flash, redirect, url_for, session
from hashlock import hash_pass, verify_pass
from password_strength_checker import check_password_strength
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For flash messages and temporary session

# Configure session
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    PERMANENT_SESSION_LIFETIME=86400,  # 24 hours - will still clear on browser close
    SESSION_REFRESH_EACH_REQUEST=True
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.args.get('new') == '1':
        session.clear()
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        password = request.form.get('password')
        strength, tips = check_password_strength(password)
        
        if tips:  # Password is not strong enough
            return render_template('index.html', has_password=False, strength=strength, tips=tips)
        
        # Store the hash in session
        session['password_hash'] = hash_pass(password).decode()
        session.modified = True  # Ensure session is saved
        flash('Password registered successfully!', 'success')
        return redirect(url_for('index'))
    
    has_password = 'password_hash' in session
    return render_template('index.html', has_password=has_password)

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if 'password_hash' not in session:
        flash('Please register a password first!', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        password = request.form.get('password')
        try:
            stored_hash = session.get('password_hash', '').encode()
            if verify_pass(password, stored_hash):
                flash('Password verified successfully! ✅', 'success')
                return render_template('verify.html', verification_success=True)
            else:
                flash('Invalid password! ❌', 'error')
                return render_template('verify.html', verification_success=False)
        except Exception:
            session.clear()
            flash('Session expired. Please register your password again.', 'error')
            return redirect(url_for('index'))
    
    return render_template('verify.html')

@app.route('/view-hash', methods=['GET', 'POST'])
def view_hash():
    if 'password_hash' not in session:
        flash('Please register a password first!', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        password = request.form.get('password')
        try:
            stored_hash = session.get('password_hash', '').encode()
            if verify_pass(password, stored_hash):
                return render_template('view_hash.html', 
                                    hash_value=session.get('password_hash'),
                                    redirect_after=True)
            else:
                flash('Invalid password! Access denied.', 'error')
                return render_template('view_hash.html', error=True)
        except Exception:
            session.clear()
            flash('Session expired. Please register your password again.', 'error')
            return redirect(url_for('index'))
    
    return render_template('view_hash.html')

if __name__ == '__main__':
    app.run(debug=True)

# This is for Vercel deployment
app.debug = False
