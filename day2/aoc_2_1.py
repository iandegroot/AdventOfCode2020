
num_valid_passwords = 0

with open('input_day2.txt') as input_file:
    for line in input_file:
        result = line.split("-")
        lower = int(result[0])
        upper = int(result[1].split()[0])

        result = result[1].split(":")
        letter = result[0][-1]
        password = result[1].strip()
        num_occurances = password.count(letter)

        print("lower: {} upper: {} letter: {} password: {} num_occurances: {}".format(lower, upper, letter, password, num_occurances))

        if (num_occurances >= lower and num_occurances <= upper):
            print("Valid!")
            num_valid_passwords += 1

print(num_valid_passwords)
