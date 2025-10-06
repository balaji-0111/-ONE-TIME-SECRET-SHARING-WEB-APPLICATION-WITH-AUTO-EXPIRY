# 🕵️‍♂️ ONE-TIME SECRET SHARING WEB APPLICATION WITH AUTO EXPIRY 🔐

Welcome to the **One-Time Secret Sharing Web Application**! 🚀  
This project allows users to securely share sensitive messages via unique, single-use links.  
Once the recipient views the secret, it **automatically expires**, ensuring privacy and data security.  
Perfect for temporary password sharing, private notes, and confidential information exchange! 💬

---

## 🌟 Features
✨ **One-Time Access:** Each secret link can be viewed only once — after that, it auto-deletes.  
🕒 **Auto Expiry:** Messages automatically expire after a custom set time.  
🔒 **Secure Storage:** Secrets are temporarily stored in a SQLite database.  
💻 **User-Friendly Interface:** Simple, responsive, and clean design.  
📊 **Backend Logging:** Tracks creation, viewing, and expiry events in the terminal.  
🧩 **Lightweight:** Built using Python Flask — minimal setup and easy to run.  

---

## 🛠️ Tech Stack
| Layer | Technology Used | Purpose |
|:--|:--|:--|
| Frontend | HTML, CSS | To design a simple and modern UI |
| Backend | Python (Flask Framework) | Handles requests, routing, and DB operations |
| Database | SQLite3 | Stores secrets temporarily |
| Others | UUID, Datetime | Generates unique IDs and manages expiry times |

---

## ⚙️ Requirements
Ensure you have the following installed on your system:

- **Python 3.8 or Higher** 🐍  
  Check version:
  ```bash
  python --version
