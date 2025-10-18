"""
Простой модуль калькулятора для выполнения базовых арифметических операций.
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def power(base, exponent):
    # Возведение в степень
    result = 1
    for i in range(exponent):
        result *= base
    return result

def calculate(operation, x, y):
    # Главная функция для вычислений
    if operation == 'add':
        return add(x, y)
    elif operation == 'subtract':
        return subtract(x, y)
    elif operation == 'multiply':
        return multiply(x, y)
    elif operation == 'divide':
        return divide(x, y)
    elif operation == 'power':
        return power(x, y)
    else:
        raise ValueError(f"Unknown operation: {operation}")

# Пример использования
if __name__ == "__main__":
    print("Добро пожаловать в калькулятор!")
    print("Доступные операции: add, subtract, multiply, divide, power")
    
    try:
        op = input("Введите операцию: ")
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        
        result = calculate(op, num1, num2)
        print(f"Результат: {result}")
    
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")