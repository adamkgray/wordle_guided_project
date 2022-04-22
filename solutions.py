import random


def green(string):
    GREEN = '\033[32m'
    END = '\033[0m'
    return GREEN + string + END


def yellow(string):
    YELLOW = '\033[33m'
    END = '\033[0m'
    return YELLOW + string + END


def readfile(file_path):
    with open(file_path, "r") as f:
        lines = []
        for line in f:
            line = line.strip()
            lines.append(line)
        return lines


def random_answer(answers):
    return random.choice(answers)


def get_guess(guesses):
    guess = input("> ")
    while guess not in guesses:
        guess = ("> ")
    return guess


def accuracy(guess, answer):
    colored_guess = ""
    for i in range(5):
        if guess[i] not in answer:
            colored_guess += guess[i]
        elif guess[i] == answer[i]:
            colored_guess += green(guess[i])
        else:
            colored_guess += yellow(guess[i])
    return colored_guess


# read answers from file
answers = readfile("answers.txt")

# read guesses from file
guesses = readfile("guesses.txt")

# choose random answer
answer = random_answer(answers)

# take 6 turns
for i in range(6):
    # show turn number
    print("guess #{}".format(i - 1))

    # get guess from user
    guess = get_guess(answers)

    # print colored result
    colored_guess = accuracy(guess, answer)
    print(colored_guess)

    # end if guess was correct
    if guess == answer:
        break
