import sys
path = sys.path[0].replace('\\test', '')
sys.path.insert(0, path)

from parse import  last_slice_delete, query_string_parse, get_home_url, get_path, get_query_string
import unittest

class UtilsTest(unittest.TestCase):
    test_url1 = "http://www.naver.com/"
    test_url2 = "http://www.naver.com"

    test_url3 = "http://www.naver.com/path1"
    test_url4 = "http://www.naver.com/path1?"

    test_url5 = "http://www.naver.com/path1/path2"
    test_url6 = "http://www.naver.com/path1/path2/"


    test_url11 = "http://www.naver.com/p?a=10&b=12"
    test_url12 = "http://www.naver.com/p?a=10&b=12&c="

    test_url13 = "?a=10&b=12"
    test_url14 = "a=10&b=12"


    def test_get_home_url(self):
        self.assertEqual(get_home_url(self.test_url1), "http://www.naver.com")
        self.assertEqual(get_home_url(self.test_url2), "http://www.naver.com")
        self.assertEqual(get_home_url(self.test_url3), "http://www.naver.com")
        self.assertEqual(get_home_url(self.test_url4), "http://www.naver.com")
        self.assertEqual(get_home_url(self.test_url5), "http://www.naver.com")
        self.assertEqual(get_home_url(self.test_url6), "http://www.naver.com")
        self.assertEqual(get_home_url(self.test_url11), "http://www.naver.com")
        self.assertEqual(get_home_url(self.test_url12), "http://www.naver.com")
        self.assertEqual(get_home_url(self.test_url13), "")
        self.assertEqual(get_home_url(self.test_url14), "")



    def test_last_slice_delete(self):
        last_slice_delete(self.test_url1)
        last_slice_delete(self.test_url2)
        last_slice_delete(self.test_url3)
        last_slice_delete(self.test_url4)
        last_slice_delete(self.test_url5)
        last_slice_delete(self.test_url6)


    def test_query_string_parse(self):
        self.assertEqual(query_string_parse(self.test_url4), {})
        self.assertEqual(query_string_parse(self.test_url1), {})

        self.assertEqual(query_string_parse(self.test_url11), {"a" : '10', "b" : '12'})
        self.assertEqual(query_string_parse(self.test_url12), {"a" : '10', "b" : '12', "c" : ''})


        self.assertEqual(query_string_parse(self.test_url13), {"a" : '10', "b" : '12'})
        self.assertEqual(query_string_parse(self.test_url14), {"a" : '10', "b" : '12'})

    def test_get_path(self):
        self.assertEqual(get_path(self.test_url1), '/')
        self.assertEqual(get_path(self.test_url2), '')
        self.assertEqual(get_path(self.test_url3), '/path1')
        self.assertEqual(get_path(self.test_url4), '/path1')
        self.assertEqual(get_path(self.test_url5), '/path1/path2')
        self.assertEqual(get_path(self.test_url6), '/path1/path2/')
        self.assertEqual(get_path(self.test_url11), '/p')
        self.assertEqual(get_path(self.test_url13), '')
        self.assertEqual(get_path(self.test_url14), '')
    #
    def test_get_query_string(self):
        self.assertEqual(get_query_string(self.test_url1), '')
        self.assertEqual(get_query_string(self.test_url2), '')
        self.assertEqual(get_query_string(self.test_url3), '')
        self.assertEqual(get_query_string(self.test_url4), '')
        self.assertEqual(get_query_string(self.test_url5), '')
        self.assertEqual(get_query_string(self.test_url6), '')
        self.assertEqual(get_query_string(self.test_url11), 'a=10&b=12')
        self.assertEqual(get_query_string(self.test_url12), 'a=10&b=12&c=')
        self.assertEqual(get_query_string(self.test_url13), 'a=10&b=12')
        self.assertEqual(get_query_string(self.test_url14), 'a=10&b=12')

if __name__ == '__main__':
    unittest.main()