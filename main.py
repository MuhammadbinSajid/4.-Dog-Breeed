class Dog:
    # Class variable
    species = "Canis lupus familiaris"

    def __init__(self, name, breed):
        """Initialize the dog with a name and breed."""
        self.name = name  # Instance variable
        self.breed = breed  # Instance variable

    def display_details(self):
        """Display the details of the dog."""
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")

# Create instances of Dog
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

# Display details of the dogs
print("Details of Dog 1:")
dog1.display_details()

print("\nDetails of Dog 2:")
dog2.display_details()
