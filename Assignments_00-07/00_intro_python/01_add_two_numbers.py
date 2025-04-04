def main():
    print("You can add 2 numbers with this program.")

    num1:int = int(input("Enter the first number: "))
    num2:int = int(input("Enter the second number: "))

    total:int = num1 + num2
    print(f"The total is {total}.")


if __name__ == '__main__':
    main()