# ===============================================================
# CSCI-220 Group Project: Random Password Generator
# Authors: Daniel Roberts, Griffin Brown
# Course: CSCI-220-03-04
# Instructor: Dr. Mia Wang
# Due Date: November 25th, 2025
#
# Certification: We certify that this project is entirely our own
# collaborative work, with contributions shared through GitHub.
#
# Project Description:
# This program generates a randomized password based on user-defined
# parameters such as length and inclusion of special characters.
# The output resembles passwords generated akin to Google or Edge’s
# “suggested password” feature.
# ===============================================================

import random
from time import sleep

# Generate a randomized password based on user-defined parameters.
def password_generator():

    # Prompt user for desired password length
    while True:
        try:
            password_length = int(input("How long would you like your password to be? "))
            if password_length < 4:
                print("\nPassword length must be at least 4 characters.\n")
                continue
            break
        except ValueError:
            print("\nInvalid input. Please enter a valid integer.\n")

    print()
    sleep(1)

    # Prompt user for special character inclusion
    while True:
        use_specials = input("Would you like to use special characters? Respond with \"Yes\" or \"No\": ").strip().lower()

        if use_specials in ("yes", "no"):
            break
        print("\nInvalid input. Please respond with either \"Yes\" or \"No\".\n")

    print()
    sleep(1)

    # Define character sets
    ascii_list = [chr(i) for i in range(32, 127)]  # All printable ASCII
    alphanumerics = [chars for chars in ascii_list if chars.isalnum()]  # A-Z, a-z, 0-9
    specials = ["!", "?", "$", "@", "#", "_"]

    # Build password
    password_chars = [random.choice(alphanumerics) for _ in range(password_length)]

    # Optionally insert a special character at a random position
    if use_specials == "yes":
        index = random.randint(0, password_length - 1)
        password_chars[index] = random.choice(specials)

    # Combine into a final password string
    password = "".join(password_chars)

    print(f"Your unique password: {password}\n")


def project_flow():
    print("\nWelcome to the Random Password Generator!\n")
    sleep(1)

    # Main loop to generate passwords throughout user session
    while True:
        password_generator()
        sleep(1)

        # Prompt user whether to generate another password
        while True:
            again = input("Generate another? ").strip().lower()
            print()

            # Evaluate user response
            if again in ("yes", "y", "sure"):
                sleep(1)
                break
            elif again in ("no", "n", "nope"):
                sleep(1)
                print("Thank you for using the Random Password Generator! Goodbye.")
                return
            else:
                print('Invalid input. Please respond with either "Yes" or "No".\n')


if __name__ == "__main__":
    project_flow()