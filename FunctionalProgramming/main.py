# Functional Programming - map(), reduce(), filter()

# def find_even(number):
#     if number % 2 == 0:
#         return number

# <editor-fold desc="Filter">

# nums = [i for i in range(10)]
# result = set(filter(lambda num: num % 2 == 0, nums))
#
# print(result)

# </editor-fold>

# <editor-fold desc="Reduce">

# from functools import *
# nums = [i for i in range(10)]
#
# result = reduce((lambda x1, x2: x1 + x2), nums)
#
# print(result)

# </editor-fold>

# <editor-fold desc="Filter">

# nums = [i for i in range(10)]
#
# result = list(map(lambda x: x + 10, nums))
#
# print(result)

# </editor-fold>
