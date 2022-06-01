import dicttoxml
import xmltodict


class Car:
    def __init__(self, make="", model="", year=0):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.make}\n" \
               f"{self.model}\n" \
               f"{self.year}\n"

    @staticmethod
    def from_dict(data: dict):
        return Car(data['Car']['make'], data['Car']['model'], data['Car']['year'])


# <editor-fold desc="Serialization">

# cars = [Car("Toyota", "Supra", 1995), Car("Mercedes", "190 EVO 2", 1995)]
# car_dict = list(map(lambda x: x.__dict__, cars))
#
# res = dicttoxml.dicttoxml(car_dict[0], attr_type=False, custom_root="Car")
#
# file = open("data.xml", 'wb')
# file.write(res)
# file.close()
# </editor-fold>


# <editor-fold desc="Deserialization">

# file = open("data.xml", 'rb')
#
# data = file.read()
#
# res = xmltodict.parse(data)
# print(res)
#
# res = Car.from_dict(res)
# print(res)

# </editor-fold>