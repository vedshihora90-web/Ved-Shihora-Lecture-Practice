from abc import ABC,abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
    
class dog(Animal):
   def sound(self):
        print("dog bow bow")

d=dog()
d.sound()

#abstract class and methods

from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
         pass
    
    def sleep(self):
        print("animal is sleeping")

#child class

class dog(animal):
    def sound(self):
        print("dog bow bow")

class cat(animal):
    def sound(self):
        print("cat meow")

d=dog()
d.sound()
d.sleep()

c=cat()
c.sound()
c.sleep()

#abstract class shape with area()

from abc import ABC ,abstractmethod

#abstract class

class shape(ABC):
  @abstractmethod
  def area(self):
      pass

class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width
    
class circle(shape):
    def __init__(self,redius):
        self.redius=redius

    def area(self):
        return self.redius*self.redius*3.14

r=rectangle(10,5)
print("rectangle area:",r.area())

c=circle(10)
print("circle area:",c.area())


#mlmodel abstrect class

from abc import ABC,abstractmethod

class mlmodel(ABC):
    def train(self):
        pass

    @abstractmethod
    def predict(self):
        pass

#linear regression model

class linearregressionmodel(mlmodel):
    def train(self):
        print("training linear regression model")

    def predict(self):
        print("predicting linear regression model")

class desisiontreemodel(mlmodel):
    def train(self):
        print("training desison tree model")

    def predict(self):
        print("predicting desision tree model")

l=linearregressionmodel()
d=desisiontreemodel()

l.train()
l.predict()

d.train()
d.predict()


    
        





            
