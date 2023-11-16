cube_list = [x ** 3 for x in range(100, 10000)  # 1-е задание
             if x % 3 == 0 and x % 7 == 0
             and str(x)[-1] != '3'
             and str(x)[-1] != '7']
print(cube_list)


##################3
def program():  # 2-е задание
    first_list = []
    second_list = []
    third_list = []

    while True:
        string = input("Введите строку: ")

        if " " in string[-3:]:
            break

        if any(punctuation in string for punctuation in [",", ".", ":", ";"]):
            first_list.append(string[:5])

        if string[0] in ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']:
            second_list.append(string[-3:])

        if len(string) >= 5:
            third_list.append(string[2:5])

    result = [first_list, second_list, third_list]

    print(result)


##############
program()  # <- 3 Задание

s = input()

unique_chars = set(s)

count = len(unique_chars)

print(count)
