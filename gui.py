from tkinter import *
from guiClass import *


root = Tk()  # main window
root.title("Coin Caster - Alpha 0.1")

# add images/icons to your gui
menu = MainMenu(root)
coin_window = CoinWindow(root)
ledger_window = LedgerDisplay(root)
root.mainloop()  # runs root
