#!/usr/bin/python3
"""Defines the entry point of the command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Represents the class for the  command interpreter"""

    # The command prompt
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF (end-of-file) signal to exit the program"""
        return True

    def emptyline(self):
        """Do not execute anything on ENTER (receive an empty line)"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel
            saves it (to the JSON file) and prints the id.
        """
        if not arg or arg == "":
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.__ClassName[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
            based on the class name and id.
        """
        if not arg or arg == "":
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            if key not in storage.all():
                print("** no instance  found **")
            else:
                print(storage.all()[key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
