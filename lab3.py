# class Student:
#     def __init__(self):
#         self.name = None
#         self.roll_number = None
#         self.email_address = None
#         self.courses = {}
#         self.grades = {}
    
#     def student_info(self):
#         self.name = input("Enter name: ")
#         self.roll_number = input("Enter roll number: ")
#         self.email_address = input("Enter email address: ")
    
#     def course_info(self):
#         course_count = int(input("Enter the number of courses: "))
#         for i in range(course_count):
#             course_name = input(f"Enter the name of course {i+1}: ")
#             self.courses[course_name] = None
    
#     def calculate_gpa(self):
#         for course in self.courses:
#             marks = float(input(f"Enter marks for {course}: "))
#             if marks >= 90:
#                 grade = 4.0
#             elif marks >= 80:
#                 grade = 3.5
#             elif marks >= 70:
#                 grade = 3.0
#             elif marks >= 60:
#                 grade = 2.5
#             elif marks >= 50:
#                 grade = 2.0
#             else:
#                 grade = 0.0
#             self.grades[course] = grade
#             print(f"GPA for {course}: {grade}")
    
#     def calculate_cgpa(self):
#         total_grade_points = sum(self.grades.values())
#         total_courses = len(self.grades)
#         cgpa = total_grade_points / total_courses
#         return cgpa
    
#     def display_info(self):
#         print(f"\nName: {self.name}")
#         print(f"Roll Number: {self.roll_number}")
#         print(f"Email Address: {self.email_address}")
#         print("Courses and Grades: ")
#         for course, grade in self.grades.items():
#             print(f"{course}: {grade}")
#         print(f"\nCGPA: {self.calculate_cgpa()}")

# s = Student()
# s.student_info()
# s.course_info()
# s.calculate_gpa()
# s.display_info()


class Student:
    def __init__(self):
        self.name = None
        self.roll_number = None
        self.email_address = None
        self.courses = {}
        self.grades = {}
    
    # Instance method (original)
    def student_info(self):
        self.name = input("Enter name: ")
        self.roll_number = input("Enter roll number: ")
        self.email_address = input("Enter email address: ")
    
    # Instance method (original)
    def course_info(self):
        course_count = int(input("Enter the number of courses: "))
        for i in range(course_count):
            course_name = input(f"Enter the name of course {i+1}: ")
            self.courses[course_name] = None
    
    # Instance method (original)
    def calculate_gpa(self):
        for course in self.courses:
            marks = float(input(f"Enter marks for {course}: "))
            if marks >= 90:
                grade = 4.0
            elif marks >= 80:
                grade = 3.5
            elif marks >= 70:
                grade = 3.0
            elif marks >= 60:
                grade = 2.5
            elif marks >= 50:
                grade = 2.0
            else:
                grade = 0.0
            self.grades[course] = grade
            print(f"GPA for {course}: {grade}")
    
    # Instance method (original)
    def calculate_cgpa(self):
        total_grade_points = sum(self.grades.values())
        total_courses = len(self.grades)
        cgpa = total_grade_points / total_courses
        return cgpa
    
    # Class method (new for Q3)
    @classmethod
    def create_from_existing(cls, existing_student):
        """Alternative constructor that copies data from another student"""
        new_student = cls()
        new_student.name = existing_student.name
        new_student.roll_number = existing_student.roll_number
        new_student.email_address = existing_student.email_address
        new_student.courses = existing_student.courses.copy()
        new_student.grades = existing_student.grades.copy()
        return new_student
    
    # Static method (new for Q3)
    @staticmethod
    def get_grade_letter(gpa):
        """Convert GPA to letter grade"""
        if gpa >= 3.5: return 'A'
        elif gpa >= 2.5: return 'B'
        elif gpa >= 1.5: return 'C'
        elif gpa >= 0.5: return 'D'
        else: return 'F'
    
    # Modified instance method to include letter grades
    def display_info(self):
        print(f"\nName: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Email Address: {self.email_address}")
        print("\nCourses and Grades:")
        for course, grade in self.grades.items():
            letter_grade = self.get_grade_letter(grade)  # Using static method
            print(f"{course}: {grade:.1f} ({letter_grade})")
        cgpa = self.calculate_cgpa()
        print(f"\nCGPA: {cgpa:.2f} ({self.get_grade_letter(cgpa)})")

# Create and display original student (using instance methods)
s1 = Student()
s1.student_info()
s1.course_info()
s1.calculate_gpa()
s1.display_info()

# Demonstrate class method by creating a copy
s2 = Student.create_from_existing(s1)
print("\nCreated a copy of student using class method:")
s2.display_info()

# Demonstrate static method independently
sample_gpa = 3.2
print(f"\nSample GPA {sample_gpa:.1f} converts to: {Student.get_grade_letter(sample_gpa)}")


# class Person:
#     def __init__(self, name, birth_year):
#         self.name = name
#         self.birth_year = birth_year
    
#     @classmethod
#     def calculate_age(cls, birth_year, current_year):
#         return current_year - birth_year
    
#     @staticmethod
#     def is_adult(age):
#         return age > 18
    
#     def display_info(self, current_year):
#         age = Person.calculate_age(self.birth_year, current_year)
#         adult_status = Person.is_adult(age)
#         print(f"Name: {self.name}")
#         print(f"Birth Year: {self.birth_year}")
#         print(f"Age: {age}")
#         print(f"Adult: {adult_status}")

# name = input("Enter name: ")
# birth_year = int(input("Enter birth year: "))
# current_year = int(input("Enter current year: "))
# p = Person(name, birth_year)
# p.display_info(current_year)