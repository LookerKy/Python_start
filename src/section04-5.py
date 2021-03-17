# 1
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(len(q1))

# 2
print('\tapple;oragne;banana;lemon')

# 3
print('*' * 100)

# 4
q4 = "30"
str_q4 = str(q4)
comp_q4 = complex(q4)
fl_q4 = float(q4)
int_q4 = int(q4)

# 5
q5 = "Niceman"
q5_index = q5.index("man")
print(q5_index)
print(q5[q5_index : q5_index + 3])
print(q5[4:7])

# 6
q6 = "Strawberry"
print(q6[::-1])

# 7
q7 = "010-7777-9999"
print(q7.replace("-", ""))

# 정규 표현식
import re
print(re.sub("[^0-9]", '', q7))

# 8
q8 = "http://daum.net"
print(q8.replace("http://", ""))

# 9
q9 = "NiceMan"
print(q9.lower())
print(q9.upper())

# 10
q10 = "abcdefghijklmn"
print(q10[2:5])

# 11
q11 = ["Banana", "Apple", "Orange"]
q11.remove("Apple")
print(q11)

# 12
q12 = (1, 2, 3, 4)
l_q12 = list(q12)
print(type(l_q12))

# 13
q13 = {"성인": 10000, "청소년": 70000, "아동": 30000}

# 14
q13["소아"] = 0

# 15
print(q13.keys())

# 16
print(q13.values())
