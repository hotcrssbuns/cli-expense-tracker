import shlex
import json
from datetime import datetime
import sys
from tabulate import tabulate
import os
import platform


class CommandParser:
    def __init__(self):
        self.commands = {
            "add": self.add,
            "list": self.list,
            "summary": self.summary,
            "delete": self.delete,
            "update": self.update,
            "exit": self.exit,
            "commands": self.commands,
        }

        try:
            with open("sample.json", "r") as infile:
                self.expenses = json.load(infile)
        except FileNotFoundError:
            self.expenses = []

    def parse_command(self, command):
        self.parts = shlex.split(command)
        self.command = self.parts[0].lower()
        self.args = self.parts[1:]

        handler = self.commands.get(self.command)

        try:
            if handler:
                return handler(*self.args)
            else:
                print("Invalid.")

        except (TypeError, ValueError) as e:
            print(f"Invalid: {e}")

    def add(self, description, amount):
        current_time = datetime.now()
        formatted_date = current_time.strftime("%Y-%d-%m")
        id = len(self.expenses) + 1
        expense = {
            "ID": id,
            "Description": description,
            "Date": formatted_date,
            "Amount": amount,
        }
        self.expenses.append(expense)
        with open("sample.json", "w") as outfile:
            json.dump(self.expenses, outfile)

        print(f"Expense added succesfully (ID: {id})")

    def list(self):
        self.clear()
        print(tabulate(self.expenses, headers="keys", tablefmt="github"))

    def summary(self):
        total = 0
        for expense in self.expenses:
            total += int(expense["Amount"])
        print(f"Total expenses: ${total}")

    def delete(self, id):
        id = int(id)
        for expense in self.expenses:
            if id == expense["ID"]:
                index = id - 1
                self.expenses.pop(index)
        id = 1
        for expense in self.expenses:
            expense["ID"] = id
            id += 1

        with open("sample.json", "w") as outfile:
            json.dump(self.expenses, outfile)
        print("Expense deleted successfully")

    def update(self, id, description, amount):
        for expense in self.expenses:
            if id == expense["ID"]:
                expense["Description"] = description
                expense["Amount"] = amount

    def exit(self):
        sys.exit()

    def commands(self):
        print('- add "description" $10')
        print("- list")
        print("- summary")
        print("- delete 1")

    def clear(self):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
