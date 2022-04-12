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

def write_to_file(file, order_item):
    try:
        with open(file, 'a') as file:
            file.write(order_item + '\n')
    except FileNotFoundError:
        print("File cannot be found or directory is wrong")
        raise

write_to_file("order.txt", "Testing")

open_and_print('order.txt')