# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Invalid operation"



# # num1 = 10.3
# # num2 = 20.4
# # string = "Wisdom Darlington Ndata"
# def perform_operation():
#     print("Arithmetic Operations")
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     operation  = input("Enter ther operation (add, substract, multiply, divide: )").strip().lower()


#     if operation == "add":
#         return num1 + num2
#     elif operation == "subtract":
#         return num1 - num2
#     elif operation == "multiply":
#         return num1 * num2
#     elif operation == "divide":
#         # if num1 / num2 == 0:
#         if num2 == 0:
#             return "Not Divisible"
#         else:
#             return "Invalid Operation"

        
# result = perform_operation()
# print(f"Result: {result}")

    

    