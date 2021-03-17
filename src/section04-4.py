# Section04-4
# 파이썬 자료구조 Dictionary, Set

# 딕셔너리(Dictionary) : 순서x, 중복x, 수정o 삭제 o

# key, value - json 형식과 비슷함

# 선언
a = {
    'name': "Kim",
    'phone': "010-8888-9999",
    'birth': 870214
}
b = {0: 'Hello Python', 1: "Hello Coding"}
c = {'array': [1, 2, 3, 4, 5]}

print(type(a))
print(a['name'])
print(a.get('name'))  # 이렇게 가져오는게 직접접근보다 안전하다
print(a.get('address'))  # 이런식으로 존재하지 않는 key를 접근 했을 시 error가 아닌 None으로 표현된다.
print(c.get('array')[1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank1'] = [1, 2, 3]
a['rank2'] = (1, 2, 3,)
print(a)

# keys, values, items
print(a.keys())
# print(a.keys()[1:3])  # 표기는 List 형식이지만 List가 아니기 때문에 슬라이싱이 되지않는다.
print(list(a.keys())[1:3])

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))

print(2 in b)  # key를 조건으로 조회한다.
print('name' in a)
print('Kim' in a)

# 집합(Set) 순서 x, 중복x 주로 튜플이나 리스트로 변환해서 사용함
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])
d = {1, 2, 3, 4}

print(type(a))
print(c)
print(type(d))

t = tuple(b)
print(t)

lists = list(b)
print(lists)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))  # 교집합
print(s1 & s2)  # 교집합

print(s1 | s2)  # 합집합
print(s1.union(s2))  # 합집합

print(s1 - s2)  # 차집합
print(s1.difference(s2))  # 차집합

# 추가 & 제거
s3 = set([7, 8, 9, 10, 15])
s3.add(18)
print(s3)
s3.remove(7)
print(s3)