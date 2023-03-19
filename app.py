
import requests
import pytesseract
import re 
import json
from PIL import Image
from flask import Flask, render_template, request
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def checking():
    img_file = request.files['image']
    img = Image.open(BytesIO(img_file.read()))
    extracted_info = pytesseract.image_to_string(img)
    # print(extracted_info)
    gst_pattern = r"\b\d{2}[A-Z]{5}\d{4}[A-Z]{1}\d[Z,z,2]{1}\d{1}\b"
    gst_number = re.search(gst_pattern, extracted_info).group(0)
    u_gst = gst_number[:13] + "Z" + gst_number[-1]
    print(u_gst)

    headers = {
	"Content-Type": "application/json",
	"X-RapidAPI-Key": "22886f282fmsh7f05dcaead6e345p16754ejsnda3b65078829",
	"X-RapidAPI-Host": "gst-return-status.p.rapidapi.com"
    }


    
    check_url= f"https://gst-return-status.p.rapidapi.com/free/gstin/{u_gst}"
    
    response = requests.get(check_url, headers=headers)
    
    a = json.loads(response.text)
    if a['success']:
        return render_template('verifi.html',a=a)
    else:
        return "<h2>Store on blockchain</h2>"
   
if __name__ == '__main__':
    app.run(debug=True)
