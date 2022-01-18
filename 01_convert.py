'''
    데이터 타입
        1. 정수형 : int
        2. 문자열 : str
        3. 실수형 : float
        4. 논리형 : bool

    데이터 형변환 : 데이터 타입을 다른 데이터 타입으로 변경
    1. 정수로 변환
        - int(1.9) --> 1  (소수점 이하 제거)
        - int('200') --> 200  (문자열을 숫자로 변환)
        - int('3.1415') --> error  (문자열이 정수가 아님)
        - int(True) --> 1, int(False) --> 0
'''
print(int(1.9))
print(int(-1.9))
print(int('200'))
# print(int('3.1415'))
print(int(True))
print(int(False))

'''
    2. 실수로 변환
        - float(20) --> 20.0
        - float('3.1415') --> 3.1415
        - float('20') --> 20.0
        - float(False) --> 0.0, float(True) --> 1.0
'''
print(float(20))
print(float('3.1415'))
print(float('20'))
print(float(True))
print(float(False))

# ctrl + D : 윗라인 복붙
# ctrl + shift + 방향키 : 라인 옮기기
# shift + del : 라인 삭제

'''
    3. 문자열로 변환
        - str(값) 
'''
print(str(111))
print(type(str(3.1415)))
print(str(True))

'''
    4. 논리값으로 변환
        - bool(0) --> False
        - bool(0이 아닌 숫자) --> True
        - bool(문자열) --> True
        - bool('') --> False 
'''
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool('0'))
print(bool('False'))
print(bool(''))

