import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def stopwatch():
    clear_screen()
    input("Press Enter to START the stopwatch...")

    start_time = time.time()

    input("Stopwatch running... Press Enter to STOP...")

    end_time = time.time()
    elapsed = end_time - start_time

    formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed))

    clear_screen()
    print("Stopwatch stopped.")
    print("Elapsed Time:", formatted_time)

if __name__ == "__main__":
    stopwatch()