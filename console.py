#!/usr/bin/python3
""" module that contains the entry point of the command interpreter """

import cmd


class HBNBCommand(cmd.Cmd):
    """ a class for command interpreter """

    prompt = "(hbnb) "

    def do_quit(self, inputs):
        """Quit command to exit the program"""
        quit()

    def do_EOF(self, inputs):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
