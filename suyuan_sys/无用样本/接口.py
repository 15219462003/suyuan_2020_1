import requests

url = "https://v0.yiketianqi.com/api?appid=61827791&appsecret=1zGdoO62&version=v61"

payload = {'AppID': '2rtg2z53r',
'APIKey': '378d4582ad3ed253057cafe9c70fae8b',
'SecretKey': 'd6uk5fd'}
files = [
  ('Sound0', open('/C:/Users/Administrator/Desktop/Kou.wav','rb')),
  ('Sound1', open('/C:/Users/Administrator/Desktop/lijinlong001.wav','rb'))
]
headers = {
  'Content-Type': 'application/json',
  'apicode': '4af0547c15094e8ca0abb89ca2fbff96'
}

response = requests.request("GET", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))