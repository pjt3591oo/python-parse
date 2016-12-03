

해당 모듈은 url파싱에 필요한 기능을 제공하는 모듈입니다.
-----


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
