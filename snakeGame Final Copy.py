## John McGaughey
## Rebecca Rogers
## CSC 170

import random 
import pygame                              #install pygame by typing pip install pygame into the console

pygame.init()   #initialize the pygame window

#set up the display window
display_width = 600
display_height = 400
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")

imgX = 200
imgY = 200

#set up game clock to control frames-per-second fps
clock = pygame.time.Clock()

#set colors needed thru the game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0 , 0)
bright_green = (0, 255, 0)

def initializeGame():
    #pygame.init()
    
    ##gameIcon = pygame.image.load("carIcon.png")
    ##pygame.display.set_icon(gameIcon)
    pygame.display.set_caption("Snake Game")
    
    global gameDisplay
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    
    #gameDisplay.fill(white)
    #pygame.display.update()
    
    pygame.time.delay(3000)
    return gameDisplay

#text object function called by message display function
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# buttons to start game and go to end credit screen
def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
   
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

# End credit screen
def quitgame():
    end = True
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 50)
        mediumText = pygame.font.SysFont("comicsansms", 30)
        smallText = pygame.font.SysFont("comicsansms", 7)
        TextSurf, TextRect = text_objects("Thanks for playing!", largeText)
        TextSurf1, TextRect1 = text_objects("John McGaughey and Rebecca Rogers", mediumText)
        TextSurf2, TextRect2 = text_objects("Apple sound effect:  https://freesound.org/people/Koops/sounds/20279/", smallText)
        TextSurf3, TextRect3 = text_objects("Apple picture:  https://www.istockphoto.com/photos/apple?sort=mostpopular&mediatype=photography&phrase=apple", smallText)
        TextSurf4, TextRect4 = text_objects("Background Music:  https://www.bensound.com/royalty-free-music/track/little-idea", smallText)
        TextRect.center = ((display_width/2), 75)
        gameDisplay.blit(TextSurf, TextRect)
        TextRect1.center = ((display_width/2), 150)
        gameDisplay.blit(TextSurf1, TextRect1)
        TextRect2.center = ((display_width/2), 225)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextRect3.center = ((display_width/2), 275)
        gameDisplay.blit(TextSurf3, TextRect3)
        TextRect4.center = ((display_width/2), 325)
        gameDisplay.blit(TextSurf4, TextRect4)
        pygame.display.update()
        clock.tick(15)        

# main menu screen
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 80)
        TextSurf, TextRect = text_objects("Snake Game", largeText)
        TextRect.center = ((display_width/2), 100)
        gameDisplay.blit(TextSurf, TextRect)
        mediumText = pygame.font.SysFont("comicsansms", 30)
        TextSurf1, TextRect1 = text_objects("John McGaughey and Rebecca Rogers", mediumText)
        TextRect1.center = ((display_width/2), 200)
        gameDisplay.blit(TextSurf1, TextRect1)        
        button("GO!", 100, 300, 100, 50, green, bright_green, moveImage)
        button("Quit", 350, 300, 100, 50, red, bright_red, quitgame)
       
        pygame.display.update()
        clock.tick(15)

# load snake img
def loadSnake(gameDisplay):
    
    gameDisplay.fill(white)
    #pygame.display.update()
    #pygame.time.delay(3000)
    snakeImg = pygame.image.load("snakeHead.png")
    snakeImg = pygame.transform.scale(snakeImg, (25,25))
    
    return snakeImg

# load apple img
def loadApple():
    appleImg = pygame.image.load("apple.jpg")
    appleImg = pygame.transform.scale(appleImg, (25,25))
    return appleImg

# get random apple
def randomApple():
    # apple is randomly assigned and then multiplied by 25 to stay in column and rowwith snake 
    # apple does not spawn on edge of screen
    appleX = random.randrange(1, 23)
    appleY = random.randrange(1, 15)
    appleX = appleX * 25
    appleY = appleY * 25
    return appleX, appleY
    
def moveImage():
    # Load and play background music
    pygame.mixer.music.load("bensound-littleidea.MP3")
    pygame.mixer.music.play(-1)
    
    # initialize screen and snake
    screen = initializeGame()
    snakeImg = loadSnake(screen)
    
    # size of array
    score = 4
    
    # head of snake
    x = imgX
    y = imgY
    
    # define beginning snake array
    snakeArray = []
    snakeArray.append([x, y])
    snakeArray.append([x, y + 25])
    snakeArray.append([x, y + 50])
    snakeArray.append([x, y + 75])
    
    # used to determine direction of snake
    xChange = 0
    yChange = -25
    
    # game no exit
    gameExit = False
    
    ## random apple
    appleArray = []
    appleImg = loadApple()
    appleLoop = False
    # make sure apple does not spawn inside of snake
    while appleLoop == False:
        appleArray = randomApple()
        if snakeArray.count(appleArray) < 1:
            appleLoop = True
    
    # while game no exit
    while not gameExit:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xChange = -25
                    yChange = 0
                elif event.key == pygame.K_RIGHT:
                    xChange = 25
                    yChange = 0
                elif event.key == pygame.K_UP:
                    yChange = -25
                    xChange = 0
                elif event.key == pygame.K_DOWN:
                    yChange = 25
                    xChange = 0
                    
        # update x and y coordinates with the direction of snake
        x = x + xChange
        y = y + yChange
        
        previous = snakeArray[-1]
        
        # update snake but not the head
        for i in range(len(snakeArray) - 1, 0, -1):
            snakeArray[i] = snakeArray[i-1]
        # update snake head
        snakeArray[0] = [x, y]
        
        # check to see if snake ate the apple
        if x == appleArray[0] and y == appleArray[1]:
            # increase the score
            score += 1
            # get new apple placement
            appleLoop = False
            while appleLoop == False:
                appleArray = randomApple()
                if snakeArray.count(appleArray) <= 1:
                    appleLoop = True
            
            # grow the snake
            snakeArray.append(previous)
            # Monch sound effect
            gotApple = pygame.mixer.Sound("apple sound effect.wav")
            pygame.mixer.Sound.play(gotApple)
        
        # update the display
        gameDisplay.fill(white)
        for i in range(score):
            gameDisplay.blit(snakeImg, (snakeArray[i]))
        gameDisplay.blit(appleImg, (appleArray[0], appleArray[1]))
        
        
        #check for crash with sides of window
        if x >= display_width - 25 or x <= 0:
            gameExit = True
        if y >= display_height -25 or y <= 0:
            gameExit = True
        # check for crash with another piece of the snake
        if snakeArray.count([x, y]) > 1:
            gameExit = True
        
        
        # update the screen
        pygame.display.update() 
        # happens 4 times a second
        clock.tick(4)
    
def main():
    game_intro()
    pygame.quit()

main()

