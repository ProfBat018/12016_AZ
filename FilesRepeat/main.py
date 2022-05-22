# <editor-fold desc="Part 1 - Write to files">

# name = 'Elvin'
#
# file = open("data.txt", 'w')
#
# file.write(name)
#
# file.close()


# </editor-fold>

# <editor-fold desc="error with int">
# number = 5
#
# file = open("data.txt", 'w')
#
# file.write(number)
#
# file.close()

# </editor-fold>

# <editor-fold desc="How to write any data">

# import pickle  # Binary serializasiya üçün kitabxana
# Binary serializasiya - İstənilən məlumat növünü binaryarray formatına çevirib, yazılması

# <editor-fold desc="Serializasiya">

# import pickle
# number = 5
#
# file = open("data.txt", 'wb')
#
# pickle.dump(number, file)
# file.close()

# </editor-fold>
# <editor-fold desc="Deserializasiya">

# import pickle
#
# file = open("data.txt", 'rb')
#
# number = pickle.load(file)
# print(number)

# </editor-fold>
# </editor-fold>


# <editor-fold desc="Task1">
#
# file = open("task1.txt", 'r')
#
# text = file.read()
#
# file.close()
# text = text.split()
#
# for word in text:
#     if len(word) >= 7:
#         file = open("task1_uploaded.txt", 'a')
#         file.write(word + '\n')
#
# file.close()

# </editor-fold>

# Variables, If Conditions, Loops, Functions, Data Structures, Work with files


# def foo(num1=2, num2):
    # print(num1, num2)


# foo(5, 6)
