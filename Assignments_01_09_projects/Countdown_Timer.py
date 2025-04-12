import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    
    print("00:00\nTime's up!")

def main():
    try:
        seconds = int(input("Enter the time in seconds for countdown: "))
        countdown_timer(seconds)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
