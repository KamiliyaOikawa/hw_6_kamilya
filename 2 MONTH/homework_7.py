class Sort:
    def __init__(self, numbers=list):
        self.numbers = numbers

    def divide(self, lst):
        if len(lst) <= 1:
            return lst
        element = lst[0]
        left = list(filter(lambda num: num < element, lst))
        center = [nums for nums in lst if nums == element]
        right = list(filter(lambda num: num > element, lst))

        return self.divide(left) + center + self.divide(right)

    def quick_sort(self):
        if len(self.numbers) <= 1:
            return self.numbers
        element = self.numbers[0]
        left = list(filter(lambda num: num < element, self.numbers))
        center = [nums for nums in self.numbers if nums == element]
        right = list(filter(lambda num: num > element, self.numbers))

        return self.divide(left) + center + self.divide(right)

    def __str__(self):
        return f'List of numbers: {self.numbers}\n'


num = Sort(numbers=[7, 45 , 4, 1, 6, 99, 12, 14, 55, 123, 22, 1, 90])
print(num)
print(num.quick_sort())

# 2 задание
n = int(input('Введите трехзначные число: '))
d1 = n % 10
d2 = n % 100 // 10
d3 = n // 100
if d1 == d3:
    print('Ваше число уникальное.')
else:
    print('Ваше число НЕ уникальное.')
