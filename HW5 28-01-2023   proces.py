# 1) Create class Person : name , age = 0 , money , health
# 2) By default health is 100
# 3) Person also has method : live_one_year()
# 4) live_one_year : 1) Will you able to smoke ? 2) Will you be able to drink 3) Will tou be able to use some drugs ?
# 5) if smoke = health - 3 , if drink = health - 8 , if drugs = health - 10
#  else - 1
# add random and make some randomDeather
# every live_one_yeat -> randomDeather
# every live_one_yeat -> if age > 90 : print("Goodbye")
# every live_one_yeat -> if health >= 0 : print("Goodbye") ,but if user has money he might to pay for life , but health can't be over than 100

import random
class Person:
    def __init__(self, name = "John", age = 0, money = 0, health = 100):
        self.name = name
        self.age = age
        self.money = money
        self.health = health

    def __str__(self):
        return f" Person name: {self.name}, " \
               f" age: {self.age}, " \
               f" money: {self.money}, ;" \
               f" health: {self.health};" \

    def toLive(self):
        while True:
            question = "If you wanna continue press 'y/Y' if not 'n/N'"
            if input(question).lower() == "y":
                self.live_one_year()               
            else:
                print(p)
                print("Bye")
                break       

    def live_one_year(self):
        randomDeather = random.randint(1, 90)
        print("randomDeather = ", randomDeather)
        self.age += 1
        print("Age = ", self.age)

        while True:
            if self.age > 90 or self.age == randomDeather:
                print("Goodbye 1")
                break
            if self.health <=0 and self.money == 0:
                print("Goodbye 2")
                break
            if self.health <=0 and self.money > 0:
                question = "Do you want to pay for life? press 'y/Y' if not 'n/N'"
                if input(question).lower() == "y":
                    if self.money + self.health <= 100:
                        self.health = self.health + self.money
                        self.money = 0
                        print("money =  {}, health = {}".format(self.money, self.health))
                    elif self.money + self.health > 100:
                        self.health = 100
                        self.money = 0
                        print("money =  {}, health = {}".format(self.money, self.health))
                else:
                    print("Goodbye 3")
                    break

            question1 = "Will you able to smoke? press 'y/Y' if not 'n/N'"
            question2 = "Will you be able to drink? press 'y/Y' if not 'n/N'"
            question3 = "Will tou be able to use some drugs? press 'y/Y' if not 'n/N'"
            if input(question1).lower() == "y":
                self.health -= 3
            if input(question2).lower() == "y":
                self.health -= 8
            if input(question3).lower() == "y":
                self.health -= 10
            else:
                self.health -= 1
            break

        def toLive(self):
            while True:
                question = "If you wanna continue press 'y/Y' if not 'n/N'"
                if input(question).lower() == "y":
                    self.live_one_year()
                else:
                    break

p = Person("Tailer", 75, 500, 100)

print(p)

# p.live_one_year()
# print(p)

p.toLive()
