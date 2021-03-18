# section06-1
# 함수 및 람다
# 함수는 하나의 기능을 하나의 함수로 만드는 것이 가장 좋다.

# 선언
def hello(world):
    print("hello", world)


hello("python")
hello(7777)


def hello_return(world):
    val = "hello " + str(world)
    return val


str_hello = hello_return("Python!!!!!!!!!!!!")
print(str_hello)


# 다중 리턴
def mul_return(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3


val1, val2, val3 = mul_return(30)
print(val1, val2, val3)


def mul_return2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


lt = mul_return2(100)
print(lt, type(lt))


# *args : 다양한 매개변수를 받아서 프로그래밍을 할때 튜플로 받게해줌 가변 인자


def args_func(*args):
    # print(args)
    # for t in args:
    #     print(t)
    for i, t in enumerate(args):
        print(i, t)


args_func("kim", "park")


# **kwagrs :키워드 파라미터 가변인


def kwargs_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


kwargs_func(name="kim", age=27)


# 혼합
def example_func(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


example_func(10, 20)
example_func(10, 20, "kim", "park", age1=24, age2=25)


# 중첩 함수(클로저)
def nested_func(num):
    def func_in_func(num):
        print('>>>', num)

    print("in func")
    func_in_func(num + 1000)


nested_func(10000)


# 예제 6 힌트
def mul_return3(x: int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


print(mul_return3(5))


# 람다식
# 람다식 : 메모리 절약 가독성 향상 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(heap 초기화) -> 메모리 초기화


# 일반적 함수 -> 변수 할당
def mul_10(num: int) -> int:
    return num * 10


var_func = mul_10
# 객체를 생성하며 메모리에 할당됨
print(var_func, type(var_func))

# 람다 함수 익명함수일때 많이사용함
# lambda parmas : 실행내용
lambda_mul_10 = lambda num: num * 10

print(">>>", lambda_mul_10(10))


def func_final(x, y, func):
    print(x * y * func(10))


func_final(10, 10, lambda_mul_10)

func_final(10, 10, lambda x: x * 1000)


def calc():
    a = 3
    b = 5
    total = 0

    def mul_add(x: int) -> int:
        nonlocal total
        nonlocal a
        if a != 10:
            a = 10
        total2 = 0
        total += x * a + b  # 클로저 밖에 선언한 지역변수는 유지됨 (누적이 가능해짐)
        total2 += x * a + b  # 클로저함수에 선언한 변수는 유지되지 않음
        return total

    return mul_add


c = calc()
print(c(1), c(2))


# 함수 다양한 사

# 다양한 반환 값

# *args, **kwargs

# 람다 함수

# 클로저 문제 1
def counter():
    i = 0

    def count():
        nonlocal i
        i += 1
        return i
    return count


c = counter()
for i in range(10):
    print(c(), end=" ")


print()

print((lambda x: str() if x == 1 else float(x) if x == 2 else x + 10)(5))
