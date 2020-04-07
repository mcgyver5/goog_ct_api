import timeit
code_to_test = """
import requests
domain = "python.org"
api_url = "https://crt.sh/?q=%.{}&output=json".format(domain)

data = requests.get(api_url)

import json
json_list = json.loads(data.text)
new_list = []
for cert in json_list:
    domains = cert['name_value'].split('\\n')
    for domain in domains:
        if not domain in new_list:
            new_list.append(domain)
new_list.sort()
#for d in new_list:
#    print(d)
"""

elapsed = timeit.timeit(code_to_test,number = 10)/10
print(elapsed)
