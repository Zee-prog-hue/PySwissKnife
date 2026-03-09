import time
import os
import winsound

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_and_formate_time():
    till_time = input("Enter the time in H:M:S format: ")
    try:
        h, m, s = map(int, till_time.split(':'))
        total_seconds = h * 3600 + m * 60 + s
        return total_seconds
    except ValueError:
        print("Invalid time format. Please enter time in H:M:S format.")
        return None
    
def run_timer():
    clear_screen()
    total_seconds = get_and_formate_time()

    if total_seconds is None:
        return print("Exiting timer due to invalid input.")
    while total_seconds > 0:
        clear_screen()
        print("Timer started for", time.strftime("%H:%M:%S", time.gmtime(total_seconds)))
        time.sleep(1)
        total_seconds -= 1
        
    clear_screen()    
    print("Time's up!")
    winsound.Beep(1000, 2000)  # Beep at 1000 Hz for 2 second
    
if __name__ == "__main__":
    run_timer()