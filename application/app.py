from flask import Flask, url_for, request, render_template
from flask.scaffold import _matching_loader_thinks_module_is_package
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to the index page"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_world(name=None):
    return render_template("hello.html", name=name)

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
    print(url_for("static", filename="style.css"))

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if valid_login(request.form["username"],
                       request.form["password"]):
            return log_the_user_in(request.form["username"])
    else:
        error = "Invalid username and password"
        return render_template("login.html", error=error)
    
with app.test_request_context("/hello", method="POST"):
    assert request.path == "/hello"
    assert request.method == "POST"
