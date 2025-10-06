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
Flask Framework 🌐
Install using pip:

bash
Copy code
pip install flask
SQLite3 (comes pre-installed with Python)

VS Code or Any IDE 💻
Recommended for better debugging and project view.

🚀 Getting Started
1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/balaji-0111/One-Time-Secret-Sharing-Web-App.git
2️⃣ Navigate to the Project Directory
bash
Copy code
cd One-Time-Secret-Sharing-Web-App
3️⃣ Create a Virtual Environment (optional but recommended)
bash
Copy code
python -m venv venv
4️⃣ Activate the Virtual Environment
Windows

bash
Copy code
venv\Scripts\activate
Mac/Linux

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
Visit 👉 http://127.0.0.1:5000/
You’ll see the homepage to create and share one-time secrets.

🖥️ Usage
🔐 Create a Secret
Enter a message and set an expiry time (in minutes).

Click Generate Link to get a one-time secret URL.

Copy and share the link securely.

👀 View a Secret
Open the shared link once.

The message will be displayed securely.

After viewing, the secret expires automatically.

⏳ Expired or Viewed
If the link is opened again or after expiry time:

The page will display: “Secret expired or already viewed.”

🧠 Example Demo
1️⃣ Home Page: Enter your secret message.
2️⃣ Generate Link: App creates a unique one-time URL.
3️⃣ View Secret: Receiver opens the link and reads the message.
4️⃣ Auto Delete: Message expires immediately after viewing.

🗄️ Database Workflow
Action	Database Change	Log Message
Create secret	Row inserted (is_viewed=0)	[DB] Inserted secret with key=xxxx
View secret	Row updated (is_viewed=1)	[DB] Secret xxxx viewed → Marked is_viewed=1
Expired/View again	Row deleted	[DB] Secret xxxx expired or already viewed → Deleted

🧩 Folder Structure
csharp
Copy code
One-Time-Secret-Web-App/
│
├── app.py               # Main Flask backend
├── templates/           # HTML files (frontend)
│   ├── index.html
│   ├── link.html
│   ├── view_secret.html
│   └── expired.html
├── static/              # CSS and assets
│   └── style.css
├── database.db          # SQLite database (auto-created)
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
🧾 Example SQL Schema
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

The database clears expired or viewed entries automatically.

No sensitive information is permanently stored.

👨‍💻 Developer
Balaji B
🎓 IT Postgraduate | 🧠 Python & SQL Enthusiast | 💼 Aspiring Software Engineer
📧 Email: [your-email@example.com]
🌐 GitHub: balaji-0111

📜 License
This project is open-source under the MIT License.
Feel free to fork and enhance it. ❤️
