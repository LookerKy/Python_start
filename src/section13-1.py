import random
import time

word = []

n = 1
cor_cnt = 0

with open("./src/resource/word.txt", 'r')as f:
    for c in f:
        word.append(c.strip())

# print(word)

# blocking
input("Ready? Press Enter key")

start = time.time()

while n <= 5:
    random.shuffle(word)
    q = random.choice(word)

    print()

    print("* Question $ {}".format(n))
    print(q)

    x = input()
    print()
    if str(x).strip() == str(q).strip():
        print("Pass!")
        cor_cnt +=1
    else:
        print("Wrong")

    n += 1

end = time.time()
et = end - start
et = format(et, ".3f")

if cor_cnt >= 3:
    print("합격")
else:
    print("불합격")

print("총 게임시간 :", et, "초", "정답 개수 : {}".format(cor_cnt))

if __name__ == '__main__':
    pass
