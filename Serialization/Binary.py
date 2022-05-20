import pickle

#  <editor-fold desc="Write bytes">
#
# cars = ["IS350", "Supra", "S600", "K5"]
#
# file = open("data.txt", 'wb')
#
# pickle.dump(cars, file)
#
# file.close()
#
# </editor-fold>

# <editor-fold desc="Read bytes">
#
# file = open("data.txt", 'rb')
#
# cars = pickle.load(file)
# print(cars)

# </editor-fold>


class IP:
    def __init__(self, address: str):
        tmp = address.split('.')
        self.octet1 = tmp[0]
        self.octet2 = tmp[1]
        self.octet3 = tmp[2]
        self.octet4 = tmp[3]

    def __str__(self):
        return f"{self.octet1}.{self.octet2}.{self.octet3}.{self.octet4}"


# <editor-fold desc="Write IP">

# addresses = [IP("192.168.1.1"), IP("192.168.2.1"), IP("192.168.3.1"), IP("192.168.4.1"), IP("192.168.5.1"), IP("192.168.6.1")]
#
# file = open("data2.bin", 'wb')
#
# pickle.dump(addresses, file)


# </editor-fold>

# <editor-fold desc="Read IP">
#
# file = open("data2.bin", 'rb')
#
# addresses = pickle.load(file)
#
# for i in addresses:
#     print(i)

# </editor-fold>

