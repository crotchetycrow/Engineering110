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