# Section05-1
# 파이썬 흐름제어 제어문
# 조건문 실습

print(type(True))
print(type(False))

# 예
if True:
    print("yes")

if False:
    print("No")

if False:
    print("No")
else:
    print("yes2")

# 관계 연산자
# >, >=, <, <=, == , !=
a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

# 참 거짓 종류 (True, False)
# 참 : 내용이 있는 튜플 문자열 딕셔너리 리스트 1
# 거짓 : 내용이 없는 튜플 문자열 리스트 딕셔너리 0

city = ""
names = ["kim", "Woo"]

if city:
    print(">>>>True")
else:
    print(">>>>False")
if names:
    print(">>>>True")
else:
    print(">>>>False")

# 논리 연산자
# and, or, not
# 산술 > 관계 > 논리 순서로 적용

a = 100
b = 60
c = 15

print('and : ', a > b and b > c)
print('or : ', a > b or c > b)
print("not : ", not a > b)

print("우선순위 : ", 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print("pass")
else:
    print("non pass")

# 다중 조건문
num = 90

if num >= 90:
    print("등급 A : ", num)
elif num >= 80:
    print("등급 B : ", num)
elif num >= 70:
    print("등급 C", num)
else:
    print("non pass")

# 중첩 조건문

age = 27
height = 175

if age >= 20:
    if height >= 170:
        print("A")
    elif height >= 160:
        print("B")
    else:
        print("X")
else:
    print("age X")
