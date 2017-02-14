class A(object):
    def __init__(self, v):
        self.v = v
    
    def __add__(self, i):
        self.v += i
        return self

    def __sub__(self, i):
        self.v -= i
        return self
    
    def __mul__(self, i):
        self.v *= i
        return self

    def __truediv__(self, i):
        self.v /= i
        return self

    def __str__(self):
        return str(self.v)

a = A(10)
print(a / 10)