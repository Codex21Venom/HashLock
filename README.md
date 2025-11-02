# 🔐 HashLock — Secure Password Confirmation Tool

**HashLock** is a Python-based password confirmation and authentication tool that ensures secure password handling using modern cryptographic standards.  
It verifies passwords, checks their strength, and safely stores their hashes for session-based use — combining simplicity with strong security.

---

## 🚀 Features
- Secure password hashing using **bcrypt**
- Automatic password **strength analysis**
- Multi-attempt authentication with lockout mechanism
- Clean, interactive CLI interface
- Countdown-based security exit
- Modular design — integrates easily with other tools

---

## 🧠 How It Works
1. User enters a password — strength is checked instantly.  
2. Password is hashed using `bcrypt` (with unique salt).  
3. The user confirms their password to verify correctness.  
4. Once confirmed, authentication and hash retrieval features become available.  
5. Failed authentication after 3 attempts triggers a secure exit.

---

## 🧩 Project Structure
HashLock/
│
├── hashlock.py # Main program file
├── password_strength_checker.py # Password strength module
└── README.md # Project documentation


---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
  git clone https://github.com/Codex21Venom/HashLock.git
  cd HashLock
```
###2️⃣ Install required libraries
```bash
  pip install bcrypt
```
###▶️ Usage
Run the tool:
```bash
  python hashlock.py
```
