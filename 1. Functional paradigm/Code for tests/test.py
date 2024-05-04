# global_variable = 0

# def impure_function(x):
#     global global_variable
#     global_variable += x
#     return global_variable

# print(impure_function(5))  # Вывод: 5
# print(impure_function(5))  # Вывод: 8

# def pure_function(x, y):
#     return x + y

# print(pure_function(5, 3))
# print(pure_function(5, 3))

# add_one = lambda x: x + 1
# print(add_one(5))  # Вывод: 6

# def f(x):  # первого класса
#     return x + 3

# def g(function, x):  # высшего порядка
#     return function(x) * function(x)

# print(g(f, 7))  # Вывод: 100

# def factorial_with_loop(n):
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result

# def factorial_with_recursion(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial_with_recursion(n - 1)
    
# global_variable = 0

# def impure_function(x):
#     global global_variable
#     global_variable += x
#     return global_variable

# print(impure_function(5))  # Вывод: 5
# print(impure_function(5))  # Вывод: 10

# def pure_function(x, y):
#     return x + y

# print(pure_function(5, 3))  # Вывод: 8
# print(pure_function(5, 3))  # Вывод: 8

# a = 202  # переменная
# def foo(x, y):
#     return x + y
# ''' Единая арифметика '''
# sum_int = foo(7, 1)
# sum_float = foo(2.4, 0.03)
# print("Hello, world!")
# print(12)
# print(foo(2, 5))
# if a != b:
#     print(0)
# elif a == b:
#     print("1")

#     array = [1, 2, "hehe", True]

# target = []
# for item in source_list:
#     trans1 = G(item)
#     trans2 = F(trans1)
#     target.append(trans2)

# compose2 = lambda A, B: lambda x: A(B(x))
# target = map(compose2(F, G), source_list)


print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
summ = 1095
pages = 0
a = 1
print(summ, a, pages)
while summ > 0:
    summ -= a
    a += 1
    pages += 1
    print(summ, a, pages)
print(pages)