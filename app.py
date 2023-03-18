import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    prompt = "Hello, GPT-3!"
    url = "https://gst-return-status.p.rapidapi.com/free/gstin/27A5JCM9929L1ZM"
    response = requests.post("https://gst-return-status.p.rapidapi.com/free/gstin/27A5JCM9929L1ZM"),
    headers = {
	"Content-Type": "application/json",
	"X-RapidAPI-Key": "834dfdf592mshe0ed34b5a181dfbp1a2eafjsn91d66a151700",
	"X-RapidAPI-Host": "gst-return-status.p.rapidapi.com"
        },

       
    
    response = requests.request("GET",url,headers=headers)

    # result = response.json()["choices"][0]["text"]
    return  "<p>Hello, World!</p>"
if __name__ == '__main__':
    app.run(debug=True)
