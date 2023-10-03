class Calculator:

   def add(self,num_1,num_2):
        self.result = num_1 + num_2
        print(self.result) 

   def subtract(self,num_1,num_2):
        self.result = num_1 - num_2
        print(self.result)

   def multiply(self,num_1,num_2):
        self.result = num_1 * num_2
        print(self.result)

   def divide (self,num_1,num_2):
        self.result = num_1 / num_2
        print(self.result)
    
calculator = Calculator()   
calculator.add(5,15)
calculator.subtract(5,15)
calculator.multiply(5,15)
calculator.divide(15,5)

     
