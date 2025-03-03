from commands import CommandParser

parser = CommandParser()


def main():
    while True:
        print("expense-tracker ", end="")
        choice = input()
        parser.parse_command(choice)


main()
