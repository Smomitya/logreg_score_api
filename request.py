import requests
import sys

x = sys.argv[1]
y = sys.argv[2]
r = requests.get(url = "http://localhost:8000/get_score/", params = {"x": x, "y": y})
print(r.json())