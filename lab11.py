# # Q1
# class AgeChecker:
#     def __init__(self):
#         try:
#             self.yOEdu=int(input("enter years of education: "))
#             if self.yOEdu<=16:
#                 print("it's not enough!")
#             elif self.yOEdu>16:
#                 print("You are eligible!")
#         except ValueError as e:
#             print(f"Invalid Value: {e}")   

# AgeChecker()     

# Q2
# def smart_division():
#     try:
#         dividend=int(input("enter dividend: "))
#         divisor=int(input("enter divisor: "))
#         print(dividend/divisor)
#     except ZeroDivisionError as e:
#         print(f"Error: {e}")
#     except ValueError as e:
#         print(f"Invalid Value: {e}")   
# smart_division()

# Q3
# def factorial():
#     try:
#         number = int(input("Enter a positive integer: "))
#         if number < 0:
#             raise ValueError("Factorial is not defined for negative numbers")
#         if number == 0:
#             print(1)
#         else:
#             result = 1
#             for i in range(1, number + 1):
#                 result *= i
#             print(f"Factorial of {number} is {result}")
#     except ValueError as e:
#         print(f"Error: {e}")
# factorial()


# class InsufficientEducationError(Exception):
#     pass

# class AgeChecker:
#     def __init__(self):
#         try:
#             self.yOEdu = int(input("Enter years of education: "))
#             if self.yOEdu <= 16:
#                 raise InsufficientEducationError
#             else:
#                 print("You are eligible!")
#         except ValueError:
#             print("Invalid Value (must be an integer)")
#         except InsufficientEducationError:
#             print("Error: It's not enough! (Minimum 16 years required)")
# AgeChecker()