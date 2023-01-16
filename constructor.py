'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
class Tejas:
    x=0
    def _init_(self,name,id,roll):
        print("i am constructor")
        
    def display(self,name,roll):
        return roll
        
emp=Tejas("tejas",91,9)
print(emp.display("tejas",44))
print(getattr( emp,'name'))  
