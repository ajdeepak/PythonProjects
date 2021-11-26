def add(num1,num2):
    return num1 + num2
def subt(num1,num2):
    return num1 - num2
def multi(num1,num2):
    return num1 * num2
def div(num1,num2):
    return num1 / num2


def calculator():
    print("Enetr the first number")
    num1=int(input())    
    print("Enetr the second number")
    num2=int(input())
    print(" Enetr 1 for Addition \n Enetr 2 for substraction \n Enetr 3 for multiplication \n Enetr 4 for divide")
    choice=int(input())
    if choice==1:
        print(add(num1,num2))
    elif choice==2:
        print(subt(num1,num2))
    elif choice==3: 

        print(multi(num1,num2))
    elif choice==4:  
        print(multi(num1,num2))
    else :
     print("please select valid option ")

def call_again():
  print("press y for calculate again and n for end")
  choice2=input()
  if choice2 == 'y':
    calculator()
  else:
    print("thank you for using our calulator")
    exit()


print("welcome to the calculator") 
calculator()
while(True):
  call_again()

    

   