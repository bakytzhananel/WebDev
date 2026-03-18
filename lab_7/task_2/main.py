from models import Animal, Dog, Cat

def main():
    # Create objects
    animal = Animal("Generic", 5, "gray")
    dog = Dog("Buddy", 3, "brown", "Labrador")
    cat = Cat("Misty", 2, "white", True)

    # Store in list
    animals = [animal, dog, cat]

    # Iterate and demonstrate polymorphism
    for a in animals:
        print(a)                 # __str__
        print(a.speak())         # polymorphism
        print(a.info())          # parent method
        print("-----")

    # Call unique methods
    print(dog.fetch())
    print(cat.sleep())


if __name__ == "__main__":
    main()
