# class Person:
#     def __init__(self, n, s):
#
#         self.name = n
#         self.surname = s
#
#
# p1 = Person("Sam", "Baker")
# print(p1.name, p1.surname)
class Date():
    month = ['январь', 'февраль',]

    def __init__(self, day, month, year):

        self.day = day
        self.month = month
        self.year = year
        self.month_name = Date.month[month - 1]

