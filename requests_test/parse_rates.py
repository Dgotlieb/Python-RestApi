import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=EUR&from=USD&amount=1"

payload = {}
headers= {
  "apikey": "XXXXXXXXXXXX"
}

response = requests.request("GET", url, headers=headers, data = payload)
data = response.json()
results = data['result']
print(results)
