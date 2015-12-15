## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dos is-a Animal
class Dog(Animal):
    def __init__(self, name):
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        self.name = name

## Person is-a object
class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None

## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is a fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## Frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet called rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
