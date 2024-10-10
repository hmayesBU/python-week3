# Practicing Lists, Tuples and Sets
'''
my_list = [26, "Birthday", 5.2, 1970, "2nd wind"]
print(len(my_list))
my_list.append("August")
my_list.insert(0,"Wednesday's Child")
print(my_list)
my_list.remove("2nd wind")
print(my_list)
print(my_list[0])
my_list[1] = "My Birthday"
print(my_list)
print(type(my_list))
my_tuple = tuple(my_list)
print(type(my_tuple))
print(my_tuple[0])
print(len(my_tuple))
#my_tuple[0] = "Wednesday"
my_second_tuple = (5,13,24)
joined_tuple = my_tuple + my_second_tuple
print(joined_tuple)
my_joined_list = list(joined_tuple)
print(type (my_joined_list))
my_set = set(my_joined_list)
len(my_set)
my_set.add("Random")
print(my_set)
my_set.add(1970)
print(my_set)
my_second_set = {1,3,24}
commen_set = my_set & my_second_set
print(commen_set)
'''

# Practicing Dictionaries
car_details = {"car_make":"Toyota", "car_model":"Corolla"}
print(car_details)
make = car_details["car_make"]
print(car_details)
car_details["year"] = 2024
print(car_details)
car_details["colour"] = "Red"
print(car_details)
del car_details["colour"]
print(car_details)