from flask import Flask, request
import sqlite3, os
 
app = Flask(__name__)
 
@app.route("/user")
def user():
    name = request.args.get("name")
    conn = sqlite3.connect("db.sqlite")
    # SQL injection: user input goes straight into the query
    conn.execute("SELECT * FROM users WHERE name = '" + name + "'")
    return "ok"
 
@app.route("/run")
def run():
    # Command injection: user input goes straight into a shell command
    os.system("ping " + request.args.get("host"))
    return "ok"
