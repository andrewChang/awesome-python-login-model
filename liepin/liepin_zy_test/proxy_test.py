import requests
from retrying import retry
import json
import jsonpath
import re
from bs4 import BeautifulSoup
import os
import lxml


@retry(stop_max_attempt_number=3)
def parse_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) \
              AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 \
              Safari/537.36"
    }
    proxies = {
        "http": "socks5h://127.0.0.1:3333",
        "https": "socks5h://127.0.0.1:3333"
    }
    response = requests.get(url, headers=headers, verify=True,
                            timeout=2, proxies=proxies)
    return response.text


def json_test():
    # json.loads json字符串 转 Python数据类型
    json_string = '''
    {
        "name": "crise",
        "age": 18,
        "parents": {
            "monther": "妈妈",
            "father": "爸爸"
                }
    }
    '''
    print(f'json_string数据类型={type(json_string)}')
    data = json.loads(json_string)
    print(f'data数据类型={type(data)}')
    json_string2 = json.dumps(data)
    print(f'json_string2数据类型={type(json_string2)}')
    print('*'*100)


def jsonpath_test():
    url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/71.0.3578.98 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    html = response.text
    data = json.loads(html)
    cities = jsonpath.jsonpath(data, '$..allCitySearchLabels..name')
    print(cities)


def pattern_test():
    string = "a;dj jkl,jj;j;sd"
    pattern = re.compile(r'[;,\s]+')
    result = pattern.split(string)
    print(result)


def beautiful_soup_test():
    url = r"https://www.liepin.com/"
    response = requests.get(url=url)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    file_name = "test.txt"
    if os.path.exists(file_name):
        print(f"{file_name} is exists")
    else:
        with open(file_name, "w") as file:
            file.write(soup.prettify(response))
    print(soup.title)


if __name__ == '__main__':
    # url = "https://www.google.com/"
    # try:
    #     html = parse_url(url=url)
    #     print(html)
    # except Exception as e:
    #     print(f'-----------------{e}---------------------------')
    # jsonpath_test()
    # pattern_test()
    beautiful_soup_test()