import pygame

import constants

from cell_objects import MazeTracer, MazeGrid, MazeCell

def askDimensions():
    try:
        widthWanted = int(input("\nWhat width would you like the maze to be?\n"))
        heightWanted = int(input("\nWhat height would you like the maze to be?\n"))
    except ValueError:
        print("\nInvalid Input")
        main()

    return widthWanted, heightWanted

def askOutput():
    try:
        outputWanted = int(input("\nWould you like to output as a .jpeg (1) or as a .txt(2) or no output (3)?\n"))

        if outputWanted == 1 or outputWanted == 2 or outputWanted == 3:
            return outputWanted
        else:
            print("\nInvalid input")
            main()
    
    except ValueError:
        print("\nInvalid input")
        main()
        

def createOutput(output):
    global screen
    global width, height

    if(len(mazeGrid.maze_grid[0])*width * 2 < 1920 and len(mazeGrid.maze_grid)*height * 2 < 1080):
        if output == 1:
            pygame.draw.rect(screen, constants.WHITE, [0, height/2, width, height])
            pygame.draw.rect(screen, constants.WHITE, [len(mazeGrid.maze_grid[0])*width * 2 - width/2, len(mazeGrid.maze_grid)*height * 2 - 3*height/2, width, height])
            pygame.image.save(screen, "maze_file.jpeg")
        elif output == 2:
            return
            #TODO

    else:
        newWidth = width*4
        newHeight = height*4
        
        if output == 1:
            pygame.draw.rect(screen, constants.WHITE, [0, (2000/newHeight)/2, (2000/newWidth), (2000/newHeight)])
            pygame.draw.rect(screen, constants.WHITE, [len(mazeGrid.maze_grid[0])*(2000/newWidth) * 2 - (2000/newWidth)/2, len(mazeGrid.maze_grid)*(2000/newHeight) * 2 - 3*(2000/newHeight)/2, (2000/newWidth), (2000/newHeight)])
            pygame.image.save(screen, "maze_file.jpeg")
        elif output == 2:
            return
            #TODO

def drawMaze():
    global screen
    global mazeGrid
    global width, height

    i = 0
    j = 0
    if(len(mazeGrid.maze_grid[0])*width * 2 < 1920 and len(mazeGrid.maze_grid)*height * 2 < 1080):
        for i, line in enumerate(mazeGrid.maze_grid):
                for j, char in enumerate(mazeGrid.maze_grid[i]):
                    pygame.draw.rect(screen, constants.WHITE, [2*j*width + width/2, 2*i*height + height/2, width, height])

                    if(mazeGrid.maze_grid[i][j].dirExit == "N"):
                        pygame.draw.rect(screen, constants.WHITE, [2*j*width + width/2, 2*i*height - height/2, width, height])
                    if(mazeGrid.maze_grid[i][j].dirExit == "S"):
                        pygame.draw.rect(screen, constants.WHITE, [2*j*width + width/2, 2*i*height + height/2 + height, width, height])
                    if(mazeGrid.maze_grid[i][j].dirExit == "E"):
                        pygame.draw.rect(screen, constants.WHITE, [2*j*width + width/2 + width, 2*i*height + height/2, width, height])
                    if(mazeGrid.maze_grid[i][j].dirExit == "W"):
                        pygame.draw.rect(screen, constants.WHITE, [2*j*width - width/2, 2*i*height + height/2, width, height])
    else:
        newWidth = width*4
        newHeight = height*4
        
        for i, line in enumerate(mazeGrid.maze_grid):
                for j, char in enumerate(mazeGrid.maze_grid[i]):
                    
                    pygame.draw.rect(screen, constants.WHITE, [2*j*(2000/newWidth) + (2000/newWidth)/2, 2*i*(2000/newHeight) + (2000/newHeight)/2, 2000/newWidth, 2000/newHeight])
                
                    if(mazeGrid.maze_grid[i][j].dirExit == "N"):
                        pygame.draw.rect(screen, constants.WHITE, [2*j*(2000/newWidth) + (2000/newWidth)/2, 2*i*(2000/newHeight) - (2000/newHeight)/2, (2000/newWidth), (2000/newHeight)])
                    if(mazeGrid.maze_grid[i][j].dirExit == "S"):
                        pygame.draw.rect(screen, constants.WHITE, [2*j*(2000/newWidth) + (2000/newWidth)/2, 2*i*(2000/newHeight) + (2000/newHeight)/2 + (2000/newHeight), (2000/newWidth), (2000/newHeight)])
                    if(mazeGrid.maze_grid[i][j].dirExit == "E"):
                        pygame.draw.rect(screen, constants.WHITE, [2*j*(2000/newWidth) + (2000/newWidth)/2 + (2000/newWidth), 2*i*(2000/newHeight) + (2000/newHeight)/2, (2000/newWidth), (2000/newHeight)])
                    if(mazeGrid.maze_grid[i][j].dirExit == "W"):
                        pygame.draw.rect(screen, constants.WHITE, [2*j*(2000/newWidth) - (2000/newWidth)/2, 2*i*(2000/newHeight) + (2000/newHeight)/2, (2000/newWidth), (2000/newHeight)])




pygame.init()

done = False

clock = pygame.time.Clock()

def main():
    global mazeGrid
    global done
    global screen
    global width, height
    
    mazeGrid = MazeGrid()

    width, height = askDimensions()   

    mazeGrid.gridMaze(width, height)

    mazeTracer = MazeTracer()

    mazeTracer.chooseStartCell(mazeGrid)

    output = askOutput()
    
    while not mazeGrid.checkComplete():
        mazeTracer.update(mazeGrid)


    if(len(mazeGrid.maze_grid[0])*width * 2 < 1920 and len(mazeGrid.maze_grid)*height * 2 < 1080):
       
        screen = pygame.display.set_mode([len(mazeGrid.maze_grid[0])*width * 2, len(mazeGrid.maze_grid)*height * 2], pygame.FULLSCREEN)

    else:
        screen = pygame.display.set_mode([1000, 1000], pygame.FULLSCREEN)


    while not done:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

        screen.fill(constants.BLACK)
        
        drawMaze()

        pygame.display.flip()


    createOutput(output)
    
    
    pygame.quit()


if __name__ == "__main__":
    main()




