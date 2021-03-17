# Section04-2
# 문자열, 문자열 연산, 슬라이싱

# 문자열 선언
str1 = "I am a Boy"
str2 = "Nice man"
str3 = ""
str4 = str()

print(len(str1), len(str2), len(str3), len(str4))

# escape 문자열

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw string - 있는 그대로 표현
raw_s1 = r'/User/ino/Project/Python3'
print(raw_s1)
raw_s2 = r'\\a\\a'
raw_s3 = '\\a\\a'
print(raw_s2)
print(raw_s3)

# multi line
multi_str = \
    """
    hello
    hi
    hi
    """
print(multi_str)

# 문자열 연산
str_o1 = "*"
str_o2 = "abc"
str_o3 = "def"
str_o4 = "Niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)
# print(str_o1 + 3)  # error
print(str_o2 * 3)
print('a' in str_o4)
print('z' not in str_o4)
print('Nice' in str_o4)

# 형 변환
print(str(77) + 'a')
print(str(10.4))

# 문자열 함수
# https://www.w3schools.com/python/python_ref_string.asp

a = 'Orange'
b = 'nice man'

print(a.islower())
print(b.endswith('e'))
print(b.endswith('n'))
print(b.capitalize())
print(a.replace("Oran", "good"))
print(list(reversed(a)))


# slice
d = "niceman"
f = "orange"

print(d[0:3])
print(d[0:4])
print(d[0:len(d)])
print(d[:4])
print(f[:])
print(f[0:4:2])  # 점프 슬라이싱
print(f[1:-2])
print(f[::-1])
