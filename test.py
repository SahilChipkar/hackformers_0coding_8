import requests
import pytesseract
import re 
import json
from PIL import Image
from flask import Flask, render_template


extractedInformation = pytesseract.image_to_string(Image.open('9.jpeg'))

print(extractedInformation)

gst_pattern = r"\b\d{2}[A-Z]{5}\d{4}[A-Z]{1}\d[Z,z,2,7]{1}\d{1}\b"
gst_number = re.search(gst_pattern, extractedInformation)

app = Flask(__name__)

@app.route('/')
def get_gst_status():
    url = ("https://gst-return-status.p.rapidapi.com/free/gstin/"+gst_number)

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