from commands import CommandParser
from colorama import Fore

parser = CommandParser()


def main():
    while True:
        print(Fore.GREEN + "expense-tracker " + Fore.WHITE, end="")
        choice = input()
        parser.parse_command(choice)


main()
