class Cars():
    # properties
    def __init__(self,color,seats,value):
        self.color = color
        self.seats = seats
        self.value = value
        self.brand = "BMW" 

    # functions
    def conformBrand(self):
        response = input("Is your car brand a BMW (y/n): ")
        if response == "y":
            print("Your specification is registered")
        else:
            question = input("What is your cars brand?: ")
            self.brand = question
            print("Your brand has been registerd as", self.brand)


# Creating object outside of the class
car1 = Cars("blue",4,"100k")
print(car1)

# Calling fuction for the object
car1.conformBrand()