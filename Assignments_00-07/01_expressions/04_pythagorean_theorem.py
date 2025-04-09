import math 

def calculate_hypotenuse():
    side1 = float(input("Enter length of side AB: "))
    side2 = float(input("Enter length of side AC: "))

    hypotenuse:float = math.sqrt(side1 ** 2 + side2 ** 2)

    print(f"The length of BC (the hypotenuse) is: {str(hypotenuse)}")

if __name__ == "__main__":
    calculate_hypotenuse()
