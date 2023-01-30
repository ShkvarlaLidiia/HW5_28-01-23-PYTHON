# CREATE PROGRAM

# Animals

# 1) Add new animal into animals array []
# 2) Add property to animal
# 3) Append animal into  array []
# 4) Drop (delete) animal from array []
# 5) Edit animals prop


def run():

    data_base = []

    def appendToDB(db, obj):
        db.append(obj)

    def createAnimal():
        return {}

    def dropAnimal(db, obj):
        db.pop(obj)
       


    def createAnimalProperties(Animal):
        while True:
            question = "If you wanna continue press 'y/Y' if not 'n/N'"
            if input(question).lower() == "y":
                key = input("Enter key name: ")
                Animal[key] = input(f"Enter {key} : ")
            else:
                appendToDB(data_base, Animal)
                print(data_base)
                break       


    while True:
        question = "Do you want to create an Animal 'y/Y' if not 'n/N'"
        if input(question).lower() == "y":
            Animal = createAnimal()

            question2 = "Do you want to add some props 'y/Y' if not 'n/N'"
            if input(question2).lower() == "y":
                createAnimalProperties(Animal)                

                question4 = "Do you want to Edit animals prop 'y/Y' if not 'n/N'"
                if input(question4).lower() == "y":
                    editAnimal = int(input("Enter position to edit: "))
                    keyForEdit = input("key For Edit: ")
                    new = input("enter new value: ")
                    data_base[editAnimal][keyForEdit] = new

                    question3 = "Do you want to Drop (delete) animal from array 'y/Y' if not 'n/N'"
                    if input(question3).lower() == "y":
                        delAnimal = int(input("Enter position to delete: "))
                        dropAnimal(data_base, delAnimal)

                    else:
                        print(data_base)
                        break

run()

