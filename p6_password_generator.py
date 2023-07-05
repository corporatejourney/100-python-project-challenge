import random
import string


class PasswordGenerator:
    """A simple password generator class."""

    def __init__(self) -> None:
        pass

    def generate_password(self,length):
        """
        Geneate a random password of specified length.

        Parameter:
        - length(int): The desired lenght of the password

        Returns:
        -str: The generated password.
        """

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
#Create an instance of the PasswordGenerator class
generator = PasswordGenerator()

#Prompt the user for the desired password length
length = int(input("Enter the desired length for the password:"))

#Generate the password using the class method
password = generator.generate_password(length)

#Print the generated password
print("Generator Password:", password)