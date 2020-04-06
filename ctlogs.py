import json
import requests

def requestLogs(domain):
    return 200

def get_domains_from_json(file_data):
    my_list = []
    json_list = json.loads(file_data)
    for cert in json_list:
        try: 
            w = str(cert.get('name_value'))
            x,y = w.split("\n")
            my_list.append(str(x))
        except:
            x = ""
    answer = list(set(my_list))
    answer.sort()
    return answer

def get_domains_from_json_list(json_list):
    my_list = []
    for cert in json_list:
        try:
            domainList = str(cert.get('name_value'))
            for domain in domainList.split("\n"):
                if not domain in my_domain_list:
                    my_domain_list.append(domain)
        except Exception as e:
            print(e)
        return my_domain_list 

def get_domains_from_api(domain):
    my_domain_list = []
    try:
        api_url = "https://crt.sh/?q=%.{}&output=json".format(domain)
        print(api_url)
        data = requests.get(api_url)

        json_list = json.loads(data.text)
        my_domain_list = get_domains_from_json_list(json_list)
    except Exception as e:
        print("error")
        print(e)
    return my_domain_list

'''
            
def get_domains_from_api(domain):
    my_domain_list = []
    try:
        api_url = "https://crt.sh/?q=%.{}&output=json".format(domain)
        print(api_url)
        data = requests.get(api_url)

        json_list = json.loads(data.text)
        new_list = []
        for cert in json_list:
            domainList = str(cert['name_value']).strip()
            for domain in domainList.split("\n"):
                if not domain in my_domain_list:
                    my_domain_list.append(domain)
        my_domain_list.sort()

    except Exception as e:
        print("error")
        print(e)
    return my_domain_list
  
'''
