import numpy as np
import random
import sys

sys.setrecursionlimit(10**8) # Increasing recursion limit

# Recursive Backtracking Maze Algorithm
def backtracking(col, row): 
    visited[col, row]=1 # Marking visited
    
    while(1):
        cannotGo=[] # 1:North 2:East 3:South 4:West
        if row-2<=0:
            cannotGo.append(1)
        if col+2>=SIZE-1:
            cannotGo.append(2)
        if row+2>=SIZE-1:
            cannotGo.append(3)
        if col-2<=0:
            cannotGo.append(4)
        
        direction = random.randint(1, 4) # Determining direction (only array borders are considered)
        if direction in cannotGo:
            continue
    
        if direction==1 and visited[col, row-2]!=1: # Recursing by determined direction
            visited[col, row-1]=1
            backtracking(col, row-2)
        elif direction==2 and visited[col+2, row]!=1:
            visited[col+1, row]=1
            backtracking(col+2, row)
        elif direction==3 and visited[col, row+2]!=1:
            visited[col, row+1]=1
            backtracking(col, row+2)
        elif direction==4 and visited[col-2, row]!=1:
            visited[col-1, row]=1
            backtracking(col-2, row)
        
        # Backtrack
        if cannotGo == [] and visited[col, row-2]==1 and visited[col+2, row]==1 and visited[col-2, row]==1 and visited[col, row+2]==1:
            return
        elif cannotGo == [1] and visited[col+2, row]==1 and visited[col-2, row]==1 and visited[col, row+2]==1:
            return
        elif cannotGo == [2] and visited[col, row-2]==1 and visited[col-2, row]==1 and visited[col, row+2]==1:
            return
        elif cannotGo == [3] and visited[col, row-2]==1 and visited[col+2, row]==1 and visited[col-2, row]==1:
            return
        elif cannotGo == [4] and visited[col, row-2]==1 and visited[col+2, row]==1 and visited[col, row+2]==1:
            return
        elif cannotGo == [1, 4] and visited[col+2, row]==1 and visited[col, row+2]==1:
            return
        elif cannotGo == [1, 2] and visited[col-2, row]==1 and visited[col, row+2]==1:
            return    
        elif cannotGo == [3, 4] and visited[col+2, row]==1 and visited[col, row-2]==1:
            return
        elif cannotGo == [2, 3] and visited[col-2, row]==1 and visited[col, row-2]==1:
            return
        else:
            continue
    
    
def mazeGenerator(size):
    global SIZE
    if size%2==0: # 짝수면 규격이 몬가 안맞던뎅
        size-=1
    SIZE=size
        
    global visited
    visited = np.zeros((size, size), dtype=int) # Generating array for backtracking
    
    backtracking(1, 1) # let's gogo
    
    return visited
#Algorithm implemented by YEOUNHYEOK