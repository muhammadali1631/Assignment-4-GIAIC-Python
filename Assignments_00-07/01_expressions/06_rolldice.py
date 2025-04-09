import random 

sides = 6

def main():
    die1:int = random.randint(1, sides)
    die2:int = random.randint(1, sides)

    total:int = die1 +die2

    print(f"Dice have {sides} sides each.")
    print(f"First Die: {die1}")
    print(f"Second Die: {die2}")
    print(f"Total of two die is {total}")

if __name__ == "__main__":
    main()