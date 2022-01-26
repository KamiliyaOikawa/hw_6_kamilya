u = [-1, 0, 1, 2, -1, -4]

class Oikawa:
    def sum(self, numbers, desired_sum):
        required = {}
        for i in range(len(numbers)):
            if desired_sum - numbers[i] in required:
                return [required[desired_sum - numbers[i]], i]
            else:
                required[numbers[i]] = i


p = Oikawa()
u = [-1, 0, 1, 2, -1, -4]
print(p.sum(u, 0))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
# desired_sum = int(input())
