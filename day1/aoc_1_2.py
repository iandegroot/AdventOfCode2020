
numbers = []

with open('input_day1.txt') as input_file:
    for line in input_file:
        numbers.append(int(line.strip()))

print(numbers)

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if (numbers[i] + numbers[j] < 2020):
            for k in range(j, len(numbers)):
                if (numbers[i] + numbers[j] + numbers[k] == 2020):
                    print("The numbers are {}, {}, and {}".format(numbers[i], numbers[j], numbers[k]))
                    print("The answer is {}".format(numbers[i] * numbers[j] * numbers[k]))

