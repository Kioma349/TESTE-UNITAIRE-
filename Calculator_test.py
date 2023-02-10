                                        #Exercice 1 

"""
TESTE UNITAIRES 


COMMENTAIRES 
Ses testes couvrent tous les scénarios possibles pour la classe Calculator, 
incluant les opérations valides et les opérations non valides, ainsi que les entrées 
valides et les entrées non valides pour les nombres. Les tests vont garantir que les 
fonctions renvoient les résultats attendus pour les entrées valides 
et lèvent une exception pour les entrées non valides.
"""

class Calculator:
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y


    def power(x, y):
        result = 1
        for i in range(y):
            result *= x
        return result
    def square_root(x):
        if x == 0 or x == 1:
            return x
        val = x
        precision = 0.0000001
        while abs(val - x / val) > precision:
            val = (val + x / val) / 2

        return val

def calculate(operation, x, y):

    if operation == "add":
            result = Calculator.add(x,y)
    elif operation == "substract":
        result = Calculator.subtract(x,y)
    elif operation == "multiply":
            result = Calculator.multiply(x,y)
    elif operation == "divide":
        result = Calculator.divide(x,y)
    elif operation == "power":
        result = Calculator.power(x,y)
    elif operation == "square_root":
        result = Calculator.square_root(x)
    return result



operation = input("Enter the operation you would like to perform (add,subtract, multiply, divide, square_root, power): ")
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the secod number : "))

print(calculate(operation, num1, num2))

#TESTS UNITAIRES
import unittest


class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = Calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = Calculator.subtract(5, 2)
        self.assertEqual(result, 3)

    def test_multiply(self):
        result = Calculator.multiply(2, 3)
        self.assertEqual(result, 6)


    def test_divide(self):
        result = Calculator.divide(6, 2)
        self.assertEqual(result, 3)

    def test_power(self):
        result = Calculator.power(2, 3)
        self.assertEqual(result, 8)

    def test_square_root(self):
        result = Calculator.square_root(4)
        self.assertAlmostEqual(result, 2, delta=0.0001)

    def test_calculate_add(self):
        result = Calculator.calculate("add", 2, 3)
        self.assertEqual(result, 5)

    def test_calculate_subtract(self):
        result = Calculator.calculate("subtract", 5, 2)
        self.assertEqual(result, 3)

    def test_calculate_multiply(self):
        result = Calculator.calculate("multiply", 2, 3)
        self.assertEqual(result, 6)

    def test_calculate_divide(self):
        result = Calculator.calculate("divide", 6, 2)
        self.assertEqual(result, 3)



    def test_calculate_power(self):
        result = Calculator.calculate("power", 2, 3)
        self.assertEqual(result, 8)

    def test_calculate_square_root(self):
        result = Calculator.calculate("square_root", 4)
        self.assertAlmostEqual(result, 2, delta=0.0001)

    def test_calculate_invalid_operation(self):
        with self.assertRaises(ValueError):
            Calculator.calculate("invalid_operation", 2, 3)







                                        