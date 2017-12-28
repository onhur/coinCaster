"""

File: apiCall.py
Author: Alan Korek
Date: 20171221
ledger application

"""
# import
import json
import os


# variables
file_name = 'ledger'
file_path = 'C:\\Users\\alan\\PycharmProjects\\coinCaster'
file_suffix = 'dat'
file = os.path.join(file_path, file_name + "." + file_suffix)


#  add line to ledger
def add_line(coin_type, cost_each, date, total_cost, line_total_coin):
    ledger_array = []
    line = {"coin_type": coin_type, "date": date, "cost_each": cost_each, "total_cost": total_cost,
            "line_total_coin": line_total_coin}
    ledger_array.append(line)
    return ledger_array


# save ledger to file
def save_ledger(ledger):
    with open(file, 'w') as f:
        f.writelines(json.dumps(ledger))


# load ledger from saved file
def load_ledger():
    ledger_load_file = open(file).read()
    ledger_array = json.loads(ledger_load_file)
    return ledger_array

