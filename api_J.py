import requests
import json

resp = requests.get('http://ip-api.com/json/208.80.152.201')
print(json.loads(resp.content))