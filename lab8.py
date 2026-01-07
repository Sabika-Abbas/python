from abc import ABC, abstractmethod
# class Super(ABC):
#     def delegate(self):
#         self.action()
#     @abstractmethod
#     def action(self):
#         pass

# class Sub(Super):
#     def action(self):
#         print("Action is taken")

# X=Sub()
# X.action()

'''
class Vehicle(ABC):
    def __init__(self,name,numOFTyres):
        self.name=name
        self.numOfTyres=numOFTyres
    
    @abstractmethod
    def print_info(self):
        pass

class Car(Vehicle):
    def __init__(self, name, numOFTyres,numOfDoors, has_sunroof):
        super().__init__(name, numOFTyres)
        self.numOfDoors=numOfDoors
        self.has_sunroof=has_sunroof

    def print_info(self):
        print(f"Name of Car: {self.name}\nNumber of tyre:{self.numOfTyres}\nNumber of doors:{self.numOfDoors}\nHas sunroof:{self.has_sunroof}")
        
class Truck(Vehicle):
    def __init__(self, name, numOFTyres, fuel_type, load_capacity):
        super().__init__(name, numOFTyres)
        self.fuel_type=fuel_type
        self.load_capacity=load_capacity

    def print_info(self):
        print(f"Name of Car: {self.name}\nNumber of tyre:{self.numOfTyres}\nFuel type:{self.fuel_type}\nLoad capacity:{self.load_capacity}")

class Motorcycle(Vehicle):
    def __init__(self, name, numOFTyres, enfine_CC, has_sidecar):
        super().__init__(name, numOFTyres)
        self.engine_CC=enfine_CC
        self.has_sidecar=has_sidecar

    def print_info(self):
        print(f"Name of Car: {self.name}\nNumber of tyre:{self.numOfTyres}\nEngine CC:{self.engine_CC}\nHas sidecar:{self.has_sidecar}")

car = Car("Toyota Corolla", 4, 4, True)
truck = Truck("Ford F-150", 8, "Diesel", "5 tons")
motorcycle = Motorcycle("Harley Davidson", "Petrol", 1200, False)

car.print_info()
print()
truck.print_info()
print()
motorcycle.print_info()
'''

class Calculator(ABC):
    def __init__(self):
        self.x=int(input("Enter first Operand: "))
        self.y=int(input("Enter second Operand: "))
    
    @abstractmethod
    def Mathematical_operation(self):
        pass

class Addition(Calculator):
    def __init__(self):
        super().__init__()

    def Mathematical_operation(self):
        return self.x+self.y
    
class Subtraction(Calculator):
    def __init__(self):
        super().__init__()

    def Mathematical_operation(self):
        return self.x-self.y

class Multiplication(Calculator):
    def __init__(self):
        super().__init__()

    def Mathematical_operation(self):
        return self.x*self.y

class Division(Calculator):
    def __init__(self):
        super().__init__()

    def Mathematical_operation(self):
        if self.y==0:
            return "Zero Division Error"
        return self.x/self.y
    
add = Addition()
print("Addition Result:", add.Mathematical_operation(),"\n")

sub = Subtraction()
print("Subtraction Result:", sub.Mathematical_operation(),"\n")

mul = Multiplication()
print("Multiplication Result:", mul.Mathematical_operation(),"\n")

div = Division()
print("Division Result:", div.Mathematical_operation())
