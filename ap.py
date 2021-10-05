class MyClass:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def foo1(self):
        return self.a * self.b

    def foo2(self):
        return (self.a * self.b, self.c * self.b) * 2

    def foo3(self):
        return self.a * self.b * self.c
