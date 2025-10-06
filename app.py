from flask import Flask, render_template, request
from datetime import datetime, timedelta
import sqlite3
import os
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key'
DATABASE = 'database.db'

# Debug: show DB path
print("Working dir:", os.getcwd())
print("Absolute DB path:", os.path.abspath(DATABASE))

# ---------------------- DATABASE SETUP ----------------------
def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS secrets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    secret_key TEXT UNIQUE,
                    secret_text TEXT,
                    created_at DATETIME,
                    expires_at DATETIME,
                    is_viewed INTEGER DEFAULT 0
                )''')
    conn.commit()
    conn.close()
    print("[DB] Initialized with table 'secrets'")

# ---------------------- ROUTES ----------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    secret_text = request.form['secret']
    expiry_minutes = int(request.form.get('expiry', 5))
    secret_key = str(uuid.uuid4())[:8]
    created_at = datetime.now()
    expires_at = created_at + timedelta(minutes=expiry_minutes)

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO secrets (secret_key, secret_text, created_at, expires_at) VALUES (?, ?, ?, ?)",
              (secret_key, secret_text, created_at, expires_at))
    conn.commit()
    conn.close()

    print(f"[DB] Inserted secret with key={secret_key}, expires_at={expires_at}")

    return render_template('link.html', link=request.host_url + 'secret/' + secret_key)

@app.route('/secret/<secret_key>')
def view_secret(secret_key):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT secret_text, expires_at, is_viewed FROM secrets WHERE secret_key = ?", (secret_key,))
    row = c.fetchone()

    if row is None:
        print(f"[DB] Secret {secret_key} not found or already expired")
        return render_template('expired.html', message="Secret not found or already expired.")

    secret_text, expires_at, is_viewed = row
    expires_at = datetime.strptime(expires_at, '%Y-%m-%d %H:%M:%S.%f')

    if is_viewed or datetime.now() > expires_at:
        conn.execute("DELETE FROM secrets WHERE secret_key = ?", (secret_key,))
        conn.commit()
        conn.close()
        print(f"[DB] Secret {secret_key} expired or already viewed → Deleted")
        return render_template('expired.html', message="Secret expired or already viewed.")

    # Mark as viewed
    c.execute("UPDATE secrets SET is_viewed = 1 WHERE secret_key = ?", (secret_key,))
    conn.commit()
    conn.close()
    print(f"[DB] Secret {secret_key} viewed → Marked is_viewed=1")
    return render_template('view_secret.html', secret=secret_text)

# ---------------------- MAIN ----------------------
if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        init_db()
    app.run(debug=True)
