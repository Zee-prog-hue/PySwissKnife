import time
import os
import threading

running = False
start_time = None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_time(start_time):
    elapsed_time = time.time() - start_time
    return time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

def timer():
    global running, start_time
    while running:
        clear_screen()
        print("Stopwatch running... Elapsed time:",
              calculate_time(start_time))
        time.sleep(1)

if __name__ == "__main__":
    input("Press Enter to START the stopwatch...")
    
    running = True
    start_time = time.time()

    timer_thread = threading.Thread(target=timer)
    timer_thread.start()

    input("Press Enter to STOP the stopwatch...")
    
    running = False
    timer_thread.join()

    clear_screen()
    print("Stopwatch stopped.")
    print("Final Time:", calculate_time(start_time - 1))  # Subtracting 1 second to account for the last sleep in the timer thread
    