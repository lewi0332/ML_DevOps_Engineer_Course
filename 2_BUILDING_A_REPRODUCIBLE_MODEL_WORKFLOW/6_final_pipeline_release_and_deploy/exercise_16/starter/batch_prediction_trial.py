import requests
import json

with open("/home/derricklewis/Documents/model/input_example.json") as fp:
    data = json.load(fp)

results = requests.post("http://localhost:5000/invocations", json=data)

print(results.json())
