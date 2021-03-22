# Section09
# 파일 읽기 쓰기
# 읽기 모드: r 쓰기모드 w 추가모드 a
# .. 상대경로, .: 절대경로

# 예제1 파일 읽기

from random import randint

f = open("./src/resource/review.txt", 'r')
content = f.read()
print(content)
print(f.__dir__())
f.close()

# 예제 2
# with를 쓰면 알아서 close됨
with open('./src/resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(f))

# 예제3
with open('./src/resource/review.txt', 'r') as f:
    for c in f:
        print("C____", c)

with open('./src/resource/review.txt', 'r') as f:
    content = f.read()
    print('>', content)
    content = f.read()
    print('>', content)

with open('./src/resource/review.txt', 'r') as f:
    line = f.readline()
    # print(line)
    while line:
        print(line, end='### ')
        line = f.readline()

print()

with open('./src/resource/review.txt', 'r') as f:
    content = f.readlines()
    print(content)
    for c in content:
        print(c, end="@@@@@@")

print()
score = []
with open("./src/resource/score.txt", 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)

print("Avg : {:6.3}".format(sum(score) / len(score)))

with open("./src/resource/test1.txt", 'w') as f:
    f.write("nice man\n")

with open("./src/resource/test1.txt", 'a') as f:
    f.write("Good man\n")

with open("./src/resource/test1.txt", 'w') as f:
    for cnt in range(6):
        f.write(str(randint(0, 50)))
        f.write("\n")

with open("./src/resource/test2.txt", 'w') as f:
    name_list = ["kim\n", "park\n", "cho\n"]
    f.writelines(list)  # 리스트 파일로 저장

with open("./src/resource/test3.txt", 'w') as f:
    print("test contest!!", file=f)
    print("test contest!!2", file=f)
