import re
import requests
from lab_1 import get_emails_from_resp


URL = 'http://mosigra.ru'


def get_relative_url_from_resp(main_url, resp):
    return set(re.findall('<a\s+(?:[^>]*?\s+)?href="([^"]*)"', resp.text))


if __name__ == '__main__':
    r = requests.get(URL)
    emails = get_emails_from_resp(r)
    navi_urls = get_relative_url_from_resp(URL, r)
    used_urls = set()
    next_navi_urls = set()

    while True:
        for url in navi_urls:
            print(URL+url)
            r = requests.get(URL+url)
            emails.update(get_emails_from_resp(r))
            new_urls = get_relative_url_from_resp(URL, r)
            next_navi_urls.update(new_urls - used_urls)

        if len(next_navi_urls) == 0:
            break
        used_urls.add(navi_urls)
        navi_urls = next_navi_urls

    print(emails)