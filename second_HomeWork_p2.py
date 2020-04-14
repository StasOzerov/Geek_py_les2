
# p 2 ------------------------------------------------------

list = []

while True:
    element = input("Введите элемент массива:\n")
    if element.isdigit():
        element = int(element)
    if element == 0:
        list.append(element)
        break
    list.append(element)

print(list)

l = len(list)

if l % 2 == 1:
    l -= 1

i = 0
while l:
    list[i], list[i+1] = list[i+1], list[i]
    i += 2
    if i == l:
        break

print(list)

