class Calculator:

    def __add__(self, other):
        return 6 + other

    def __sub__(self, other, number):
        summary = other - number
        return summary

    def __mul__(self, other, number, number1, number2, number3):
        sumurry= other* number* number1* number2* number3
        return sumurry

    def __truediv__(self, other, number):
        summary= other / number
        return summary


    def __len__(self, string_sum):
        return len(string_sum)

calc = Calculator()
print(calc.__add__(6))
print(calc.__sub__(9, 4))
print(calc.__mul__(1, 2, 3, 4, 5))
print(calc.__truediv__(22, 7))
print(calc.__len__('adilet'))
