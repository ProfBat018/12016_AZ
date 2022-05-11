# def - definition

# def name_of_func():
#   action

# Function must be lowercase.
# Before and after function we should write two row with blank lines


# <editor-fold desc="Part 1">


# def print_hello():
#     print("Hello World")
#
#
# print_hello()

# </editor-fold>

# <editor-fold desc="Part 2">

# def print_even(num):    # num - parameter
#     if num % 2 == 0:
#         print(num)
#
#
# nums = [i for i in range(10)]
#
# print(nums)
#
# for number in nums:
#     print_even(number)

# </editor-fold>

# <editor-fold desc="Part 3">

# def print_even(num):
#     if num % 2 == 0:
#         return num
#
#
# result = print_even(4)
# print(result)

# </editor-fold>

# <editor-fold desc="Part 4">


def add(num1, num2=5):  # default parameter
    return num1 + num2


first_num = int(input("Enter first number: "))    # 5
second_num = int(input("Enter second number: "))  # 10


result = add(first_num, second_num)
print(result)

# </editor-fold>

# <editor-fold desc="Part 5">


# def add(num1=5, num2):  # default parameter
#     return num1 + num2
#
#
# first_num = int(input("Enter first number: "))    # 5
# second_num = int(input("Enter second number: "))  # 10
#
#
# result = add(first_num, second_num)
# print(result)
#
# </editor-fold>



