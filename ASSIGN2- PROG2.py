stock = {"rice": 50, "wheat": 30, "sugar": 20, "oil": 15, "salt": 40}

bill_list = []
total_bill = 0

while True:
    print("Available stock:", stock)
    item = input("Enter item name: ")

    if item in stock:
        qty = int(input("Enter quantity: "))

        if stock[item] >= qty:
            price = float(input("Enter price per unit: "))
            bill_list.append((item, qty, price))

            stock[item] = stock[item] - qty

            total_bill += qty * price
            print(item, "added to bill")
        else:
            print("Not enough stock ")
    else:
        print(item, "is not available in stock.")

    ch = input("Do you want to add more items? (Y/N): ")
    if ch in 'Yy':
        continue
    else:
        break

print("\n----- FINAL BILL -----")


print("Total Bill Amount:", total_bill)
print("Updated Stock:", stock)
