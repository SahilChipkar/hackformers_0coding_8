from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/')
def get_gst_return_status():
    url = "https://gst-return-status.p.rapidapi.com/free/gstin/27ANGPS5101F1Z6"

    headers = {
        "Content-Type": "application/json",
        "X-RapidAPI-Key": "834dfdf592mshe0ed34b5a181dfbp1a2eafjsn91d66a151700",
        "X-RapidAPI-Host": "gst-return-status.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return jsonify(success=data['success'])

if __name__ == '__main__':
    app.run(debug=True)