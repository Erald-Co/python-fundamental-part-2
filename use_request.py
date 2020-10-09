import requests

url = "https://detik.com"
try:
    requests.get(url)
except Exception as e:
    print("There is an error", e)

print("Lewat jalan ini")