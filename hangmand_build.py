import random


capitals_list = ["LONDON", "PARIS", "BUCHAREST", "WARSOW", "BUDAPEST", "ROME", "ATHENS", "BERLIN", "LISBON",
                 "MADRID", "KIEV", "SOFIA", "DUBLIN", "BRUSSELS", "COPENHAGEN", "LUXEMBOURG", "AMSTERDAM", "STOCKHOLM"]


def pick_category(capitals):
    capital = random.choice(capitals)
    return capital


def get_hashed(word):
    result = ""
    for i in range(len(word)):
        i = "_"
        result = result + i
    return result


def uncover(hashed_password, password, letter):
    hashed_password = list(hashed_password)
    for i in range(len(password)):
        if letter == password[i]:
            hashed_password[i] = password[i]

    return "".join(hashed_password)


def is_win(hashed_password, password):
    if hashed_password == password:
        return True
    else:
        return False


def is_loose(life_points):
    if life_points == 0:
        return True
    else:
        return False


# def update(used_letters, letter):
#     used_letters = []
#     if letter not in used_letters:
#         used_letters.update(letter)


def get_input(word):
    print("\n\n")
    while True:
        letter_guessed = input("Please enter a letter: ")
        print("\n")
        if letter_guessed.isalpha():
            return letter_guessed
            continue
        elif len(letter_guessed) > 1 and len(letter_guessed) != len(word):
            print("Please only use one letter at a time")
        else:
            print("Wrong input. Please use letters only!")


def main():
    capital = pick_category(capitals_list)
    hashed_capital = get_hashed(capital)
    life_points = len(capital) + 2
    print("You have " + str(life_points - 1) +
          " tries to guess the capital:", end="")
    for x in hashed_capital:
        print(x, end=" ")

    used_letters = []
    while True:
        letter = get_input(capital).upper()
        if letter not in used_letters:
            print("You have " + str(life_points - 1) + " lives left." + "\n")
            used_letters.append(letter)
            hashed_capital = uncover(hashed_capital, capital, letter)
            for x in hashed_capital:
                print(x, end=" ")
            life_points = life_points - 1
            if is_loose(life_points) is True:
                print("\n\n" + "You are out of lives! " +
                      "The capital was: " + capital.upper())
                break
            print("       " + "Letters used: " + " ".join(used_letters))
        else:
            print("You have already used this letter, try a different one!")

        if is_win(hashed_capital, capital) or is_win(letter, capital) is True:
            print("\n\n" + "The capital is: " + capital.upper() +
                  "\n\n" + "Congratualtions! You win!")
            break


main()
