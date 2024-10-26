if __name__ == "__main__":
    print("Let's find a number in a list.")
    N = int(input("How many numbers would you like to enter? "))
    numbers = []
    print(f"Please enter {N} numbers:")
    for i in range(N):
        numbers.append(int(input(f"Number {i+1}: ")))
    X = int(input("What number would you like to find? "))

    if X in numbers:
        print(numbers.index(X) + 1)
    else:
        print(-1)
