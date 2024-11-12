# def calculate_age(birth_year):
#     """
#     Calculate the age based on the birth year.

#     Args:
#         birth_year: The year of birth.

#     Returns:
#         The calculated age.
#     """
#     current_year = 2024  # Replace with the actual current year
#     return current_year - birth_year


# # لیستی از دیکشنری‌ها برای ذخیره اطلاعات افراد
# people = [
#     {"first_name": "mahdi", "last_name": "kaviani", "birth_year": 2003},
#     {"first_name": "melika", "last_name": "ahmadian", "birth_year": 2003},
#     {"first_name": "mahshid", "last_name": "nemati", "birth_year": 2005},
#     {"first_name": "zahra", "last_name": "taheri", "birth_year": 2001},
# ]


# # نمایش نام کامل افراد با حروف بزرگ
# for person in people:
#     full_name = f"{person['first_name']} {person['last_name']}"
#     print(full_name.upper())


# # محاسبه سن و میانگین سن
# ages = [calculate_age(person["birth_year"]) for person in people]
# average_age = sum(ages) / len(ages)
# print(f"میانگین سن: {average_age:.2f}")


# name = input("What is your name? ")
# letter_count = len(name)
# print("Your name has", letter_count, "letters.")


# # Assuming the program is run in 2023 (can be adjusted if needed)
# current_year = 2024

# # Get user input for birth year
# birth_year = int(input("Enter your year of birth: "))

# # Calculate age in 2022
# age = current_year - birth_year

# # Display the result
# print(f"In 2024 , you would have been {age} years old.")


# m = "Hello, world"

# def average(a, b):
#     m = (a + b) / 2
#     return m
# x = average(1, 2)

# print(m) # prints "Hello, world"


### starting own codes###

# x = int(input("Pleas enter your first number "))
# y = int(input("Now pleas enter your secend number "))
# sum_xy = x + y
# minus_xy = x - y
# multiplication_xy = x * y
# # division_xy = x / y
# if y == 0:
#     division_xy = "Can not divide by zero"
# else:
#     division_xy = x / y
# print(
#     f"SUM = {sum_xy}, MINUS = {minus_xy}, MULTIPLICATION = {multiplication_xy}, DIVISION = {division_xy}"
# )


# import logging

# # Set up logging configuration
# logging.



# def calculator():
#     x = int(input("Please enter your first number: "))
#     y = int(input("Now please enter your second number: "))
    
#     sum_xy = x + y
#     minus_xy = x - y
#     multiplication_xy = x * y
    
#     if y == 0:
#         division_xy = "Cannot divide by zero"
#     else:
#         division_xy = x / y
    
#     print(f"SUM = {sum_xy}, MINUS = {minus_xy}, MULTIPLICATION = {multiplication_xy}, DIVISION = {division_xy}")

# # Call the calculator function
# calculator()



# import tkinter as tk
# from tkinter import messagebox

# def calculator():
#     def calculate():
#         try:
#             x = float(entry_x.get())
#             y = float(entry_y.get())
            
#             sum_xy = x + y
#             minus_xy = x - y
#             multiplication_xy = x * y
            
#             if y == 0:
#                 division_xy = "Cannot divide by zero"
#             else:
#                 division_xy = x / y
            
#             result_label.config(text=f"SUM = {sum_xy}\nMINUS = {minus_xy}\nMULTIPLICATION = {multiplication_xy}\nDIVISION = {division_xy}")
#         except ValueError:
#             messagebox.showerror("Error", "Please enter valid numbers")

#     # Create the main window
#     window = tk.Tk()
#     window.title("Calculator")
#     window.geometry("300x250")

#     # Create and place widgets
#     tk.Label(window, text="Enter first number:").pack(pady=5)
#     entry_x = tk.Entry(window)
#     entry_x.pack(pady=5)

#     tk.Label(window, text="Enter second number:").pack(pady=5)
#     entry_y = tk.Entry(window)
#     entry_y.pack(pady=5)

#     calculate_button = tk.Button(window, text="Calculate", command=calculate)
#     calculate_button.pack(pady=10)

#     result_label = tk.Label(window, text="")
#     result_label.pack(pady=10)

#     # Start the GUI event loop
#     window.mainloop()

# # Call the calculator function
# calculator()




# import tkinter as tk
# from tkinter import messagebox
# import math

# def calculator():
#     def calculate():
#         try:
#             x = float(entry_x.get())
#             operation = operation_var.get()
            
#             if operation != "sqrt":
#                 y = float(entry_y.get())
            
#             if operation == "add":
#                 result = x + y
#             elif operation == "subtract":
#                 result = x - y
#             elif operation == "multiply":
#                 result = x * y
#             elif operation == "divide":
#                 if y == 0:
#                     result = "Cannot divide by zero"
#                 else:
#                     result = x / y
#             elif operation == "power":
#                 result = x ** y
#             elif operation == "sqrt":
#                 if x < 0:
#                     result = "Cannot calculate square root of negative number"
#                 else:
#                     result = math.sqrt(x)
            
#             result_label.config(text=f"Result: {result}")
#         except ValueError:
#             messagebox.showerror("Error", "Please enter valid numbers")

#     def update_entry_y_state(*args):
#         if operation_var.get() == "sqrt":
#             entry_y.config(state="disabled")
#         else:
#             entry_y.config(state="normal")

#     # Create the main window
#     window = tk.Tk()
#     window.title("Advanced Calculator")
#     window.geometry("400x400")

#     # Create and place widgets
#     tk.Label(window, text="Enter first number:").pack(pady=5)
#     entry_x = tk.Entry(window)
#     entry_x.pack(pady=5)

#     tk.Label(window, text="Enter second number:").pack(pady=5)
#     entry_y = tk.Entry(window)
#     entry_y.pack(pady=5)

#     # Operation selection
#     operation_var = tk.StringVar(window)
#     operation_var.set("add")  # default value
#     operation_var.trace("w", update_entry_y_state)

#     operations = [
#         ("Add", "add"),
#         ("Subtract", "subtract"),
#         ("Multiply", "multiply"),
#         ("Divide", "divide"),
#         ("Power", "power"),
#         ("Square Root", "sqrt")
#     ]

#     tk.Label(window, text="Select operation:").pack(pady=5)
#     for text, value in operations:
#         tk.Radiobutton(window, text=text, variable=operation_var, value=value).pack(anchor='w')

#     calculate_button = tk.Button(window, text="Calculate", command=calculate)
#     calculate_button.pack(pady=10)

#     result_label = tk.Label(window, text="")
#     result_label.pack(pady=10)

#     # Start the GUI event loop
#     window.mainloop()

# # Call the calculator function
# calculator()