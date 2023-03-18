import requests



url = "https://gst-return-status.p.rapidapi.com/free/gstin/27AAJCM9929L1ZM"

headers = {
	"Content-Type": "application/json",
	"X-RapidAPI-Key": "2be714b04amshdfc1a9be215a79cp127fccjsn58a2b5c2bc70",
	"X-RapidAPI-Host": "gst-return-status.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)


