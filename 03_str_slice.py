'''
    문자열 슬라이스
    형식
    문자열[begin;end;step]
        1) begin : 시작 인덱스, 포함, 생략하면 0부터 시작
        2) end : 종료 인덱스, 불포함, 생략하면 끝까지
        3) step : 증가/감소, 생략하면 1씩 증가
'''
s = 'Hello World'
print(s[0:6])  # 0번 ~ 5번 인덱스
print(s[::])  # 전부 출력
print(s[0:8:2])  # 0번 ~ 7번 인덱스까지 인덱스 번호를 2씩 증가
print(s[:9])  # 0번 ~ 8번 인덱스까지
print(s[-4:])  # 뒤 4글자
print(s[-4:-9])  # 아무 내용 출력 X
print(s[-9:-4])

# len(문자열) : 문자열의 글자수
# len('Hello') --> 5
print(len(s))

tel1 = '02-2072-3404'
tel2 = '1588-5700'

# tel1과 tel2의 뒷번호 4자리만 추출
print(tel1[-4:])
print(tel2[-4:])

# tel1과 tel2의 뒷자리 4자리만 제외하고 추출해서 출력
print(tel1[:-4])
print(tel2[:-4])

# 마이너스 인덱스를 사용하지 않고 추출
print(tel1[:len(tel1)-4])
print(tel2[:len(tel2)-4])
