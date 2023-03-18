import requests
import pytesseract
import re 
import json
from PIL import Image
from flask import Flask, render_template

img_path = 'img1.jpeg'

extracted_info = pytesseract.image_to_string(Image.open(img_path))
gst_pattern = r"\b\d{2}[A-Z]{5}\d{4}[A-Z]{1}\d[Z,z,2]{1}\d{1}\b"
gst_number = re.search(gst_pattern, extracted_info).group(0)
# print(gst_number)

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html')



@app.route('/check')
def home():
   
    headers = {
        "Content-Type": "application/json",
        "X-RapidAPI-Key": "834dfdf592mshe0ed34b5a181dfbp1a2eafjsn91d66a151700",
        "X-RapidAPI-Host": "gst-return-status.p.rapidapi.com"
    }
    
    
    check_url= f"https://gst-return-status.p.rapidapi.com/free/gstin/{gst_number}"
    
    
    response = requests.get(check_url, headers=headers)
    
   
    a = json.loads(response.text)
    if a['success']:
        return render_template('verifi.html')
    else:
        return "<h2>Store on blockchain</h2>"

if __name__ == '__main__':
    app.run(debug=True)
