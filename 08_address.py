#메모리 주소 안 바뀌는 형태
# mutable --> list, set, dict
lst = [1,2,3,4,5]
print(id(lst))
lst.append(6)
print(id(lst))
lst.pop(3)
print(lst)
print(id(lst))
# id : RAM 내 해당 데이터가 저장되어 있는 주소
# hdd/ssd(프로그램) --> MainMemory(프로세스)

s = {1,3,4,5}
print(s)
print(id(s))
s.pop()
print(s)
print(id(s))
s.add(100)
print(s)
print(id(s))

# 메모리 주소가 바뀌는 형태
# immutable --> int, float, str, tuple
num = 10
print(num, id(num))
num = 20
print(num, id(num))
num = 10
print(num, id(num))
# --> 10의 주소를 num이 쓰겠다
num += 20
print(num, id(num))
newNum = num  # 동일한 메모리 주소를 저장
print(num, id(num), newNum, id(newNum))
