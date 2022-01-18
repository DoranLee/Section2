s = 'maple'
print(len(s))
print(len(s)/2)
print(len(s)//2)

# / : 소수점 O
# // : 소수점 X (나누기 몫만 표시)

n = len(s)
i = (n-1)/2
print(n)
print(i)
print(s,'의 가운데 글자는', s[int(i)],'입니다.')

i = n//2
print(s,'의 가운데 글자는', s[i],'입니다.')