# print("sarthak")
# name = 'sarthak'
# print(name[0:4])            #slicing
# print(name.upper())         #upper
# print(name.lower())         #lower
# print(name.title())        # capital first word
# print(name.capitalize()) # capital first word
# print(name.casefold()) # all small
# print(name.count('a')) #count thr number of elements
# last_name = "maan"
# print(name + " " + last_name)    #joining two variables
# print("a" in  name)

# _name = 'MAAN'
# age = 20
# AGE = 22
# print(_name)
# print(age)
# print(AGE)
# print(type(_name))
# print(len(name))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> LIST : collection of items , mutable , indexed , heterogenous
# my_list = [1,2,3,4,5,6, "sarthii" , "sart"]
# print(my_list)
# print(len(my_list))

# print(type(my_list))

# print(my_list[2])

# print(my_list[2:6])

# my_list.append("maan")
# print(my_list)

# my_list.insert(2 , "abc")
# print(my_list)

# my_list.extend([1,5,2])
# print(my_list)


# my_list.pop()
# print(my_list)

# my_list.remove("abc")
# print(my_list)

# del my_list[0]
# print(my_list)

# my_list2 = [2 , 3 ,4.0 ,9 ,7,6]
# my_list2.sort()
# print(my_list2)
# print(max(my_list2))
# my_list2.reverse()
# print(my_list2)

# Tuple : ordered and unchangeable i.e immutable 
my_tuple = ("apple" , "banana" , "cherry" , "date" , "elephant" , "fruit"  , "grapes")
print(my_tuple)
print(len(my_tuple))
print(type(my_tuple))
print(my_tuple[2])
print(my_tuple[2:6])

#tuple unpacking
a,b,c = (1,2,3)
print(a)
print(b)
print(c)
print(a,b,c)

#homework
# my_list1 = [2,3,4,4,5,6,"hello"]
# print(my_list1[6])

#Dictionary -> mutable , unique keys , 

student = {"name" : ["Sarthak" , "MAAN"] , "class" : "4th year" , "address" : "karnal"}
print(student)
print(type(student))
print(len(student))
print(student["name"])
print(student.keys())
print(student.values())


#SETS -> 
my_set = {"hello" , "same" , "from" , "my" , "side"}
print(my_set)
print(len(my_set))
print(type(my_set))
my_set.add(100)
print(my_set)
my_set.update([11,12,13])
print(my_set)
my_set.discard(12)
print(my_set)


