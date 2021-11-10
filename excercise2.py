# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
print("Calculator")
while 1:
    print("Enter the two numbers for the calculation:")
    x = float(input())
    y = float(input())
    print("Enter the operation you want to perform by entering the operator")
    print("+ = (Addition)")
    print("- = (Subtraction)")
    print("* =(Multiplication)")
    print("/ = (Division)")
    print("**=(Power)")
    print("%=(Percent)")
    z = input()
    if x == 45 and y == 3 and z == "*":
        print("The multiplication of", x, "and", y, "is 555")
        break

    if x == 56 and y == 9 and z == "+":
        print("The addition of", x, "and", y, "is 77")
        break

    if x == 56 and y == 6 and z == "/":
        print("The division of", x, "and", y, "is 4")
        break

    if z == "+":
        print("The addition of", x, "and", y, "is:", x + y)
        break

    if z == "-":
        print("The subtraction of", x, "and", y, "is:", x - y)
        break

    if z == "*":
        print("The multiplication of", x, "and", y, "is:", x * y)
        break

    if z == "/":
        print("The division of", x, "and", y, "is:", x / y)
        break

    if z == "**":
        print("The power of", x, "and", y, "is:", x ** y)
        break

    if z=="%":
        print("The percent of", x, "and" , y, "is:",x % y)
    break
