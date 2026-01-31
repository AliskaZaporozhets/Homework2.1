# number = input("Enter your number: ")
# a = list(number)
#
# print(a[0], end='\n')
# print(a[1], end='\n')
# print(a[2], end='\n')
# print(a[3])

# 7. Виведення числа в стовпчик
# Написати програму, яка просить користувача ввести 4-х значне число з клавіатури,
# після чого друкує на екрані стовпчик цифр, з якого це число складається.
# Наприклад, користувач вводить 1234, а програма виводить:
# 1
# 2
# 3
# 4

number = int(input('Please, enter your number: '))
a = number // 1000
b = (number // 100) % 10
c = (number // 10) % 10
d = (number % 10)

print(a)
print(b)
print(c)
print(d)
