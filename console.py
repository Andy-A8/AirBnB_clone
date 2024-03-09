#!/bin/bash/python3
"""Defines the entry point of the command interpreter"""


import cmd


class HBNBCommand(cmd.cmd):
    """Represents the class for the  command interpreter"""

    def do_quit(self, arg):
        """To exit the program: Quit command"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
