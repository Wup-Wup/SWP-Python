import random
import database
import window
import requests


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


def sendRequest(username, countScissors, countRock, countPaper, countSpock, countLizard, apiIP="http://127.0.0.1:5000"):
    reqUrl = apiIP + "/v1/updateRecord"
    reqUrl += "?username=" + str(username) + "&voteScissors=" + str(countScissors)
    reqUrl += "&voteRock=" + str(countRock) + "&votePaper=" + str(countPaper)
    reqUrl += "&voteSpock=" + str(countSpock) + "&voteLizard=" + str(countLizard)
    responseCode = 0
    try:
        response = requests.post(reqUrl, None)
        responseCode = response.status_code
    except:
        return 0
    return responseCode



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

myCursor.execute("Select count(player_symbol) from game where player_symbol = 'Paper'")
numberPaper = myCursor.fetchone()
myCursor.execute("Select count(player_symbol) from game where player_symbol = 'Rock'")
numberRock = myCursor.fetchone()
myCursor.execute("Select count(player_symbol) from game where player_symbol = 'Scissors'")
numberScissors = myCursor.fetchone()
myCursor.execute("Select count(player_symbol) from game where player_symbol = 'Spock'")
numberSpock = myCursor.fetchone()
myCursor.execute("Select count(player_symbol) from game where player_symbol = 'Lizard'")
numberLizard = myCursor.fetchone()

sendRequest("Bertoni", numberScissors, numberRock, numberPaper,numberSpock, numberLizard)

if stats():
    database.select(myCursor)
