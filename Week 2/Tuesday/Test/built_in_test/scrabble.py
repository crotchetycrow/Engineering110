# import sys
# sys.path.append('../file_handling/orders.py')

letter_score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                "x": 8, "z": 10}


def calculate(word):
    score = 0
    for letter in word:
        score += letter_score[letter]
    print(f'Your total is {score}')
    write_to_file("scrabble_score.txt", word, score)
    open_and_print("scrabble_score.txt")


def open_and_print(file):
    try:
        with open(file, "r") as file:

            for line in file.readlines():
                print(line.rstrip('\n'))

    except FileNotFoundError:
        print("File cannot be found or directory is wrong")
        raise
    finally:
        print("\nExecution complete")

def write_to_file(file, word, score):
    try:
        with open(file, 'a') as file:
            file.write(f'Your word "{word}" scored {str(score)} points' + '\n')
    except FileNotFoundError:
        print("File cannot be found or directory is wrong")
        raise

calculate("alien")
calculate("human")