
num_valid_passwords = 0

with open('input_day2.txt') as input_file:
    for line in input_file:
        result = line.split("-")
        index1 = int(result[0])
        index2 = int(result[1].split()[0])

        result = result[1].split(":")
        letter = result[0][-1]
        password = result[1].strip()
        num_occurances = password.count(letter)

        if (password[index1 - 1] == letter and password[index2 - 1] != letter or
            password[index1 - 1] != letter and password[index2 - 1] == letter):
            num_valid_passwords += 1

print(num_valid_passwords)
