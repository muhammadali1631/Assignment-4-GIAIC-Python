def main():
    print("Welcome to the Mad Libs Game!")

    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb (past tense): ")
    noun2 = input("Enter another noun: ")
    adjective2 = input("Enter another adjective: ")
    verb2 = input("Enter another verb (past tense): ")

    story = f"Once upon a time, there was a {adjective1} {noun1} who loved to {verb1}. One day, it met a {noun2} and thought it was very {adjective2}. They decided to {verb2} together, and they lived happily ever after."

    print("\nHere is your story:")
    print(story)

if __name__ == "__main__":
    main()
