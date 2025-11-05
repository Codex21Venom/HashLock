# HashLock 🔒

<p align="center">
  <a href="https://hash-lock.vercel.app/">
    <img src="./Gemini_Generated_Image_nlujianlujianluj.png" alt="HashLock Logo" width="480" />
  </a>
</p>

## About
HashLock is a secure password management system with a modern web interface. It provides robust password strength checking, secure hashing using bcrypt, and an intuitive user interface for managing and verifying passwords.

## Live Website
🌐 [Visit HashLock Website](https://hash-lock.vercel.app/)

## Features

### 🛡️ Security Features
- Strong password validation
- Bcrypt hashing implementation
- Secure session management
- Real-time password strength feedback

### 🎨 User Interface
- Modern, responsive design
- Dark theme optimized for readability
- Interactive animations and transitions
- Mobile-friendly layout

### ⚙️ Core Functionality
- Create and verify secure passwords
- View secure password hashes
- Password strength visualization
- Detailed feedback on password requirements


<div align="center">
  <img src="./Cyber.gif" alt="HashLock Demo" width="800" style="max-width: 100%; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);" />
</div>

## 🧠 How It Works
1. User enters a password — strength is checked instantly.  
2. Password is hashed using `bcrypt` (with unique salt).  
3. The user confirms their password to verify correctness.  
4. Once confirmed, authentication and hash retrieval features become available.  
5. Failed authentication after 3 attempts triggers a secure exit.

---

## Technology Stack
- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Security**: Bcrypt hashing
- **Deployment**: Vercel

## Project Structure
```
HashLock/
├── interface.py          # Flask application and routes
├── hashlock.py          # Core password hashing functionality
├── password_strength_checker.py  # Password validation logic
├── static/              # Static assets
│   ├── style.css       # Stylesheet
│   └── images/         # Images and icons
├── templates/          # HTML templates
│   ├── base.html      # Base template
│   ├── index.html     # Home page
│   ├── verify.html    # Password verification
│   └── view_hash.html # Hash viewing page
└── requirements.txt    # Python dependencies
```

## Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/Codex21Venom/HashLock.git
cd HashLock
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python interface.py
```

The application will be available at `http://localhost:5000`

## Security Features
- Password strength requirements:
  - Minimum 8 characters
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Secure bcrypt hashing
- Protection against common password vulnerabilities
- Session security measures

## Deployment
The project is deployed on Vercel and is publicly accessible. The deployment automatically updates when changes are pushed to the main branch.

### Deployment URL
[https://hash-lock.vercel.app/](https://hash-lock.vercel.app/)

## Contributing
Feel free to contribute to this project by:
1. Forking the repository
2. Creating a feature branch
3. Submitting a pull request

## Contact
Project Link: [https://github.com/Codex21Venom/HashLock](https://github.com/Codex21Venom/HashLock)

