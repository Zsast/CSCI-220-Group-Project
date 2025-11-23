import random
from time import sleep
from graphics import GraphWin, Point, Rectangle, Text, Entry

GREEK_WORDS = [  # List of Greek words to embed in passwords
    "alpha","beta","gamma","delta","epsilon","zeta","eta","theta",
    "iota","kappa","lambda","mu","nu","xi","omicron","pi","rho",
    "sigma","tau","upsilon","phi","chi","psi","omega"
]

ASCII_LIST = [chr(i) for i in range(32, 127)]  # All printable ASCII characters
ALPHANUMERICS = [c for c in ASCII_LIST if c.isalnum()]  # Letters and digits only
SPECIALS = ["!", "?", "$", "@", "#", "_"]  # Optional special characters


def password_generator(password_length=None, use_specials=None):
    console_mode = (password_length is None and use_specials is None)  # Detect console usage

    if password_length is None:  # Prompt for length in console mode
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

    if use_specials is None:  # Prompt for special characters in console mode
        while True:
            use_specials = input(
                "Would you like to use special characters? Respond with \"Yes\" or \"No\": "
            ).strip().lower()
            if use_specials in ("yes", "no"):
                break
            print("\nInvalid input. Please respond with either \"Yes\" or \"No\".\n")
        print()
        sleep(1)

    password_chars = [random.choice(ALPHANUMERICS) for _ in range(password_length)]  # Base password
    word = random.choice(GREEK_WORDS)  # Pick a Greek word

    if len(word) > password_length:  # Truncate word if too long
        word = word[:password_length]

    wlen = len(word)
    insert_pos = random.randint(0, password_length - wlen)  # Random insertion position
    password_chars[insert_pos:insert_pos + wlen] = list(word)  # Insert Greek word

    if use_specials == "yes":  # Optionally add a special character
        valid_slots = [
            i for i in range(password_length)
            if not (insert_pos <= i < insert_pos + wlen)
        ]
        if valid_slots:
            idx = random.choice(valid_slots)
        else:
            idx = random.randint(0, password_length - 1)
        password_chars[idx] = random.choice(SPECIALS)

    password = "".join(password_chars)  # Final password string

    if console_mode:  # Print in console mode
        print(f"Your unique password: {password}\n")

    return password


def graphics_ui():
    win = GraphWin("Random Password Generator", 640, 480)  # Create GUI window
    win.setCoords(0, 0, 100, 100)

    def inside(click, x1, y1, x2, y2):  # Helper: detect clicks inside rectangle
        x = click.getX()
        y = click.getY()
        return x1 <= x <= x2 and y1 <= y <= y2

    Text(Point(50, 92), "Random Password Generator").draw(win)  # Title

    Text(Point(30, 75), "Password length:").draw(win)  # Label for length input
    length_entry = Entry(Point(65, 75), 5)
    length_entry.setText("12")
    length_entry.draw(win)

    Text(Point(30, 60), "Use special characters?").draw(win)  # Specials toggle
    specials_rect = Rectangle(Point(55, 55), Point(75, 65))
    specials_rect.draw(win)
    specials_label = Text(Point(65, 60), "OFF")
    specials_label.draw(win)
    use_specials = False

    gen_rect = Rectangle(Point(20, 35), Point(45, 45))  # Generate button
    gen_rect.draw(win)
    Text(Point(32.5, 40), "Generate").draw(win)

    quit_rect = Rectangle(Point(55, 35), Point(80, 45))  # Quit button
    quit_rect.draw(win)
    Text(Point(67.5, 40), "Quit").draw(win)

    Text(Point(20, 20), "Password:").draw(win)  # Output label
    output_text = Text(Point(60, 20), "")
    output_text.draw(win)

    error = Text(Point(50, 10), "")  # Error message display
    error.setTextColor("red")
    error.draw(win)

    while True:  # Main event loop
        click = win.getMouse()

        if inside(click, 55, 55, 75, 65):  # Toggle special character usage
            use_specials = not use_specials
            specials_label.setText("ON" if use_specials else "OFF")

        elif inside(click, 20, 35, 45, 45):  # Generate password
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

        elif inside(click, 55, 35, 80, 45):  # Quit button
            break

    win.close()


def console():
    print("\nWelcome to the Random Password Generator!\n")  # Welcome message
    sleep(1)

    while True:  # Loop for generating passwords
        password_generator()
        sleep(1)

        while True:  # Prompt to generate again
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


if __name__ == "__main__":
    # console() # Uncomment this line to use console mode
    graphics_ui()  # Launch GUI by default
