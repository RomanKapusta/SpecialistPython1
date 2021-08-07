# Дан треугольник со сторонами a, b и c. Определите, является ли он равнобедренным.
# Формат входных данных: дано три натуральных числа. Гарантируется, что отрезки с данными длинами образуют треугольник.
# Формат выходных данных: Выведите «YES», если треугольник равнобедренный, и «NO» в противном случае.

# TODO: your code here

number_a = int(input("a ="))
number_b = int(input("b ="))
number_c = int(input("c ="))

if number_a == number_b and number_b == number_c and number_c == number_a:
    print ("Yes",)
else:
    print ("No",)
