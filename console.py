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

    def do_delete(self, arg):
        """Deletes an instance based on the class name and id
            (save the change into the JSON file).
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
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based
            or not on the same class name. Ex. $ all BaseModel or $ all.
            The printed result must be a list of strings.
        """
        if len(arg) > 0 and arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            str_list = []
            for obj in storage.all().values():
                if len(arg) > 0 and arg[0] == obj.__class__.__name__:
                    str_list.append(obj.__str__())
                elif len(arg) == 0:
                    str_list.append(obj.__str__())
            print(str_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
            by adding or updating attribute-save the change into the Json file
        """



if __name__ == '__main__':
    HBNBCommand().cmdloop()
