# Addition

num1 = float(input("Enter First Number for Addition: "))
num2 = float(input("Enter Second Number for Addition: "))

add_result = num1 + num2

print(f"Addition: {num1}+{num2} = {add_result}\n")

# Division

num3 = float(input("Enter the Dividend for Division: "))
num4 = float(input("Enter the Divisor for Division: "))
if num4 == 0:
    print("Error:Division by zero is not possible")
else:
    div_result = num3/num4
    print(f"Division: {num3} / {num4} = {div_result}")

