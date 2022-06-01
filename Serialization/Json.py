#   JSON və requests modulu
# JSON - Javascript object notation

import json


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
        return Car(data['make'], data['model'], data['year'])


# <editor-fold desc="Serialize">

# cars = [Car("Toyota", "Supra", 1995), Car("Mercedes", "190 EVO 2", 1995)]
#
# result = json.dumps(cars, default=lambda x: x.__dict__)
# file = open("data.json", 'w')
# file.write(result)
# file.close()

# </editor-fold>

# <editor-fold desc="Deserialize">

# file = open("data.json", "r")
# data = json.load(file)
# result = []
#
# for item in data:
#     result.append(Car.from_dict(item))
#
# for car in result:
#     print(car)

# </editor-fold>

# <editor-fold desc="Serialize 1 object">

# import dicttoxml
#
# cars = [Car("Toyota", "Supra", 1995), Car("Mercedes", "190 EVO 2", 1995)]
# car_dict = list(map(lambda x: x.__dict__, cars))
#
# res = dicttoxml.dicttoxml(car_dict, attr_type=False, custom_root="Car")
# print(res)

# </editor-fold>

