num = int(input("Enter a number: "))

if num % 5 == 0:
    if num % 11 == 0:
        print("Divisible by both 5 and 11")
    else:
        print("Divisible only by 5")
else:
    if num % 11 == 0:
        print("Divisible only by 11")
    else:
        print("Not divisible by 5 or 11")