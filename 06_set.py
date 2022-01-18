'''
    세트(set)
        집합 형태의 자료형
        1. 중복된 데이터가 저장될 수 없음 --> 고유값만 저장
        2. 데이터가 자동정렬됨 --> 저장되는 순서가 없음 (인덱스가 없음)
'''
# set 생성
set1 = {1,2,3,2,3,3,5,6}
print(set1)
list1 = ['A',1,5,1,'B','A']
set2 = set(list1)
print(set2)
# set2를 리스트로 저장
list2 = list(set2)
print(list2)

# 데이터 추가
set2.add(30)
set2.add(30)
print(set2)

# 데이터 삭제
set2.remove(30)
# set2.remove(30) -> 데이터가 없으면 error
print(set2)

set2.discard(7) # 삭제할 데이터가 없어도 error 나지 않음
print(set2)

