import sys
import json

from urllib.request import urlopen

def requestLogs(domain):
    return 200

def get_domains_from_json(file_data):
    json_list = json.loads(file_data)
    answer = get_domains_from_json_list(json_list)
    return answer

def get_domains_from_json_list(json_list):
    my_domain_list = []
    for cert in json_list:
        try:
            domainList = str(cert.get('name_value')).strip()
            for domain in domainList.split("\n"):
                if not domain in my_domain_list:
                    my_domain_list.append(domain)
        except Exception as e:
            print(e)
    my_domain_list.sort()

    return my_domain_list 

def get_domains_from_api(domain):
    my_domain_list = []
    try:
        api_url = "https://crt.sh/?q=%.{}&output=json".format(domain)
        #data = requests.get(api_url)
        data = urlopen(api_url).read()
        json_list = json.loads(data)
        my_domain_list = get_domains_from_json_list(json_list)
    except Exception as e:
        print("error")
        print(e)
    return my_domain_list

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print("usage:  python ct.logs.py domain")
    else:
        domain = sys.argv[1]
        print(domain)
        domain_list = get_domains_from_api(domain)
        for found_domain in domain_list:
            print(found_domain)

