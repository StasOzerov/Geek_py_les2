
# p 5 ------------------------------------------------------

my_list = [7, 5, 3, 3, 2]
print("Текущий рейтинг:\n", my_list)

while True:
    a = input("Введите натуральное число:\n")
    if a.isdigit():
        a = int(a)
        my_list.append(a)
        my_list.sort(reverse = True)
        print("Обновлённый рейтинг:\n", my_list)
        continue
    print("Неверно")
