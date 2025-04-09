def main():
    degrees_fahrenheit: float = float(input("\033[1;3m Enter temperature in Fahrenheit: \033[0m"))
    celsius: int = (degrees_fahrenheit - 32) * 5.0 / 9.0

    print(f"Temperature: {degrees_fahrenheit}F = {celsius}C")

if __name__ == '__main__':
    main()