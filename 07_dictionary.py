'''
    딕셔너리(dict)
        데이터1 - 데이터2 "한 쌍"으로 저장
        ㄴ> key(비밀번호/키값) - value(금고 속 내용물/저장할 값)
        키값을 이용해서 데이터를 읽기, 저장, 삭제, 수정
        키값은 중복 안 됨, 저장할 값은 중복 가능
'''
# 딕셔너리 생성 ( Key : Value )
dict1 = {'홍길동':20, '김철수':44, '이영희':35}
print(dict1)
# 키 값이 홍길동에 해당하는 값을 읽어옴
# 딕셔너리변수[키값] --> 키값에 해당하는 밸류값을 읽어옴
print(dict1['홍길동'])
print(dict1['김철수'])
# print(dict1['김영희']) --> KeyError

# 중간에 에러가 발생하면 프로그램이 바로 종료
print('프로그램 끝')

# 딕셔너리 생성2
dict2 = dict(ab431 = 'Test', 메롱 = False)
# dict 내 키값은 문자로 자동변환 --> '' 넣지 않아도 됨
print(dict2['ab431'])
print(dict2['메롱'])

# 데이터 추가
dict1['김영희'] = 99
print(dict1)

dict2.setdefault('C','Hello')
print(dict2)

# 데이터 변경
dict1['김철수'] = 99
print(dict1)
dict2['A'] = 3.14
print(dict2)
# 수정할 키값이 없으면 새로 데이터 추가
dict1['메론'] = 88
print(dict1)

# 데이터 삭제
dict1.pop('김철수') #해당 키값 데이터 삭제
# dict1.pop('김철수') --> 삭제할 키값이 없으면 Error
print(dict1)
dict1.popitem() #맨 마지막 키값에 해당하는 데이터 삭제
print(dict1)

