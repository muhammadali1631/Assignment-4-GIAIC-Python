def main():
    lst = []

    val = input("Please enter an element of the list or press enter to stop. ")
    while val:
        lst.append(val)
        val = input("Please enter an element of the list or press enter to stop. ")

    print("Here's the list:", lst)

if __name__ == '__main__':
    main()