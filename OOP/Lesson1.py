# OOP - Object Oriented Programming
# Obyekt yönümlü proqramlaşdırma

# Task - 10 Kompyuter var. Kompyuteri silmək
# və əlavə etmək funksiyaları yaradın

# <editor-fold desc="Procedure">

# [['Asus', 'Rog G531GT', 'i7-9750H'], ['Asus', 'Rog ', 'i7-10750H'], ['Acer', 'predator helios 300', 'ryzen 3550H']]

# computers = list()
#
#
# def create_pc():
#     make = input("Enter make of pc: ")
#     model = input("Enter model of pc: ")
#     processor = input("Enter processor of pc: ")
#
#     computer = [make, model, processor]
#     return computer
#
#
# for i in range(3):
#     computers.append(create_pc())
#
# print(computers)
# </editor-fold>

# <editor-fold desc="OOP">

class Computer:
    def __init__(self, make, model, processor):
        self.make = make
        self.model = model
        self.processor = processor

    def edit_make(self, new_make):
        self.make = new_make

    def edit_model(self, new_model):
        self.model = new_model

    def edit_processor(self, new_processor):
        self.processor = new_processor

    def __str__(self):
        return f"{self.make}\n{self.model}\n{self.processor}\n"

    @staticmethod
    def create_computer(make: str, model: str, processor: str):
        temp = Computer(make, model, processor)
        return temp



# computers = [create_computer(input("Enter make: "),
#                              input("Enter model: "),
#                              input("Enter processor: ")) for i in range(2)]
#


c1 = Computer("Asus", "ROG", "i7-9750H")

c1.edit_model("TUF")
Computer.edit_model(c1, "fdgsd")

c3 = Computer.create_computer("Asus", "ROG", "i7-9750H")


# </editor-fold>


