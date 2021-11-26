'''
Data Structures

list - sequence of mutable values
tuple - sequence of immutable values
set - collection of unique values
dict - collection of key-value pairs
...

'''
# list
names = ["Harry", "Ron", "Hermione", "Ginny"]
names.append("Draco")
names.sort()
print(names)

# tuple:
coordinateX = 10.0
coordinateY = 20.0
coordinate = (coordinateX, coordinateY)
print(coordinate)

# set
s = set() # create an empty set
s.add(1) # add elements to set
s.add(2)
s.add(3)
s.add(4)
s.add(1)
s.remove(2)
print(s)
print(f"The set has {len(s)} elements.")

# dictionary
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
houses["Hermione"] = "Gryffindor"
print(houses)

