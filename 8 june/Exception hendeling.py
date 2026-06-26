'''
An exception is an error that occurs during
program exception if on exception is not
handeled the proggram stop immediatly

To avoid program crashes python provide
exception handling using

try , catch ,  else , finally
'''

#1.try.....exception

try:
    num=int(input("enter your number:"))
    print(100/num)
except ZeroDivisionError:
    print("cannot divisible by zero")
except ValueError:
    print("invalid input")

#2.try....except....else

try:
    num=int(input("enter your number:"))
    result=100/num
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print("result:",result*2)

#3.try.....except......finally

try:
    file=open("demo.txt","r")
    print(file.read())
except FileNotFoundError:
    print("file not found")
finally:
    print("program finish")

#4.try....except....else...finally

try:
    num=int(input("enter your number:"))
    result=1000/num
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print("result:",result)
finally:
    print("program finish")



