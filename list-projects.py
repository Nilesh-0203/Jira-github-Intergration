# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = ""

API_TOKEN = ""
auth = HTTPBasicAuth("nkudale939@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))) 
print(json.loads(response.text)[1]["name"])