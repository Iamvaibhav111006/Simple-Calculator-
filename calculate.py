def calculate(number1, operator, number2):

    if operator == "+":
        return number1 + number2

    elif operator == "-":
        return number1 - number2

    elif operator == "*":
        return number1 * number2

    elif operator == "/":
        return number1 / number2

    elif operator == "%":
        return number1 % number2

    elif operator == "**":
        return number1 ** number2

    else:
      return("operator not available")
number1 = int(input("Enter first number: "))
operator = input("Enter operator: ")
number2 = int(input("Enter second number: "))

   

result = calculate(number1, operator, number2)

print("Result:", result)