# Dictionary = {'name':'jashan','age':22}
# Set = {'jashan', 22, 'python'}

# Dictionary = {'name':'jashan','age':22, 'course': 'python'}
# Set = {10, 20, 30, 20, 10}
# print(Set)

# Dictionary = {}
# print(Dictionary)

# my_dict = {"name": "Alice", "age": 25}
# print(my_dict["city"])  # KeyError: 'city'

# person = {'name': 'Alice', 'age': 25}

# # Key exists
# print(person.get('name'))       # 'Alice'

# # Key doesn't exist, no default
# print(person.get('city'))       # None

# # Key doesn't exist, with default
# print(person.get('city', 'N/A')) # 'N/A'

# student = {
#     "name" : "Jashan",
#     "age" : 22
# }
# student["city"] = "Bhogpur" #adding new key
# student["age"] = 23       # upding existing key
# print(student)



# student = {
#     "name" : "Jashan",
#     "age" : 22
# }  
# student.pop("age") 
# print(student)

# student = {
#     "name" :"Jashan",
#     "age"  :22
# }  
# for value in student.values():
#     print(value)

# for x in dict → Keys

# for x in dict.values() → Values

# for k, v in dict.items() → Key-Value pairs

# pharmacy = {
#     "fever" : "pacimol",
#     "stomach pain" : "drofit m",
#     "vomiting" : "vomishunt",
#     "acid" : "dsr"

# }
# for key, value in pharmacy.items():
#     print(f"{key}:{value}")


# fruit_set = {"apple", "mango", "banana", "litchi" }
# if "apple" in fruit_set:
#     print("yes,'apple' is in the set. ")

# else:
#     print("No, apple is not in the set.") 

# set = {4, 6, 5, 3}
# set.update([8, 9, 0]) #set.append(8, 9, 0) fails because sets lack append and it expects one element.
# print(set)

# my_set = [4, 9, 9, 7, 3, 4, 6]
# new_set = set(set(my_set))

# print(my_set)
# print(new_set)

# a = {1, 2, 3}
# b = {3, 4, 5}
# result = a.union(b)
# print(result)


# a = {1, 2, 3}
# b = {3, 4, 5}
# result = a.intersection(b)
# print(result)

# a = {1, 2, 3}
# b = {3, 4, 5}
# result = a.difference(b)
# print(result)

# a = {1, 2, 3}
# b = {3, 4, 5}
# result = b.difference(a)
# print(result)

# a = {1, 2, 3}
# b = {3, 4, 5}
# result = b.symmetric_difference(a)
# print(result)

# Dictionary comprehension: numbers 1-5 and their squares

# squares = {n: n**2 for n in range(1,6)}
# print(squares)

# vowels = {char for char in "programming" if char in 'aeiou'}
# print(vowels)

# consonants = { char for char in "python" if char not in "aeiou"}
# # print(consonants)

# subjects = {
#     "english" : 78,
#     "math"    : 60,
#     "hindi"   : 99,
#     "science" : 88
# }
# print(subjects.get("hindi", "not found"))
# print(subjects.get("physics", "not found"))

# Write a short program that counts how many times each word appears in a list using a dictionary

# medicines = ['vomishunt', 'comon', 'metrofur', 'vomishunt', 'pacimol', 'enteroquinol', 'dsr', 'dsr',
#             'pacimol', 'vomishunt']
# medicine_count = {}
# for medicine in medicines:
#     medicine_count[medicine] = medicine_count.get(medicine, 0) + 1
    
# print(medicine_count)

# orders = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 
#           'mango', 'banana', 'orange', 'apple']
# fruit_count = {}
# for fruits in orders:
#     fruit_count[fruits] = fruit_count.get(fruits, 0) + 1
# print(fruit_count)    

# Write a real-life example where a set is better than a list.
# available_medicine = {'paracetamol', 'ciprofoxacin', 'amoxicillin', 'metformin'}
# customer_prescription = ['paracetamol', 'aspirin', 'amoxicillin', 'ibuprofen']

# in_stock = set()
# for med in customer_prescription:
#     if med in available_medicine:
#         in_stock.add (med)

# print(in_stock)        

# medicine_list = ['paracetamol', 'amoxicillin', 'metformin'] * 1000  # 3000 items
# prescription = 'paracetamol'

# # Must scan ALL 3000 items every time!
# if prescription in medicine_list:  # ← 3000 comparisons 😴
#     print("In stock")

# medicine_set = {'paracetamol', 'amoxicillin', 'metformin'}  # Just 3 unique
# prescription = 'paracetamol'
# # Hash lookup = instant!
# if prescription in medicine_set:  # ← 1 operation ⚡
#     print("In stock")
# Sets = hash tables = direct access. || Lists = arrays = sequential scan. Pharmacy cashiers need SET speed! 🏥🚀

