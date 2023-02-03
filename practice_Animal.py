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

    def delAnimal(db, pos):
        db.pop(pos)


    def editAnimal(db, val, valNew):
        for el in db:
            for k in el.keys():
                if el[k] == val:
                    key = k  
            if el.get(key) == val:
                el[key] = valNew

    # можна так:
    #     if val in el.values():
    #         el.update({key:valNew})

    def createAnimalProperties(Animal):

        while True:

            question = "If you wanna continue press 'y/Y' if not 'n/N'"

            if input(question).lower() == "y":
                key = input("Enter key name: ")
                Animal[key] = input(f"Enter your {key} : ")

            else:
                appendToDB(data_base, Animal)
                print(data_base)
                break

    print("Hello , Animal")

    while True:
        question = "Do you want to create an Animal 'y/Y' if not 'n/N'"
        if input(question).lower() == "y":
            Animal = createAnimal()

            question2 = "Do you want to add some props 'y/Y' if not 'n/N'"
            if input(question2).lower() == "y":
                createAnimalProperties(Animal)

                question = "Do you want to delete an Animal 'y/Y' if not 'n/N'"
                if input(question).lower() == "y":
                    pos = int(input("enter position: "))
                    delAnimal(data_base, pos)
                    print(data_base)

                question = "Do you want to edit an Animal 'y/Y' if not 'n/N'"
                if input(question).lower() == "y":
                    # pos = int(input("enter position: "))  можна без індексу!
                    # key = input("enter key ")  і можна без ключа!
                    val = input("enter value ")
                    valNew = input("enter new value ")
                    editAnimal(data_base, val, valNew)
                    print(data_base)
        else:
            print(data_base)
            break

run()

