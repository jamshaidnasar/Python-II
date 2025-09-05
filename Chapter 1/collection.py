# Lists

# The list type is probably the most commonly used collection type in Python.
# Despite its name, a list is more like an array in other languages, mostly
# JavaScript. In Python, a list is merely an ordered collection of valid Python values.
# A list can be created by enclosing values, separated by commas, in square brackets:


# Create Lists
intList = [ 1 , 2 , 3 , 4 , 5 , 6, 7]
stringList = [ "Jamshaid" , "Nasar" ]
emptyList = []
mixedList = [ 1, 'abc' , True , 2.34]


# Prints Lists

print(intList)
print(stringList)
print(emptyList)
print(mixedList)


# More About Lists
names = [ "Jamshaid" , "Nasar" , "Olga" , "Janan" , "JK" ]

# vaule one is 0
print(names[0])   # Jamshaid
print(names[1])   # Nasar
print(names[2])   # Olga
print(names[3])   # Janan
print(names[4])   # JK


# from end side names
# Using - Start from -1 not from 0

print(names[-1])  # JK
print(names[-2])  # Janan
print(names[-3])  # Olga
print(names[-4])  # Nasar
print(names[-5])  # Jamshaid


# change the value of in list
# list name and vaule number to change vaule

names[4] = "JO"
print(names)


# add new value in List
# list name and append

names.append("Iqbal")
print(names)


# add value in last with fix position
# value of number after it will that
# new vaule like 5 start from ZERO !!

names.insert(5, "Jamshid")
print(names)


# remove an vaule from list

names.remove("Jamshid")
names.remove("JO")
names.remove("Iqbal")
print("Final List:", names)


# prints len of list
print("Final listLen", len(names))



# Tuples

# A tuple is similar to a list except that it is fixed-length and immutable. So the values in the tuple
# cannot be changed nor the values be added to or removed from the tuple. Tuples are commonly used for
# small collections of values that will not need to change, such as an IP address and port. Tuples are
# represented with parentheses instead of square brackets:

# Tuples can be without brackets
name = "Jamshaid" , "Nasar"
print(name)

# Tuples with brackets also same things
name = ( "Jamshaid" , "Nasar" , "Olga")
print(name)

# print one by one
print(name[0])
print(name[1])
print(name[2])

# Dictionaries in Python

# A dictionary in Python is a collection of key-value pairs. The dictionary is surrounded by curly braces.
# Each pair is separated by a comma and the key and value are separated by a colon.

myAbout = {

  "name" : "Jamshaid" ,
  "age" : 15 ,
  "Height" : 5.64 ,

}

print(myAbout)


name = myAbout["name"]
print(name)


# Set

# A set is a collection of elements with no repeats and without insertion order but sorted order.
# They are used in situations where it is only important that some things are grouped together,
# and not what order they were included. For large groups of data, it is much faster to check whether
# or not an element is in a set than it is to do the same for a list.


nameSet = { "Jamshaid" , "Olga" , "Nasar"}
print(nameSet)

newSet = set(nameSet)
print(newSet)

# That was Our Colletion in PYTHON !!
