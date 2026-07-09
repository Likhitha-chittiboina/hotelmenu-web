print("=================================")
print("      WELCOME TO HOTEL MENU")
print("=================================")

total = 0

while True:
    print("\n1. Idli - ₹30")
    print("2. Dosa - ₹50")
    print("3. Biryani - ₹150")
    print("4. Tea - ₹20")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        qty = int(input("Enter quantity: "))
        total += qty * 30
        print("Idli added!")

    elif choice == 2:
        qty = int(input("Enter quantity: "))
        total += qty * 50
        print("Dosa added!")

    elif choice == 3:
        qty = int(input("Enter quantity: "))
        total += qty * 150
        print("Biryani added!")

    elif choice == 4:
        qty = int(input("Enter quantity: "))
        total += qty * 20
        print("Tea added!")

    elif choice == 5:
        break

    else:
        print("Invalid Choice!")

print("\n===========================")
print("Total Bill = ₹", total)
print("Thank You! Visit Again.")
print("===========================")