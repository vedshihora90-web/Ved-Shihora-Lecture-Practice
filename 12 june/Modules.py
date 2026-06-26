#python modules&functions

#1.math modules

print("\n =======math ,odules======")
import math

#1.sqrt()

num=36
r=math.sqrt(num)
print(r)

#2.pow()

base=2
power=6
r=math.pow(base,power)
print("base","power","=",r)

#3.ceil()

num=2.4
r=math.ceil(num)
print(r)

#4.floor()

num=4.5
r=math.floor(num)
print(r)

#5.factorial()

num=5
r=math.factorial(num)
print(r)

#6.gcd()

num1=18
num2=45
r=math.gcd(num1,num2)
print(r)

#7.sin()

r=math.sin(0)
print(r)

#8.cos()

r=math.cos(1)
print(r)

#9.tan()

r=math.tan(1)
print(r)

#10.log()

num=10
result=math.log(num)
print(result)

#11.pi

print(math.pi)

#12.e

print(math.e)

#2.RANDOM module

import random
print("\n=======Random Module=====")

#1.randint()

r=random.randint(1,20)
print(r)

#2.random()

r=random.random()
print(r)

#3.choice()

colors=["blue","red","yellow","pink"]
r=random.choice(colors)
print(r)

#4.shuffle()

num=[1,2,3,4,5,6]
random.shuffle(num)
print(num)

#5.uniform()

r=random.uniform(1,100)
print(r)

#6.randrange()

r=random.randrange(1,20,2)
print(r)

#7.sample()

num=[10,20,30]
r=random.sample(num,2)
print(r)

#3.UUID module

#1.uuid.uuid1()
print("\n========UUID Modules======")
import uuid
r=uuid.uuid1()
print(r)

#2.uuid.uuid4()

r=uuid.uuid4()
print(r)

#3.uuid.uuid3()

r=uuid.uuid3(uuid.NAMESPACE_DNS,"example.com")
print(r)

#4.uuid.uuid5()

r=uuid.uuid5(uuid.NAMESPACE_DNS,"example.com")
print(r)

