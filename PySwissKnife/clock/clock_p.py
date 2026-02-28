import time
import os

def curr_time():
    current_time = time.localtime()
    return time.strftime("%Y-%m-%d %H:%M:%S", current_time)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    while True:
        clear_screen()
        print("Current Time:", curr_time())
        time.sleep(1)
if __name__ == "__main__":
    main()