def safe_divide(numerator, denominator):
    try: 
        num1 = float(numerator)
        num2 = float(denominator)
        try:
            result = num1 / num2
            return f"Result: {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    except ValueError: 
        return "Error: Please enter numeric values only."