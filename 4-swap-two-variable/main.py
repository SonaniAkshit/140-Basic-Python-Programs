# swap the value using temporary variable,string value allowed in using temporary variable
a = input("Enter value of first variable (a): ") #
b = input("Enter value of second variable (b): ")
temp = a
a = b
b = temp
print(f"swapped using temporary variable: a= {a}, b= {b}\n")

# swap without using temporary variable
#Method 1: Using Arithmetic Operators
a = float(input("Enter value of first variable (a): "))
b = float(input("Enter value of second variable (b): "))
a = a + b
b = a - b
a = a - b
print(f"swapped using Arithmetic Operators: a= {a}, b= {b}\n")

#Method 2: Using XOR Bitwise Operator (Only for integers)
a = int(input("Enter value of first variable (a): "))
b = int(input("Enter value of second variable (b): "))
a = a ^ b
b = a ^ b
a = a ^ b
print(f"swapped using XOR Bitwise Operator: a= {a}, b= {b}\n")

#Method 3: Pythonic Way (Tuple unpacking)
a = int(input("Enter value of first variable (a): "))
b = int(input("Enter value of second variable (b): "))
a, b = b, a
print(f"swapped using Pythonic Way (Tuple unpacking): a= {a}, b= {b}\n")