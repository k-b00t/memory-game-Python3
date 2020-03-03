from os import system, name
from re import match as regExTest
from time import sleep
from random import randrange


cache = { 
    'config': {
        'rounds': 10,
        'tableTimer': 5,
        'gameDificulty': 5
    },
    'playersName': {
        'playerOne': 'Player One',
        'playerTwo': 'Computer'
    },
    'score': {
        'playerOne': 0,
        'playerTwo': 0
    },
    'tableValues': False,
    'playersValues': [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
}




''' ---------------------- INTERFACE CONSTRUCTOR ---------------------- '''


def printBanner():
    print('\n' + ' ' * 4 + '-------- MEMORY GAME --------\n\n')



def printIntro():
    print(' ' * 4 + '0-Play')
    print(' ' * 4 + '1-Rules (not implemented)')
    print(' ' * 4 + '2-Terms (not implemented)')
    print(' ' * 4 + '3-Options')



def printOptions():
    print('\n' + ' ' * 4 + '--------- OPTIONS ----------\n\n')
    print(' ' * 4 + '0 Player name:        ' + str(cache['playersName']['playerOne']))
    print(' ' * 4 + '1 Rounds:             ' + str(cache['config']['rounds']))
    print(' ' * 4 + '2 Dificulty:          ' + str(cache['config']['gameDificulty']) + '/9')
    print(' ' * 4 + '3 Memorize timer:     ' + str(cache['config']['tableTimer']) + ' seconds')
    print(' ' * 4 + '4 Exit\n')
    
    

def printRules():
    print('    ')



def printTerms():
    print('    ')



def printScore():
    print('\n ' * 2 + 'Score: ' + ' ' * 4 + 'Pl One ' + str(cache['score']['playerOne']) + ' ' * 4 + 'Pl Two ' + str(cache['score']['playerTwo']) + '\n\n\n')



def printBoardGame(values=False, temp=0):
    printScore()

    if not values:
        values = cache['playersValues']

    print('        1   2   3   4')
    print('      +---------------+')
    print('    A | ' + values[0][0] + ' | ' + values[1][0] + ' | ' + values[2][0] + ' | ' + values[3][0] + ' | ')
    print('      +---------------+')
    print('    B | ' + values[0][1] + ' | ' + values[1][1] + ' | ' + values[2][1] + ' | ' + values[3][1] + ' | ')
    print('      +---------------+')
    print('    C | ' + values[0][2] + ' | ' + values[1][2] + ' | ' + values[2][2] + ' | ' + values[3][2] + ' | ')
    print('      +---------------+')
    print('    D | ' + values[0][3] + ' | ' + values[1][3] + ' | ' + values[2][3] + ' | ' + values[3][3] + ' | ')
    print('      +---------------+')
    print('    E | ' + values[0][4] + ' | ' + values[1][4] + ' | ' + values[2][4] + ' | ' + values[3][4] + ' | ')
    print('      +---------------+\n')

    if temp != 0:
        print('  Clear display in: ' + str(temp) + ' seconds')



def printBoardGameResolved():
    values = cache['tableValues']
    tableTimer = cache['config']['tableTimer']

    for i in range(tableTimer, 0, -1):
        printBoardGame(values, i)
        sleep(1)
        clearDisplay()



def printPlayerTurn(player):
    clearDisplay()
    print('\n\n\n     Turn for: ' + cache['playersName'][player])
    sleep(1.5)
    clearDisplay()



def printComputerInput(values):
    printBoardGame()
    print('  Enter Row and column: ')
    sleep(.7)
    
    clearDisplay()
    printBoardGame()
    print('  Enter Row and column: ' + str(values[0][0] + 1) + chr(values[0][1] +65))
    print('  Enter Row and column: ')
    sleep(.3)
    
    clearDisplay()
    printBoardGame()
    print('  Enter Row and column: ' + str(values[0][0] + 1) + chr(values[0][1] +65))
    print('  Enter Row and column: ' + str(values[1][0] + 1) + chr(values[1][1] +65))
    sleep(.5)
    


def printPlayerScore(player):
    clearDisplay()
    print('\n\n\n     Player: ' + cache['playersName'][player] + ' gain one point!!')
    sleep(1.5)
    clearDisplay()



def printEndGame():
    if cache['score']['playerOne'] > cache['score']['playerTwo']:
        player = cache['playersName']['playerOne']
    else:
        player = cache['playersName']['playerTwo']

    print('\n\n\n     Player ' + player + ' WIN!!')
    printScore()
    exit(0)



def clearDisplay():
    if name == 'nt':
        system('cls')
    elif name == 'posix':
        system('clear')





''' ---------------------- GAME LOGIC ---------------------- '''


def userOptionChecker(value):
    if value == 'main menu':
        userInput = int( input('\n  Choose selection: '))

        while not userInput in [0,1,2,3]:
            userInput = int( input('  Choose a valid selection: '))


        if userInput == 0:
            clearDisplay()
            startGame()

        elif userInput == 1:
            clearDisplay()
            printRules()
            resetInterface()

        elif userInput == 2:
            clearDisplay()
            printTerms()
            resetInterface()

        elif userInput == 3:
            clearDisplay()
            printOptions()
            setOptions()
            resetInterface()






def setOptions():
    inputPlayer = ''

    while inputPlayer != 4:
        inputPlayer = int(input(' ' * 2 + 'Please choose selection: '))

        while not inputPlayer in [0,1,2,3,4]:
            inputPlayer = int(input(' ' * 2 + 'Please choose a valid selection: '))

        if inputPlayer == 0:
            playerName = str( input(' ' * 2 + 'Introduce alias: '))
            cache['playersName']['playerOne'] = playerName

        elif inputPlayer == 1:
            rounds = input(' ' * 2 + 'Introduce rounds: (0-9)')

            while not rounds in '0123456789':
                rounds = input(' ' * 2 + 'Introduce a valid rounds (0-9): ')

            cache['config']['rounds'] = int(rounds)

        elif inputPlayer == 2:
            dificulty = input(' ' * 2 + 'Introduce CPU dificult (0-9): ')
            
            while not dificulty in '0123456789':
                dificulty = input(' ' * 2 + 'Introduce a valid CPU dificult (0-9): ')

            cache['config']['gameDificulty'] = int(dificulty)

        elif inputPlayer == 3:
            timer = input(' ' * 2 + 'Introduce memorize timer (0-9): ')

            while not timer in '0123456789':
                timer = input(' ' * 2 + 'Introduce memorize timer (0-9): ')

            cache['config']['tableTimer'] = int(timer)
        
        clearDisplay()
        printOptions()

    main()

    






def createRandomValues():
    gameValues = 'ABCDEFGHIJ'
    resultComputed = []

    for i in range(2):
        temporalArrayValues = []
        copyGameValues = gameValues

        for i in range(1, 11):
            if i != 10:
                numRandom = randrange(0, len(copyGameValues) -1)
            else:
                numRandom = 0

            randomChart = copyGameValues[numRandom]
            copyGameValues = copyGameValues[0: numRandom] + copyGameValues[numRandom +1:]

            temporalArrayValues.append(randomChart)

            if i % 5 == 0:
                resultComputed.append(temporalArrayValues)
                temporalArrayValues = []

    cache['tableValues'] = resultComputed






def loopEntryValuesPlAndPc(turn):
    rounds = cache['config']['rounds']

    while cache['score']['playerOne'] + cache['score']['playerTwo'] != rounds:
        successPl = True
        successPc = True

        if turn:
            while successPl:
                printPlayerTurn('playerOne')
                printBoardGameResolved()
                plOneValues = playerInputValues()
                successPl = checkPlayerValues(plOneValues, 'playerOne')

                if cache['score']['playerOne'] + cache['score']['playerTwo'] == rounds:
                    printEndGame()
        else:
            turn = True
      
        while successPc:
            plTwoValues = computerInputValues()

            printPlayerTurn('playerTwo')
            printBoardGameResolved()
            printComputerInput(plTwoValues)

            successPc = checkPlayerValues(plTwoValues, 'playerTwo')

            if cache['score']['playerOne'] + cache['score']['playerTwo'] == rounds:
                printEndGame()




def playerInputValues():
    tempPlValues = []
    printBoardGame()

    for i in range(2):
        playerInput = input('  Enter Row and column: ')
        
        while not str(playerInput[0]) in '1234' and not playerInput[1] in 'ABCDE':
            playerInput = input('  Enter Row and column (e.g "4A"): ')

        tempPlValues.append([
            int(playerInput[0]) -1,
            ord(playerInput[1]) -65
        ])

    clearDisplay()
    return tempPlValues





def computerInputValues():
    probability = randrange(0,10)
    emptyPlayersValues = []

    for i in range( len(cache['playersValues'])):
        for j in range( len(cache['playersValues'][i])):
            if cache['playersValues'][i][j]  == ' ':
                emptyPlayersValues.append([i, j])

    randomValueOne = randrange(0, len(emptyPlayersValues))
    randomValueOne = emptyPlayersValues[randomValueOne]

    if probability < cache['config']['gameDificulty']:
        letterSelected = cache['tableValues'][randomValueOne[0]][randomValueOne[1]]
        
        for i in range( len(cache['tableValues'])):
            for j in range( len(cache['tableValues'][i])):
                if letterSelected == cache['tableValues'][i][j] and randomValueOne != [i, j]:
                    randomValueTwo = [i, j]
    else:
        randomValueTwo = randrange(0, len(emptyPlayersValues))
        randomValueTwo = emptyPlayersValues[randomValueTwo]

    return [randomValueOne, randomValueTwo]






def checkPlayerValues(values, player):
    letterOne = cache['tableValues'][ values[0][0] ][ values[0][1] ]
    letterTwo = cache['tableValues'][ values[1][0] ][ values[1][1] ]

    if values[0] != values[1]:
        if letterOne == letterTwo:
            cache['score'][player] += 1
            cache['playersValues'][ values[0][0] ][ values[0][1] ] = letterOne
            cache['playersValues'][ values[1][0] ][ values[1][1] ] = letterTwo
            
            printPlayerScore(player)
            return True

    return False






def startGame():
    createRandomValues()

    turn = randrange(0, 2)

    if turn == 0:
        turn = False

    loopEntryValuesPlAndPc(turn)





def resetInterface():
    input('\nPress any key to continue...')
    main()






def main():
    clearDisplay()
    printBanner()
    printIntro()
    userOptionChecker('main menu')





if __name__ == '__main__':
    main()