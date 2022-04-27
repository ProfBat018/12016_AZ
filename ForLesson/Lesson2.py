# num = int(input("Enter your number: "))
#
# result = 0
# multiple = 1
#
# while num != 0:
#     n = num % 10
#     num = num // 10
#     if n != 3 and n != 6:
#         result = (n * multiple) + result
#         multiple *= 10
# print(result)
#

# <editor-fold desc="Example 1">


# nums = [1, 2, 3, 4, 5]

# for i in range(5):
#     print(nums[i], end=' ')

# i = 0
# while i < 5:
#     print(nums[i], end=' ')
#     i += 1

# </editor-fold>

# <editor-fold desc="List methods">

nums = [i for i in range(1, 11)]

# <editor-fold desc="Count - obyektin sayini cap edir">

# res = nums.count(5)
# print(res)

# </editor-fold>

# <editor-fold desc="Clear - siyahini temizleyir">

# nums.clear()
# print(nums)

# </editor-fold>

# <editor-fold desc="Index - obyekin sirasini gosterir">

# res = nums.index(5)
# print(res)

# </editor-fold>

# <editor-fold desc="Sort - siyahinin butun elementlerini cesidleyir">

# nums.sort()
# print(nums)

# </editor-fold>

# <editor-fold desc="Append - siyahinin axirina elave edir">

# nums.append(132)
# print(nums)

# </editor-fold>

# <editor-fold desc="Insert(iki parametr qebul edir) - obykti lazimi indeksa elave edir">

# print(nums)
# nums.insert(1, 22)
# print(nums)

# </editor-fold>

# <editor-fold desc="Pop(0 ve ya 1 parametr qebul edir) - azirinci ve ya indkeskde olani silir ">

# print(nums)
# nums.pop()
# print(nums)

# print(nums)
# nums.pop(1)
# print(nums)

# </editor-fold>

# <editor-fold desc="Remove - deyer ile silir">

# nums.append(1)
# nums.append(1)
# nums.append(1)
# print(nums)
# nums.remove(1)
# nums.remove(1)
# nums.remove(1)
# print(nums)

# nums.append(1)
# nums.append(1)
# nums.append(1)
#
# print(nums)
# count = nums.count(1)
# for i in range(count):
#     nums.remove(1)
# print(nums)
# </editor-fold>

# <editor-fold desc="Reverse - tersine cevirir">

# nums.reverse()
# print(nums)

# </editor-fold>

# <editor-fold desc="Extend-listi append eliyir">
# nums2 = [111, 222, 333]
#
# print(nums)
# nums.extend(nums2)
# print(nums)

# </editor-fold>

# <editor-fold desc="Copy - Deyerleri kopyalayir">

# res = nums.copy()
# print(res)
# nums.pop()
# print(res)

res = list()

for i in range(len(nums)):
    res.append(nums[i])
print(res)
# </editor-fold>

# </editor-fold>

