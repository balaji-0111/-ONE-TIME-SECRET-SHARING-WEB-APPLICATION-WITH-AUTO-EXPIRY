import sqlite3, time
from datetime import datetime

DB = "database.db"

def decrypt_message(message, shift=3):
    def encrypt_message(message, shift):
        encrypted_msg = ""
        for char in message:
            if char.isalpha():
                shift_amount = shift % 26
                if char.islower():
                    encrypted_msg += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
                else:
                    encrypted_msg += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            else:
                encrypted_msg += char
        return encrypted_msg
    return encrypt_message(message, -shift)

def fetch_rows():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    try:
        c.execute("SELECT id, secret_key, secret_text, created_at, expires_at, is_viewed FROM secrets ORDER BY id")
        rows = c.fetchall()
    except Exception:
        rows = []
    conn.close()
    return rows

def pretty(rows):
    if not rows:
        print(f"{datetime.now()}  -- no rows")
        return
    print(f"{datetime.now()}  -- {len(rows)} row(s):")
    for r in rows:
        id, key, enc, created, expires, viewed = r
        try:
            dec = decrypt_message(enc, 3)
        except Exception:
            dec = "[decrypt error]"
        print(f" id={id} key={key} viewed={viewed} created={created} expires={expires}")
        print(f"    encrypted: {enc}")
        print(f"    decrypted: {dec}")
    print("-"*60)

if __name__ == '__main__':
    print("Starting DB monitor (polls every 1s). Ctrl-C to stop.")
    try:
        while True:
            rows = fetch_rows()
            pretty(rows)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped.")