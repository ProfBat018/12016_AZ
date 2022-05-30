# <editor-fold desc="Get all host with ip">

# import socket
#
#
# def show_all_hosts(address: str):
#     res = list()
#     for i in range(38, 255):
#         try:
#             tmp = socket.gethostbyaddr(address + '.' + str(i))
#             host = [tmp[0], tmp[2]]
#             res.append(host)
#             print(res)
#         except:
#             print(f"Not found: {address + '.' + str(i)} ")
#     return res
#
#
# result = show_all_hosts("10.2.24")
# print(result)

# </editor-fold>

# <editor-fold desc="">

# class - User defined data type

class Car:
    def __init__(self, id: int, make="", model="", year=0):
        self.id = id
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.id}\n" \
               f"{self.make}\n" \
               f"{self.model}\n" \
               f"{self.year}\n"

    def edit_make(self, new_make):
        self.make = new_make

    def edit_model(self, new_model):
        self.model = new_model

    def edit_year(self, new_year):
        self.year = new_year


class Showroom:
    def __init__(self, cars: list):
        self.cars = cars
        self.budget = 10000


def list_cars(cars: list):
    for car in cars:
        print(car)


def removeById(id: int, cars: list):
    for car in cars:
        if car.id == id:
            cars.remove(car)
            break


c1 = Car(1, "Mercedes", "CLS 350", 2015)
c2 = Car(2, "Toyota", "Prius", 2015)

cars = [c1, c2]
list_cars(cars)
removeById(1, cars)
list_cars(cars)



# </editor-fold>
