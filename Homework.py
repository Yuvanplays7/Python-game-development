#Task 1
student = {

    "name": "Rahul",
    "age": 18,
    "city": "Dheli",
    "class": 12
}

print(student)
#Task 2 
student2={"name":"Priya",
          "age":17 ,
          "marks":85
          }
for value in student2.values():
    print(value)
#Task 3 
car={"brand":"Bmw",
     "color":"neon green"
     }

car["year"]=2024

print(car)

#task 4 
person={"name":"Aman","age":20,"city":"mumbai"}
del person["age"]
person["age"]=21
del person["city"]
person["city"]="pune" 
print(person)
#task5

book={"name":"python basics",
      "author":"jhon",
      "price":500
      }
del book["price"]
print(book)

