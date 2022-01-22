import re
import requests
import const
import datetime
import json

 
def query_cve_created_date(cve):
    url = f"{const.CVE_BASE_URL}{cve}"
    res = requests.get(url, headers=const.HEADERS_GET).text
    with open('cve.html', 'w+', encoding='utf-8') as f:
        f.write(res)
    m = re.search('<b>(\d{8})<', res)
    if m:
        print(m.group(1))
        created_date = datetime.datetime.strptime(m.group(1), '%Y%m%d')
        return created_date
    else:
        print(f'[Error] Fail to get added date for {cve}.')
        return None

def get_known_exploits():
    try:
        with open(const.KNOWN_EXPLOITS_FILE) as f:
            data = json.load(f)
            return data
    except:
        print(f'[Error] Fail to read {const.KNOWN_EXPLOITS_FILE} into json obj')
        raise