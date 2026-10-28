from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello"



# Intentionally insecure: debug mode exposes the Werkzeug debugger (CodeQL: py/flask-debug)
app.run(debug=True)
# Debug mode must be disabled to avoid exposing the Werkzeug debugger
app.run(debug=False)
