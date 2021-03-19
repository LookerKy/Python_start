# Section08
# 파이썬 모듈과 패키지

#사용 1
from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex2 : ", Fibonacci.fib2(400))

print("ex2: ", Fibonacci().title)


#사용 2
from pkg.fibonacci import *

Fibonacci.fib(10)

print("ex2 : ", Fibonacci.fib2(3))

print("ex2: ", Fibonacci().title)

from pkg.fibonacci import Fibonacci as fb

fb.fib(1000)

print("ex3: ", fb.fib2(1600))


import pkg.culc as c

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))


# 사용 5
from pkg.culc import div as d
print("ex5 : ", int(d(100, 10)))


# 사용 6
import pkg.prints as p
p.print1()
p.print2()


from pkg.printhello import PrintHello

p = PrintHello("hihi")

p.hello()
print(PrintHello("lee kyu young").name)
