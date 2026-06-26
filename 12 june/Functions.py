#functions in python

def prints():
    print("Welcome students")
print()

#function with parameters:

def add(a,b):
    print(a+b)

add(10,20)

#recursion:

def factorials(n):
    if n==1:
        return 1
    return n*factorials(n-1)
print(factorials(1))
print(factorials(5))

#sum of numbers

def total(n):
    if n==0:
        return 0
    return n+total(n-1)

print(total(5))

#lamada function

square=lambda x:x*x
print(square(5))

#map()

num=[1,2,3,4,5,6,7,8,9,10]
result=list(map(lambda x:x%2!=0,num))
print(result)

result1=list(map(lambda x:x*2,num))
result2=list(filter(lambda x:x%2==0,num))

#global keyword

x=10
def show():
    print(x)
    show()

#computer

count=0
def increment():
    global count
    count+=1

increment()
increment()
print(count)

#function scope with global

def greet():
    global count
    count=0
def increment():
    global count
    count+=1
print(count)

greet()
increment()
increment()

#tnrn classification

#TNRN
def greet():
    print("welcome students")
greet()

#TSRN

def add(a,b):
    print("addition:",a+b)
add(10,10)

#TNRS
def message():
    return"hello students"
print(message())

#TSRS
def multi(a,b):
    return a*b
print(multi(4,5))
