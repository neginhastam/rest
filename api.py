import requests

res=requests.get('https://dog.ceo/api/breeds/image/random')
if res.status_code==200:
    temp=res.json()
    print(temp)
    print(temp['message'])
    print(temp['status'])
else:
    print(res.status_code)
