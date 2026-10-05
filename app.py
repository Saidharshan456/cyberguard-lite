from flask import Flask, render_template, Response, request

app = Flask(__name__)


# -----------------------------------
# Password Strength Checker
# -----------------------------------

def check_password(password):
    score = 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(not c.isalnum() for c in password):
        score += 1

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Moderate"

    else:
        return "Strong"


# -----------------------------------
# Home Page
# -----------------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    password_result = "Not tested"
    score = 75

    if request.method == "POST":

        password = request.form.get("password", "")

        if password:

            password_result = check_password(password)

            if password_result == "Strong":
                score = 100

            elif password_result == "Moderate":
                score = 90

            else:
                score = 75

    return render_template(
        "index.html",
        score=score,
        password_result=password_result
    )
@app.route("/about")
def about():
    return render_template("about.html")

# -----------------------------------
# Robots.txt
# -----------------------------------

@app.route("/robots.txt")
def robots():

    robots_content = """User-agent: *
Allow: /

Sitemap: https://cyberguard-lite.onrender.com/sitemap.xml
"""

    return Response(
        robots_content,
        mimetype="text/plain"
    )


# -----------------------------------
# Sitemap.xml
# -----------------------------------

@app.route("/sitemap.xml")
def sitemap():

    sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

    <url>
        <loc>https://cyberguard-lite.onrender.com/</loc>
    </url>

    <url>
        <loc>https://cyberguard-lite.onrender.com/about</loc>
    </url>

</urlset>
"""

    return Response(
        sitemap_content,
        mimetype="application/xml"
    )


# -----------------------------------
# Start Flask
# -----------------------------------

if __name__ == "__main__":
    app.run(debug=True)
S
