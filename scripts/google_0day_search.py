import datetime
from urllib import request
from apiclient.discovery import build
import common.const as const
import argparse
import requests
import urllib.parse
import re
import utils


def api_custom_search(search_string, search_engine):
    service = build("customsearch", "v1", developerKey=const.GOOGLE_API_KEY)

    res = {}
    try:
        res = service.cse().list(
            q=search_string,
            cx=search_engine,
        ).execute()
    except Exception as ex:
        print(str(ex))
        print("error: performing google custom search")

    return res

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # note: we are limited to 100 free requests a day...
    parser.add_argument('-k', '--key', help='keyword to search by Google News', default='0day')
    args = parser.parse_args()

    # result = api_custom_search(args.key, const.GOOGLE_NEWS_SEARCH_ENG)
    # print(result.get('queries').get('request')[0].get('totalResults'))

start = datetime.datetime.strptime("20211126", "%Y%m%d")
end = start + datetime.timedelta(days=25)
url_news_search('CVE-2021-44228', start, end)    
    

