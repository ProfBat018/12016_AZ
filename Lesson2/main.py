# <editor-fold desc="Part1">

# a = 5
# b = 6

# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
# print(a == b)
# print(a != b)

# a += b  # a = a + b
# </editor-fold>

# <editor-fold desc="Type Casting">

# Explicit type casting
# Implicit type casting

# num1 = bool(input("Enter first number: "))      # Explicit type casting
# num2 = bool(input("Enter second number: "))     # 2
#
# print(num1 + num2)  # Implicit bool to int


# print(str(bool(2)) + str(bool('a')))
# print(bool(2) + bool('a'))

# </editor-fold>

# num1 = int(input())     # 6
# num2 = int(input())     # 3


# if num1 == num2:
#     print(num1)
# elif num1 > num2:
#     print("num1 > num2")
# elif num1 < num2:
#     print("num1 < num2")
# else:
#     print("Error")

# if num1 == num2:
#     print(num1)
# else:
#     if num1 > num2:
#         print("num1 > num2")
#     else:
#         if num1 < num2:
#             print("num1 < num2")
#         else:
#             print("Error")


# num1 = int(input("Enter first num: "))
# num2 = int(input("Enter second num: "))
# num3 = int(input("Enter third num: "))
#
# choice = int(input("Enter your choice:\n"
#                    "1.Biggest\n"
#                    "2.Smallest\n"
#                    "3.Average\n"))
#
# biggest = 0
# smallest = 0
# average = 0

# <editor-fold desc="Example 1">

# if choice == 1:
#     if num2 < num1 > num3:
#         biggest = num1
#     elif num1 < num2 > num3:
#         biggest = num2
#     elif num1 < num3 > num2:
#         biggest = num3
#     print(biggest)
#
# elif choice == 2:
#     if num2 > num1 < num3:
#         smallest = num1
#     elif num1 > num2 < num3:
#         smallest = num2
#     elif num1 > num3 < num2:
#         smallest = num3
#     print(smallest)
#
# elif choice == 3:
#     average = (num1 + num2 + num3) / 3
#
#     print(f"Average is: {average}")
# else:
#     print("Error")

# </editor-fold>

# Example 2
#
# if choice == 1:
#     if num1 > num2 and num1 > num3:
#         biggest = num1
#     elif num2 > num1 and num2 < num3:
#         biggest = num2
#     elif num3 > num1 and num3 > num2:
#         biggest = num3
# elif choice == 3:
#     average = (num1 + num2 + num3) / 3
#
#     print(f"Average is: {average}")
# else:
#     print("Error")

num = 0
if num:
    print(num)
else:
    print("Error")


