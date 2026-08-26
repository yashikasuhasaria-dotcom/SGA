#program to display the menu of a calculator and perform addition,subtraction,multiplication and division
num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
choice=1
while choice!=5:
  print("1:addition 2:subtraction 3:multiplication 4:division 5:exit")
  choice=int(input("enter your choice from 1 to 5: "))
  if choice ==1:
    print("the result is: " ,num1+num2)
  elif choice==2:
    print("the result is: ",num1-num2)
  elif choice==3:
    print("the result is: ",num1*num2)
  elif choice==4:
    print("the result is: ",num1/num2)
  elif choice==5:
    pass
  else:
    print("invalid")