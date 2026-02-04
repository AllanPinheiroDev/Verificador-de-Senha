from flask import Flask, render_template, request
import re, hashlib, requests

app = Flask(__name__)

def check_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[0-9]", password): score += 1
    if re.search(r"[!@#$%^&*]", password): score += 1

    if score <= 2: return "🔴 Fraca"
    elif score <= 4: return "🟡 Média"
    else: return "🟢 Forte"

def check_pwned(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    r = requests.get(url)
    for line in r.text.splitlines():
        h, count = line.split(":")
        if h == suffix:
            return f"⚠️ Vazou {count} vezes"
    return "✅ Não encontrada em vazamentos"

@app.route("/", methods=["GET", "POST"])
def index():
    result = leak = None
    if request.method == "POST":
        password = request.form["password"]
        result = check_strength(password)
        leak = check_pwned(password)
    return render_template("index.html", result=result, leak=leak)

app.run(debug=True)
