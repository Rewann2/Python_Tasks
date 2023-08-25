import requests

while True:
    url = requests.get("https://www.boredapi.com/api/activity")
    print(url.json()['activity'])
    x= input('if you need more suggest activities write [y] if not write[n]')
    if x== 'n':
        break
    