# ===============================================================
# CSCI-220 Group Project: Random Password Generator
# Authors: Daniel Roberts, Griffin Brown
# Course: CSCI-220-03-04
# Instructor: Dr. Mia Wang
# Due Date: November 25th, 2025
# ===============================================================

import random
from time import sleep
from graphics import GraphWin, Point, Rectangle, Text, Entry

# ===============================================================
# Spelled-out Greek alphabet for embedding into passwords
GREEK_WORDS = [
    "alpha","beta","gamma","delta","epsilon","zeta","eta","theta",
    "iota","kappa","lambda","mu","nu","xi","omicron","pi","rho",
    "sigma","tau","upsilon","phi","chi","psi","omega"
]
# ===============================================================


def password_generator(password_length=None, use_specials=None):

    # Console input if GUI didn't supply length
    if password_length is None:
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

    # Console input if GUI didn't supply special-char flag
    if use_specials is None:
        while True:
            use_specials = input("Would you like to use special characters? Respond with \"Yes\" or \"No\": ").strip().lower()
            if use_specials in ("yes", "no"):
                break
            print("\nInvalid input. Please respond with either \"Yes\" or \"No\".\n")

        print()
        sleep(1)

    # Character sets
    ascii_list = [chr(i) for i in range(32, 127)]
    alphanumerics = [c for c in ascii_list if c.isalnum()]
    specials = ["!", "?", "$", "@", "#", "_"]

    # Base characters
    password_chars = [random.choice(alphanumerics) for _ in range(password_length)]


    # Insert one Greek letter into every password
    word = random.choice(GREEK_WORDS)

    # truncate if user picks a very short password
    if len(word) > password_length:
        word = word[:password_length]

    wlen = len(word)
    insert_pos = random.randint(0, password_length - wlen)

    password_chars[insert_pos:insert_pos + wlen] = list(word)


    # Optional special character (avoid overwriting the embedded word)
    if use_specials == "yes":
        valid_slots = [
            i for i in range(password_length)
            if not (insert_pos <= i < insert_pos + wlen)
        ]
        if valid_slots:
            idx = random.choice(valid_slots)
        else:
            idx = random.randint(0, password_length - 1)  # fallback
        password_chars[idx] = random.choice(specials)

    password = "".join(password_chars)

    # Console output only if console-driven
    # (Your GUI never calls this branch; left unchanged.)
    if password_length is None or use_specials is None:
        print(f"Your unique password: {password}\n")

    return password


def project_flow():
    print("\nWelcome to the Random Password Generator!\n")
    sleep(1)

    while True:
        password_generator()
        sleep(1)

        while True:
            again = input("Generate another? ").strip().lower()
            print()

            if again in ("yes", "y", "sure"):
                sleep(1)
                break
            elif again in ("no", "n", "nope"):
                sleep(1)
                print("Thank you for using the Random Password Generator! Goodbye.")
                return
            else:
                print('Invalid input. Please respond with either "Yes" or "No".\n')


def graphics_ui():
    win = GraphWin("Random Password Generator", 640, 480)
    win.setCoords(0, 0, 100, 100)

    def inside(click, x1, y1, x2, y2):
        x = click.getX()
        y = click.getY()
        return x1 <= x <= x2 and y1 <= y <= y2

    # Title
    Text(Point(50, 92), "Random Password Generator").draw(win)

    # Length input
    Text(Point(30, 75), "Password length:").draw(win)
    length_entry = Entry(Point(65, 75), 5)
    length_entry.setText("12")
    length_entry.draw(win)

    # Specials toggle
    Text(Point(30, 60), "Use special characters?").draw(win)
    specials_rect = Rectangle(Point(55, 55), Point(75, 65))
    specials_rect.draw(win)
    specials_label = Text(Point(65, 60), "OFF")
    specials_label.draw(win)
    use_specials = False

    # Generate button
    gen_rect = Rectangle(Point(20, 35), Point(45, 45))
    gen_rect.draw(win)
    Text(Point(32.5, 40), "Generate").draw(win)

    # Quit button
    quit_rect = Rectangle(Point(55, 35), Point(80, 45))
    quit_rect.draw(win)
    Text(Point(67.5, 40), "Quit").draw(win)

    # Output
    Text(Point(20, 20), "Password:").draw(win)
    output_text = Text(Point(60, 20), "")
    output_text.draw(win)

    # Error
    error = Text(Point(50, 10), "")
    error.setTextColor("red")
    error.draw(win)

    # Main loop
    while True:
        click = win.getMouse()

        # Toggle specials
        if inside(click, 55, 55, 75, 65):
            use_specials = not use_specials
            specials_label.setText("ON" if use_specials else "OFF")

        # Generate
        elif inside(click, 20, 35, 45, 45):
            try:
                length = int(length_entry.getText())
                if length < 4:
                    error.setText("Length must be at least 4.")
                    continue
            except:
                error.setText("Length must be an integer.")
                continue

            error.setText("")

            pwd = password_generator(length, "yes" if use_specials else "no")
            output_text.setText(pwd)

        # Quit
        elif inside(click, 55, 35, 80, 45):
            break

    win.close()


if __name__ == "__main__":
    # project_flow()
    graphics_ui()
