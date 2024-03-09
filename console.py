#!/bin/bash/python3
"""Defines the entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.cmd):
    """Represents the class for the  command interpreter"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
