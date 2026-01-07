# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.area = self.width * self.height
#         print(f"Rectangle(width={self.width}, height={self.height}, area={self.area})")

# # Rectangle(4, 5)

# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#         print(f"Square(side={self.width}, area={self.area})")
    
# Square(4)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def print_name(self):
#         print(f"Name: {self.name}")
    
#     def print_age(self):
#         print(f"Age: {self.age}")

# class Student:
#     def __init__(self, student_id, roll_number):
#         self.student_id = student_id
#         self.roll_number = roll_number
    
#     def print_student_info(self):
#         print(f"Student ID: {self.student_id}, Roll Number: {self.roll_number}")

# class Resident(Person, Student):
#     def __init__(self, name, age, student_id, roll_number):
#         Person.__init__(self, name, age)
#         Student.__init__(self, student_id, roll_number)
    
#     def print_info(self):
#         self.print_name()
#         self.print_age()
#         self.print_student_info()

# resident = Resident("John Doe", 20, "S12345", 101)
# resident.print_info()

class Hospital:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Doctor(Hospital):
    def __init__(self, name, address, specialization):
        super().__init__(name, address)
        self.specialization = specialization
    
    def __str__(self):
        return f"Doctor: {self.name}, Specialization: {self.specialization}"

class Patient(Hospital):
    def __init__(self, name, address, disease):
        super().__init__(name, address)
        self.disease = disease
    
    def __str__(self):
        return f"Patient: {self.name}, Disease: {self.disease}"

class MedicalTest:
    def __init__(self, doctor, patient, test_name, test_result):
        self.doctor = doctor
        self.patient = patient
        self.test_name = test_name
        self.test_result = test_result
    
    def display_test_info(self):
        print("Medical Test Information:")
        print(self.doctor)
        print(self.patient)
        print(f"Test Name: {self.test_name}")
        print(f"Test Result: {self.test_result}")

doc = Doctor("Dr. Smith", "123 Hospital St", "Cardiology")
patient = Patient("Jane Doe", "456 Patient Ave", "Heart Condition")
test = MedicalTest(doc, patient, "ECG", "Normal")
test.display_test_info()


# class A(object):
#     def immn(self):
#         print("in a")

# class B(object):
#     def immn(self):
#         print("in b")

# class X(A, B):
#     def immn(self):
#         print("in x")

# class Y(B, A):
#     def immn(self):
#         print("in y")

# class Z(X, Y):
#     def immn(self):
#         print("in z")

# obj = Z()
# print(Z.mro())
# obj.immn()

# class A(object):
#     def immn(self):
#         print("in a")

# class B(object):
#     def immn(self):
#         print("in b")

# class X(A, B):
#     def immn(self):
#         print("in x")

# class Y(A, B):  # Changed from (B, A) to (A, B) to match X
#     def immn(self):
#         print("in y")

# class Z(X, Y):
#     def immn(self):
#         print("in z")

# obj = Z()
# print(Z.mro())
# obj.immn()  # Output: "in z"