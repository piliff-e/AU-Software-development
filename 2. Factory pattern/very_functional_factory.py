#!/usr/bin/env python

"""
CALCULATOR using a Factory pattern in a (very) Functional style
"""

import re


# Словарь, сопоставляющий символы операций функциям
operators = {
    '+': lambda a, b: a + b,  # Сложение
    '-': lambda a, b: a - b,  # Вычитание
    '*': lambda a, b: a * b,  # Умножение
    '/': lambda a, b: a / b if b != 0 else ZeroDivisionError("Division by zero"),  # Деление (с проверкой деления на ноль)
    #'#': lambda  a, b: a//b if b != 0 else ZeroDivisionError("Division by zero") -- Тестирование паттерна
    # '^': lambda a, b: a ** b  # Возведение в степень (закомментировано)
}


# Функция для разбора выражения и выполнения вычислений
def calculate(operators):
    # Динамическое формирование строки приглашения на основе операций, доступных в словаре operators
    prompt = "This calculator supports only "
    prompt += ', '.join(operators.keys())
    prompt += ".\nIt can only be used for two numbers.\nEnter expression to calculate: "

    # Получение ввода от пользователя
    line = input(prompt)

    # Использование регулярного выражения для разбиения ввода на операнды и оператор
    match = re.match(r'(\d+)\s*([-+*/^#])\s*(\d+)', line)
    if match:
        # Извлекаем операнды и оператор
        operand1 = float(match.group(1))
        operator = match.group(2)
        operand2 = float(match.group(3))

        # Получение функции операции из словаря operators
        operation_func = operators.get(operator)
        if operation_func:
            # Выполнение вычислений
            result = operation_func(operand1, operand2)
            return f'Result: {result}'
        else:
            return f'Unsupported operation: {operator}'
    else:
        return "Invalid input format"


# Каррирование для создания функции с предопределенными операторами
def calc_with_operators(operators):
    return lambda: calculate(operators)


# Тестирование калькулятора
calc = calc_with_operators(operators)
print(calc())
