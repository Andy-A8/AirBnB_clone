#!/usr/bin/python3
"""Defines the entry point of the command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Represents the class for the  command interpreter"""

    # The command prompt
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF (end-of-file) signal to exit the program"""
        return True

    def emptyline(self):
        """Do not execute anything on ENTER (receive an empty line)"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
