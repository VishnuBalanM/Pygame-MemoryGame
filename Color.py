
#My First Game


import random, sys, time, pygame, math
from pygame.locals import *



over=0
Number_of_flash = 30
Width = 940
Height = 600
flash_speed = 200 # in milliseconds
flash_delay = 200 # in milliseconds
button_size = 200
button_gapsize = 20
Timeout = 4 # 4 seconds before game over if no button is pushed.


WHITE         = (255, 255, 255)
BLACK         = (  0,   0,   0)
BRIGHTRED     = (255,   0,   0)
RED           = (155,   0,   0)
BRIGHTGREEN   = (  0, 255,   0)
GREEN         = (  0, 155,   0)
BRIGHTBLUE    = (  0,   0, 255)
BLUE          = (  0,   0, 155)
BRIGHTYELLOW  = (255, 255,   0)
YELLOW        = (155, 155,   0)
DARKGRAY      = ( 40,  40,  40)
BRIGHTMAJANTA = (255, 0  , 255)
MAJANTA       = (155, 0  , 155)
BRIGHTCYAN    = (0  , 255, 255)
CYAN          = (0  , 155, 155)

bgColor = BLACK
b = (250,200,100)
pygame.init()

def font1():
        font=pygame.font.Font(None,70)
        text=font.render("TRY",True,CYAN)
        text_rect=text.get_rect()
        text_rect.centery=130
        text_rect.centerx=475
        screen.blit(text,text_rect)
        font=pygame.font.Font(None,70)
        text=font.render("YOUR",True,CYAN)
        text_rect=text.get_rect()
        text_rect.centery=190
        text_rect.centerx=475
        screen.blit(text,text_rect)
        font=pygame.font.Font(None,70)
        text=font.render("MEMORY",True,CYAN)
        text_rect=text.get_rect()
        text_rect.centery=250
        text_rect.centerx=475
        screen.blit(text,text_rect)
        font=pygame.font.Font(None,70)
        text=font.render("Vishnu",True,BRIGHTRED)
        text_rect=text.get_rect()
        text_rect.centery=550
        text_rect.centerx=470
        screen.blit(text,text_rect)

screen = pygame.display.set_mode((Width, Height))
screen.fill((255,255,255))

clock = pygame.time.Clock()
pygame.display.update()



def event() :
        while True :
                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                                sys.exit()
                                pygame.quit()
                        if event.type == pygame.MOUSEBUTTONUP:
                                posx, posy = event.pos
                                if play_rect.collidepoint( (posx, posy) ):
                                        return True
                for event in pygame.event.get(KEYUP):
                        if event.key == K_ESCAPE:
                                sys.exit()
                                pygame.quit()


Xaxis = int((Width - 100 - (2 * button_size) - button_gapsize) / 2)
Yaxis = int((Height - (2 * button_size) - button_gapsize) / 2)

screen = pygame.display.set_mode((Width, Height))


screen.fill((255,255,255))
#pygame.draw.circle(screen,b,(470,230),200)
font1()
font=pygame.font.Font(None,50)
text = font.render("PLAY", True, BLACK)
rect = text.get_rect()
rect.centerx=470
rect.centery=360
play_rect = pygame.draw.rect(screen,BRIGHTGREEN,[412,330,120,60])
screen.blit(text, rect)

pygame.display.update()

while True :
        if event() :
                break


# Rect objects for each of the six buttons
YELLOW_RECT = pygame.Rect(Xaxis , Yaxis , button_size, button_size)
BLUE_RECT   = pygame.Rect(Xaxis +button_size + button_gapsize, Yaxis, button_size, button_size)
RED_RECT    = pygame.Rect(Xaxis , Yaxis + button_size + button_gapsize, button_size, button_size)
GREEN_RECT  = pygame.Rect(Xaxis  + button_size + button_gapsize, Yaxis + button_size + button_gapsize, button_size, button_size)
MAJANTA_RECT= pygame.Rect(Xaxis  + button_size + button_size + button_gapsize + button_gapsize, Yaxis , button_size,button_size)
CYAN_RECT   = pygame.Rect(Xaxis +button_size + button_size + button_gapsize + button_gapsize, Yaxis + button_size + button_gapsize, button_size, button_size)



#main function
def main():
    global clock, screen,score, font, sound1, sound2, sound3, sound4, sound5, sound6

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption('Simulate The Pattern')

    font = pygame.font.Font('freesansbold.ttf', 16)
    info_Surf = font.render('Match the pattern by clicking on the button or using the Q, W, E, A, S, D keys.', 1, DARKGRAY)
    info_Rect = info_Surf.get_rect()
    info_Rect.topleft = (10, Height - 25)

    # load the sound files
    sound1 = pygame.mixer.Sound('beep1.ogg')
    sound2 = pygame.mixer.Sound('beep2.ogg')
    sound3 = pygame.mixer.Sound('beep3.ogg')
    sound4 = pygame.mixer.Sound('beep4.ogg')
    sound5 = pygame.mixer.Sound('beep5.ogg')
    sound6 = pygame.mixer.Sound('beep6.ogg')

    
    pattern = [] # stores the pattern of colors
    currentStep = 0 # the color the player must push next
    lastClickTime = 0 # timestamp of the player's last button push
    waitingForInput = False

    while True: # main game loop
        clickedButton = None # button that was clicked (set to YELLOW, RED, GREEN, BLUE, MAJANTA, or CYAN)
        screen.fill(bgColor)
        drawButtons()

        score_Surf = font.render('Score: ' + str(score), 1, WHITE)
        score_Rect = score_Surf.get_rect()
        score_Rect.topleft = (Width - 100, 10)
        screen.blit(score_Surf, score_Rect)

        screen.blit(info_Surf, info_Rect)

        checkForQuit()
        for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                clickedButton = getButtonClicked(mousex, mousey)
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    clickedButton = YELLOW
                elif event.key == K_w:
                    clickedButton = BLUE
                elif event.key == K_a:
                    clickedButton = RED
                elif event.key == K_s:
                    clickedButton = GREEN
                elif event.key == K_e:
                    clickedButton = MAJANTA
		elif event.key == K_d:
		    clickedButoon = CYAN


        if not waitingForInput:
            # play the pattern
            pygame.display.update()
            pygame.time.wait(1000)
            pattern.append(random.choice((YELLOW, BLUE, MAJANTA, RED, GREEN, CYAN)))
            for button in pattern:
                flashButtonAnimation(button)
                pygame.time.wait(flash_delay)
            waitingForInput = True
        else:
            # wait for the player to enter buttons
            if clickedButton and clickedButton == pattern[currentStep]:
                # pressed the correct button
                flashButtonAnimation(clickedButton)
                currentStep += 1
                lastClickTime = time.time()

                if currentStep == len(pattern):
                    # pressed the last button in the pattern
                    changeBackgroundAnimation()
                    score += 1
                    waitingForInput = False
                    currentStep = 0 # reset back to first step

            elif (clickedButton and clickedButton != pattern[currentStep]) or (currentStep != 0 and time.time() - Timeout > lastClickTime):
                # pressed the incorrect button, or has timed out
                gameOverAnimation()
		gameover()
                # reset the variables for a new game:
                pattern = []
                currentStep = 0
                waitingForInput = False
                score = 0
                pygame.time.wait(1000)
                changeBackgroundAnimation()

        pygame.display.update()
        clock.tick(Number_of_flash)

#exiting function
def terminate():
    pygame.quit()
    sys.exit()


#checking for exit
def checkForQuit():
    for event in pygame.event.get(QUIT): 
        terminate() 
    for event in pygame.event.get(KEYUP): 
        if event.key == K_ESCAPE:
            terminate() 
        pygame.event.post(event) 



#making the animation
def flashButtonAnimation(color, animationSpeed=50):
    if color == YELLOW:
        sound = sound1
        flashColor = BRIGHTYELLOW
        rectangle = YELLOW_RECT
    elif color == BLUE:
        sound = sound2
        flashColor = BRIGHTBLUE
        rectangle = BLUE_RECT
    elif color == RED:
        sound = sound3
        flashColor = BRIGHTRED
        rectangle = RED_RECT
    elif color == GREEN:
        sound = sound4
        flashColor = BRIGHTGREEN
        rectangle = GREEN_RECT
    elif color == MAJANTA:
        sound = sound5
        flashColor = BRIGHTMAJANTA
        rectangle = MAJANTA_RECT
    elif color == CYAN:
        sound = sound6
        flashColor = BRIGHTCYAN
        rectangle = CYAN_RECT


    orig_Surf = screen.copy()
    flash_Surf = pygame.Surface((button_size, button_size))
    flash_Surf = flash_Surf.convert_alpha()
    r, g, b = flashColor
    sound.play()
    for start, end, step in ((0, 255, 1), (255, 0, -1)): # animation loop
        for alpha in range(start, end, animationSpeed * step):
            checkForQuit()
            screen.blit(orig_Surf, (0, 0))
            flash_Surf.fill((r, g, b, alpha))
            screen.blit(flash_Surf, rectangle.topleft)
            pygame.display.update()
            clock.tick(Number_of_flash)
    screen.blit(orig_Surf, (0, 0))



#drawing the required button
def drawButtons():
    pygame.draw.rect(screen, YELLOW, YELLOW_RECT)
    pygame.draw.rect(screen, BLUE,   BLUE_RECT)
    pygame.draw.rect(screen, RED,    RED_RECT)
    pygame.draw.rect(screen, GREEN,  GREEN_RECT)
    pygame.draw.rect(screen, MAJANTA,MAJANTA_RECT)
    pygame.draw.rect(screen, CYAN,   CYAN_RECT)



#for changing background for each button click
def changeBackgroundAnimation(animationSpeed=40):
    global bgColor
    newBgColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    newBgSurf = pygame.Surface((Width, Height))
    newBgSurf = newBgSurf.convert_alpha()
    r, g, b = newBgColor
    for alpha in range(0, 255, animationSpeed): # animation loop
        checkForQuit()
        screen.fill(bgColor)

        newBgSurf.fill((r, g, b, alpha))
        screen.blit(newBgSurf, (0, 0))

        drawButtons() # redraw the buttons on top of the tint

        pygame.display.update()
        clock.tick(Number_of_flash)
    bgColor = newBgColor


#animation when game is over
def gameOverAnimation(color=WHITE, animationSpeed=50):
    # play all beeps at once, then flash the background
    orig_Surf = screen.copy()
    flash_Surf = pygame.Surface(screen.get_size())
    flash_Surf = flash_Surf.convert_alpha()
    sound1.play() # play all four beeps at the same time, roughly.
    sound2.play()
    sound3.play()
    sound4.play()
    sound5.play()
    sound6.play()
    r, g, b = color
    for i in range(3): 
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
                for alpha in range(start, end, animationSpeed * step): 
                	checkForQuit()
                	flash_Surf.fill((r, g, b, alpha))
                	screen.blit(orig_Surf, (0, 0))
                	screen.blit(flash_Surf, (0, 0))
                	drawButtons()
                	pygame.display.update()
                	clock.tick(Number_of_flash)


#checking clicked button
def getButtonClicked(x, y):
    if YELLOW_RECT.collidepoint( (x, y) ):
        return YELLOW
    elif BLUE_RECT.collidepoint( (x, y) ):
        return BLUE
    elif RED_RECT.collidepoint( (x, y) ):
        return RED
    elif GREEN_RECT.collidepoint( (x, y) ):
        return GREEN
    elif MAJANTA_RECT.collidepoint( (x, y) ):
        return MAJANTA
    elif CYAN_RECT.collidepoint( (x, y) ):
        return CYAN
    return None



#game over display
def gameover():
        global score,over
        mouse=False
        screen.fill((255,255,255))
        font=pygame.font.Font(None,80)
        scoreText = font.render("GAME OVER", True, RED)
        scoreRect = scoreText.get_rect()
        scoreRect.centerx=510
        scoreRect.centery=150
        screen.blit(scoreText,scoreRect)
        font=pygame.font.Font(None,50)
        scoreText = font.render("Your Score Is ", True, BRIGHTYELLOW)
        scoreRect = scoreText.get_rect()
        scoreRect.centerx=500
        scoreRect.centery=280
        screen.blit(scoreText,scoreRect)
        font=pygame.font.Font(None,70)
        scoreText = font.render(str(score), True, BRIGHTYELLOW)
        scoreRect = scoreText.get_rect()
        scoreRect.centerx=500
        scoreRect.centery=380
        screen.blit(scoreText,scoreRect)
        font=pygame.font.Font(None,40)
        scoreText = font.render("Retry", True, BLACK)
        scoreRect1 = scoreText.get_rect()
        scoreRect1.centerx=360
        scoreRect1.centery=500
        screen.blit(scoreText,scoreRect1)
        font=pygame.font.Font(None,40)
        scoreText = font.render("Quit", True, BLACK)
	scoreRect2 = scoreText.get_rect()
        scoreRect2.centerx=660
        scoreRect2.centery=500
        screen.blit(scoreText,scoreRect2)
        pygame.display.update()
        while mouse==False:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                                mouse=True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                mx,my = pygame.mouse.get_pos()
                                if mx>=scoreRect1[0]-10 and mx <= (scoreRect1[2]+scoreRect1[0]+10) and my >=scoreRect1[1]-10 and my < (scoreRect1[1]+scoreRect1[3]+10):
                                        over=0
                                else:
                                        terminate()
                                mouse=True


if over == 0:
        score=0
        screen.fill((0,0,0))
	main()


#calling main loop
if __name__ == '__main__':
    main()


