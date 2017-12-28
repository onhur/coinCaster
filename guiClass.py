"""

Name: guiClass.py
Author: Alan Korek
Date: 2017 12 27
Script holds all the class's for the GUI configuration

"""
from tkinter import *
from ledger import *


def to_do():
    print('TODO')



class MainMenu:

    def __init__(self, root):

        menu = Menu(root)
        root.config(menu=menu)

        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu, underline=0)
        file_menu.add_command(label="Save file", command=to_do, underline=0)
        file_menu.add_command(label="Open file", command=to_do, underline=0)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit, underline=0)

        coin_menu = Menu(menu)
        menu.add_cascade(label="Coin", menu=coin_menu, underline=0)
        coin_menu.add_command(label="New Coin", command=to_do, underline=0)
        coin_menu.add_command(label="Refresh Coin", command=to_do, underline=0)

        ledger_menu = Menu(menu)
        menu.add_cascade(label="Ledger", menu=ledger_menu, underline=0)
        ledger_menu.add_command(label="Add Transaction", command=to_do, underline=0)
        ledger_menu.add_command(label="Remove Transaction", command=to_do, underline=0)
        ledger_menu.add_separator()
        ledger_menu.add_command(label="Refresh Ledger", command=to_do, underline=0)
        ledger_menu.add_command(label="Search Ledger", command=to_do, underline=0)

        help_menu = Menu(menu)
        menu.add_cascade(label="Help", menu=help_menu, underline=0)
        help_menu.add_command(label="About", command=to_do, underline=0)
        help_menu.add_command(label="Help", command=to_do, underline=0)

