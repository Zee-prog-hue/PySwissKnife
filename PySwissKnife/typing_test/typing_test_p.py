# - import modules
# - paragraph variable
# - wait for Enter
# - record start_time
# - take user input
# - record end_time
# - calculate stats
# - print results

import time
import rich
import lorem_text as lt
import random


## Formulas
"""
time_taken = end_time - start_time
WPM = (total_characters / no_of_chars_in_word) / (time_taken / 60)
Accuracy = (Correct_characters / total_characters) * 100


"""
# R_paragraph = lt.paragraph()
C_paragraph = ["The quick brown fox jumps over the lazy dog.", "Pack my box with five dozen liquor jugs.", "How vexingly quick daft zebras jump!"]

def choices():
    choice = input("Random text(Comming soon) or custom text? (R/C): ").strip().upper()
    # if choice == 'R':
    #     return R_paragraph
    if choice == 'C':
        return random.choice(C_paragraph)
    else:
        print("Invalid choice. Please enter 'R' for random text or 'C' for custom text.")


def calculations(paragraph, user_input, start_time, end_time):  
    time_taken = end_time - start_time
    total_characters = len(paragraph)
    no_of_chars_in_word = 5
    WPM = (total_characters / no_of_chars_in_word) / (time_taken / 60)
    correct_characters = 0

    for p, u in zip(paragraph, user_input):
        if p == u:
            correct_characters += 1

    Accuracy = (correct_characters / total_characters) * 100
    return WPM, Accuracy

def timer(paragraph):
    input("Press Enter to start the test...")
    start_time = time.time()
    print("\n Type the following paragraph:\n")
    print("\n",paragraph)
    user_input = input("\nYour input: \n")
    end_time = time.time()
    return paragraph, user_input, start_time, end_time

def results(paragraph, user_input, start_time, end_time):
    WPM, Accuracy = calculations(paragraph, user_input, start_time, end_time)
    print(f"\nTime taken: {end_time - start_time:.2f} seconds")
    print(f"Words Per Minute (WPM): {WPM:.2f}")
    print(f"Accuracy: {Accuracy:.2f}%")


if __name__ == "__main__":
    paragraph = choices()
    paragraph, user_input, start_time, end_time = timer(paragraph)
    results(paragraph, user_input, start_time, end_time)
    