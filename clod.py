import requests
import json
domain = "dhs.state.mn.us"
api_url = "https://crt.sh/?q=%.dhs.state.mn.us&output=json"

data = requests.get(api_url)

json_list = json.loads(data.text)
new_list = []
for cert in json_list:
    if not cert in new_list:
        new_list.append(cert)
new_list.sort()
for d in new_list:
    print(d['name_value'])

