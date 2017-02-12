

# 해당 모듈은 url파싱에 필요한 기능을 제공하는 모듈입니다.
-----

## parse.py
1. 구현 기능
    * 최상위 url 가져오기
    * 패스 가져오기
    * 쿼리 스트링 가져오기
    * 쿼리 스트링 파싱
    * 해당 링크 마지막에 존재하는 /,?와 같은 특수문자 제거

2. `테스트 코드 실행`

```
python ./test/test.py
```


3. 해당 코드에서 사용되는 테스트 url들
    * "http://www.naver.com/"
    * "http://www.naver.com"
    * "http://www.naver.com/path1"
    * "http://www.naver.com/path1?"
    * "http://www.naver.com/path1/path2"
    * "http://www.naver.com/path1/path2/"
    * "http://www.naver.com/p?a=10&b=12"
    * "http://www.naver.com/p?a=10&b=12&c="
    * "?a=10&b=12"
    * "a=10&b=12"


## category.py

1. 모듈 설명
	해당 모듈은 메인 페이지에서 카테고리의 정보를 dictionary로 만들어 주는 모듈입니다.
	
	반환 형태 : 
	
	```
	{'001': 'category1', '002': 'category2' ...}
	```
	
2. 사용방법 
	카테고리의 쿼리스트링을 넘겨주면 해당 쿼리스트링을 딕셔너리로 만들어 줍니다.
	
	```.py
	from category import Category
	
	SHOP_URL = 'http://www.dahong.co.kr'
	QUERY_STRING_KEY = 'a'

	if __name__ =='__main__':
    
    	c = Category(SHOP_URL, QUERY_STRING_KEY)
    	print(c())
	```	
	
3. 출력결과
	
	```
	{'1': 'TOP', '41': 'BIKINI', '5': 'PANTS', '318': 'SHIRTS & BLOUSE', '4': 'DRESS', '6': 'BAG & SHOES', '321': 'SKIRT', '3': 'OUTER', '8': 'ACC', '9': 'INNER'}
	```	
	
	