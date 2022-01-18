'''
    인덱스(index)
        1. 각 문자마다 부여된 번호
        2. 맨 앞글자부터는 0부터 시작
        3. 맨 뒷글자부터는 -1부터 시작
'''
s = 'Hello'
print(s[0], s[-5]) # H
print(s[1], s[-4]) # e
print(s[2], s[-3]) # l
print(s[3], s[-2]) # l
print(s[4], s[-1]) # o

# s[2] = 'K', print(s) --> error (부분 수정 불가)

num = 100
print(str(num)[0])
print(str(num)[1])
print(str(num)[2])

