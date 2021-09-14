import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes": 10, "name": "Tim", "view": 100000},
    {"likes": 10, "name": "Tim", "view": 100000},
    {"likes": 10, "name": "Tim", "view": 100000},
]
for i in range(len(data)):
    response = requests.put(BASE + "video/1" + str(), data[i])
    print(response)


input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/2")
print(response)
