# section10
# 예외 처리

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크 등

# syntaxError

# print("test)
# if True
#     pass

# NameError : 참조 변수 없음
a = 10
b = 10
# print(c)

# ZeroDivisionError : 0 나누기 에러
# print(10/0)


# indexError : 인덱스 범위 오버
x = [10, 20, 30]
print(x[0])
# print(x[3])


# KeyError

dic = {"name": "Kim", "Age": 33, "City": 'Seoul'}
# print(dic['hobby'])
print(dic.get('hobby'))

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

import time

print(time.time())
# print(time.month()) #error


# Value Error
x = [1, 5, 9]

# x.remove(10)
print(x.index(9))

# FileNotFoundError

# f = open('test.txt', 'r')


# TypeError

x = [1, 2, 3, 4]
y = (1, 2)
z = "test"

# print(x + y)

# print(x + z)

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장 (EAFP 코딩 스타일)


# 예외 처리 기본
# try: 에러가 발생할 가능 성이 있는 코드실 행
# except : 에러명 1
# except : 에러명 2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제 1

name = ['kim', "lee", "Park"]

try:
    z = "kim"  # cho 예외 발생
    x = name.index(z)
    print('{} Found it in name'.format(z, x + 1))
except ValueError:
    print('Not found it! - Occurred ValueError')
else:
    print("Ok! else")

try:
    z = "ㄸ"
    x = name.index(z)
    print('{} Found it in name'.format(z, x + 1))
except:
    print('Not found it! - Occurred Error')
else:
    print("Ok! else")

try:
    z = "ㄸ"
    x = name.index(z)
    print('{} Found it in name'.format(z, x + 1))
except:
    print('Not found it! - Occurred Error')
else:
    print("Ok! else")
finally:
    print("Ok")


# 예제 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print("Type")
finally:
    print('Ok Finally!')


# 예제 5
try:
    z = "ㄸ"
    x = name.index(z)
    print('{} Found it in name'.format(z, x + 1))
except ValueError as l:
    print(l)
except IndexError as i:
    print(i)
except Exception as e:
    print(e)
else:
    print("Ok! else")
finally:
    print('finallyok')


# 예제 6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = "11"
    if a == "kim":
        print("ok")
    else :
        raise ValueError
except ValueError:
    print("problem")
except Exception as e:
    print(e)
else:
    print("ok!!")

