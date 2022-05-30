class Person:
    __salary = 0

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class Teacher(Person):
    def __init__(self, name, surname, age, salary, experience):
        super().__init__(name, surname, age)
        self.__salary = salary
        self.experience = experience

    @property   # get_salary
    def salary(self):
        return self.__salary * 0.95

    @salary.setter  # set_salary
    def salary(self, value):
        if value > 200:
            self.__salary = value


p1 = Person("Elvin", "Azimov", 20)

p2 = Teacher(p1.name, p1.surname, p1.age, 3000, 4)

print(p2.salary)
p2.salary = 1
print(p2.salary)

