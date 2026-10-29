import os
import sqlite3
from flask import Flask, request
 
app = Flask(__name__)
 
@app.route("/user")
def get_user():
    name = request.args.get("name")
    conn = sqlite3.connect("db.sqlite")
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    return str(conn.execute(query).fetchall())
 
@app.route("/ping")
def ping():
    host = request.args.get("host")
    os.system("ping -c 1 " + host)
    return "done"
 
if __name__ == "__main__":
    app.run(debug=True)
app.run is For Sale
app.run is available for purchase. Buy now on Afternic, Aliyun, Nameslink, Dynadot, or Sedo.
 
