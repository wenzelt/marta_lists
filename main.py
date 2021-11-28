# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("list_short.txt") as f:
        short = f.readlines()

    with open("list_long.txt") as f:
        long = f.readlines()

    output = []

    # for i in long:
    #     long.append(i.replace('\n',""))
    short = [i.replace('\n',"") for i in short]
    long = [i.replace('\n',"") for i in long]


    for short_line in short:
        for long_line in long:
            if short_line in long_line:
                output.append(short_line) if short_line not in output else None

    with open("output.txt", "w+") as f:
        for i in output:
            f.write(str(i+"\n"))

