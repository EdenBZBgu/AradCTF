# Python Flask example (server.py)
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/proxy')
def proxy():
    r = requests.get('https://www.aradcohen.com/')
    return r.text

app.run()