class Calculator:
    calculation_type  = "Arithmetic Operations"

    @staticmethod
    def add (a, b):
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        print(f"Calcualtion type: {cls.Calculation_type}")
        return a * b