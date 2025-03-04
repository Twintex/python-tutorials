person = {

    "firt_name" : "David",
    "Last_name" : "Bassey",
    "Age" : 45, 
    "Height" : 1.8, 
    "Skin_color" : "Dark",
}

person["Age"] = 56

person["email"] = "david@gmail.com"

del person["Skin_color"]

person["Job"] = "Soft ware dev"

Job = person.pop("Job")

print(Job)