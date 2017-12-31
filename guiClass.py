"""

Name: guiClass.py
Author: Alan Korek
Date: 2017 12 27
Script holds all the class's for the GUI configuration

"""
# imports
from tkinter import *
from coinClass import Coin
from ledger import *
from toolTip import *

# global variables
RIPPLE_COIN = Coin("ripple")
BITCOIN_COIN = Coin("bitcoin")
STELLAR_COIN = Coin("Stellar")


def to_do():
    print('TODO')

# Class to make the main menu
# TODO: Add functions
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


# Class that creates the coin window at the top of the screen
# TODO: Make it so coins can be added removed by the end user
class CoinWindow:

    def __init__(self, root):
        ripple_image_file = "img\\ripple.png"
        bitcoin_image_file = "img\\bitcoin.png"
        stellar_image_file = "img\\Stellar.png"
        add_line_image = "img\\pluss.png"

        bd_size = 1
        padx_size = 2
        pady_size = 2

        coin_frame = Frame(root)
        coin_frame.pack(side=TOP, anchor=W, fill=X)

        border_label = Label(coin_frame, bd=bd_size, relief=SUNKEN, anchor=W)
        border_label.pack(side=TOP, fill=X)

        ripple_image = PhotoImage(file=ripple_image_file)
        ripple_image_label = Label(border_label, image=ripple_image)
        ripple_image_label.image = ripple_image
        ripple_image_label.pack(side=LEFT, anchor=W)

        ripple_label = Label(border_label, text="{0} : ${1}".format(RIPPLE_COIN.name, RIPPLE_COIN.price_usd))
        ripple_label.pack(side=LEFT, anchor=W, padx=padx_size, pady=pady_size)

        bitcoin_image = PhotoImage(file=bitcoin_image_file)
        bitcoin_image_label = Label(border_label, image=bitcoin_image)
        bitcoin_image_label.image = bitcoin_image
        bitcoin_image_label.pack(side=LEFT, anchor=W, padx=padx_size, pady=pady_size)

        bitcoin_label = Label(border_label, text="{0} : ${1}".format(BITCOIN_COIN.name, BITCOIN_COIN.price_usd))
        bitcoin_label.pack(side=LEFT, anchor=W, padx=padx_size, pady=pady_size)

        stellar_image = PhotoImage(file=stellar_image_file)
        stellar_image_label = Label(border_label, image=stellar_image)
        stellar_image_label.image = stellar_image
        stellar_image_label.pack(side=LEFT, anchor=W, padx=padx_size, pady=pady_size)

        stellar_label = Label(border_label, text="{0} : ${1}".format(STELLAR_COIN.name, STELLAR_COIN.price_usd))
        stellar_label.pack(side=LEFT, anchor=W, padx=padx_size, pady=pady_size)

        add_ledger_line_image = PhotoImage(file=add_line_image)
        add_ledger_line_image_label = Label(root, image=add_ledger_line_image)
        add_ledger_line_image_label.image = add_ledger_line_image

        add_ledger_line_button = Button(root)
        add_ledger_line_button.config(image=add_ledger_line_image)
        add_ledger_line_button.pack(side=RIGHT, anchor=N)

        createToolTip(add_ledger_line_button, "Add new line to the widget")

# class to show fill in the ledger window
class LedgerDisplay:
    def __init__(self, root):
        padx_size = 1
        pady_frame_size = 10
        bd_size = 2
        header_fg = "white"
        header_bg = "dark blue"
        column_width = 10

        ledger_frame = Frame(root)
        ledger_frame.pack(side=TOP, anchor=W, padx=padx_size, pady=pady_frame_size)

        type_label = Label(ledger_frame, text="Coin Type", bd=bd_size, fg=header_fg, bg=header_bg, width=column_width)
        type_label.grid(row=0, column=0, padx=padx_size, sticky=W)

        date_label = Label(ledger_frame, text="Date", bd=bd_size, fg=header_fg, bg=header_bg, width=column_width)
        date_label.grid(row=0, column=1, padx=padx_size, sticky=W)

        cost_each_coin_label = Label(ledger_frame, text="Cost", bd=bd_size, fg=header_fg, bg=header_bg, width=column_width)
        cost_each_coin_label.grid(row=0, column=2, padx=padx_size, sticky=W)

        total_cost_label = Label(ledger_frame, text="Total Cost (USD)", bd=bd_size, fg=header_fg, bg=header_bg, width=column_width)
        total_cost_label.grid(row=0, column=3, padx=padx_size, sticky=W)

        total_coin_label = Label(ledger_frame, text="Total Coin", bd=bd_size, fg=header_fg, bg=header_bg, width=column_width)
        total_coin_label.grid(row=0, column=4, padx=padx_size, sticky=W)

        pl_label = Label(ledger_frame, text="Profit or Loss", bd=bd_size, fg=header_fg, bg=header_bg, width=column_width)
        pl_label.grid(row=0, column=5, padx=padx_size, sticky=W)


        self.show_lines(ledger_frame)

    def show_lines(self, root):
        ledger = load_ledger()

        padx_size = 2
        pady_size = 2
        bd_size = 1
        line_fg = "black"
        line_bg = "lite gray"
        profit_fg = "blue"
        loss_fg = "red"
        profit_threshold = 0

        for row, line in enumerate(ledger, start=2):

            type_label = Label(root, text=line['coin_type'])
            type_label.grid(row=row, column=0, padx=padx_size)

            date_label = Label(root, text=line['date'])
            date_label.grid(row=row, column=1, padx=padx_size)

            cost_each_coin_label = Label(root, text=line['cost_each'])
            cost_each_coin_label.grid(row=row, column=2, padx=padx_size)

            total_cost_label = Label(root, text=line['total_cost'])
            total_cost_label.grid(row=row, column=3, padx=padx_size)

            total_coin_label = Label(root, text=line['line_total_coin'])
            total_coin_label.grid(row=row, column=4, padx=padx_size)

            total_profit_loss = (float(line['line_total_coin']) * float(RIPPLE_COIN.price_usd))\
                                - float(line['total_cost'])

            if total_profit_loss > profit_threshold:
                total_profit_loss_label = Label(root, text=total_profit_loss, fg=profit_fg)
            else:
                total_profit_loss_label = Label(root, text=total_profit_loss, fg=loss_fg)

            total_profit_loss_label.grid(row=row, column=5, padx=padx_size)

