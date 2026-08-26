#Display the multiplication tables from 5 to 10 using nested for loops.
for i in range(5, 11):
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
    print()