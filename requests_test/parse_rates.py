import requests

res =  requests.get("https://api.exchangeratesapi.io/latest?base=USD")
data = res.json()
results = data['rates']
currency_value = results['ILS']
print("Result is: ", currency_value)
