# Section04
# 파이썬 데이터 타입

v_str1 = "Niceman"
v_bool = True  # 1
v_str2 = "Good boy"
v_float = 10.3
v_int = 7
v_dict = {
    "name": "Kim",
    "age": 25
}
v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {8, 9, 10}

print(type(v_tuple))
print(type(v_set))
print(type(v_float))
print(type(v_list))

# 연산자
i1 = 39
i2 = 939
big_int1 = 999999999999999999999999999999999
big_int2 = 888882934234234023849023840238409238
f1 = 1.234
f2 = 3.784
f3 = 0.234
f4 = 10.

print(i1 * i2)
print(f1 ** f2) # 제곱
print(big_int1 * big_int2)
print(i2 % i1)
print(i2 // i1)
print(i2 / i1)

result = f3 + i2
print(result, type(result))

# 형변환 - int, float, complex(복소수), str
a = 5.
b = 4
c = 6
s = str(6)
print(type(a), type(b))
result2 = a + b
print(result2, type(result2))
print(int(result2))
print(float(b + c))
print(s)
print(type(s))

# 수치 연산 함수
# https://docs.python.org/3/library/math.html

print(abs(-7))  # 절대값
n, m = divmod(100, 8)  # 몫 나머지를 각각의 변수에 할당
print(n, m)

import math

print(math.ceil(5.1))  # 파라미터에 들어간 수보다 크면서 가장 작은정수 (올림)
print(math.floor(3.874)) # 내림 함수
