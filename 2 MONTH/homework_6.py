class Oikawa:
    def sum(self, numbers, desired_sum):
        required = {}
        for i in range(len(numbers)):
            if desired_sum - numbers[i] in required:
                return [required[desired_sum - numbers[i]], i]
            else:
                required[numbers[i]] = i


p = Oikawa()
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 20]

print(p.sum(input_list, 20))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
# desired_sum = int(input())
