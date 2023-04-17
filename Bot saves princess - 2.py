#Hackerrank Bot saves princess - 2 challenge
#Author: Luciano Andrade

#In this version of "Bot saves princess", Princess Peach and bot's position are randomly set. Can you save the princess?

#Task

#Complete the function nextMove which takes in 4 parameters - an integer N, integers r and c indicating the row & column position of the bot and the character array grid - and outputs the next move the bot makes to rescue the princess.

#Input Format

#The first line of the input is N (<100), the size of the board (NxN). The second line of the input contains two space separated integers, which is the position of the bot.

#Grid is indexed using Matrix Convention

#The position of the princess is indicated by the character 'p' and the position of the bot is indicated by the character 'm' and each cell is denoted by '-' (ascii value: 45).

#Output Format

#Output only the next move you take to rescue the princess. Valid moves are LEFT, RIGHT, UP or DOWN

def nextMove(n,r,c,grid):
    
    princess="p"
    
    p=[[index1, index2] for index1,value1 in enumerate(grid) for index2,value2 in enumerate(value1) if value2==princess]

    row = p[0][0]
    col = p[0][1]

    if r > row:
        move = "UP"
    elif r < row:
        move = "DOWN"
    elif c > col:
        move = "LEFT"
    elif c < col:
        move = "RIGHT"
    
    return move

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))

