import random, time, copy

def listPrint(list):
    if list != []:
        for i in list:
            if i == list[-1]:
                print ("and " + i)
            else:
                print(i + " ", end='')
    else:
        print ("List is empty")

sports = ['baseball', 'basketball', 'football', 'hockey']
colors = ['red', 'blue', 'yellow']
blank = []
listPrint(sports)
listPrint(colors)
listPrint(blank)