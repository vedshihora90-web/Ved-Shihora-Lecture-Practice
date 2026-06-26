#type casting
#type casting mean coverting one data type into onther data type.

num=10
result=float(num)
print(result)
print(type(result))

#constructor

# __init__().

class student:
    def __init__(self,name):
        self.name=name
        
s1=student("zeel")
print(s1.name)

#delete keywoed(del)

x=100
print(x)
del x
#print(x)

#list
numbers=[10,20,30]
del numbers[0]
print(numbers)

#dictionary

student={"name":"raj",
                "age":19,
                "course":"python"}

print(student)
del student["age"]
print(student)


