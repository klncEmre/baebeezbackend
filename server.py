from flask import Flask, session, jsonify
import urllib.parse
import os
import psycopg2 as dbapi2



app = Flask(__name__)


@app.route("/")
def home_page():
    return jsonify({"data":"data1"})


if __name__ == "__main__":
    app.run(debug=True)