🕵️‍♂️ One-Time Secret Sharing Web Application with Auto Expiry 🔐
Welcome to the One-Time Secret Sharing Web Application! 🚀
This project allows users to securely share sensitive messages via unique, single-use links with client-side encryption.
Once the recipient views the secret, it automatically expires, ensuring privacy and data security.
Perfect for temporary password sharing, private notes, and confidential information exchange! 💬

🌟 Features
✨ One-Time Access: Each secret link can be viewed only once — after that, it auto-deletes.
🕒 Auto Expiry: Messages automatically expire after a custom set time.
🔒 Client-Side Encryption: Secrets are encrypted before being sent to the server.
🔑 Passphrase Protection: Optional passphrase for additional security layer.
💻 User-Friendly Interface: Simple, responsive, and clean design.
📊 Backend Logging: Tracks creation, viewing, and expiry events.
🧩 Lightweight: Built using Python Flask with SQLite database.

🛠️ Tech Stack
Layer	Technology Used	Purpose
Frontend	HTML, CSS, JavaScript	Modern UI with client-side crypto
Backend	Python (Flask Framework)	Handles API requests and DB operations
Database	SQLite3	Stores encrypted secrets temporarily
Encryption	Web Crypto API	AES-256-GCM for secure encryption
Utilities	UUID, Datetime	Unique IDs and expiry management
⚙️ Requirements
Ensure you have the following installed on your system:

Python 3.8 or Higher 🐍
Check version:

bash
python --version
Flask Framework 🌐
Install using pip:

bash
pip install flask
Modern Web Browser 🔧
Supports Web Crypto API (Chrome 60+, Firefox 63+, Safari 14+)

🚀 Getting Started
1️⃣ Clone the Repository
bash
git clone https://github.com/balaji-0111/One-Time-Secret-Sharing-Web-App.git
2️⃣ Navigate to the Project Directory
bash
cd One-Time-Secret-Sharing-Web-App
3️⃣ Create a Virtual Environment (optional but recommended)
bash
python -m venv venv
4️⃣ Activate the Virtual Environment
Windows

bash
venv\Scripts\activate
Mac/Linux

bash
source venv/bin/activate
5️⃣ Install Dependencies
bash
pip install flask
6️⃣ Run the Application
bash
python app.py
7️⃣ Open in Browser
Visit 👉 http://127.0.0.1:5000/
You'll see the homepage to create and share encrypted one-time secrets.

🖥️ Usage
🔐 Create a Secret
Enter your secret message

Set an expiry time (in minutes)

Optional: Add a passphrase for extra security

Click "Generate Secure Link"

Copy and share the encrypted secret URL

👀 View a Secret
Open the shared link

If passphrase protected: Enter the passphrase

The message will be decrypted and displayed securely in your browser

After viewing, the secret expires automatically

⏳ Expired or Viewed
If the link is opened again or after expiry time:

The page will display: "Secret expired or already viewed."

🔐 Encryption Methodology
Client-Side Encryption Flow:
Key Generation: Random AES-256 key or derived from passphrase using PBKDF2

Encryption: AES-GCM mode with random initialization vector (IV)

Storage: Only encrypted data, IV, and salt (if passphrase used) sent to server

Decryption: Happens entirely in the user's browser

Security Features:
Zero Knowledge: Server never sees plaintext secrets

Cryptographically Secure: Uses Web Crypto API standards

Forward Secrecy: Each secret uses unique encryption keys

Integrity Protection: AES-GCM includes authentication

🗄️ Database Workflow
Action	Database Change	Log Message
Create secret	Row inserted (encrypted_data, iv, salt, view_count=0)	[DB] Inserted encrypted secret with key=xxxx
View secret	Row updated (view_count incremented)	[DB] Secret xxxx viewed → view_count increased
Burn after read	Row deleted after first view	[DB] Secret xxxx burned after reading → Deleted
Auto expiry	Row deleted by cleanup job	[DB] Secret xxxx expired → Deleted
🧩 Folder Structure
text
One-Time-Secret-Web-App/
│
├── app.py                 # Main Flask backend
├── templates/             # HTML files (frontend)
│   ├── index.html         # Create secret page
│   ├── link.html          # Generated link page
│   ├── view_secret.html   # View/decrypt secret page
│   └── expired.html       # Expired secret page
├── static/                # CSS, JS, and assets
│   ├── style.css          # Styling
│   ├── crypto.js          # Encryption/decryption logic
│   └── app.js             # Frontend application logic
├── database.db            # SQLite database (auto-created)
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
