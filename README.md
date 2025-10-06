# 🕵️‍♂️ ONE-TIME SECRET SHARING WEB APPLICATION WITH AUTO EXPIRY 🔐

Welcome to the **One-Time Secret Sharing Web Application**! 🚀  
This project allows users to securely share sensitive messages via unique, single-use links.  
Once the recipient views the secret, it **automatically expires**, ensuring privacy and data security.  
Perfect for temporary password sharing, private notes, and confidential communication! 💬  

---

## 🌟 Features

- 🔒 **One-Time Access:** Each secret link can be viewed only once — after that, it auto-deletes.  
- ⏳ **Auto Expiry:** Messages automatically expire after a custom set time.  
- 🧠 **Secure Storage:** Secrets are temporarily stored in an SQLite database.  
- 💻 **User-Friendly Interface:** Simple, responsive, and clean web design.  
- 📊 **Backend Logging:** Tracks creation, viewing, and expiry events in real-time.  
- ⚡ **Lightweight:** Built using Python Flask — minimal setup and easy to deploy.  

---

## 🛠️ Tech Stack

| Layer | Technology Used | Purpose |
|:--|:--|:--|
| **Frontend** | HTML, CSS | To design a simple and modern user interface |
| **Backend** | Python (Flask Framework) | Handles requests, routing, and DB operations |
| **Database** | SQLite3 | Stores and manages secrets temporarily |
| **Others** | UUID, Datetime | Generates unique IDs and manages expiry times |

---

## ⚙️ Requirements

Ensure you have the following installed before running the project:

- **Python 3.8 or higher** 🐍  
  Check version:
  ```bash
  python --version
Flask Framework 🌐
Install using pip:

bash
Copy code
pip install flask
SQLite3 (pre-installed with Python)

VS Code or Any IDE 💻 (for development and debugging)

🚀 Getting Started
1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/balaji-0111/One-Time-Secret-Sharing-Web-App.git
2️⃣ Navigate to the Project Directory
bash
Copy code
cd One-Time-Secret-Sharing-Web-App
3️⃣ Create a Virtual Environment (optional)
bash
Copy code
python -m venv venv
4️⃣ Activate the Virtual Environment
On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
5️⃣ Install Dependencies
bash
Copy code
pip install flask
6️⃣ Run the Application
bash
Copy code
python app.py
7️⃣ Open in Browser
Visit the following URL in your web browser:

cpp
Copy code
http://127.0.0.1:5000/
🖥️ Usage
🔐 Creating a Secret
Enter a message and set an expiry time (in minutes).

Click Generate Link to create a one-time secret URL.

Copy and share the generated link securely.

👀 Viewing a Secret
Open the shared link once to reveal the message.

After viewing, the secret automatically expires.

⏳ Expired or Viewed Secrets
If the same link is opened again or after expiry,
the page displays:
“Secret expired or already viewed.”

🧠 Example Demo
Home Page: Enter your secret message.

Generate Link: App creates a unique one-time URL.

View Secret: Receiver opens the link and sees the message.

Auto Delete: Message expires immediately after viewing.

🗄️ Database Workflow
Action	Database Change	Terminal Log
Create Secret	Row inserted (is_viewed=0)	[DB] Inserted secret with key=xxxx
View Secret	Row updated (is_viewed=1)	[DB] Secret xxxx viewed → Marked is_viewed=1
Expired/Viewed Again	Row deleted	[DB] Secret xxxx expired or already viewed → Deleted

📁 Folder Structure
php
Copy code
One-Time-Secret-Web-App/
│
├── app.py               # Main Flask backend logic
├── templates/           # HTML files (frontend)
│   ├── index.html
│   ├── link.html
│   ├── view_secret.html
│   └── expired.html
├── static/              # CSS and assets
│   └── style.css
├── database.db          # SQLite database (auto-generated)
├── requirements.txt     # Dependencies
└── README.md            # Documentation file
🧾 SQL Schema
sql
Copy code
CREATE TABLE IF NOT EXISTS secrets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    secret_key TEXT UNIQUE,
    secret_text TEXT,
    created_at DATETIME,
    expires_at DATETIME,
    is_viewed INTEGER DEFAULT 0
);
🛡️ Security Notes
Each secret link is randomly generated using UUID for uniqueness.

The database automatically removes expired or viewed secrets.

No sensitive data is stored permanently — ensuring complete privacy.

👨‍💻 Developer
Balaji B
🎓 IT Postgraduate | Python & SQL Enthusiast | Aspiring Software Engineer
📧 Email: [your-email@example.com]
🌐 GitHub: balaji-0111

📜 License
This project is open-source under the MIT License.
Feel free to fork, modify, and enhance it! ❤️

