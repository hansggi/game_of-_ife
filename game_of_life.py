#this small program shows Conways Game of Life: how cells evolve under certain simple rules
#Adjust the probability parameter "prob" to make different patterns
import random
import numpy as np
import time
from matplotlib import pyplot as plt
import matplotlib.animation as animation

N = 100 #dim of board
prob = 0.7 #probability that a given cell will start out as alive

def make_board(N, p): #makes a N x N board, probability p for a given cell to start out alive
    board = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if random.uniform(0, 1)  < p:
                    board[i,j] = 1
    return board

def count_neighbours(i, j, board):
    count = 0
    if j != 0:
        count += board[i, j-1]
        if i != 0:
            count += board[i-1, j-1]
        if i != N-1:
            count += board[i+1, j-1]
    if j != N-1:
        count += board[i, j+1]
        if i != 0:
            count += board[i-1, j+1]
        if i != N-1:
            count += board[i+1, j+1]
    if i != 0:
        count += board[i-1, j]
    if i != N-1:
        count += board[i+1, j]
    
    return count

def next_gen(board):
    old_board = board.copy()
    for i in range(N):
        for j in range(N):
            k = count_neighbours(i, j, old_board)
            if k <= 1:
                board[i,j] = 0
            elif k >= 4:
                board[i,j] = 0
            elif k == 3:
                board[i,j] = 1
    return board
            
board = make_board(N, prob)
fig = plt.gcf() #get current figure, create new if none exist
im = plt.imshow(board, cmap = "magma")

def animate(i):
    im.set_data(next_gen(board))
    return im, 

anim = animation.FuncAnimation(fig, animate, frames = 1000, interval = 100)
plt.draw()
plt.show()
