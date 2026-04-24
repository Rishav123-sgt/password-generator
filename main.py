import random
import string

class PasswordGenerator:
    def __init__(self, length=12):
        self.length = length

    def generate(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password

if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        generator = PasswordGenerator(length)
        print("\nGenerated Password:", generator.generate())
    except ValueError:
        print("Please enter a valid number.")
