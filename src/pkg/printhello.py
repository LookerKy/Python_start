class PrintHello:
    def __init__(self, name="Lee"):
        self.name = name

    def hello(self):
        print("hello my name is %s" % self.name)

    @classmethod
    def hi(cls, n):
        print(n)

