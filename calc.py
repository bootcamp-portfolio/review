
class Calc():
    #property
    num1=0
    num2=0

    #constructor
    def __init__(self, num1, num2): #본인 자신?
        self.num1= num1
        self.num2=num2

    #method
    def add(self): #this->self
        result=self.num1+self.num2
        return result #class
   
    def sub(self):
        result=self.num1-self.num2
        return result