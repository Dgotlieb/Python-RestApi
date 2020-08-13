import requests
res = requests.get('https://google.com')
if res.ok:
    print(res.content)
