# Example for class object
class Animal:
    # if variable starts with __ means private variable
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0
    # constructor

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    # getter setter example
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        self.__sound

    def get_type(self):
        print("ANIMAL")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {} ".format(self.__name, self.__height, self.__weight, self.__sound)


cat = Animal('Whiskers', 3, 10, 'Meow')
print(cat.toString())

# inheritance


class Dog(Animal):

    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("DOG")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {} His owner is {}".format(self.get_name(), self.get_height(), self.get_weight(), self.get_sound(), self.__owner)


spot = Dog("Spot", 53, 26, "Ruff", "Derek")
print(spot.toString())


class AnimalTesting:
    # polymorphism
    def get_type(self, animal):
        animal.get_type()


test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)
