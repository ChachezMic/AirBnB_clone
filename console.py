#!/usr/bin/python3
"""This is a module that defines class that creates a command interpreter
"""


import cmd
import sys
import models
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    hbnb command intertpreter
    """
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """
        quit the interpreter.
        """
        return True

    def do_create(self, arg):
        """
        creates a new instance of base model.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            my_model = getattr(models, class_name)
            instance = my_model()
            storage.save()
            print(instance.id)
        except AttributeError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        shows all the instances of class_name and its id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            my_model = getattr(models, class_name)
            if len(args) == 1:
                print("** instance id missing **")
                return

            obj_id = args[1]
            instance = storage.get(class_name, obj_id)
            if instance is None:
                print("** no instance found **")
            else:
                print(instance)
        except AttributeError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        deletes an instance based on the classname and its id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        try:
            my_model = getattr(models, class_name)
            if len(args) == 1:
                print("** instance id missing **")
            obj_id = args[1]
            instance = storage.get(class_name, obj_id)
            if instance is None:
                print("** no instance found **")
            else:
                storage.delete(instance)
                storage.save()
                print(f"{class_name} deleted")

        except AttributeError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        prints all instances based on or not class_name and id
        """
        if arg:
            try:
                my_model = getattr(models, arg)
                instances = storage.all(my_model)
            except AttributeError:
                print("** class doesn't exist **")
        else:
            all_instances = storage.all()

            instance_list = []
            for instance in all_instances.values():
                instance_list.append(str(instance))
                print(instance_list)

    def do_update(self, arg):
        """
        updates an existing instance of a model_class based on user_input
        """
        args = arg.split()
        if len(args) != 4:
            print("** Usage: update <class name> <id> <attribute name> <attribute value> **")
            return
        class_name = args[0]
        obj_id = args[1]
        try:
            my_model = getattr(models, class_name)
        except AttributeError:
            print("** class doesn't exist **")
            return
        instance = storage.get(class_name, obj_id)

        if instance is None:
            print("** no instance found **")
            return
        attr_name = args[2]
        try:
            setattr(instance, attr_name, args[3])
            storage.save()
            print("** Object updated **")

        except AttributeError:
            print("** attribute name missing **")

    def do_EOF(self, arg):
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
