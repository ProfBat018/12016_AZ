# Random ədədlər ilə dolu olan iki siyahı var.
# Bu siyahılarda eyni olan elementləri çap edin

import random

nums1 = list()
nums2 = list()
nums3 = list()

length = int(input("Enter length: "))
start = int(input("Enter start: "))
end = int(input("Enter end: "))

for i in range(length):
    nums1.append(random.randint(start, end))
    nums2.append(random.randint(start, end))

# <editor-fold desc="For example 1">

# for i in range(length):
#     for j in range(length):
#         if nums1[i] == nums2[j] and nums3.count(nums1[i]) == 0:
#             nums3.append(nums1[i])
#             break

# </editor-fold>

# <editor-fold desc="For example 2">
#
# for i in range(length):
#     for j in range(length):
#         if (nums1[i] == nums2[j]) and (nums1[i] not in nums3):
#             nums3.append(nums1[i])
#             break
# </editor-fold>

# <editor-fold desc="For example">

check = True

for i in range(length):
    for j in range(length):
        if nums1[i] == nums2[j]:
            for k in range(len(nums3)):
                if nums1[i] == nums3[k]:
                    check = False
                    break
                else:
                    check = True
            if check:
                nums3.append(nums1[i])
                check = False
                break

# </editor-fold>


print(nums3)


