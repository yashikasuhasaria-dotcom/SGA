#write a program to check no of days in a month by entering the month number
month=int(input("Enter a month number: "))
if month==4 or month==6 or month==11 or month==9:
  print("it has 30 days")
elif month==2:
  print("it has 28 or 29 days")
else:
  print("it has 31 days")
  