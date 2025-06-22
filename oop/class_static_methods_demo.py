class Calculator:
    Calculation_type  = "Arithmetic Operation"

    @staticmethod
    def add (a, b):
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        print(f"Calcualtion type: {cls.Calculation_type}")
        return a * b