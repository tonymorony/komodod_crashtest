#!/usr/bin/env python3

import csv
from subprocess import check_output

ac_name = "RPCTEST"

file = open("calls.txt", "r")

with open('errors_test.csv', 'w+') as csvfile:
    for line in file:
        lineargs = line.split()
        command = ["komodo-cli", "-ac_name=" + ac_name] + lineargs
        output = check_output(command)
        fieldnames = ['Call', 'Output']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Call': command, 'Output': output})
