# <editor-fold desc="Intro">

# open("file path", "access mode")
# access mode - w, r, a, wb, rb, ab
# w - write
# r - read
# a - append
# wb - write bytes
# rb - read bytes
# ab - append bytes

# </editor-fold>

# <editor-fold desc="Write">

#
# text = "Hello World"
#
# file = open("data.txt", 'w')
# file.write(text)
# file.close()

# </editor-fold>

# <editor-fold desc="Read">

# file = open("data.txt", 'r')
# res1 = file.read()  # Bütün sətrləri qaytarır
# res2 = file.readline()
# res3 = file.readlines()
# file.close()

# </editor-fold>

# <editor-fold desc="Append">

# file = open("data.txt", 'a')
# file.write("\nTest")
# file.writelines(["\nTest\n", "Test1\n", "Test2\n"])

# file.close()

# </editor-fold>


