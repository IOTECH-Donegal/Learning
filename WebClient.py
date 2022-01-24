import requests
url = 'http://localhost:8888/animal'

r = requests.get(url+'s')
print(r.text)

r = requests.get(url + '/Ellie')
print(r.text)

payload = '{ "Max": { "type": "Mouse", "born": 2019 } }'
header = { 'content-type': 'application/json' }
r = requests.post(url, data=payload, headers=header)
print(r.text)

payload = '{ "type": "Giraffe", "born": 2017 }'
header = { 'content-type': 'application/json' }
r = requests.post(url + '/Zed', data=payload, headers=header)
print(r.text)

r = requests.delete(url + '/Ellie')
print(r.text)

