import random, math, os

def collatz(number):
    if (number % 2) == 0:
        return (number // 2)
    else:
        return ((3 * number) +1)

while True:
    try:
        number = int(input("Enter a number: "))
        break
    except:
        print("Please enter a number, not a letter or special character.")
while number != 1:
    number= collatz(number)
    print (number)
