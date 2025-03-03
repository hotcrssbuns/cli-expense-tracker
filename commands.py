import shlex
import json
from datetime import datetime
import os


class CommandParser:
    def __init__(self):
        self.commands = {
            "add": self.add,
            "list": self.list,
            "summary": self.summary,
            "delete": self.delete,
            "update": self.update,
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

    def add(self, description, log, amount, amount_number):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%d-%m")
        id = len(self.expenses) + 1
        expense = {
            "id": id,
            "description": log,
            "time": formatted_time,
            "amount": amount_number,
        }
        self.expenses.append(expense)
        with open("sample.json", "w") as outfile:
            json.dump(self.expenses, outfile)

        print(f"Expense added succesfully (ID: {id})")

    def list(self): ...

    def summary(self): ...

    def delete(self): ...

    def update(self): ...
