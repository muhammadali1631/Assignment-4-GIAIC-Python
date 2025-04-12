def num_in_stock(fruit):
    inventory = {
        'apple': 50,
        'banana': 100,
        'pear': 1000,
        'orange': 200,
        'grape': 0
    }
    
    return inventory.get(fruit.lower(), 0)

def main():
    fruit = input("Enter a fruit: ").lower()

    stock = num_in_stock(fruit)
    
    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

if __name__ == "__main__":
    main()
