'''
    컬렉션(collection)
        변수 하나에 여러개의 값을 저장해서 관리
        List / Set / Tuple / Dictionary
'''
'''
    List
        데이터를 원하는 만큼 여러개 저장
        1. 중복된 데이터가 저장
        2. 데이터를 추가한 순서가 보장
        3. 추가, 삭제, 수정이 가능
'''
# List 생성
list1 = [1,1,'Hello',4,5,True,'World']
print(list1)
# List도 인덱스 번호를 이용해서 데이터를 하나씩 뽑을 수가 있음 (0, 1, 2, ...)
print(list1[0])
print(list1[2])
print(type(list1[-2]))
print(list1[-5])
# print(list1[7]) --> out of range error

# 리스트 1번 ~ 4번 인덱스 추출
print(list1[1:5])

# 추출한 리스트를 새 리스트로 생성
# 기존 리스트 내용은 그대로 유지됨
list2 = list1[1:5]
print(list1, list2)

# 리스트의 마지막 데이터 2개 추출
print(list1[-2:])

# 추가 / 삭제 / 수정
# List에 데이터 추가 : 맨 뒤에 추가
list1.append('Test')
list1.append(100)
print(list1)
# 3번 인덱스에 데이터를 끼워 넣기 -> 한칸씩 뒤로 밀림
list1.insert(3,111)
print(list1)

# 수정
list1[3] = 'Hello'
print(list1)
# 6번 인덱스 값을 'Hello'로 수정
list1[6] = "Hello"
print(list1)

# 삭제
# pop : 인덱스 번호에 해당하는 데이터를 삭제, 인덱스 생략 시 마지막 데이터 삭제
# 맨마지막 데이터를 삭제
list1.pop()
print(list1)
# 해당 인덱스 데이터를 삭제
list1.pop(1)
print(list1)

# 데이터를 검색하여 삭제
list1.remove('Test')
print(list1)
# 중복데이터가 있을 시, 최초 검색된 1개 데이터만 삭제
list1.remove('Hello')
print(list1)
# 데이터의 인덱스 번호 검색
print(list1.index('World'))
# print(list1.index('Test')) --> 데이터가 없으면 error

# 전체 데이터 삭제
print(len(list1))
list1.clear()
print(list1)
print(len(list1))


