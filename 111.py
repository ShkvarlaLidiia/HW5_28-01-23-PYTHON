db = [{'name': 'Piter', 'age': '20'}, {'name': 'Bob', 'age': '55'}]
print(db)
val = "Piter"
key = "name"
x1 = db[0]
x2 = db[1]
y = x1.values()
z = x1.keys()
g = x1.get(key)
# print(x)
# print(y)
print(z)
# print(g)

a = x1.get(key)
b = x2.get(key)

print(a, b)











# key = input("enter key ")
# value = input("enter value ")
# valueNew = input("enter new value ")
# i = 1
# for el in db:   
#     print(i)
#     if el.get(key) == value:
#         el[key] = valueNew
#     i += 1
# print(db)    


# key = input("enter key ")
# value = input("enter value ")
# valueNew = input("enter new value ")
# for el in db:   
#     if value in el.values():
#         el.update({key:valueNew})
#     else:
#         print("нема такого")

# print(db)        

# ВИДАЛЕННЯ зі СПИСКУ
# print(db)
# for el in db:
#     print(el.values())
#     if "Bob" in el.values():
#         db.remove(el)

# print(db)

# РЕДАГУВАННЯ ЗАДАНОГО ЗНАЧЕННЯ

# key = "name"
# old = "Piter"
# new = "QQQ"

# for el in db:
#     if old in el.values():
#         el.update({key:new})

# print(db)


# ДРУГИЙ  ВАРІАНТ

# while True:
    
#     question = "Do you want to delete an user 'y/Y' if not 'n/N'"
#     if input(question).lower() == "y":
#         pos = int(input("enter position "))
#         db.pop(pos)
#         print(db)

#     question = "Do you want to edit an user 'y/Y' if not 'n/N'"
#     if input(question).lower() == "y":
#         key = input("enter key ")
#         value = input("enter value ")
#         valueNew = input("enter new value ")
#         for el in db:
#             if value in el.values():
#                 el.update({key:valueNew})
#             else:
#                 print("нема такого")
        
#         print(db)        
#     else:
#         print(db)
#         break

