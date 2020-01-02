import random

class MazeGrid():

    def __init__(self):
        self.maze_grid = []

        self.width = 0
        self.height = 0

    def gridMaze(self, width, height):
        self.width = width
        self.height = height

        i = 0
        j = 0
    
        while i < height:
            self.maze_grid.append([])
            while j < width:
                self.maze_grid[i].append(MazeCell())
                j+=1
            j = 0
            i+=1
        i = 0

    def checkComplete(self):
        i = 0
        j = 0

        while(i < self.height):
            while(j < self.width):
                if (self.maze_grid[i][j].isPartOfMaze == False):
                    return False
                j+=1
            i+=1
            j=0
            
        return True



class MazeCell():

    dirExit = ""


    inTracing = False
    isPartOfMaze = False





class MazeTracer():

    def __init__(self):
        self.currentCellX = 0
        self.currentCellY = 0

        self.startCellX = 0
        self.startCellY = 0

        self.cellsAdded = 0

        self.direction = ""

    def chooseRandomCell(self, mazeGrid):
        chosen = False
    
        while not chosen:
            testCellX = random.randint(0,mazeGrid.width-1)
            testCellY = random.randint(0,mazeGrid.height-1)
            testCell = mazeGrid.maze_grid[testCellY][testCellX]
            if(testCell.isPartOfMaze == False):
                self.currentCellX = testCellX
                self.currentCellY = testCellY

                self.startCellX = testCellX
                self.startCellY = testCellY

                chosen = True

    def randomizeDirection(self, mazeGrid):
        previousOppositeDirection = self.oppositeDirection()

        directionChosen = False
        
        while not directionChosen:
            if(random.randint(1,2) == 1):
                if(random.randint(1,2) == 1 and self.currentCellY > 0):
                    self.direction = "N"
                    directionChosen = True
                elif(self.currentCellY < mazeGrid.height-1):
                    self.direction = "S"
                    directionChosen = True
            else:
                if(random.randint(1,2) == 1 and self.currentCellX > 0):
                    self.direction = "W"
                    directionChosen = True
                elif(self.currentCellX < mazeGrid.width-1):
                    self.direction = "E"
                    directionChosen = True

        while(self.direction == previousOppositeDirection):
            if(random.randint(1,2) == 1):
                if(random.randint(1,2) == 1 and self.currentCellY > 0):
                    self.direction = "N"
                elif(self.currentCellY < mazeGrid.height-1):
                    self.direction = "S"
            else:
                if(random.randint(1,2) == 1 and self.currentCellX > 0):
                    self.direction = "W"
                elif(self.currentCellX < mazeGrid.width-1):
                    self.direction = "E"

    def navigateMaze(self, mazeGrid):
        while(mazeGrid.maze_grid[self.currentCellY][self.currentCellX].isPartOfMaze == False):
            self.randomizeDirection(mazeGrid)

            currentCell = mazeGrid.maze_grid[self.currentCellY][self.currentCellX]

            currentCell.dirExit = self.direction
            currentCell.inTracing = True

            if(self.direction == "N"):
                self.currentCellY -= 1
            elif(self.direction == "S"):
                self.currentCellY += 1
            elif(self.direction == "W"):
                self.currentCellX -= 1
            elif(self.direction == "E"):
                self.currentCellX += 1

            newCell = mazeGrid.maze_grid[self.currentCellY][self.currentCellX]

            if (newCell.inTracing == False):
                self.cellsAdded += 1


    def oppositeDirection(self):
        if(self.direction == "N"):
            return "S"
        elif(self.direction == "S"):
            return "N"
        elif(self.direction == "E"):
            return "W"
        elif(self.direction == "W"):
            return "E"

    def addToMaze(self, mazeGrid):
        self.currentCellX = self.startCellX
        self.currentCellY = self.startCellY

        i = 0

        j = 0
        k = 0

        while(j < mazeGrid.height):
            while(k < mazeGrid.width):
                if (mazeGrid.maze_grid[j][k].inTracing == True):
                    mazeGrid.maze_grid[j][k].inTracing = False
                k+=1
            j+=1
            k=0
        
        
        while(i < self.cellsAdded):
            currentCell = mazeGrid.maze_grid[self.currentCellY][self.currentCellX]
            currentCell.isPartOfMaze = True
            if(currentCell.dirExit == "N"):
                self.currentCellY -= 1
            elif(currentCell.dirExit == "S"):
                self.currentCellY += 1
            elif(currentCell.dirExit == "E"):
                self.currentCellX += 1
            elif(currentCell.dirExit == "W"):
                self.currentCellX -= 1
            
            i += 1

        self.cellsAdded = 0
        

    def chooseStartCell(self, mazeGrid):
        initialCellX = random.randint(0,mazeGrid.width-1)
        initialCellY = random.randint(0,mazeGrid.height-1)

        mazeGrid.maze_grid[initialCellY][initialCellX].isPartOfMaze = True


    def update(self, mazeGrid):
        self.chooseRandomCell(mazeGrid)
        self.navigateMaze(mazeGrid)
        self.addToMaze(mazeGrid)
        
        
    

