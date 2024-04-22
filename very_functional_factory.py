#!/usr/bin/env python

"""
CALCULATOR using a Factory pattern in a (very) Functional style
"""

import re

# Create a dictionary mapping operation symbols to functions
operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b if b != 0 else ZeroDivisionError("Division by zero")#,
    # '^': lambda a, b: a ** b
}


# Function to parse and perform calculation
def calculate(operators):
    # Construct the prompt string dynamically based on the operators
    prompt = "This calculator supports only "
    prompt += ', '.join(operators.keys())
    prompt += ".\nIt can only be used for two numbers.\nEnter expression to calculate: "

    # Input from user
    line = input(prompt)

    # Use regular expression to split the input into operands and operator
    match = re.match(r'(\d+)\s*([-+*/^])\s*(\d+)', line)
    if match:
        # Extract operands and operator
        operand1 = float(match.group(1))
        operator = match.group(2)
        operand2 = float(match.group(3))

        # Get operation function from operators dictionary
        operation_func = operators.get(operator)
        if operation_func:
            # Perform the calculation
            result = operation_func(operand1, operand2)
            return f'Result: {result}'
        else:
            return f'Unsupported operation: {operator}'
    else:
        return "Invalid input format"


# Currying to create a function with predefined operators
def calc_with_operators(operators):
    return lambda: calculate(operators)


# Test the calculator
calc = calc_with_operators(operators)
print(calc())
