import random
import database
import window


def compare(p1, com, values, results):
    print("Player:" + answer)
    print("Computer:" + computer)
    calc = values[p1] - values[com]
    return results[calc % 5]


def stop():
    while True:
        cont = input("Would you like to play again? n/y \n")
        if cont == "y":
            return True
        elif cont == "n":
            return False


def stats():
    while True:
        cont = input("Would you like to see the stats of your games? n/y \n")
        if cont == "y":
            return True
        elif cont == "n":
            return False


myCursor, myDb = database.connect()
state = True
counter = 0
pWin = 0
comWin = 0

while state:
    daList = ["Scissors", "Rock", "Paper", "Lizard", "Spock"]
    result = ["Draw", "Player won", "Player won", "Player lost", "Player lost"]
    daValue = {"Scissors": 4, "Rock": 0, "Paper": 2, "Lizard": 3, "Spock": 1}
    answer = window.choosing_window()
    computer = random.choice(daList)
    resultString = compare(answer, computer, daValue, result)
    print(str(resultString) + "\n")
    if resultString == "Player won":
        pWin = pWin + 1
        winner = "Player"
    elif resultString == "Player lost":
        comWin = comWin + 1
        winner = "Computer"
    else:
        winner = "Draw"
    counter = counter + 1
    database.insert(myDb, myCursor, answer, computer, winner)
    state = stop()

print("Stats for this session: ")
print("Number of Games: " + str(counter))
print("Player won " + str(pWin) + " times")
print("Computer won " + str(comWin) + " times")
print("There has been " + str(counter - pWin - comWin) + " draws\n")

if stats():
    database.select(myCursor)
