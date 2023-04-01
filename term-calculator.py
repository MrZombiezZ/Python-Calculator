def calculate(operation, num1, num2):
    if operation == 1:
        return num1 + num2
    elif operation == 2:
        return num1 - num2
    elif operation == 3:
        return num1 * num2
    elif operation == 4:
        if num2 == 0:
            raise ValueError("Cannot Divide By Zero")
        return num1 / num2
    elif operation == 5:
        return num1 ** num2
    elif operation == 6:
        if num1 < 0:
            raise ValueError("Cannot Take The Square Root Of A Negative Number")
        return num1 ** 0.5
    else:
        raise ValueError("Invalid Operation")

try:
    red_text = "\033[91m"
    blue_text = "\033[94m"
    green_text = "\033[92m"
    end_color = "\033[0m"
    operation = int(input(red_text + "Enter The Operation -> "+ blue_text +"(1:Add, 2:Subtract, 3:Multiply, 4:Divide, 5:Power, 6:Square Root): " + end_color))
    num1 = float(input(green_text + "Enter The First Number "+ end_color +": "))
    num2 = float(input(green_text + "Enter The Second Number "+ end_color +": "))
    result = calculate(operation, num1, num2)
    print("Result "+ blue_text +"= " + end_color, result)
except ValueError as err:
    print(err)
