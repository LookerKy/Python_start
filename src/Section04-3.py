# Section04-3
# 파이썬 List, Tuple

name1 = "lee"
name2 = "park"

# 리스트(순서 o 중복 o 수정o 삭제o)
# 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'pen', 'Banana', "Orange"]
e = [10, 100, ['pen', 'Banana', "Orange"]]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0] + d[1])
print(e[2][1])
print(e[-1][-2])
print(e[-1][1][4])
print('e - ', list(e[-1][1]))


# 슬라이싱
print(d[0:2])
print(e[2][1:3])

# 연산
print(c + d)  # 하나의 리스트로 만들어줌
print(c * 3)  # 리스트의 길이가 늘어남
print(str(c[0]) + 'hi')

# list 수정 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1:3] = [12, 13, 14]
print(c)
c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)
del c[-1]
print(c)
print()
print()

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2, 7)  # index, insert content
print(y)
y.remove(2)  # 리스트 내에 있는 일치하는 내용을 찾아서 삭제
print(y)
y.pop()  # LIFO
print(y)
ex = [88, 77]
y.append(ex)  # 리스트 자체가 삽입됨
y.extend(ex)  # 원소 자체가 끝에 삽입
print(y)

# 튜플 (순서o , 중복o, 수정x, 삭제x)
# 중요 데이터 key값 디비 패스워드 등 수정되거나 삭제되면 프로그램에 영향을 미치는 것을 튜플로 선언함

# 선언
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(a)
print(b)
print(c[2])
print(c[3])
print(d[2][2])

# 슬라이싱
print(d[2:])
print(d[2][0:2])

# 연산
print(c + d)
print(c * 3)

# 튜플 함수
z = (5, 2, 1, 3, 1)

print(z)
print(3 in z)
print(z.index(2))
print(z.count(1))
