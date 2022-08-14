num1 = int(input("Enter First Number :"))
num2 = int(input("Enter Second Number :"))

opr = input("What To Do ?!")

match opr:
    case "add":
        result = num1 + num2
    case "subtract":
        result = num1 - num2
    case "multiply":
        result = num1 * num2
    case "divide":
        result = float(num1 / num2)

print(result)