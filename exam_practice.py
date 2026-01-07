# class Student:
#     def __init__(self, name,roll,marks):
#         self.__name=name
#         self.__roll=roll
#         self.__marks=marks

#     def set_name(self,name):
#         self.__name=name

#     def get_name(self):
#         return self.__name
    
#     def set_roll(self, roll):
#         self.__roll = roll
        
#     def get_roll(self):  
#         return self.__roll
        
#     def set_marks(self, marks):  
#         self.__marks = marks
        
#     def get_marks(self):  
#         return self.__marks
    
#     def print_student(self):
#         print(f"Name: {self.__name}\nRoll #: {self.__roll}")
#         for i in range(len(self.__marks)):
#             print(f"Quiz {i+1}: {self.__marks[i]}")
#     def avg(self):
#         avg=sum(self.__marks)/len(self.__marks)
#         print(f"Average: {avg}")

#     def __dict__(self):
#         return {
#             'name': self.__name,
#             'roll': self.__roll,
#             'marks': self.__marks
#         }
    
# s=Student("Sabika","105", [88,89,90])
# s.print_student()
# s.avg()
# print("Dictionar representation:", s.__dict__())

# class Time:
#     def __init__(self,seconds=0,minutes=0,hours=0):
#         self.seconds=seconds
#         self.minutes=minutes
#         self.hours=hours

#     def print_time(self):
#         return f"{self.hours}:{self.minutes}:{self.seconds}"
    
#     def add_time(self,t):
#         self.seconds+=t.seconds
#         self.minutes+=t.minutes
#         self.hours+=t.hours

#         if self.seconds>=60:
#             self.minutes+=1
#             self.seconds-=60

#         if self.minutes>=60:
#             self.hours+=1
#             self.minutes-=60

#         if self.hours >= 24:
#             self.hours -= 24
                
# t1=Time(50,22,6)
# t2=Time(23,40,20)
# print(t1.print_time())
# print(t2.print_time())
# t1.add_time(t2)
# print(t1.print_time())

'''
Imagine a tollbooth at a bridge. Cars passing by the booth are expected to pay a Rs. 50 toll. Mostly
they do, but sometimes a car goes by without paying. The tollbooth keeps track of the number of
cars that have gone by, and of the total amount of money collected. Write code to model this
tollbooth with a class called Toll_Booth having two attributes: num_car, to hold the total
number of cars, and total_money, to hold the total amount of money collected. A constructor
initializes both of these to 0. A method called paying_car() increments the car total and adds
Rs. 50 to the cash total. Another method, called no_pay_car(), increments the car total but adds
nothing to the cash total. Finally, a method function called display() displays the two totals
along with the number of defaulters. Include a program to test this class. Write client code that
repeatedly allows the user to select one key to count a paying car, and another to count a nonpaying
car; and any other key to exit. On exit, print the final statistics of cars passed through the booth,
total cash collected and the number of defaulters.
'''

# class Toll_Booth:
#     def __init__(self):
#         self.num_car=0
#         self.total_money=0
#         self.paying_cars=0
#         self.non_paying_cars=0

#     def paying_car(self):
#         self.num_car+=1
#         self.total_money+=50
#         self.paying_cars+=1

#     def no_paying_car(self):
#         self.num_car+=1
#         self.non_paying_cars+=1

#     def display(self):
#         print(f"Total cars: {self.num_car}")
#         print(f"Paying cars: {self.paying_cars}")
#         print(f"Non-paying cars: {self.non_paying_cars}")
#         print(f"Total money collected: Rs.{self.total_money}")

# t=Toll_Booth()
# while True:
#     print('''
#           1. Paying Car
#           2. Non Paying Car
#           3. Exit:''')
#     x=input("Select one: ")
    
#     if x=="1":
#         t.paying_car()
#     elif x=="2":
#         t.no_paying_car()
#     elif x=="3":
#         t.display()
#         break
#     else:
#         print("Invalid choice!")    

'''a. Define the following functions:
 input_in_range(min_value,max_value): inputs from user and returns an integer
value making sure that the input is in range min_value and max_value (both inclusive). It
prints an error message 'Value out of range' every time the user enters an out of range
value, then prompting the user again for the input.
 create_list(n,min_value,max_value): creates and returns a list of n integers, all
in range between min_value and max_value (both inclusive); makes use of
input_in_range function for input and range checking.
b. Write a program that opens a file called 'my_list.txt', makes use of input_list function
to input a list of 3 integers, all between 1 and 100 (both inclusive), and saves this list in the file and
closes it.
c. Identify exceptions that can possibly occur in the code.
d. Define try-except blocks in the code to handle the possible exceptions.
e. Add else and finally blocks in the main code to handle filing.
f. In the function input_in_range, raise a ValueError Exception to indicate out of range user
input.
g. Define a new exception class called OutOfRangeError. In the function input_in_range,
raise this exception to indicate out of range user input.
h. In exception handler defined in the function input_in_range, add another except block to
handle KeyBoardInterrupt, to print the message 'You terminated the program'
before exiting the program. This exception occurs if the user presses ctrl+C during the run time.'''

# def input_in_range(min_value, max_value):
#     while True :
#         x=int(input("Enter a number between 0 and 100: "))
#         try:
#             if x<min_value or x>max_value:
#                 raise ValueError
#             else:
#                 return x
#         except ValueError:
#             print("Please enter a valid integer")
        
#         except KeyboardInterrupt:
#             print("\nYou terminated the program")
#             exit()

# def create_list(n,min_value,max_value):
#     lst=[]
#     for i in range(n):
#         val=input_in_range(min_value,max_value)
#         lst.append(str(val))

#     return lst

# def open_file():
#     try:
#         # Create list of 3 integers between 1 and 100
#         numbers = create_list(3, 1, 100)
        
#         # Open file and write the list
#         with open('my_list.txt', 'w') as f:
#             f.write('\n'.join(numbers))  # Write each number on a new line
            
#     except IOError as e:
#         print(f"File error occurred: {e}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#     else:
#         print("List successfully written to file")
#     finally:
#         print("Program execution completed")

# open_file()

# class InvalidWithdrawl(Exception):
#     def __init__(self, b=0,a=0):
#         self.balance=b
#         self.amount=a
#     def deficit(self):
#         return self.balance-self.amount
    
# total_balance=1000
# amount=int(input('Enter amount to be drawn from the account: '))
# i=InvalidWithdrawl(total_balance,amount)
# try:
#     if amount>total_balance:
#         raise i
#     print("your deficit is:",i.deficit())
# except InvalidWithdrawl:
#     print('You do not have enough balance!')


# class EmptyFileError(Exception):
#     pass
# class NotAList(Exception):    
#     pass

# try:
#     with open("my_list.txt") as f:
#         content=f.read().strip()
#         if content=="":
#             raise EmptyFileError
#         try:
#             data=eval(content)
#             if not isinstance(data, list):  # Check if it's a list
#                     raise NotAList("The file does not contain a valid list.")
#             else:
#                 print(eval(content))
#                 print('Total integers in the list are',len(content))
#         except (SyntaxError, ValueError):  # If ast.literal_eval fails
#             raise NotAList("The file does not contain a valid Python list.")
        
# except FileNotFoundError:
#     print("File is not found")

# except EmptyFileError as e:
#     print("File is empty",e)

# except NotAList:
#     print("File doesnot contain a list")\


# x="Global"
# class A:
#     x="Class A"
#     def methodA(self):
#         x="Method A"
#         v=self.B()
#         v.methodB()
#     class B:
#         x="Class B"
#         def methodB(self):
#             x="Method B"
#             print(x)

# a=A()
# a.methodA()

# def multiply(a,b):
#     return a*b

# def multiply(a):
#     return a*10

# print(multiply(5))

# class Point:
#     def __init__(self,xcoord=0,ycoord=0):
#         self.x=xcoord
#         self.y=ycoord
#     def setx(self,xcoord):
#         self.x=xcoord
#     def sety(self,ycoord):
#         self.y=ycoord
#     def get(self):
#         return self.x, self.y
#     def move(self, dx, dy):
#         self.x+=dx
#         self.y+=dy

# p1=Point(7)
# print(p1.get())
# print(p1.get())

# class Point:
#     def __init__(self,xcoord=0,ycoord=0):
#         self.__x=xcoord
#         self.__y=ycoord
#     def setx(self,xcoord):
#         self.__x=xcoord
#     def sety(self,ycoord):
#         self.__y=ycoord
#     def get(self):
#         return self.__x, self.__y
#     def move(self, dx, dy):
#         self.__x+=dx
#         self.__y+=dy

# p1=Point(7)
# print(p1.get())
# p1.__x=4

# p1.sety(4)
# print(p1.get())
# print(p1.__dict__)

# count=0
# class Tracker:
#     def __init__(self):
#         global count
#         count+=1
#         self.serialNo=count
#     def reportSerial(self):
#         print(f"I am object {self.serialNo}")

# t1=Tracker()
# t2=Tracker()
# t3=Tracker()
# t1.reportSerial()
# t2.reportSerial()
# t3.reportSerial()


# class Tracker:
#     count=0
#     def __init__(self):
#         Tracker.count+=1
#         self.serialNo=Tracker.count
#     def reportSerial(self):
#         print(f"I am object {self.serialNo}")
        

# t1=Tracker()
# t2=Tracker()
# t3=Tracker()
# t1.reportSerial()
# t2.reportSerial()
# t3.reportSerial()

# class mystr:
#     def __init__(self,x=""):
#         self.x=x
#     def __add__(self,obj):
#         return self.x+str(obj)
#     def __iadd__(self,obj):
#         self.x+=str(obj)
#         return self.x

# m=mystr("x")
# print(m+[2,3])

# m+=3
# print(m)

# class MyStr():
#     def __init__(self, s=''):
#         self.strg=s
#     def __add__(self,anyObject):
#         return self.strg + str(anyObject)

# x=MyStr('Python')
# print(x+' Programming')
# print(x+3)
# print(x+3.7)
# print(x+[2,3])

# class Point:
#     def __init__(self,xcoord=0,ycoord=0):
#         self.x=xcoord
#         self.y=ycoord
#     def setx(self,xcoord):
#         self.x=xcoord
#     def sety(self,ycoord):
#         self.y=ycoord
#     def __str__(self):
#         return f"({self.x},{self.y})"
#     def move(self, dx, dy):
#         self.x+=dx
#         self.y+=dy
#     def __add__(self,p2):
#         return self.x+p2.x,self.y+p2.y
#     def __lt__(self,p2):
#         return self.x<p2.x,self.y<p2.y
#     def __invert__(self):
#         return -self.x, -self.y
#     def __pos__(self):
#         return -self.x
    
# p1=Point(3,4)
# print(p1)
# p2=Point(2,5)
# print(p2)
# print(p1+p2)
# print(p1<p2)
# print(+p1)
# print(~p1)

# def funC():
#     print("executed")
# m=funC()

# def funcObject():
#     print('I am function object')

# def func_c():
#     return funcObject()

# func_c()

# def decorator1(f):
#     def myWrapper():
#         print('*'*5)
#         f()
#         print('*'*5)
#     return myWrapper

# @decorator1
# def myfunc():
#     print('Congratulations!')
    
# print(myfunc)
# print(myfunc( ))
# print(f( ))
# print(myWrapper())

# class myClass:
#     classAttribute='ClassAttribute'

#     def __init__(self):
#         self.instanceAttribute='InstanceAttribute'

#     def instanceMethod(self):
#         print(myClass.classAttribute) #classattirbute
#         print(self.classAttribute) #classattirbute
#         print(self.instanceAttribute)  #instanceattirbute
#         print('This is an instance method\n')
    
#     @classmethod
#     def classMethod(cls):
#         print(cls.classAttribute)
#         # print(cls.instanceMethod()) #error
#         # myClass.instanceMethod() #error
#         # myClass.instanceMethod #class attribute only
#         myClass.staticMethod()
#         print("class method\n")
    
#     @staticmethod
#     def staticMethod():
#         print(myClass.classAttribute)
#         # print(myClass.classMethod())  #will also return none with class attribute
#         # myClass.classMethod()
#         # print(myClass.instanceMethod())  #error
#         print("static method\n")

#     def anothermethod(self):
#         # self.classMethod()
#         # self.instanceMethod()
#         # self.staticMethod()
#         # print(myClass.instanceMethod())  #error
#         myClass.classMethod()
#         myClass.staticMethod()

# m=myClass()
# # m.instanceMethod()

# m.classMethod()
# # myClass.classMethod()

# # m.staticMethod()
# # myClass.staticMethod()

# # m.anothermethod()


# class Fraction:
#     def __init__(self, x=0, y=1):
#         self.numerator=x
#         self.denominator=y
#     def setNumerator(self,x):
#         self.numerator=x
#     def setDenominator(self,y):
#         if y!=0:
#             self.denominator=y
#         else:
#             print('Invalid value, setting to 1 instead')
#     def __str__(self):
#         return str(self.numerator)+'/'+str(self.denominator)
#     def convertDecimal(self):
#         return self.numerator/self.denominator
#     def __add__(self,f2):
#         if isinstance(f2,Fraction):
#             return self.numerator*f2.denominator+f2.numerator*self.denominator, self.denominator*f2.denominator
#         else:
#             return 'Wrong argument, only fractions allowed'
#     def __gt__(self,f2):
#         if isinstance(f2,Fraction):
#             return self.numerator*f2.denominator>f2.numerator*self.denominator
#         else:
#             return 'Wrong argument, only fractions allowed'
#     def simplify(self):
#         HCF=Fraction.findHCF(self.numerator,self.denominator)
#         self.numerator=int(self.numerator/HCF)
#         self.denominator=int(self.denominator/HCF)

#     def findHCF(a,b):
#         factor_a=Fraction.findFactors(a)
#         factor_b=Fraction.findFactors(b)
#         for i in range (len(factor_a)-1,-1,-1):
#             if factor_a[i] in factor_b:
#                 return factor_a[i]
            
#     def findFactors(x):
#         factors=[]
#         for i in range(1,x+1):
#             if x%i==0:
#                 factors.append(i)
#         return factors

# f1=Fraction(8,10)
# f1.simplify()
# print(f1)

# f2=Fraction(1,8)
# print(f1+f2) 
# print(f1>f2)

# from abc import ABC, abstractmethod
# class Polygon(ABC):
#     @abstractmethod
#     def noOfSides(self):
#         print("I am polygon")

# class Square(Polygon):
#     def noOfSides(self):
#         # super().noOfSides()
#         Polygon.noOfSides(self)
#         print('I have 4 sides')

# class Triangle(Polygon):
#     def noOfSides(self):
#         print('I have 3 sides')


# # a=Polygon()
# b=Square()
# b.noOfSides()
# c=Triangle()
# c.noOfSides()

# from collections import Container
# class OddContainer:
#     def contains (self, x):
#         if not isinstance(x, int) or not x % 2:
#             return False
#         return True

# num=OddContainer()
# print(1 in num)
# print(2 in num)
# print(237813 in num)
# print(isinstance(num,OddContainer))
# print(issubclass(OddContainer,Container))

# class Airplane():
#     def fly(self):
#         print("fly with fuel!")
#     def setNoOfPassengers(self,p):
#         self.noOfPassengers=p

# class Duck():
#     def fly(self):
#         print("fly with wings!!")
#     def swim(self):
#         print("swim in ponds!!")

# class Fish:
#     def swim(self):
#         print("fish swim in sea")

# def moves(x):
#     x.fly()

# a=Airplane()
# d=Duck()
# f=Fish()
# moves(a)
# moves(d)
# moves(f)

# class hello:
#     sound="bark"
#     def speak(self):
#         '''this is speak method'''
#         # print(self.sound)
#         # print("hello")
#         print(hello.sound)

# h=hello()
# # h.speak()
# # h.sound="meow"
# # h.speak()
# # hello.sound="chu chu"
# # h.speak()
# # help(hello.speak)
# print(type(h))


'''
A class File has two attributes name and size. Image is a
subclass of File with an additional attribute of alternate_txt
and a method display() to print all details of image. Let’s
assume that an image can either be a GIF or a JPG.
Implement these subclasses of Image, then override the
display() method in each to also include a reference to what
type it is.
'''
# class File:
#     def __init__(self,name,size):
#         self.name=name
#         self.size=size

# class Image(File):
#     def __init__(self, name, size,alternate_txt):
#         super().__init__(name, size)
#         self.alternate_txt=alternate_txt

#     def display(self):
#         return f"Name: {self.name}\nSize: {self.size}\nAlternate txt: {self.alternate_txt}"

# class GIF(Image):
#     def __init__(self, name, size, alternate_txt):
#         super().__init__(name, size, alternate_txt)
    
#     def display(self):
#         return f"{super().display()}\nType:GIF"

# class JPG(Image):
#     def __init__(self, name, size, alternate_txt):
#         super().__init__(name, size, alternate_txt)
    
#     def display(self):
#         return f"{super().display()}\nType:JGP"

# g=GIF("flower","16x16","flower.txt")
# print(g.display())


'''
1. Write a Python class Restaurant with attributes like menu_items, book_table, and
customer_orders, and methods like add_item_to_menu, book_tables, and
customer_order.
Perform the following tasks now:

2. Now add items to the menu.
3. Make table reservations.
4. Take customer orders.
5. Print the menu.
6. Print table reservations.
7. Print customer orders.
Note: Use dictionaries and lists to store the data.
'''
# class Restaurant:
#     def __init__(self):
#         self.menu_items=["Biryani", "Nihari","Tandoori Roti","Karhai"]
#         self.book_table=None
#         self.customer_order=None

#     def add_item_to_menu(self,item):
#         self.menu_items.append(item)
#         return self.menu_items
    
#     def book_tables(self):
#         self.book_table=input("Enter table you want to reserve from table 1-4: ")
#         while self.book_table>"4" or self.book_table<"0":
#             self.book_table=input("Table unavailable choose between 1-4: ")
#         return self.book_table

#     def customer_orders(self):
#         print(self.menu_items)
#         self.customer_order=input("enter your oder from given menu: ")
#         while self.customer_order not in self.menu_items:
#             self.customer_order=input("Please enter items from given menu: ")
#         return self.customer_order

#     def display_info(self):
#         print(f"Menu: {self.menu_items}")
#         print(f"Table number {self.book_table} successfully reserved!")
#         print(f"{self.customer_order} successfully orders")

# r=Restaurant()
# r.add_item_to_menu("Cold drink")
# r.book_tables()
# r.customer_orders()
# r.display_info()
        

'''
1. Write a Python class Inventory with attributes like item_id,
item_name, stock_count, and price, and methods like
add_item, update_item, and check_item_details.
2. Use a dictionary to store the item details, where the key is the
item_id and the value is a dictionary containing the item_name,
stock_count, and price.
'''
# class Inventory:
#     def __init__(self):
#         self.items={}
    
#     def add_item(self, item_id, item_name, stock_count, price):
#         """Add a new item to the inventory"""
#         if item_id not in self.items:
#             self.items[item_id] = {
#                 'item_name': item_name,
#                 'stock_count': stock_count,
#                 'price': price
#             }
#             print(f"Item {item_name} (ID: {item_id}) added successfully.")
#         else:
#             print("item id already exists")

#     def update_item(self, item_id, item_name=None, stock_count=None, price=None):
#         """Update existing item details"""
#         if item_id in self.items:
#             item = self.items[item_id]
#             if item_name is not None:
#                 item['item_name'] = item_name
#             if stock_count is not None:
#                 item['stock_count'] = stock_count
#             if price is not None:
#                 item['price'] = price
#             print(f"Item ID {item_id} updated successfully.")
#         else:
#             print(f"Item ID {item_id} not found in inventory.")
    
#     def check_item_details(self, item_id):
#         """Display details of a specific item"""
#         if item_id in self.items:
#             item = self.items[item_id]
#             print(f"\nItem ID: {item_id}")
#             print(f"Name: {item['item_name']}")
#             print(f"Stock Count: {item['stock_count']}")
#             print(f"Price: ${item['price']:.2f}")
#         else:
#             print(f"Item ID {item_id} not found in inventory.")


# # Demonstration
# inventory = Inventory()

# # Add items to inventory
# inventory.add_item("1001", "Laptop", 10, 999.99)
# inventory.add_item("1002", "Mouse", 50, 19.99)
# inventory.add_item("1003", "Keyboard", 30, 49.99)

# # Try to add duplicate item
# inventory.add_item("1001", "Duplicate Laptop", 5, 899.99)

# # Update an item
# inventory.update_item("1002", stock_count=45, price=15.99)

# # Check item details
# inventory.check_item_details("1001")
# inventory.check_item_details("1002")

# # Try to check non-existent item
# inventory.check_item_details("9999")


# def cheers(print_winner):
#     def mywrapper(winner_name):
#         print_winner(winner_name)
#         print("how do you spell winner?")
#         print("I know! I know!")
#         for i in winner_name:
#             print(i.upper(),end=" ")
#     return mywrapper

# @cheers
# def print_winner(winner_name):
#     print("The winner is", winner_name)

# print_winner("Huskies")

# class Polygon:
#     def __init__(self,no_of_sides=3,lengths=[]):
#         self.no_of_sides=no_of_sides
#         self.lengths=lengths
#     def set_no_of_sides(self,n):
#         try:    
#             if not isinstance(n,int):
#                 raise TypeError
#             if n>=3:
#                 self.no_of_sides=n
#         except TypeError as e:
#             print("n must be integer",e)
#     def set_lengths(self,l):
#         try:
#             if len(l)== self.no_of_side:
#                 for i in l:
#                     if isinstance(i,int) or isinstance(i,float):
#                         if i>0:
#                             self.lengths=l
#                     else:
#                         raise TypeError
#             else:
#                 raise ValueError("no of sids should be equal to l")
#         except TypeError as e:
#             print("n must be integer or float",e)

#     def perimeter(self):
#         if self.lengths==0:
#             return 0
#         else:
#             self.peri=0
#             for x in self.lengths:
#                 self.peri+=x
#                 return self.peri
            
# p=Polygon(4,[3,4,3,4])
# print(p.perimeter())

# x=1
# def nester():
#     print(x)
#     class C:
#         print(x)
#         def method1(self):
#             print(x)
#         def method2(self):
#             x=3
#             print(x)
#     l=C()
#     l.method1()
#     l.method2()

# print(x)
# nester()

# class A:
#     def innn(self):
#         print("in a")
#     class B:
#         def innn(self):
#             print("in b")
#     class C:
#         def innn(self):
#             print("in c")
#     class X(A,B,C):
#         def innn(self):
#             print("in b")
#     class Y(A,B,C):
#         def innn(self):
#             print("in b")
    
# def star(func):
#     def inner(a):
#         print("X"*5)
#         func(a)
#         print("X"*5)
#     return inner

# def percent(func):
#     def inner(a):
#         print("T"*5)
#         func(a)
#         print("T"*5)
#     return inner

# @star
# @percent
# def printmsg(msg):
#     print(msg)
# printmsg("hello")

# class A:
#     def innn(self):
#         print("in a")
# class B:
#     def innn(self):
#         print("in b")
    
# class X(A,B):
#     pass

# class Y(A):
#     def innn(self):
#         print("in y")
# class Z(X,Y,B):
#     pass
# obj=Z()
# obj.innn()
# print(Z.mro())

# def squared(func):
#     return lambda x:func(x)*func(x)

# def x_times_3(x):
#     return x*3
# x_times_3=squared(x_times_3)
# print(x_times_3(2))

# def x_minus_1(x):
#     return x-1
# x_minus_1=squared(x_minus_1)
# print(x_minus_1(3))

# class TestPrivate:
#     def setPrivateAttr(self,x):
#         self.__privateAttr=x
#     def getPrivateAttr(self):
#         return self.__privateAttr
#     def __privateMethod(self):
#         print("I am private method")
# p2=TestPrivate()
# p2.setPrivateAttr(44)
# print(p2.getPrivateAttr())
# print(p2.__privateAttr)
# print(p2._TestPrivate__privateAttr)

# try:
#     year=int(input("enter years: "))
# except IndexError:
#     print("invalid")
# except:
#     print("incorrect")

# class Animal:
#     def setSpecie(self,x):
#         self.specie=x
#     def getSpecie(self):
#         return self.specie
    
# a1=Animal()
# print(a1.getSpecie())
# a1.setSpecie("mouse")

# class Diet:
#     ingredient_usage={}
#     def __init__(self, ingredient:str=None,quantity:float=None,calories:float=None):
#         self.ingredient=ingredient
#         self.quantity=quantity
#         self.calories=calories
        
#         if ingredient is not None:
#             Diet.ingredient_usage[ingredient] = Diet.ingredient_usage.get(ingredient, 0)

#     def print_ingredient(self):
#         print(f"<{self.ingredient}>:<{self.quantity}><{self.calories}>")
    
#     def tracker(self):
#         self.count=0

# class Age:
#     try:
#         age=int(input("Enter your age: "))
#         if isinstance(age, int):
#             raise TypeError
#         elif age<0:
#             raise ValueError
#         elif age%2==0:
#             print("age is even")
#         elif age%2!=0:
#             print("age is odd")
        
        
#     except ValueError:
#         print("Age should be positive")
#     except TypeError:
#         print("Age should be integer")
# Age()

# try:
#     raise Exception("this is always raise")
#     print("never executed")
# except Exception as ex:
#     print(f"i caught error {ex!r}")
# print("error after exceitions")

# animal="cat"
# family="felidae"

# class Pantherine:
#     animal="Lion"
#     family="Panthera"
#     def __init__(self):
#         self.family="neofelis"
#         animal="Leopard"
#         def display_info():
#             print(self.family)
#             print(self.animal)
#             print(family)
#             print(animal)
#         display_info()
# f=Pantherine()

# def decor1(func):
#     def inner():
#         x=func()
#         return x*x
#     return inner
# def decor(func):
#     def inner():
#         x=func()
#         return x*2
#     return inner

# @decor1
# @decor
# def num():
#     return 10

# print(num())

# @decor
# @decor1
# def num2():
#     return 10

# print(num2())

# class Point:
#     def __init__(self,xcoord=0,ycoord=0):
#         self.x=xcoord
#         self.y=ycoord
#     def setx(self,xcoord):
#         self.x=xcoord
#     def sety(self,ycoord):
#         self.y=ycoord
#     def __str__(self):
#         return f"({self.x},{self.y})"
    
# class Linesegment:
#     def __init__(self,p1=Point(),p2=Point()):
#         self.p1=p1
#         self.p2=p2
#     def setp1(self,p1):
#         self.p1=p1
#     def setp2(self,p2):
#         self.p2=p2
#     def getp1(self):
#         return self.p1
#     def getp2(self):
#         return self.p2
#     def find_distance(self):
#         self.distance=((self.p1.x-self.p2.x)**2+(self.p1.y-self.p2.y)**2)**0.5
#         return self.distance
#     def __gt__(self,anotherpoint):
#         return self.find_distance() > anotherpoint.find_distance()
    
# ls1 = Linesegment(Point(0,0), Point(3,4))  
# ls2 = Linesegment(Point(1,1), Point(4,5)) 
# print(ls1.find_distance())
# print(ls1 > ls2)

# class DistanceFinder:
#     def find_distance(self,p=Point()):
#         distance=((self.x-p.x)**2+(self.y-p.y)**2)**0.5
#         return distance
    
# class Point(DistanceFinder): pass

    
# def avg(x):
#     try:
#         assert len(x)!=0
#         return sum(x)/len(x)
#     except AssertionError:
#         print("no grade data")
# print(avg([3,4,2]))
# avg([])

# class circle:
#     def __init__(self,r):
#         self.radius=r
#     def area(self):
#         try:
#             assert self.radius>0
#             return 3.14*self.radius*self.radius
#         except AssertionError:
#             return "invalid radius"
# c=circle(-2)
# print(c.area())
    
# def pretty_print_list(items):
#     assert isinstance(items, list), "Input must be a list"
#     assert len(items) > 0, "List cannot be empty"
    
#     for index, item in enumerate(items, start=1):
#         print(f"{index}. {item}")

# # Example usage:
# # fruits = ["Apple", "Banana", "Orange"]
# # fruits=[]
# fruits="3"
# pretty_print_list(fruits)

'''
Assume there is a file called 'my_file.txt' which contains a list of integers, for example
[1,22,34].
The following code opens this file in read mode, reads the list, and prints the contents along with
the total number of integers in the list on screen.
f=open('my_file.txt')
content=eval(f.read())
print(content)
print('Total integers in the list are',len(content))
f.close()

Modify this code to handle the following possible errors through try-except code:
 FileNotFoundError, if the file does not exist.
 Assert that file is not empty, otherwise print the message 'File is empty'.
 Assert that contents of the file are in list form, otherwise print the message 'File does
not contain a list'.
'''
# try:
#     f=open('my_file.txt')
#     content=eval(f.read())
#     assert content!=""
#     assert isinstance(content,list)
#     print(content)
#     print('Total integers in the list are',len(content))
#     f.close()
# except FileNotFoundError:
#     print("file is not found!")
# except AssertionError:
#     print("file is empty")
# except AssertionError:
#     print("file doesn't have a list")


# try:
#     f() # Function f can raise an exception
# except Exception:
#     print(1)
# except ValueError:
#     print(2)