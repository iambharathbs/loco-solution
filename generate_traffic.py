import requests

while True:
    try:
        response = requests.get("http://localhost:8080/")
        print(response.text)
    except Exception as e:
        print(e)
