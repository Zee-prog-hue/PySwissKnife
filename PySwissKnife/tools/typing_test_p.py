import time
import random
from lorem_text import lorem

def get_random_words(n=20):
    words = lorem.sentence().split()
    result = []

    while len(result) < n:
        result.extend(words)
        words = lorem.sentence().split()

    return " ".join(result[:n])


def calculate_wpm(start_time, end_time, typed_text):
    time_taken = end_time - start_time
    words = len(typed_text.split())
    minutes = time_taken / 60
    wpm = words / minutes if minutes > 0 else 0
    return round(wpm)


def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()

    correct = 0
    for i in range(min(len(original_words), len(typed_words))):
        if original_words[i] == typed_words[i]:
            correct += 1

    accuracy = (correct / len(original_words)) * 100
    return round(accuracy, 2)


def run_typing_test():

    choice = input("Random text or custom text? (R/C): ").strip().upper()

    if choice == "R":
        paragraph = get_random_words(20)
    else:
        paragraph = input("Enter the text for typing test:\n")

    print("\nType the following text:\n")
    print(paragraph)
    print("\nPress ENTER when ready...")
    input()

    start_time = time.time()

    typed_text = input("\nStart typing:\n")

    end_time = time.time()

    wpm = calculate_wpm(start_time, end_time, typed_text)
    accuracy = calculate_accuracy(paragraph, typed_text)

    print("\n----- RESULT -----")
    print(f"WPM: {wpm}")
    print(f"Accuracy: {accuracy}%")
    print("------------------")


if __name__ == "__main__":
    run_typing_test()