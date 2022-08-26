"""
Main Part of a program written by Mosiichuk Kyrylo
"""

from sys import argv

import classes
import load


def __creator():
    print("Creator of a program: Mosiichuk Kyrylo\n")


def __task_term():
    print(" From given data, Find all of tasks which have been done with mark 90% and higher\n "
          "First line: Average mark of chosen tasks rounded to 1 symbol after comma, task, number of tries\n "
          "Second line Tasks with mark less than 75%: Surname,Name, Father Name, Mark, Year \n"
          "(Use a tab as delimiter between ranges and sort tries by decreasing (mark,year,Surname,Name,Father name )")


def __print():
    """
    :return:Info about Var creator task etc
    """
    __creator()
    __task_term()


def check():
    """
    starting program if enough arguments
    """
    __print()
    print("*****")
    if len(argv) == 2:
        process(argv[1])
    else:
        print("***** program aborted *****")


def process(file_name):
    """
    taking file path and getting information about another files for work
    :param file_name: file with staff like encoding, filepath for serving a program
    """
    try:
        json_file = load.loader_from_ini(file_name)
        with classes.Info() as info:
            load.load(info, json_file["input"]["csv"], json_file["input"]["json"], json_file["input"]["encoding"])
            load.outputprint(info, json_file["output"]["fname"], json_file["output"]["encoding"])
    except BaseException:
        print("\n***** program aborted *****")


check()
