class Fibonacci:
    def __init__(self, title="fibonacci"):
        self.title = title

    @classmethod
    def fib(cls, n):
        a, b = 0, 1
        while a < n:
            print(a, end=" ")
            a, b = b, a + b

        print()

    @classmethod
    def fib2(cls, n):
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a + b
        return result
