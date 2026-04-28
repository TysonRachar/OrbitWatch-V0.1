import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # throws error if status != 200

    users = response.json()

    for user in users:
        print(user["name"])
        print("-------------------+")
        print(user["email"])

except requests.exceptions.RequestException as e:
    print("Request failed:", e)