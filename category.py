'''
메인 페이지에서 카테고리를 아래의 형타로 만들어서 반환을 해준다
{'1': 'TOP', '41': 'BIKINI', '5': 'PANTS', '318': 'SHIRTS & BLOUSE', '4': 'DRESS', '6': 'BAG & SHOES', '321': 'SKIRT', '3': 'OUTER', '8': 'ACC', '9': 'INNER'}

'''

import requests as rq
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import re


SHOP_URL = 'http://www.dahong.co.kr'
QUERY_STRING_KEY = 'a'


def get_soup(url):
    res = rq.get(url)
    soup = BeautifulSoup(res.content, 'html5lib')
    return soup


class Category:

    def __init__(self, url, query_string_key):
        self.url = url
        self.query_string_key = query_string_key
        self.soup = get_soup(url)
        self.category = {}

        #생성과 동시에 시작
        self.category_analysis()

    def category_analysis(self):
        a_tags = {}

        for query_string_value in range(0, 10):
            search_target = 'a=' + str(query_string_value)
            similar_tags = self.soup.find_all(href = re.compile(search_target))

            for a_tag in similar_tags:
                href = a_tag.get('href')
                category = a_tag.text
                query_string = urlparse(href).query
                query_string_value = parse_qs(query_string)[self.query_string_key][0]
                if category:
                    a_tags.setdefault(query_string_value, category)

        self.category = a_tags

    def __call__(self):
        return self.category


if __name__ =='__main__':
    ''' test '''
    c = Category(SHOP_URL, QUERY_STRING_KEY)
    print(c())