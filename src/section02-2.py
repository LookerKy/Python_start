# Section02-2
# 기초 코딩 실습

# import this
import sys

# 파이썬 기본 인코딩은 utf-8이다.
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('hello')

# 변수 선언
myName = 'Good boy'

# 조건문
if myName == 'Good boy':
    print("ok")

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = %d' % (i, j, i * j))

# 변수 선언(한글)
이름 = "좋은사람"
print(이름)


# 함수 선언

def hello():
    print("hello world")


hello()


# 클래스
class Cookie:
    pass


# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))
