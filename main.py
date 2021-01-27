import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_win(values):
    for char in values:
        if char == '_':
            return False
    return True


def print_hangman(values):
    print()
    print("\t +--------+")
    print("\t |       | |")
    print("\t {}       | |".format(values[0]))
    print("\t{}{}{}      | |".format(values[1], values[2], values[3]))
    print("\t {}       | |".format(values[4]))
    print("\t{} {}      | |".format(values[5], values[6]))
    print("\t         | |")
    print("  ___________| |___")
    print("  ```````````````````````")
    print()


def print_hangman_win():
    print()
    print("\t +--------+")
    print("\t |       | |")
    print("\t         | |")
    print("\t O       | |")
    print("\t/|\\      | |")
    print("\t |       | | ")
    print("  ___/_\\______| |___")
    print("  ```````````````````````")
    print()


def print_word(values):
    print()
    print("\t", end="")
    for x in values:
        print(x, end="")
    print()


def hangman_game(word):
    clear()

    # this list will store all of the letters to be displayed
    word_display = []

    # this list stores all of the correctly guessed letters
    correct_letters = []

    # this list stores all of the incorrect guesses made
    incorrect_letters = []

    # this stores the number of incorrect guesses/chances
    number_of_wrong_guesses = 0

    # this list stores hangman's body values
    hangman_values = ['O', '/', '|', '\\', '|', '/', '\\']

    # this list stores all of the body values displayed to the user
    show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']

    for char in word:
        if char.isalpha():
            word_display.append('_')
            correct_letters.append(char.upper())
        else:
            word_display.append(char)

    while True:
        # prints the necessary components
        print_hangman(show_hangman_values)
        print_word(word_display)
        print()
        print("Incorrect letters : ", incorrect_letters)
        print()

        inp = input("Enter a letter 〈(•ˇ‿ˇ•)-→ : ")
        # determines  if input exceeds one letter
        if len(inp) != 1:
            clear()
            print("That's more than one letter you @%$# try again")
            continue

        # determines if input is a letter
        if not inp[0].isalpha():
            clear()
            print("That's not even a letter, genius! Try again")
            continue

        # determines if input has already been tried
        if inp.upper() in incorrect_letters:
            clear()
            print("Already TrIeD!!")
            continue

        # checks if the letter is in the word
        if inp.upper() not in correct_letters:

            # updating incorrect letter list
            incorrect_letters.append(inp.upper())

            # updating hangman display
            show_hangman_values[number_of_wrong_guesses] = hangman_values[number_of_wrong_guesses]
            number_of_wrong_guesses = number_of_wrong_guesses + 1

            # checking if the player lost
            if number_of_wrong_guesses == len(hangman_values):
                print()
                clear()
                print("\t GAME OVERRRRRR!!!")
                print("the word is :", word.upper())
                break

        else:

            # updating the word display
            for i in range(len(word)):
                if word[i].upper() == inp.upper():
                    word_display[i] = inp.upper()

            # checking if the player has won
            if check_win(word_display):
                clear()
                print("\t Congratulations!")
                print_hangman_win()
                print("The word is : ", word.upper())
                break
        clear()


if __name__ == '__main__':

    clear()

    topics = {1: "DC characters", 2: "Marvel characters", 3: "Anime characters"}

    dataset = {
        "DC characters": ["SUPERMAN", "JOKER", "HARLEY QUINN", "GREEN LANTERN", "FLASH", "WONDER WOMAN", "AQUAMAN",
                          "MARTIAN MANHUNTER", "BATMAN"],
        "Marvel characters": ["CAPTAIN AMERICA", "IRON MAN", "THANOS", "HAWKEYE", "BLACK PANTHER", "BLACK WIDOW"],
        "Anime characters": ["MONKEY D. LUFFY", "RORONOA ZORO", "LIGHT YAGAMI", "MIDORIYA IZUKU"]
    }

    while True:
        print()
        print("╔══════ ≪≫°✺°≪ ≫ ══════╗")
        print("\t\tGAME MENU")
        print("╚══════ ≪≫°✺°≪ ≫ ══════╝")
        for key in topics:
            print("Press", key, "to select", topics[key])
        print("Press", len(topics) + 1, "to quit")
        print()

        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            clear()
            print("You did it wrong, genius. ∠( ᐛ 」∠)＿ Try again")
            continue

            # if the number entered is more than the number of categories then we tell them
        if choice > len(topics) + 1:
            clear()
            print("Thats not even a topic you dumb#@$% ( ︶︿︶)_╭∩╮")
            continue

            # this deals with the exit choice if 3 is entered
        elif choice == len(topics) + 1:
            print()
            print("Bye then! ¯\_ಠ_ಠ_/¯ ")
            break

        chosen_topic = topics[choice]
        ran = random.choice(dataset[chosen_topic])
        hangman_game(ran)
