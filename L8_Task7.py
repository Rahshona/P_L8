class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Sum of x_1 and x_2 is:   x = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Product of x_1 and x_2 is:  x = {self.a * other.a + (self.b * other.b)} + {self.b * other.a} * i'


x_1 = ComplexNumber(2, 4)
x_2 = ComplexNumber(5, -8)
print(x_1 + x_2)
print(x_1 * x_2)
