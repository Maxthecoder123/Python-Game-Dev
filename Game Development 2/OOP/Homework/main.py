class Students():
    # properties
    def __init__(self,name,age,address,grade):
        self.name = name
        self.age = age
        self.address = address
        self.grade = grade

    # functions
    def conformName(self):
        response = input("Is your students name John (y/n): ")
        if response == "y":
            print("Your specification is registered")
        else:
            question = input("What is your students name?: ")
            self.name = question
            print("Your students name has been registerd as", self.name)


# Creating object outside of the class
student1 = Students("John Smith",16,"6 Oxford Road",[90,84,79,82,91])
print(student1)

student2 = Students("Poppy",17,"23 Mail Street",[91,88,71,89,99])
print(student1)

# Calling fuction for the object
student1.conformName()
student2.conformName()
