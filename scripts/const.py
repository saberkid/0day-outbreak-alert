GOOGLE_API_KEY = "AIzaSyDLeOLUe7jLTakzcXZ6lfxhOEr7dondwcQ"
GOOGLE_NEWS_SEARCH_ENG = "f5465c81af33ec09c"

HEADERS_GET = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

CVE_BASE_URL = "https://cve.mitre.org/cgi-bin/cvename.cgi?name="

KNOWN_EXPLOITS_FILE= "known_exploited_vulnerabilities.json"

MONITORING_DAYS = 30
REQUEST_INTERVAL = 2