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

class Person:
    def __init__(self, name = "John", age = 0, money = 0, health = 100):
        self.name = name
        self.age = age
        self.money = money
        self.health = health

    def __str__(self):
        return f"Person: {self.name}, " \
               f" age: {self.age}, " \
               f" money: {self.money}, ;" \
               f" health: {self.health};" \

    def live_one_year(self):
        self.age += 1
        while True:
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

p = Person("Tailer", 0, 5000, 100)
print(p)
p.live_one_year()
print(p)
