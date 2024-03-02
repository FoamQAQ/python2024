import random
filename = "./5letterword.txt"


def import_txt_file(filename):
    words = []
    with open(filename, 'r') as file:
        for line in file:
            clean_line = line.strip()
            if len(clean_line) == 5:
                words.append(clean_line)
    return words


words = import_txt_file(filename)


def bullscows(guess: str, secret: str) -> (int, int):
    bulls = 0
    cows = 0
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return (bulls, cows)


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret = random.choice(words)
    attempts = 0
    while True:
        attempts += 1
        guess = ask("Введите слово: ", words)
        bulls, cows = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", bulls, cows)
        if bulls == len(secret):
            return attempts

def ask(prompt: str, valid: list[str] = None) -> str:
    word = ""
    word = input(prompt)
    return word


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls,cows))


print(gameplay(ask,inform,words))
