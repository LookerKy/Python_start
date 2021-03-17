# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

# for a1 in q1.items():
#     if a1[0] == "가을":
#         print(a1[1])

print(''.join([q1[s] for s in q1 if s == '가을']))

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

# [true value for x in dict if else]
bi = [q2[x] for x in q2 if x == "여름" or x == "봄"]
print(bi)
hasApple = ['사과다' for key, val in q2.items() if key == "사과" or val == "사과"]
print(hasApple)

if len(hasApple) > 0:
    print("has apple")
else:
    print("non apple")

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

score = [100, 28, 57, 10, 46, 80]

for s in score:
    if s >= 81:
        print("A")
    elif s >= 61:
        print("B")
    elif s >= 41:
        print("C")
    elif s >= 21:
        print("D")
    else:
        print("E")

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
three_num = [12, 6, 18]
best = three_num[0]
a = 18
b = 6
c = 12
max(a, b, c)
best = a
if b > a:
    best = b
if c > best:
    best = c

print(best)

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
id_num1 = "911212-1000000"
id_num2 = "911212-2000000"

if int(id_num1[7]) % 2 == 0:
    print("여자")
else:
    print("male")

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for ss in q3:
    if ss == "정":
        continue
    print(ss)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for x in range(1, 101):
    if x % 2 == 1:
        print(x, end=" ")

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
print()
for x in q4:
    if len(x) > 4:
        print(x, end=" ")

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

print()

for x in q5:
    if x.islower():
        print(x, end=" ")

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
print()

for x in q6:
    print(x.upper(), end=" ") if x.islower() else print(x.lower(), end=" ")
