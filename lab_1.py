import re
import requests


URL = 'http://mosigra.ru'


if __name__ == '__main__':
    r = requests.get(URL)
    regex = "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    emails = re.findall(regex, r.text)
    print(emails)
