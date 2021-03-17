# Section05-2

v1 = 1
while v1 < 11:
    print("v1 is: ", v1)
    v1 += 1

for v2 in range(10):
    print(v2)

for v3 in range(1, 11):
    print(v3)

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print(sum1)
print(sum(range(1, 101)))
print(sum(range(1, 101, 2)))

# 시퀀스 (순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 딕셔너리
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

name = ["kim", "Park", "cho", "choi", "yoo"]

for n in name:
    print("you are :", n)

word = "dreams"

for s in word:
    print("word : ", s)

my_info = {
    "name": "kim",
    "age": 33,
    "city": "seoul"
}

# default 는 key
for key in my_info:
    print("my_info : ", key)

for key in my_info.values():
    print("my_info : ", key)

for key in my_info.keys():
    print("my_info : ", key)

for key in my_info.items():
    print("my_info : ", key)

names = "KennRY"

for n in names:
    print(n.lower()) if n.isupper() else print(n.upper())

# break

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 37, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        break
    print(num)

# for-else(반복문이 break에 걸리지 않을 경우에는 else가 동작함)
for num in numbers:
    if num == 33:
        break
    print(num)
else:
    print("not found 33")

# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:  # is는 변수가 같은 object를 가르키면 True == 은 같은 값을 가르키면 True
        continue
    print("타입: ", type(v))

# List Comprehension
# variable = [x for x in range | dict | list if x == 0 ] 내부적으로 append 되어 리스트에 원소들이 추가됨
quit_list = [1, 2, 3, 4, 5, 6, 7]
cp = [x for x in quit_list if x % 2 == 0]
print(cp)
