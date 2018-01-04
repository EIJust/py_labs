import re
import requests


URL = 'http://mosigra.ru'


def get_emails_from_resp(resp):
    regex = "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    return set(re.findall(regex, resp.text))


if __name__ == '__main__':
    r = requests.get(URL)
    print(get_emails_from_resp(r))
