#!/usr/bin/env python

"""
CALCULATOR using a Factory pattern in a Functional style
"""

import re


# Определение функций для арифметических операций
def summ(a, b):
    """ Сложение """
    return a + b


def sub(a, b):
    """ Вычитание """
    return a - b


def mult(a, b):
    """ Умножение """
    return a * b


def div(a, b):
    """ Деление (с проверкой деления на ноль) """
    if b == 0:
        raise ZeroDivisionError
    return a / b


def pwr(a, b):
    """ Возведение в степень """
    return a ** b

#Тестирование паттерна Филиппа
#def intdiv(a, b):
#    if b == 0:
#        raise ZeroDivisionError
#    return a // b


# Словарь, сопоставляющий символы операций соответствующим функциям
operators = {
    '+': summ,  # Сложение
    '-': sub,  # Вычитание
    '*': mult,  # Умножение
    '/': div,  # Деление
    #'//': intdiv, TEST
    # '^': pwr  # Возведение в степень (закомментировано)
}


# Фабрика обобщенной функции операции
def operation_factory(line, operators):
    # Динамическое формирование регулярного выражения на основе операторов, доступных в словаре operators
    pattern = r'(\d+)\s*(' + '|'.join(re.escape(op) for op in operators.keys()) + r')\s*(\d+)'
    match = re.match(pattern, line)
    if match:
        # Извлечение операндов и оператора
        operand1 = float(match.group(1))
        operator = match.group(2)
        operand2 = float(match.group(3))

        operation_func = operators.get(operator)
        if operation_func:
            # Выполнение вычислений
            result = operation_func(operand1, operand2)
            return f'Result: {result}'
        else:
            return f'Unsupported operation: {operator}'
    else:
        return "Invalid input format"


# Функция для разбора и выполнения вычислений
def calc():
    # Динамическое формирование строки приглашения на основе операторов, доступных в словаре operators
    prompt = "This calculator supports only "
    prompt += ', '.join(operators.keys())
    prompt += ".\nIt can only be used for two numbers.\nEnter expression to calculate: "
    line = input(prompt)
    return operation_factory(line, operators)


# Тестирование калькулятора
print(calc())
