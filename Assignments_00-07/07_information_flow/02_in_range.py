def in_range(n, low, high):
    return low <= n <= high

def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    
    if in_range(n, low, high):
        print(f"{n} is between {low} and {high}.")
    else:
        print(f"{n} is not between {low} and {high}.")

if __name__ == "__main__":
    main()
