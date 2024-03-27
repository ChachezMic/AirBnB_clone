#!/usr/bin/python3
"""This is a module that defines class that creates a command interpreter
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    hbnb command intertpreter
    """
    prompt = '(hbnb)'

    def do_quit(self, org):
        """
        quit the interpreter.
        """
        return True

    def do_EOF(self, org):
        """
        Exit on end of file.
        """
        print()
        return True

    def emptyline(self):
        """
        Handle emptylines gracefully.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
