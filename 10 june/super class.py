#polymorphism

#two types
'''1.method overloading
   2.method overriding'''

#method overloading mean creating mulipal method with same name but different parameter.
#python never support tradition method overloading directly,but it can be using defalut parameter.

class calculater:
    def add(self,a,b=0,c=0):
        return a+b+c

obj=calculater()
print(obj.add(10,20))
print(obj.add(10,20,30))

#2.method overriding

class Animal:
    def sound(self):
        print("animalm make sound")
class Dog(Animal):
    def sound(self):
        print("dog sound")
obj=Dog()
obj.sound()

#in that example dog class use sound method of parent class that is method overriding

#issubclass()
#return true or false
class Animal():
    pass
class Dog(Animal):
    pass
print(issubclass(Dog,Animal))
print(issubclass(Animal,Dog))


#super keyword

#it helps the reusing the parent class cod in child class

class person:
    def __init__(self,name):
        self.name=name
    
class students(person):
    def __init__(self,name,marks):
      super().__init__(name)
      self.marks=marks
        
    def display(self):
        print("name:",self.name)
        print("marks:",self.marks)

obj=students("rahul","67")
obj.display()

#1.using super() with constructor

class parent:
    def __init__(self):
        print("parent constructor.")

class child(parent):
    def __init__(self):
        super().__init__()
        print("child constructor.")

obj=child()

#2.access parent class method
class animal:
    def sound(self):
        print("animal make sound")

class dog(animal):
    def sound(self):
        super().sound()
        print("dog sound")

obj=dog()
obj.sound()


#3.parent class amd child class both have variables:

class person:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
class student(person):
    def display(self):
        print("name:",self.name)
        print("marks:",self.marks)

obj=student("zeel",34)
obj.display()


