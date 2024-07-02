import requests
res = requests.post('http://127.0.0.1:5000/data/1', json={"user_name":"daniel"})
if res.ok:
    print(res.json()) 
