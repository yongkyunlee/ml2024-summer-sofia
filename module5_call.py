from module5_oop import Numbers

if __name__ == "__main__":
    while True:
        try:
            N = int(input("How many numbers would you like to enter? "))
            if N > 0:
                break
            print("Enter a positive number.")
        except ValueError:
            print("Enter a valid integer.")

    numbers = Numbers()
    print(f"Enter {N} numbers:")
    for i in range(N):
        while True:
            try:
                num = int(input(f"Number {i+1}: "))
                numbers.add_number(num)
                break
            except ValueError:
                print("Please enter a valid integer.")

    while True:
        try:
            X = int(input("What number would you like to find? "))
            break
        except ValueError:
            print("Enter a valid integer.")

    result = numbers.find_number(X)
    print(result)
