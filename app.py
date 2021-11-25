from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to the index page"

@app.route("/hello")
def hello_world():
    return "Hello World"

@app.route("/user/<username>")
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route("/post/<int:post_id>")
def show_post(post_id):
    # Implementing HTML Escape
    return f'Post {escape(post_id)}'

@app.route("/path/<path:subpath>")
def show_path(subpath):
    return f'Subpath {escape(subpath)}'

with app.test_request_context():
    print(url_for("hello_world"))
    print(url_for("show_user_profile", username="Seunfunmi Adegoke, please give me a job"))
    print(url_for("hello_world", next="/"))
    print(url_for("show_path", subpath="/seun/"))
    print(url_for("show_path", subpath=""))
    print(url_for("show_path", subpath="Miles Ahead"))