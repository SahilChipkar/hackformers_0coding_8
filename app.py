from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/')
def get_gst_status():
    url = "https://gst-return-status.p.rapidapi.com/free/gstin/27AN7PS5101F1Z6"

    headers = {
        "Content-Type": "application/json",
        "X-RapidAPI-Key": "834dfdf592mshe0ed34b5a181dfbp1a2eafjsn91d66a151700",
        "X-RapidAPI-Host": "gst-return-status.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    a = json.loads(response.text)
    if a['success']:
        return "<h1>Verified</h1>"
    else:
        return "<h2>Store on blockchain</h2>"

if __name__ == '__main__':
    app.run(debug=True)
