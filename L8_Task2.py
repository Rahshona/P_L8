class DivNaZero():
    def __init__(self, div_er, den_or):
        self.div_er = div_er
        self.den_or = den_or

    @staticmethod
    def div_by_zero(div_er, den_or):
        try:
            return div_er / den_or
        except:
            return 'Err. We can not'


d = DivNaZero(11, 110)
print(DivNaZero.div_by_zero(110, 0))
print(DivNaZero.div_by_zero(110, 0.01))
print(d.div_by_zero(1100, 0))