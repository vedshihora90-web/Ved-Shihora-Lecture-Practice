#phthon mutable and immutable data types
#in phthone every value is stored as an object
#mutable object:can be change after criation
#immutable object:can not be change after criation

#concept
"  memory manegement ,variable behaviour ,function argument ,performens,debugging,learning objectives"

#everything in phthon is an object
x=10
name ="python"
numbers=[1,2,3,4]

#each object has:value ,type,memory address.

x=15
y=16
print(id(x))
print(id(y))

#int


x=15
print("befor id:",id(x))
y=x+1
print("after id:",id(y))

#string
name="python"

#mutable list
numbers=[1,2,3,4,5,6]

print("before:",numbers)
print("before id:",id(numbers))

numbers.append(7)

print("after:",numbers)
print("after id:",id(numbers))

#mutable ditionary
person={"name":"vivek",
        "age":32 }
print(person)

person ["age"]=33
print(person)

#string
a_str="ved shihora"
print(a_str)

print(a_str[0])
print(a_str[6])
print(a_str[0:3])

#set data types
basket={'apple','banana','kivi','gavava','mango'}
print(basket)
a=set('xtgfctes')
b=set('gcfcyu')
print(a)
print(b)


















