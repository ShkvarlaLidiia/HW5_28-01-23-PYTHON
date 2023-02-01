def run():

    data_base = []

    def appendToDB(db, obj):
        db.append(obj)

    def createUser():
        return {}

    def delUser(db, pos):
        db.pop(pos)




    def editUser(el, val, key, valNew):
        if val in el.values():
            el.update({key:valNew})
        else:
            print("нема такого")




    def createUserProperties(user):

        while True:

            question = "If you wanna continue press 'y/Y' if not 'n/N'"

            if input(question).lower() == "y":
                key = input("Enter key name: ")
                user[key] = input(f"Enter your {key} : ")

            else:
                appendToDB(data_base, user)
                print(data_base)
                break

    print("Hello , user")

    while True:
        question = "Do you want to create an user 'y/Y' if not 'n/N'"
        if input(question).lower() == "y":
            user = createUser()

            question2 = "Do you want to add some props 'y/Y' if not 'n/N'"
            if input(question2).lower() == "y":
                createUserProperties(user)

                question = "Do you want to delete an user 'y/Y' if not 'n/N'"
                if input(question).lower() == "y":
                    pos = int(input("enter position: "))
                    delUser(data_base, pos)
                    print(data_base)

                question = "Do you want to edit an user 'y/Y' if not 'n/N'"
                if input(question).lower() == "y":
                    pos = int(input("enter position: "))
                    key = input("enter key ")
                    val = input("enter value ")
                    valNew = input("enter new value ")
                    for el in data_base:
                        editUser(el, val, key, valNew)

                    print(data_base)
        else:
            print(data_base)
            break

run()

