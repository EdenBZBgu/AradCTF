from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route("/proxy")
def proxy():
    r = requests.get("https://www.aradcohen.com/")
    return r.text

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)