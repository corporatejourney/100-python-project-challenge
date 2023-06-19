class Calculator:
    """
    This is a calculator class.
    """

    def __init__(self, first_number, second_number, operator):
        """
        Initializes the Calculator object with two numbers and an operator.

        Parameters:
        - first_number (int): The first number.
        - second_number (int): The second number.
        - operator (str): The operator (+, -, *, /).

        Returns:
        - None
        """
        self.fnumber = first_number
        self.snumber = second_number
        self.operator = operator

    def addition(self):
        """
        Performs addition of two numbers.

        Returns:
        - int: The result of the addition operation.
        """
        if self.operator == "+":
            return self.fnumber + self.snumber

    def subtraction(self):
        """
        Performs subtraction of two numbers.

        Returns:
        - int: The result of the subtraction operation.
        """
        if self.operator == "-":
            return self.fnumber - self.snumber

    def multiplication(self):
        """
        Performs multiplication of two numbers.

        Returns:
        - int: The result of the multiplication operation.
        """
        if self.operator == "*":
            return self.fnumber * self.snumber

    def division(self):
        """
        Performs division of two numbers.

        Returns:
        - float: The result of the division operation.
        """
        if self.operator == "/":
            return self.fnumber / self.snumber


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operator = input("Enter the operator: ")

cal = Calculator(first_number, second_number, operator)
result = None

if operator in ["+", "-", "*", "/"]:
    #Instead of using explicit if-else statements, getattr is used to dynamically call the method based on the operator.
    result = getattr(cal, operator)()

if result is not None:
    print("Result:", result)
else:
    print("Invalid operator. Please enter a valid operator (+, -, *, /).")
