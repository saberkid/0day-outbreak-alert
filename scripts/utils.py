import re
import requests
import const
import datetime
import json
import urllib


def url_news_search(search_string, start, end):
    start_str = datetime.datetime.strftime(start, '%#m/%#d/%Y')
    end_str = datetime.datetime.strftime(end, '%#m/%#d/%Y')
    query_safe_string = urllib.parse.quote_plus(f"cdr:1,cd_min:{start_str},cd_max:{end_str}")
    url = f"https://www.google.com/search?q={search_string}&tbm=nws&tbs={query_safe_string}"
    print(url)
    raw = requests.get(url, headers=const.HEADERS_GET).text
    m = re.search('About (\d.*) results', raw)
    result_num = 0
    if m:
        result_num = int(m.group(1))
    print(f"{search_string} {result_num}")
    return result_num


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