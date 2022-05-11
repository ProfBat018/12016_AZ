# <editor-fold desc="Part 1">

# def check_happy(number):
#     num_list = list()
#     l_sum = 0
#     r_sum = 0
#     while number > 0:
#         digit = number % 10
#         number //= 10
#         num_list.append(digit)
#     num_list.reverse()
#     if len(num_list) % 2 == 0:
#         for i in range(0, len(num_list) // 2):
#             l_sum += num_list[i]
#         for i in range(len(num_list) // 2, len(num_list)):
#             r_sum += num_list[i]
#         if r_sum == l_sum:
#             print("Your number is happy")
#         else:
#             print("Your number is not happy")
#     else:
#         print("Your number is not even")

# </editor-fold>

# <editor-fold desc="Part 2">

# def find_add(start, end):
#     total = 0
#     for i in range(start, end):
#         total += i
#     return total
#
#
# def average(start, end):
#     length = end - start
#     add_res = find_add(start, end)
#     return add_res / length

# </editor-fold>

# <editor-fold desc="Tuple 1">

# nums = (1, 2, 3, 4, 5, 1, 6)
# print(nums)
# print(nums.index(1, 3, 6))

# </editor-fold>

# <editor-fold desc="Tuple 2">

# def foo(number1, number2):
#     return number1 + 1, number2 + 1
#
# result = foo(1, 2)
# print(result)

# </editor-fold>

# <editor-fold desc="Tuple 3">

# <editor-fold desc="">
#
# def addition(*nums):
#     total = 0
#     for i in range(len(nums)):
#         total += nums[i]
#     return total
#
#
# result = addition(1, 2, 3)
# print(result)
# </editor-fold>

#
# def addition(nums: list):
#     total = 0
#     nums[0] = 12
#     for i in range(len(nums)):
#         total += nums[i]
#     return total
#
#
# result = addition([1, 2, 3, 4, 5, 6])
# print(result)

# </editor-fold>


def foo(*args, num1, num2):
    print(num1)
    print(num2)
    print(args)


foo(1, 2, 3, 4, 5, num1=1, num2=2)
