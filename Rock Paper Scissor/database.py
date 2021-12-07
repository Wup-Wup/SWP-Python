import mysql.connector


def connect():
    myDb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pokemon03"
    )
    myCursor = myDb.cursor()
    create(myCursor)
    myDb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pokemon03",
        database="game"
    )
    myCursor = myDb.cursor()
    table(myCursor)
    return myCursor, myDb


def create(myCursor):
    myCursor.execute("CREATE DATABASE IF NOT EXISTS game")


def table(myCursor):
    myCursor.execute("CREATE TABLE IF NOT EXISTS game "
                     "(game_number INT AUTO_INCREMENT PRIMARY KEY, player_symbol VARCHAR(25), "
                     "computer_symbol VARCHAR(25), winner VARCHAR(20))")


def insert(myDb, myCursor, playerSymbol, computerSymbol, winner):
    sql = "INSERT INTO game (player_symbol, computer_symbol, winner) VALUES (%s, %s, %s)"
    values = (playerSymbol, computerSymbol, winner)
    myCursor.execute(sql, values)
    myDb.commit()


def select(myCursor):
    myCursor.execute("Select game_number from game order by game_number DESC limit 1")
    myResult = myCursor.fetchone()
    print("Games played overall: "+str(myResult[0])+"\n")

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
    print("Over every game played the player chose: ")
    print("Paper " + str(numberPaper[0]) + " times")
    print("Rock " + str(numberRock[0]) + " times")
    print("Scissors " + str(numberScissors[0]) + " times")
    print("Spock " + str(numberSpock[0]) + " times")
    print("Lizard " + str(numberLizard[0]) + " times \n")

    myCursor.execute("Select count(computer_symbol) from game where computer_symbol = 'Paper'")
    numberPaper = myCursor.fetchone()
    myCursor.execute("Select count(computer_symbol) from game where computer_symbol = 'Rock'")
    numberRock = myCursor.fetchone()
    myCursor.execute("Select count(computer_symbol) from game where computer_symbol = 'Scissors'")
    numberScissors = myCursor.fetchone()
    myCursor.execute("Select count(computer_symbol) from game where computer_symbol = 'Spock'")
    numberSpock = myCursor.fetchone()
    myCursor.execute("Select count(computer_symbol) from game where computer_symbol = 'Lizard'")
    numberLizard = myCursor.fetchone()
    print("Over every game played the computer chose: ")
    print("Paper " + str(numberPaper[0]) + " times")
    print("Rock " + str(numberRock[0]) + " times")
    print("Scissors " + str(numberScissors[0]) + " times")
    print("Spock " + str(numberSpock[0]) + " times")
    print("Lizard " + str(numberLizard[0]) + " times \n")

    myCursor.execute("Select count(winner) from game where winner = 'Player'")
    PlayerWon = myCursor.fetchone()
    myCursor.execute("Select count(winner) from game where winner = 'Computer'")
    ComputerWon = myCursor.fetchone()
    myCursor.execute("Select count(winner) from game where winner = 'Draw'")
    draw = myCursor.fetchone()

    print("Overall the Player won "+str(PlayerWon[0])+" times")
    print("Overall the Computer won "+str(ComputerWon[0])+" times")
    print("Overall there has been "+str(draw[0])+" draws")


