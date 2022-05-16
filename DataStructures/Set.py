# Set - çoxluq
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

# nums = [1, 2, 3, 4, 5] - List
# nums = (1, 2, 3, 4, 5) - Tuple
# nums = {1, 2, 3, 4, 5} - Set

# nums = {5, 1, -5, 0, 7, 9}
# nums2 = {6, 2, 3, 4, 5, 7}

# <editor-fold desc="Add and Pop">

# print(nums)
# nums.add(10)
# print(nums)

# print(nums)
# nums.pop()
# print(nums)
# nums.pop()
# print(nums)
# nums.pop()
# print(nums)

# </editor-fold>

# <editor-fold desc="Discard">

# print(nums)
# nums.discard(5)     # remove
# print(nums)

# </editor-fold>

# <editor-fold desc="Union">

# print(nums)
# nums = nums.union(nums2)
# print(nums)

# </editor-fold>

# <editor-fold desc="Intersect and Update">

# <editor-fold desc="Intersect">

# res = nums.intersection(nums2)
# print(res)

# </editor-fold>

# <editor-fold desc="Update">

# nums.intersection_update(nums2)
# print(nums)

# </editor-fold>

# </editor-fold>

# <editor-fold desc="Difference">

# print(nums.difference(nums2))

# </editor-fold>

# <editor-fold desc="Subset and Superset">

# a = {1, 2, 3, 4}
# b = {2, 4}
#
# print(a.issuperset(b))
# print(a.issubset(b))
# print()
# print(b.issuperset(a))
# print(b.issubset(a))

# </editor-fold>

# <editor-fold desc="Symmetric_difference">

# nums = {5, 1, -5, 0, 7, 9}
# nums2 = {6, 2, 3, 4, 5, 7}

# print(nums.symmetric_difference(nums2))
# a = nums.difference(nums2)
# b = nums2.difference(nums)
# print(a, b)
# a.update(b)
# print(a)

# </editor-fold>

# <editor-fold desc="Isdisjoint">

# nums = {1, 2}
# nums2 = {1, 3}
# x = nums.isdisjoint(nums2)
# print(x)

# </editor-fold>


