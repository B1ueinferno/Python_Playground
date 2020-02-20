import random, time, copy

def listPrint(list):
    lastItem = len(list)-1    
    if list != []:
        for index, i in enumerate(list):
            if index == lastItem:
                print ("and " + i)
            else:
                print(i + " ", end='')
    else:
        print ("List is empty")

sports = ['baseball', 'basketball', 'football', 'hockey', 'hockey']
colors = ['red', 'blue', 'yellow']
blank = []
listPrint(sports)
listPrint(colors)
listPrint(blank)