# section02-1
# 파이썬 기초 코딩
# 프린트 구문의 이해

# 기본출력
print('Hello Python!')
print("Hello Python!")
print("""hello python""")
print('''hello python''')

print()

# Separator 옵션 사용 - `,`로 구분된 문자열 간의 공백을 지정 문자열 혹은 문자로 대체

print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')
print("hello world", sep="@")  # 작동하지 않음

print()

# end 옵션 사용 - 끝부분을 바꿔주는 print option
print('Welcome To ', end='')
print('the black parade ', end='')
print('piano note,')

print()

# format option -
you = "you"
me = "Me"
print('{} and {}'.format(you, me), "ㅁㄴㅇㄹㅁㄴㅇㄹ")
print('{0} and {1} and {0}'.format(you, me))
print('{a} and {b}'.format(a=you, b=me))

# %s : 문자열, %d : 정수, %f 실수
print("%s's favorite number is %d" % ('name', 7))

print("Test1: %5d, price: %4.2f" % (776, 56223.1234))
print("Test1: {0: 5d}, price: {1:4.2f}".format(776, 1222223214.2423232))

# escape 문자 - \' \n \"
print("'you'")
print('"you"')
print('\'you\'')
print('\"you\"')
