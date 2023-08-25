import requests


url= requests.get("https://api.ipify.org/")

print(' your IP is : ',url.content)

