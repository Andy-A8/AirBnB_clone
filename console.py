#!/bin/bash/python3
"""Defines the entry point of the command interpreter"""


import cmd


class HBNBCommand(cmd.cmd):
    """Represents the class for the  command interpreter"""

    # The command prompt
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """To exit the program: Quit command"""
        return True

    def do_EOF(self, arg):
        """To exit the program: EOF (end-of-file) signal"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
