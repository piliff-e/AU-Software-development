#!/usr/bin/env python

"""
CALCULATOR using a Factory pattern in a Functional style
"""

import re


def summ(a, b):
    return a + b


def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def pwr(a, b):
    return a ** b


operators = {
    '+': summ,
    '-': sub,
    '*': mult,
    '/': div,
    '^': pwr
}


# Generic operation function factory
def operation_factory(line, operators):
    # Construct the regex pattern dynamically based on the operators
    pattern = r'(\d+)\s*(' + '|'.join(re.escape(op) for op in operators.keys()) + r')\s*(\d+)'
    match = re.match(pattern, line)
    if match:
        # Extract operands and operator
        operand1 = float(match.group(1))
        operator = match.group(2)
        operand2 = float(match.group(3))

        operation_func = operators.get(operator)
        if operation_func:
            # Perform the calculation
            result = operation_func(operand1, operand2)
            return f'Result: {result}'
        else:
            return f'Unsupported operation: {operator}'
    else:
        return "Invalid input format"


# Function to parse and perform calculation
def calc():
    # Construct the prompt string dynamically based on the operators
    prompt = "This calculator supports only "
    prompt += ', '.join(operators.keys())
    prompt += ".\nIt can only be used for two numbers.\nEnter expression to calculate: "
    line = input(prompt)
    return operation_factory(line, operators)


# Test the calculator
print(calc())

'''
    In this modified version, the operation_factory() function acts as the factory,
    which takes the operator as input and returns the corresponding operation function. 
    The input_calc() function then uses this factory to get the appropriate operation function
    based on the operator extracted from the input string. This implementation follows the factory 
    pattern by dynamically creating operation functions based on the input operator.
    '''

'''
In this refactored version, the operation_factory function serves as a generic factory that 
dynamically generates operation functions based on the provided operator. It raises a ValueError 
if an unsupported operator is provided. This approach enhances the factory-like behavior of your 
code by centralizing the operation function creation process and simplifying the overall structure.
'''
