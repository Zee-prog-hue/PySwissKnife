from tools.clock_p import run_clock
from tools.stopwatch_p import run_stopwatch
from tools.timer_p import run_timer
from tools.qr_generator_p import generate_qr
from tools.typing_test_p import run_typing_test
from tools.internet_speed_p import run_speed_test
import os



def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print("\nWelcome to the Python Tool Suite!")
    print("1. Clock")
    print("2. Stopwatch")
    print("3. Timer")
    print("4. QR Code Generator")
    print("5. Typing Test")
    print("6. Internet Speed Test")

    choice = input("Choose a tool (1-6): ").strip()

    if choice == '1':
        run_clock()
    elif choice == '2':
        run_stopwatch()
    elif choice == '3':
        run_timer()
    elif choice == '4':
        data = input("Enter data for QR code: ")
        output_file = input("Enter output file name (default: qr_code.png): ") or "qr_code.png"
        generate_qr(data=data, file_path=output_file)

    elif choice == '5':
        run_typing_test()

    elif choice == '6':
        run_speed_test()
        
    else:
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    while True:
        main()
        again = input("Use another tool? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break
        else:
            clear_screen()
            continue

