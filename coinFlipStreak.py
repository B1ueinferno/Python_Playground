import math, random, os

def flip100Streak():
    numberOfStreaks = 0
    flipList = []
    streakList = []
    for flip in range(100):
        flip = random.randint(0,1)
        if flip == 1:
            flipList.append("H")
        elif flip == 0:
            flipList.append("T")
    for i in range(len(flipList)-1):
        if flipList[i] == flipList[i+1]:
            streakList.append(i)
        else:
            if len(streakList) >= 5:
                numberOfStreaks += 1
            streakList = []
    return numberOfStreaks
    
def main():
    totalStreaks = 0
    for experimentNumber in range(10000):
        experiment = flip100Streak()
        print (str(experimentNumber +1) + ": Number of 6+ Streaks: " + str(experiment))
        totalStreaks = totalStreaks + experiment
    print("Total Streaks: " + str(totalStreaks))
    print('Chance of streak: %s%%' % (totalStreaks / (10000)))

if __name__ == "__main__":
    main()



