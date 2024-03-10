# se realizan cambios mas complejos a main.py
class Calculator:
    def add_numbers(self, a, b):
        return a + b

def main():
    calculator = Calculator()
    result = calculator.add_numbers(2, 3)
    print(f"El resultado es: {result}")

if __name__ == '__main__':
    main()
