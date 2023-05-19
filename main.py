import requests

def fetchandstoreresponse(url, path):
    r = requests.get(url)
    with open(path, 'w', encoding="utf-8") as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/india/how-india-can-use-its-unique-position-at-hiroshima-g7/articleshow/100335913.cms"
fetchandstoreresponse(url, "data/times.html")