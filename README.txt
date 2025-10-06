One-Time Secret Sharing Web App - Full Demo Bundle
--------------------------------------------------
Files included:
- app.py           : Flask backend (listens on all interfaces for LAN demo)
- db_monitor.py    : Live DB monitor that prints inserted/updated rows
- requirements.txt : pip dependencies
- database.db      : (created automatically on first run)
- templates/*      : HTML templates
- static/*         : CSS and images (bg.jpg if included)

Quick run (Windows):
1. Open Terminal in this folder.
2. Create venv: python -m venv venv
3. Activate venv: .\venv\Scripts\activate  (or use PowerShell Activate.ps1)
4. Install deps: pip install -r requirements.txt
5. Start app: python app.py
   - The server will run and show your LAN IP in the generated links.
6. In a second terminal (same folder), run: python db_monitor.py
   - This prints DB rows every second (encrypted & decrypted).
7. Open browser on your PC or phone (same Wi-Fi) and go to the app link printed or http://<your-lan-ip>:5000
8. Create a secret; watch the db_monitor terminal show the insert.
9. Open the generated link; watch db_monitor show row update/delete.

Notes:
- db_monitor is for demo only. Remove it for production.
- The app uses a simple Caesar cipher for demonstration; mention in viva that for production you'd use stronger encryption.
- If other devices cannot reach the app, check firewall or use ngrok for public tunneling.
