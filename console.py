#!/usr/bin/python3
"""
CLI for the airbnb clone
"""

import cmd
import models
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    # intro = "Welcome to the hbnb shell. Type help or ? to list commands\n"
    prompt = "(hbnb) "

    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_create(self, line):
        """ Creates an instance of a specified class"""
        __class_name = line
        if (not len(line)):
            print("** class name missing **")
            return
        if (self.__classes.get(line) is None):
            print("** class doesn't exist **")
            return
        inst = self.__classes[__class_name]()
        inst.save()
        print(inst.id)

    def do_show(self, line):
        """ Prints the string representation of an instance"""
        checked = self.ok(self, line)
        if (checked[0]):
            obj = checked[1]
            print(obj)

    def do_destroy(self, line):
        """ Deletes an instance"""
        checked = self.ok(self, line)
        if (checked[0]):
            obj = checked[1]
            key = checked[2]
            models.storage.all().pop(key)
            models.storage.save()
            # print(del obj)  # doesn't delete it from storage

    def do_all(self, line):
        """ Prints all instances or instances of a specified class"""
        if (len(line) and self.__classes.get(line) is None):
            print("** class doesn't exist **")
            return
        all_objs = []
        objs = models.storage.all()
        for key, obj in objs.items():
            if (not len(line)):
                all_objs.append(str(obj))
            elif (line == key.split(".")[0]):
                all_objs.append(str(obj))
        print(all_objs)

    def do_count(self, line):
        """ counts all instances or instances of a specified class"""
        if (len(line) and self.__classes.get(line) is None):
            print("** class doesn't exist **")
            return
        all_objs = []
        objs = models.storage.all()
        for key, obj in objs.items():
            if (not len(line)):
                all_objs.append(str(obj))
            elif (line == key.split(".")[0]):
                all_objs.append(str(obj))
        print(len(all_objs))

    def do_update(self, line):
        """ Updates attributes of an instance"""
        checked = self.ok(self, line)
        if (not checked[0]):
            return

        obj = checked[1]
        key = checked[2]

        # HERE IS WHERE
        args = []
        if (" {" in line):
            attr = line.split(" {")[1]
            attr = attr.replace("}", "")
            attr = attr.split(" ")
            attr_args = []
            print(attr)
            class_name, inst_id = key.split(".")
            print("-------------")
            for i in range(0, len(attr), 2):
                at = attr[i].strip(":")
                value = attr[i + 1].strip(":")
                attr_args.append([class_name, inst_id, at, value])
            print(attr_args)
            # str()
        else:
            args = shlex.split(line)
        if (not len(args) > 2):
            print("** attribute name missing **")
            return
        attr = args[2]

        if (not len(args) > 3):
            print("** value missing **")
            return
        value = args[3]  # int, float and stuff not handled yet
        setattr(obj, attr, value)
        models.storage.save()
        # print("The type of the value is: ", type(value))
        # print(obj)

    def do_EOF(self, line):
        """ Closes the shell when EOF (ctrl + D) is detected"""
        print("")  # to be removed for the checker
        return True

    def do_quit(self, line):
        """ Quits the program"""
        print("")  # to be removed for the checker
        return True

    def precmd(self, line):
        """ intercepts the cmd at precmd"""
        if (len(line)):
            if ("." in line):
                args = line
                if (" " in line):
                    args = line.split(" ")[0]
                if ("." in args):
                    class_name, others = line.split(".")
                    command, others = others.split("(")
                    params = others.replace(")", "").replace(", ", " ")
                    line = command + " " + class_name + " " + params
                    print("{} {} {}".format(command, class_name, params))
        # print(line)
        return cmd.Cmd.precmd(self, line)

    def emptyline(self):
        return False

    @staticmethod
    def ok(self, line):
        """ Checks if the input is valid"""
        params = shlex.split(line)

        if (not len(line)):
            print("** class name missing **")
            return False
        if (self.__classes.get(params[0]) is None):
            print("** class doesn't exist **")
            return [False, None]
        class_name = params[0]

        if (len(params) < 2):
            print("** instance id missing **")
            return [False, None]
        inst_id = params[1]

        objs = models.storage.all()
        key = class_name + "." + inst_id
        obj = objs.get(key)
        if (obj is None):
            print("** no instance found **")
            return [False, None]
        return [True, obj, key]


if __name__ == "__main__":
    HBNBCommand().cmdloop()
