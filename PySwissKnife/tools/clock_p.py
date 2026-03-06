import msvcrt
import time
import os
import threading

running = False

def curr_time():
    current_time = time.localtime()
    return time.strftime("%Y-%m-%d %H:%M:%S", current_time)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_time():
    while running:
        clear_screen()
        print("Current Time:", curr_time())
        time.sleep(1)
def run_clock():
    global running
    running = True
    clock_thread = threading.Thread(target=show_time)
    clock_thread.start()
    while True:
        input("Press Enter to exit the clock...")
        running = False
        clock_thread.join()
        clear_screen()
        print("Goodbye!")
        break


if __name__ == "__main__":
    run_clock()