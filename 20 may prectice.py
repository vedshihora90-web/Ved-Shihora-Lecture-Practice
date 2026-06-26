#identity operaters

a=[1,2,3,4]
b=a
c=[1,2,3,4]

print(a is b)
print(a is c)
print(a is not c)

#membership operators in python

number=[1,2,3]
print(2 is number)
print(5 is number)
print(5 is not number)

#string

text="python"
print("py" in text)

#bitwise operator in python

#1bitwise and

a=5
b=3

print(a&b)

#2bitwise xor

a=5
b=3

print(a^b)


#python control flow

#if condition

age=18
if age>=18:
    print("you are votter agible")

#if.....else stetament

number=7

if number %2==0:
    print("the num is even")

else:
    print("the num is odd")

#if.....elif....else stetament:

marks=70
if marks>=90:
    print("grade A")

elif marks>=75:
    print("grade b")

elif marks>=60:
    print("grade c")

else:
    print("fail")

    
