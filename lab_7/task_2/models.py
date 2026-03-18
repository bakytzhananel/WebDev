
class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        return "Some sound"

    def info(self):
        return f"{self.name} is {self.age} years old"

    def __str__(self):
        return f"Animal(Name: {self.name}, Age: {self.age}, Color: {self.color})"


# Child Class 1
class Dog(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed

    def speak(self):  # override (polymorphism)
        return "Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball"

    def __str__(self):
        return f"Dog(Name: {self.name}, Breed: {self.breed})"


# Child Class 2
class Cat(Animal):
    def __init__(self, name, age, color, is_lazy):
        super().__init__(name, age, color)
        self.is_lazy = is_lazy

    def speak(self):  # override
        return "Meow!"

    def sleep(self):
        return f"{self.name} is sleeping"

    def __str__(self):
        return f"Cat(Name: {self.name}, Lazy: {self.is_lazy})"
