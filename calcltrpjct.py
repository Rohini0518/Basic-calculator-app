# # calculator project


def add(n1,n2):
   return n1+n2
def sub(n1,n2):
   return n1-n2
def multiply(n1,n2):
   return n1*n2
def div(n1,n2):
   return n1/n2

dic_operations={
                 "+":add,
                 "-":sub,
                 "*":multiply,
                 "/":div
               }
def calculation_start():
   num1=int(input("what's the first number: "))      
   calculations=True
   while calculations==True:
      for symbol in dic_operations:
         print(symbol) 
      opearation_symbol=input("pick an operator from above operators: ")
      num2=int(input("what's the next number: ")) 
      operator_selection=dic_operations[opearation_symbol]
      answer=operator_selection(num1,num2)
      print(f"{num1}{opearation_symbol}{num2}={answer}")  
      cntnue_process=input(f"if you want to continue with previous answer{answer} yes or go with new number type new or type any letter to stop calculations?:")
      if cntnue_process=="yes":
         num1=answer   
         calculations=True
      elif cntnue_process=="new":
         calculations=False  
         calculation_start() 
      else:
         calculations=False   
         
calculation_start()
         