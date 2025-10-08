# Simple Flask Verification App

Small demo app showing a "system busy" message and a retry button. Useful as an example project to upload to GitHub.

## How to run locally

```bash
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000

## Upload to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:YOUR_USERNAME/simple-flask-verification-app.git
git push -u origin main
```

## License

MIT License
