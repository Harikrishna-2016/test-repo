from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello"


# Debug mode must be disabled to avoid exposing the Werkzeug debugger
app.run(debug=False)
