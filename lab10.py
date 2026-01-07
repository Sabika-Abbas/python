# from abc import ABC, abstractmethod

# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def talk(self):
#         pass

# class Cat(Animal):
#     def talk(self):
#         return "Meow!"

# class Dog(Animal):
#     def talk(self):
#         return "Woof!"

# # Example usage
# cat = Cat("Whiskers")
# dog = Dog("Buddy")

# print(f"{cat.name} says: {cat.talk()}")
# print(f"{dog.name} says: {dog.talk()}")

# from abc import ABC, abstractmethod

# class Person(ABC):
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def ticket_price(self, base_price):
#         pass

# class EmployedPerson(Person):
#     def ticket_price(self, base_price):
#         return base_price * 0.9  # 10% discount

# class Student(Person):
#     def ticket_price(self, base_price):
#         return base_price * 0.5  # 50% discount

# employed = EmployedPerson("Alice")
# student = Student("Bob")

# print(f"{employed.name}'s ticket price: ${employed.ticket_price(100):.2f}")
# print(f"{student.name}'s ticket price: ${student.ticket_price(100):.2f}")

l1=[2,4,3]
l2=[5,6,4]
def add(x,y):
    lst=[]
    o=x+y
    if o>9:
        o-=10
        lst.append(o)
    else:
        lst.append(o)

    return lst


result=map(add,l1,l2)
print(add())
