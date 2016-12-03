import re

#FIXME : 마지막에 존재하는 특수 문제 제거              => last_slice_delete      COMPLETE
#FIXME : 쿼리 스트링 파싱                            => get_query_string_parse COMPLETE

#FIXME : http://naver.com 과 같이 최 상위 url 리턴   => get_home_url        COMPLETE
#FIXME : path부분만 리턴                            => get_path            COMPLETE
#FIXME : 쿼리스트링 리턴                            => get_query_string    COMPLETE


def last_slice_delete(link):
    '''
    Deletes the last special charaters such as [?, /] and etc
    :param url: {string}
    :return: {string}
    '''

    while link[-1] in ['/', '?']:
        link = link[:-1]

    return link


def query_string_parse(link):
    '''
    :param link : {string}
    :return : {dictionary}
    '''

    a = link.split('?')

    if len(a)> 1:
        parses = a[1].split('&')
    else :
        parses = a[0].split('&')

    qs_parse = {}

    for parse in parses:
        parse_split = parse.split("=")
        key = str(parse_split[0])

        if len(parse_split) > 1:
            value = str(parse_split[1])
            qs_parse.setdefault(key, value)

    return qs_parse


def get_home_url(link):
    '''
    http://test.com과 같이 최상위 url 리턴
    :param link : {string}
    :return : {string}
    '''
    home_parse_patter = re.compile('https?:\/\/([a-z0-9\-.]+)')
    home_url = home_parse_patter.search(link)

    if (home_url):
        return home_url.group(0)
    else:
        return ''


def get_path(link):
    path = link.replace(get_home_url(link), '').split('?')[0]

    if '/' in path:
        return path
    else:
        return ''


def get_query_string(link):
    return link.replace(get_home_url(link), '').replace(get_path(link), '').replace('?', '')

