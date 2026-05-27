from flask import Flask, render_template, request, redirect
import string
import random

app = Flask(__name__)

urls = {}

@app.route("/")
def home():
    return render_template("style.html")


@app.route("/shorten", methods=["POST"])
def shorten_url():

    original_url = request.form["URL"]

    characters = string.ascii_letters + string.digits

    short_code = 'http://127.0.0.1:5000/' + ''.join(random.choice(characters) for _ in range(6))
    

    urls[short_code] = original_url

    return f"Short URL:{short_code}"

@app.route("/<short_code>")
def redirect_url(short_code):

    original_url = urls.get(short_code)

    if original_url:
        return redirect(original_url)

    return "URL not found"


if __name__ == "__main__":
    app.run(debug=True)