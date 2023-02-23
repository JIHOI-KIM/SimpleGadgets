import requests

URL = "http://182.227.191.199:1337/all"

#COOKIE, HEADER
headers = {'Content-Type': 'application/json; charset=utf-8'}
cookies = {'session_id': 'sessionidstring'}

#GET
params = {'arg1':'item1', 'arg2':'item2'}
response = requests.get(URL, params=params)
# request.get(URL, params=params, headers=headers, cookies = cookies)

#POST
data = "mypostdata"
response = requests.post(URL, data=data)
# request.post(URL, data=data, headers=headers, cookies = cookies)