# input the base and height from the user
base = float(input("Enter the length of the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
# calculate the area of triangle
area1 = base * height / 2 # method 1
area2 = 0.5 * base * height
# display the result
print(f"the area of the triangle is: {area1}")
print(f"the area of the triangle is: {area2}")