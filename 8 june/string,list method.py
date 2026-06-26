#string formating
name="alisha"
age=27

#f-string
print(f"my name is {name} and i am {age} years old.")

#using format()
print("my name is {}and i am {}years old.".format(name,age))

#using% formating
print("my name is %s and i am %d years old."%(name,age))

price=199.6557
'''
#decimal values
print(f"price:{price}")
print{f"price:{price.2f}"}'''

#list and tuple(basics and mutability)

#list mutable
my_list=[10,20,30]
print(my_list)
my_list[1]=99
print(my_list)
my_list.append(40)
print(my_list)
my_list.remove(99)
print(my_list)

#tupple imutable
my_tuple=[10,20,30,40]
print(my_tuple)

#indexing nd slicing

text="python"
#indexing
print("first letter is:",text[0])
print("last letter is:",text[-1])

#slicing
print("first three letter is:",text[0:3])
print("last three letter is:",text[-3:])
print("every second letter is:",text[::2])

#reverse string
print("reverse string:",text[::-1])

#using list with slicing and formatting
students=["amit","vivek","raj","sweta"]
print("first two students is:",students[:2])

#loop through list
for student in students:
    print(f"welcome {student}")

#list student
print("total student:",len(students))

#checking element
print("sara is present?","sara"in students)

#nested list
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
print("matrix:",matrix)
print("middle element:",matrix[1][1])

#string methods

message="python programing language"
print("uppercase:",message.upper())
print("lowercase:",message.lower())
print("capitalized:",message.capitalize())
print("replace:",message.replace("python","html"))
print("split:",message.split())

#list method

num=[1,2,3,4,5]
num.sort()
print(num)
num.reverse()
print(num)
num.insert(1,100)
print(num)

#tuple packing and unpcking
person=("alisha",21,"india")
#unpacking
name,age,country=person
print(name)
print(age)
print(country)



