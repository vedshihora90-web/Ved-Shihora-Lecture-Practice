#python operaters

#the example of arrithmatic opperators

x=10
y=20

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)
print(x//y)

#comparison opperators

x=23
y=43

print(x==y)
print(x!=y)
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)


#assignment oppereters

x=10
y=2

x=y

print(x)
print(y)

x+=y

print(x)
print(y)

x-=y

print(x)
print(y)

x*=y

print(x)
print(y)

x/=y

print(x)
print(y)

x**y

print(x)
print(y)


x//y
print(x)
print(y)

#logical oppereters(and,or,not)

#check is a number is odd or evven

num=int(input("enter a number"))

if num %2==0:
    print(f"{num}is an even number")

else:
    print("f{num}is an odd number")

#find the minimum number of two numbers:

num1=int(input("enter first number"))
num2=int(input("enter second number"))


if num1<num2:
    print(f"the minimum number is {num1}")

else:
    print(f"the minimum number is {num2}")


#find the largest number among three numbers:

x=int(input("enter first number"))
y=int(input("enter second number"))
z=int(input("enter third number"))

if x>=y and x>=z:
    print(f"the largest number is {x}")

elif y>=z and y>=x:
    print(f"the largest number is {y}")

else:
    print(f"the largest number is {z}")





    



