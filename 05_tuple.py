'''
    튜플(Tuple)
        데이터를 리스트처럼 저장
        데이터를 읽는 방식은 리스트와 동일
        단, 최초에 저장한 데이터만 유지
        데이터 추가, 삭제, 수정 불가
'''
# 튜플 생성
tup1 = (1,41,'Hello', False, 'Test', True)
print(tup1)
tup2 = 2, 52, 'Bye', True, 'Practice', False
print(tup2)
lst = [1, 'Test', True, 100]
tup3 = tuple(lst)
print(tup3)
tup4 = tuple(lst[:2])
print(tup4)
# tup1[0] = 111 --> 수정불가 error
print(tup1[0],tup1[2]) # 리스트와 동일하게 조회는 가능
# 튜플을 리스트로 저장
list1 = list(tup1)
print(list1)
