#stetament and loops

#match case statements

#work similar to switch case statements

#examples

num_1=10
num_2=5
operator="+"

match operator:
    case"+":
        print("addition",num_1+num_2)

    case"-":
        print("substraction",num_1-num_2)

    case"*":
        print("multiplication",num_1*num_2)

    case"/":
        print("divison",num_1/num_2)

    case _:
        print("invalid operater")

#day names

day=2
match day:
    case 1:
        print("monday")

    case 2:
        print("tuesday")

    case 3:
        print("wednesday")

    case 4:
        print("thursday")

    case 5:
        print("friday")

    case 6:
        print("saturday")

    case 7:
        print("sunday")

    case _:
        print("invalid tnput")



#multiple values in one case

char="a"
match char:
    case"a"|"e"|"i"|"o"|"u":
        print("vowel")
    case _:
        print("consonant")

#python lopps

#1.while loops
i=1
while i<=8:
    print(i)
    i+=1

#2.for loop
for i in range(1,9,2):
    print(i)

#3.string with loops

name="hello world!"

for ch in name:
    print(ch)

#list with loops

fruits=["apple","banana","kiwi","orange","mango"]

for item in fruits:
    print(item)

#range function
for i in range(1,2):
   for j in range(1,2):
       print(j,end=" ")
       print()

for i in range(1,8):
   for j in range(1,3):
       print(j,end=" ")
       print()

#stop loop imidiately

for k in range(1,9):
    if k==3:
        break
    print(k)

#continue statements

for i in range(1,7):
    if i==5:
        continue
    print(i)

#pass statements

for i in range(5):
    pass

#pattern in python
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

rows=5
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end="")

    for k in range(2*i-1):
        print("*",end="")

    print()

       
 

        






        




       
 

        






        
