
num = int(input("Enter a number: "))
if num <= 1:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            print('Not prime')
            break
    if is_prime == True:
        print('Its a prime no')