fruits={"apple":"red","banana":"yellow","orange":"orange","mango":"green","water melon":"red"}
print(fruits)
for key,value in fruits.items():
    print(f"{key}:{value}")

for value in fruits.values():
    print(value)

fruits["pineapple"] = "yellow"
print(fruits)

fruits.pop("orange")
print(fruits)