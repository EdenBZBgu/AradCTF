from flask import Flask
import requests
import os
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

@app.route("/proxy")
def proxy():
    try:
        r = requests.get("https://www.aradcohen.com/", verify=False)
        return r.text
    except Exception as e:
        return f"ERROR: {e}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
