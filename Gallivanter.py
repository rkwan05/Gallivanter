'''
Created on Mar. 4, 2020

@author: rkwan
'''
import pygame
import os 
from Enemies import *
from Character import *

pygame.init()

timer = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Gallivanter')
right = False
left = False
steps = 0

#Animated pictures
moveRight = [pygame.image.load('C:/Users/rkwan/Desktop/R1.png'), pygame.image.load('C:/Users/rkwan/Desktop/R2.PNG'), pygame.image.load('C:/Users/rkwan/Desktop/R3.PNG'), pygame.image.load('C:/Users/rkwan/Desktop/R4.PNG'), pygame.image.load('C:/Users/rkwan/Desktop/R5.PNG'), pygame.image.load('C:/Users/rkwan/Desktop/R6.PNG'), pygame.image.load('C:/Users/rkwan/Desktop/R7.PNG'), pygame.image.load('C:/Users/rkwan/Desktop/R8.PNG'), pygame.image.load('C:/Users/rkwan/Desktop/R9.PNG')]
standing = pygame.image.load('C:/Users/rkwan/Desktop/R10.PNG')

transparent = (0,0,0,0)
enemy_health = 100
user_health = 100


#hit sound effect
hit_sound = pygame.mixer.Sound('C:/Users/rkwan/Downloads/Hit.wav')

#dying sound effect
dying_sound = pygame.mixer.Sound('C:/Users/rkwan/Downloads/die.wav')
dying_sound.set_volume(1.0)
      
#music
music = pygame.mixer.music.load('C:/Users/rkwan/Downloads/Ducktales.mp3') 

#play the music on loop
pygame.mixer.music.play(-1)    

#making the music quieter.
pygame.mixer.music.set_volume(0.5) 


def save_highscore(new_score):
    score_file = open('Highscore.txt', 'w')
    score_file.write(str(new_score))
    score_file.close()
    
def get_highscore(highscore):
    score_file = open('Highscore.txt', 'r')
    highscore = int(score_file.read())
    return highscore
    score_file.close()

def run():
    global steps
    global screen
    global enemy_health
    global user_health
    bool = True
    
    #obstacle
    obstacle = False

    x = 350
    y = 400
    f = 0
    
    global i 

    #round number
    i = 1
    
    #starting highscore
    highscore = 0
    
    highscore = get_highscore(highscore)
    
    current_score = i
    
    if current_score > highscore:
        save_highscore(current_score)

        
    round = False

    while bool:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bool = False
                
        #starting highscore
        highscore = 0
        
        highscore = get_highscore(highscore)
        
        current_score = i
        
        if current_score > highscore:
            save_highscore(current_score)
        
        pygame.time.delay(60)
        timer.tick(27)
                
        background = pygame.image.load('C:/Users/rkwan/Desktop/picture.PNG').convert()
        
        #display the background onto the screen
        screen.blit(background, (f,0))
        
#         #settings    
#         settings_icon = pygame.image.load('C:/Users/rkwan/Desktop/Settings.png')
#         settings_sized = pygame.transform.scale(settings_icon, (50,50))
#         
#         #display settings onto the screen
#         screen.blit(settings_sized, (740, 15))
#         
        #get the position of the mouse
        mouse_pos = pygame.mouse.get_pos()
        
#         
#         #if the mouse clicks on the settings icon
#         if 740 < mouse_pos[0] < 790 and 15 < mouse_pos[1] < 65:
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 settings()
        
        if round == False:
            x,y,f,round, left, right = movement(x, y, f,round, False, False)
            
            if i == 1:                
                #font for the button attack text
                round1_font = pygame.font.Font('freesansbold.ttf', 50)
                round1_text = round1_font.render('Round 1', True, (255,255,255))
                round1_rect = round1_text.get_rect()
                round1_rect.center = (175,100)
                
                #high score text
                score_font = pygame.font.Font('freesansbold.ttf', 16)
                score_text = score_font.render('Highscore: ' + str(highscore), True, (255,255,255))
                score_rect = score_text.get_rect()
                score_rect.center = (680,40)
                
                screen.blit(score_text, score_rect)
                screen.blit(round1_text, round1_rect)
            
            if i == 2:                
                #font for the button attack text
                round_font = pygame.font.Font('freesansbold.ttf', 50)
                round_text = round_font.render('Round 2', True, (255,255,255))
                round_rect = round_text.get_rect()
                round_rect.center = (175,100)
                
                score_font = pygame.font.Font('freesansbold.ttf', 16)
                score_text = score_font.render('Highscore: ' + str(highscore), True, (255,255,255))
                score_rect = score_text.get_rect()
                score_rect.center = (680,40)
                
                screen.blit(score_text, score_rect)
                screen.blit(round_text, round_rect)
                
            if i == 3:                
                #font for the button attack text
                round_font = pygame.font.Font('freesansbold.ttf', 50)
                round_text = round_font.render('Round 3', True, (255,255,255))
                round_rect = round_text.get_rect()
                round_rect.center = (175,100)
                
                score_font = pygame.font.Font('freesansbold.ttf', 16)
                score_text = score_font.render('Highscore: ' + str(highscore), True, (255,255,255))
                score_rect = score_text.get_rect()
                score_rect.center = (680,40)
                
                screen.blit(score_text, score_rect)
                screen.blit(round_text, round_rect)
                
            if i == 4:                
                #font for the button attack text
                round1_font = pygame.font.Font('freesansbold.ttf', 50)
                round1_text = round1_font.render('Round 4', True, (255,255,255))
                round1_rect = round1_text.get_rect()
                round1_rect.center = (175,100)
                
                score_font = pygame.font.Font('freesansbold.ttf', 16)
                score_text = score_font.render('Highscore: ' + str(highscore), True, (255,255,255))
                score_rect = score_text.get_rect()
                score_rect.center = (680,40)
                
                screen.blit(score_text, score_rect)
                screen.blit(round1_text, round1_rect)
            
            #obstacle code
            t = 700
            if x >=350:
                while obstacle:
                    y = 400
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False 
                            
#                     #settings    
#                     settings_icon = pygame.image.load('C:/Users/rkwan/Desktop/Settings.png')
#                     settings_sized = pygame.transform.scale(settings_icon, (50,50))
#                     
#                     #if the mouse clicks on the settings icon
#                     if 740 < mouse_pos[0] < 790 and 15 < mouse_pos[1] < 65:
#                         if event.type == pygame.MOUSEBUTTONDOWN:
#                             settings()
                            
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
                        y = y - 200
                    
                    #tumbleweed picture
                    tumbleweed = pygame.image.load('C:/Users/rkwan/Desktop/tumbleweed.PNG').convert()
                    t=t-1
                    
                    #displaying the elements on the screen
                    obstacle_box = pygame.draw.rect(screen, (0,0,0),(t+100, 470, 70,70),1)
                    character_box = pygame.draw.rect(screen, (0,0,0),(x+10, y, 90,130),1)
                    screen.blit(background, (f,0))
                    screen.blit(pygame.transform.scale(tumbleweed, (70,70)),(t, 460))
                    screen.blit(pygame.transform.scale(standing, (125,125)), (x,y))
                    #display settings onto the screen
#                     screen.blit(settings_sized, (740, 15))
                
                    #boundary collision
                    if obstacle_box.y - 70 < character_box.y + 130 and obstacle_box.y + 70> character_box.y:
                        if obstacle_box.x > character_box.x and obstacle_box.x  < character_box.x + 90:
                            obstacle = False
                            dying_sound.play()

                            #if the obstacle touches the character, they will go back one round
                            if i <= 1:
                                i = 1
                            else:
                                i -= 1
                                
                    #while loop will be stopped if the obstacle moves off the screen            
                    if obstacle_box.x + 70 < 0:
                        obstacle = False
                        screen.fill(0,0,0)
    
                    pygame.display.update()
                    pygame.display.flip()
          
        else:
            #round 1
            if i == 1:
                round = round_1(x,y, round)

            #round 2   
            if i == 2:
                round = round_2(x,y, round)
                #obstacle will appear after this round is finished
                obstacle = True
            
            #round 3
            if i == 3:
                round = round_3(x,y, round)
            
            #round 4
            if i == 4:
                round = round_4(x,y, round)
                
            if round == False:
                f = 0
                
                #i increases after each round ends
                i +=1
                
                            
        #if steps is more than 27, then the array will reset
        if steps >= 27:
            steps = 0
                    
        #drawing the character 
        character_sized = pygame.transform.scale(moveRight[steps//3], (125,125))
        standing_sized = pygame.transform.scale(standing, (125,125))
        
        if right:
            screen.blit(character_sized, (x,y))
            #counting the steps to tell the code when the array will reset (so that it doesn't run out of photos) 
            steps += 1
            
        elif left:
            #flip the image to make it seem like the user is moving left
            screen.blit(pygame.transform.flip(character_sized, True, False), (x,y))
            steps += 1
        
        #if the character is not moving then its standing picture will be shown on the screen     
        else:
            screen.blit(standing_sized, (x,y))
            
              
        pygame.display.update()
        
        
def movement(x,y,f, round, left, right):
    y = 400
    
    #setting the background image
    if f <= -606:
        f = 0

    #controls of the character and the background
    keys = pygame.key.get_pressed()
    
    #moving to the left
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        left = True
        right = False
        
        if f >= 0:
            x -= 10
            
            if x <=0:
                x = 0
            
        else:
            f += 10
    
    #moving to the right                
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d] :
        right = True
        left = False
        
        if x < 350:
            x += 10
            
        else:
            f -= 10
    
    #jumping control   
    elif keys[pygame.K_w]or keys[pygame.K_UP] or keys[pygame.K_SPACE]:
        y = y - 150
            
    else:
        left = False
        right = False
        steps = 0
            
    #if the enemy appears
    if(f <=-250):
        round = True
        right = False
        left = False
        #transition slide
        screen.fill((0,0,0))
        #center the characters
        x = 220
    
    return x, y, f, round, left, right
    
    
#settings screen
def settings():
    x = 175
    y = 175
    
    settings_bool = True
    
    #screen initialization
    settings_screen = pygame.display.set_mode((800,600))
    settings_screen.fill((255,255,255))
    
    #background image
    background = pygame.image.load('C:/Users/rkwan/Desktop/picture.PNG').convert()
    settings_screen.blit(background, (0,0))

        
    while settings_bool:
        
        #get the position of the mouse
        mouse_pos = pygame.mouse.get_pos()
        
        #creating a box to hold all the setting elements.    
        pygame.draw.rect(settings_screen, (192,192,192), (150,100,500,400))
        
        #Sounds slider
        rectangle_1 = pygame.draw.rect(settings_screen, (0,0,0), (175,150, 450,8))
        pygame.draw.circle(settings_screen, (0,0,0),(y, 150), 10)
        
        #Slider #2 (music)
        rectangle_2 = pygame.draw.rect(settings_screen, (0,0,0), (175,230, 450,8))
        pygame.draw.circle(settings_screen, (0,0,0),(x, 230), 10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings_bool = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rectangle_1.collidepoint(event.pos):
                    mouse_pos = event.pos
                    y = mouse_pos[0]
                    #adjust the volume of the sounds
                    hit_sound.set_volume(y/500) 
                
                if rectangle_2.collidepoint(event.pos):
                    mouse_pos = event.pos
                    x = mouse_pos[0]
                    #adjust the volume of the music
                    pygame.mixer.music.set_volume(x/500)
                    
        #exit button
        if 175 < mouse_pos[0] < 625 and 425 < mouse_pos[1] < 475:
            pygame.draw.rect(settings_screen, (216,191,216), (175,425,450, 50))
            if event.type == pygame.MOUSEBUTTONDOWN:            
                settings_bool = False 
                
        else:
            pygame.draw.rect(settings_screen, (153,50,204), (175,425,450,50))

        #font for the button attack text
        exit_font = pygame.font.Font('freesansbold.ttf', 22)
        exit_text = exit_font.render('Exit', True, (255,255,255))
        exit_rect = exit_text.get_rect()
        exit_rect.center = (400, 450)
        
        #Main menu button
        if 175 < mouse_pos[0] < 625 and 355 < mouse_pos[1] < 405:
            pygame.draw.rect(settings_screen, (216,191,216), (175,355,450, 50))
            if event.type == pygame.MOUSEBUTTONDOWN:   
                #change outcome          
                settings_bool = False 
                
        else:
            pygame.draw.rect(settings_screen, (153,50,204), (175,355,450,50))

        #font for the button attack text
        menu_font = pygame.font.Font('freesansbold.ttf', 22)
        menu_text = menu_font.render('Main Menu', True, (255,255,255))
        menu_rect = menu_text.get_rect()
        menu_rect.center = (400, 380)
        
        #Save Game Button
        if 175 < mouse_pos[0] < 625 and 280 < mouse_pos[1] < 330:
            pygame.draw.rect(settings_screen, (216,191,216), (175,280,450, 50))
            if event.type == pygame.MOUSEBUTTONDOWN:   
                #change outcome          
                settings_bool = False 
                
        else:
            pygame.draw.rect(settings_screen, (153,50,204), (175,280,450,50))

        #font for the button attack text
        save_font = pygame.font.Font('freesansbold.ttf', 22)
        save_text = save_font.render('Save Game', True, (255,255,255))
        save_rect = save_text.get_rect()
        save_rect.center = (400, 305)
        
        #displaying the buttons on the screen
        settings_screen.blit(exit_text, exit_rect)
        settings_screen.blit(menu_text, menu_rect)
        settings_screen.blit(save_text, save_rect)
    
        pygame.display.flip()
      

def round_1(x,y, round):
    global enemy_sized
            
    #enemy    
    enemy = pygame.image.load('C:/Users/rkwan/Desktop/enemy.png')
    enemy_sized = pygame.transform.scale(enemy, (125, 130))
    screen.blit(enemy_sized, (x + 220, y))
    
    incorrect = 0
    variable = 1
    
    global correct_variable
    global incorrect_variable
    
    correct_variable = 0
    incorrect_variable = 0
   
    global enemy_1
    global user 
    
    user_damage = 20
    enemy_damage = 50
    
    enemy_1 = Enemies(enemy_health, enemy_damage) 
    user = Character(user_health, user_damage)
    
    global user_dead
    global enemy_dead
    
    user_dead = False
    enemy_dead = False
    
    close = False
    
    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_SPACE]:
        
        run = True
        
        while run:
            
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
#             #settings    
#             settings_icon = pygame.image.load('C:/Users/rkwan/Desktop/Settings.png')
#             settings_sized = pygame.transform.scale(settings_icon, (50,50))
# 
#             #display settings onto the screen
#             screen.blit(settings_sized, (740, 15))
#                           
            close, user_dead, enemy_dead = questions_screen('What is 1 + 1?', '', 'The answer is: 2.', incorrect,'2', user_damage, enemy_damage, close, 'Use addition to add the two numbers together.', user_dead, enemy_dead, True, False, False, False)
            
            if close == True:
                variable = variable + 1
                run = False
                #screen that shows that the health of the characters go down
                close, user_dead, enemy_dead = questions_screen('What is 2 + 2?', '', 'The answer is: 4.', incorrect,'4', user_damage, enemy_damage, close,  'Use addition to add the two numbers together.', user_dead, enemy_dead, True, False, False, False)
                
                #add textbox here to congratulate the player 
                #
                #
                
                #end the round if the enemy dies
                if enemy_dead == True:
                    round = False
                    return round
                
            if close == True:
                variable = variable + 1
                run = False
                #screen that shows that the health of the characters go down
                close, user_dead, enemy_dead = questions_screen('What is 4 + 4?', '', 'The answer is: 8.', incorrect,'8', user_damage, enemy_damage, close,  'Use addition to add the two numbers together.', user_dead, enemy_dead, True, False, False, False)
            
                if enemy_dead == True:
                    round = False
                    return round
                
            if close == True:
                variable = variable + 1
                run = False
                #screen that shows that the health of the characters go down
                close, user_dead, enemy_dead = questions_screen('What is 8 + 8?', '', 'The answer is: 16.', incorrect,'16', user_damage, enemy_damage, close,  'Use addition to add the two numbers together.', user_dead, enemy_dead, True, False, False, False)
            
                if enemy_dead == True:
                    round = False
                    return round
                
            if close == True:
                variable = variable + 1
                run = False
                #screen that shows that the health of the characters go down
                close, user_dead, enemy_dead = questions_screen('What is 9 + 9?', '', 'The answer is: 18.', incorrect,'18', user_damage, enemy_damage, close,  'Use addition to add the two numbers together.', user_dead, enemy_dead, True, False, False, False)
            
                if enemy_dead == True:
                    round = False
                    return round
                
                if user_dead == True:
                    #add something here to restart the game or round if the user dies + a message
                    #
                    #
                    
                    round = False
                    return round
                

            pygame.display.flip()
            
def round_2(x,y, round):
    global enemy_sized
            
    #enemy    
    enemy = pygame.image.load('C:/Users/rkwan/Desktop/Enemy2.png')
    enemy_sized = pygame.transform.scale(enemy, (125, 130))
    screen.blit(enemy_sized, (x + 220, y))
    
    #text box
    #text_1 = pygame.draw.rect(screen, (255, 255, 255), (100, 100, 600,125))
    
    incorrect = 0
    variable = 1
    
    global correct_variable
    global incorrect_variable
    
    correct_variable = 0
    incorrect_variable = 0
   
    global enemy_1
    global user 
    
    user_damage = 30
    enemy_damage = 35
    
    enemy_1 = Enemies(enemy_health, enemy_damage) 
    user = Character(user_health, user_damage)
    
    global user_dead
    global enemy_dead
    
    user_dead = False
    enemy_dead = False
    
    close = False
    
    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_SPACE]:
        
        run = True
        
        while run:
            print(enemy_dead)
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
#             #settings    
#             settings_icon = pygame.image.load('C:/Users/rkwan/Desktop/Settings.png')
#             settings_sized = pygame.transform.scale(settings_icon, (50,50))
# 
#             #display settings onto the screen
#             screen.blit(settings_sized, (740, 15))
                          
            close, user_dead, enemy_dead = questions_screen('What is 1 x 1?', '', 'The answer is: 1.', incorrect,'1', user_damage, enemy_damage, close, 'Use addition to add the two numbers together.', user_dead, enemy_dead, False, True, False, False)
            
            if close == True:
                variable = variable + 1
                run = False
                #screen that shows that the health of the characters go down
                close, user_dead, enemy_dead = questions_screen('What is 2 x 2?', '', 'The answer is: 4.', incorrect,'4', user_damage, enemy_damage, close,  'Use addition to add the two numbers together.', user_dead, enemy_dead, False, True, False, False)
                
                #add textbox here to congratulate the player 
                #
                #
                
                #end the round if the enemy dies
                if enemy_dead == True:
                    round = False
                    return round
                
            if close == True:
                variable = variable + 1
                run = False
                #screen that shows that the health of the characters go down
                close, user_dead, enemy_dead = questions_screen('What is 4 x 4?', '', 'The answer is: 16.', incorrect,'16', user_damage, enemy_damage, close,  'Use addition to add the two numbers together.', user_dead, enemy_dead, False, True, False, False)
            
                if enemy_dead == True:
                    round = False
                    return round
                
            if close == True:
                variable = variable + 1
                run = False
                #screen that shows that the health of the characters go down
                close, user_dead, enemy_dead = questions_screen('What is 8 x 8?', '', 'The answer is: 64.', incorrect,'64', user_damage, enemy_damage, close,  'Use addition to add the two numbers together.', user_dead, enemy_dead, False, True, False, False)
            
                if enemy_dead == True:
                    round = False
                    return round
                
            if close == True:
                variable = variable + 1
                run = False
                #screen that shows that the health of the characters go down
                close, user_dead, enemy_dead = questions_screen('What is 9 + 9?', '', 'The answer is: 18.', incorrect,'18', user_damage, enemy_damage, close,  'Use addition to add the two numbers together.', user_dead, enemy_dead, False, True, False, False)
            
                if enemy_dead == True:
                    round = False
                    return round
                
                if user_dead == True:
                    #add something here to restart the game or round if the user dies + a message
                    #
                    #
                    
                    round = False
                    return round
                

            pygame.display.flip()
            
def round_3(x,y, round):
    global enemy_sized
            
    #enemy    
    enemy = pygame.image.load('C:/Users/rkwan/Desktop/enemy3.gif')
    enemy_sized = pygame.transform.scale(enemy, (125, 130))
    screen.blit(enemy_sized, (x + 220, y))
    
    #text box
    #text_1 = pygame.draw.rect(screen, (255, 255, 255), (100, 100, 600,125))
    
    incorrect = 0
    variable = 1
    
    global correct_variable
    global incorrect_variable
    
    correct_variable = 0
    incorrect_variable = 0
   
    global enemy_1
    global user 
    
    user_damage = 35
    enemy_damage = 30
    
    enemy_1 = Enemies(enemy_health, enemy_damage) 
    user = Character(user_health, user_damage)
    
    global user_dead
    global enemy_dead
    
    user_dead = False
    enemy_dead = False
    
    close = False
    
    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_SPACE]:
        
        run = True
        
        while run:
            print(enemy_dead)
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
#                     
#             #settings    
#             settings_icon = pygame.image.load('C:/Users/rkwan/Desktop/Settings.png')
#             settings_sized = pygame.transform.scale(settings_icon, (50,50))
# 
#             #display settings onto the screen
#             screen.blit(settings_sized, (740, 15))
                          
            close, user_dead, enemy_dead = questions_screen('What is 1 / 1?', '', 'The answer is: 1.', incorrect,'1', user_damage, enemy_damage, close, 'Use addition to add the two numbers together.', user_dead, enemy_dead, False, False, True, False)
            
            if close == True:
                variable = variable + 1
                run = False
                #screen that shows that the health of the characters go down
                close, user_dead, enemy_dead = questions_screen('What is 2 / 2?', '', 'The answer is: 1.', incorrect,'1', user_damage, enemy_damage, close,  'Use addition to add the two numbers together.', user_dead, enemy_dead, False, False, True, False)
                
                #add textbox here to congratulate the player 
                #
                #
                
                #end the round if the enemy dies
                if enemy_dead == True:
                    round = False
                    return round
                
            if close == True:
                variable = variable + 1
                run = False
                #screen that shows that the health of the characters go down
                close, user_dead, enemy_dead = questions_screen('What is 4 / 4?', '', 'The answer is: 1.', incorrect,'1', user_damage, enemy_damage, close,  'Use addition to add the two numbers together.', user_dead, enemy_dead, False, False, True, False)
            
                if enemy_dead == True:
                    round = False
                    return round
                
            if close == True:
                variable = variable + 1
                run = False
                #screen that shows that the health of the characters go down
                close, user_dead, enemy_dead = questions_screen('What is 8 / 8?', '', 'The answer is: 1.', incorrect,'1', user_damage, enemy_damage, close,  'Use addition to add the two numbers together.', user_dead, enemy_dead, False, False, True, False)
            
                if enemy_dead == True:
                    round = False
                    return round
                
            if close == True:
                variable = variable + 1
                run = False
                #screen that shows that the health of the characters go down
                close, user_dead, enemy_dead = questions_screen('What is 9 / 9?', '', 'The answer is: 1.', incorrect,'1', user_damage, enemy_damage, close,  'Use addition to add the two numbers together.', user_dead, enemy_dead, False, True, False, False)
            
                if enemy_dead == True:
                    round = False
                    return round
                
                if user_dead == True:
                    #add something here to restart the game or round if the user dies + a message
                    #
                    #
                    
                    round = False
                    return round
                

            pygame.display.flip()
            
def round_4(x,y, round):
    global enemy_sized
            
    #enemy    
    enemy = pygame.image.load('C:/Users/rkwan/Desktop/enemy4.gif')
    enemy_sized = pygame.transform.scale(enemy, (125, 130))
    screen.blit(pygame.transform.flip(enemy_sized, True, False), (x + 220, y))
    
    incorrect = 0
    variable = 1
    
    global correct_variable
    global incorrect_variable
    
    correct_variable = 0
    incorrect_variable = 0
   
    global enemy_1
    global user 
    
    user_damage = 40
    enemy_damage = 30
    
    enemy_1 = Enemies(enemy_health, enemy_damage) 
    user = Character(user_health, user_damage)
    
    global user_dead
    global enemy_dead
    
    user_dead = False
    enemy_dead = False
    
    close = False
    
    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_SPACE]:
        
        run = True
        
        while run:
            print(enemy_dead)
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
#             #settings    
#             settings_icon = pygame.image.load('C:/Users/rkwan/Desktop/Settings.png')
#             settings_sized = pygame.transform.scale(settings_icon, (50,50))
# 
#             #display settings onto the screen
#             screen.blit(settings_sized, (740, 15))
                          
            close, user_dead, enemy_dead = questions_screen('What is 1 / 1?', '', 'The answer is: 1.', incorrect,'1', user_damage, enemy_damage, close, 'Use addition to add the two numbers together.', user_dead, enemy_dead, False, False, False, True)
            
            if close == True:
                variable = variable + 1
                run = False
                #screen that shows that the health of the characters go down
                close, user_dead, enemy_dead = questions_screen('What is 2 / 2?', '', 'The answer is: 1.', incorrect,'1', user_damage, enemy_damage, close,  'Use addition to add the two numbers together.', user_dead, enemy_dead, False, False, False, True)
                
                #add textbox here to congratulate the player 
                #
                #
                
                #end the round if the enemy dies
                if enemy_dead == True:
                    round = False
                    return round
                
            if close == True:
                variable = variable + 1
                run = False
                #screen that shows that the health of the characters go down
                close, user_dead, enemy_dead = questions_screen('What is 4 / 4?', '', 'The answer is: 1.', incorrect,'1', user_damage, enemy_damage, close,  'Use addition to add the two numbers together.', user_dead, enemy_dead, False, False, False, True)
            
                if enemy_dead == True:
                    round = False
                    return round
                
            if close == True:
                variable = variable + 1
                run = False
                #screen that shows that the health of the characters go down
                close, user_dead, enemy_dead = questions_screen('What is 8 / 8?', '', 'The answer is: 1.', incorrect,'1', user_damage, enemy_damage, close,  'Use addition to add the two numbers together.', user_dead, enemy_dead, False, False, False, True)
            
                if enemy_dead == True:
                    round = False
                    return round
                
            if close == True:
                variable = variable + 1
                run = False
                #screen that shows that the health of the characters go down
                close, user_dead, enemy_dead = questions_screen('What is 9 / 9?', '', 'The answer is: 1.', incorrect,'1', user_damage, enemy_damage, close,  'Use addition to add the two numbers together.', user_dead, enemy_dead, False, True, False, True)
            
                if enemy_dead == True:
                    round = False
                    return round
                
                if user_dead == True:
                    #add something here to restart the game or round if the user dies + a message
                    #
                    #
                    
                    round = False
                    return round
                

            pygame.display.flip()
            
            
def questions_screen(text, input, solution, incorrect, quest_answer,user_damage, enemy_damage, close, hint, user_dead, enemy_dead, round1, round2, round3, round4):
    #spells
    ice = False
    fire = False
    
    #health values for the characters
    health = 100
        
    #input text setup
    answer = pygame.Rect(100,200, 175,30)
    answer_status = False
    input_text = ''
        
    keys = pygame.key.get_pressed()
    
    space = False
    
    questions = True
    
    while questions:
        
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                questions = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if answer.collidepoint(event.pos):
                    answer_status = True
                else:
                    answer_status = False
                    
            if event.type == pygame.KEYDOWN:
                
                if answer_status == True:
                    if event.key  == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text = input_text + event.unicode

        #creating a new screen to display the math questions    
        questions = pygame.display.set_mode((800,600))
        questions.fill((255,255,255))
        
#         #settings icon  
#         settings_icon = pygame.image.load('C:/Users/rkwan/Desktop/Settings.png')
#         settings_sized = pygame.transform.scale(settings_icon, (50,50))
#         #display settings onto the screen
#         screen.blit(settings_sized, (740, 15))
        
        #question text
        font = pygame.font.Font('freesansbold.ttf', 30) 
        question_text = font.render(text, True, (0,0,0)) 
        
        #textbox to hold questions
        textbox = question_text.get_rect()
        textbox.center = (200,100)
        
        #user input
        questions.fill((0,0,0), answer)
        answer_text = font.render(input_text, True, (255,255,255)) 
        
        #submit button for question 1          
        if 300 < mouse_pos[0] < 375 and 200 < mouse_pos[1] < 230:
            pygame.draw.rect(questions, (216,191,216), (300,200,75,30))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_text != '':
                    if input_text == quest_answer:
                        #calls the outcome function
                        run = outcome('Correct!', False)
                        #calls the spell function by giving it booleans according to which round it is 
                        test_bool, ice, fire = spell(round1, round2, round3, round4, True, ice, fire)
                        if test_bool == False:
                            space, user_dead, enemy_dead = spell_ball(True, health, user_damage, enemy_damage, space, user_dead, enemy_dead, ice, fire)
                            if space == True:
                                close = True
                                #return the booleans that indicate whether the characters are dead or not
                                return close, user_dead, enemy_dead
                                break
                 
                    else:
                        run = outcome('Incorrect, try again.', True)
                        incorrect += 1  
                
                else:
                    print("Try again, no text was entered.")
            
        else:
            pygame.draw.rect(questions, (153,50,204), (300,200,75,30))  
          
        #font settings for the hint button
        hint_font = pygame.font.Font('freesansbold.ttf', 20)
        hint_text = hint_font.render('Hint', True, (0,0,0))
        hint_rect = hint_text.get_rect()
        hint_rect.center = (695, 535)
            
        #drawing the hint button
        if incorrect >= 2:
            
            if 620 < mouse_pos[0] < 770 and 500 < mouse_pos[1] < 570:
                pygame.draw.rect(questions, (255,255,153), (620,500,150,70))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    hint_window(hint)
                    
            else:
                pygame.draw.rect(questions, (255,255,0), (620,500,150,70))
            
            #displaying the 'hint' text
            questions.blit(hint_text, hint_rect)
                        
        #solution box  
        if incorrect >= 3:
            
            #font settings for the solution
            solution_font = pygame.font.Font('freesansbold.ttf', 20)
            solution_text = solution_font.render(solution, True, (0,0,0))
            solution_rect = solution_text.get_rect()
            solution_rect = (100,350)
            questions.blit(solution_text, solution_rect)
            
            #making the submit button disappear (not completely done --> the user is still able to press it)
            pygame.draw.rect(questions, (255,255,255), (300,200,75,30))
            
            #font settings for the 'Ok.' button
            ok_font = pygame.font.Font('freesansbold.ttf', 20)
            ok_text = ok_font.render(' Ok. ', True, (0,0,0))
            ok_rect = ok_text.get_rect()
            ok_rect = (270,460)
            questions.blit(ok_text, ok_rect)
                                    
            #if the button OK. is pressed, then the enemy will attack the user
            if 270 < mouse_pos[0] < 300 and 460 < mouse_pos[1] < 490:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    space, user_dead, enemy_dead = spell_ball(False, health, user_damage, enemy_damage, space, user_dead, enemy_dead, True, False)
                    if space == True:
                        close = True
                        return close, user_dead, enemy_dead
                        break


        #font settings for the submit button
        button_font = pygame.font.Font('freesansbold.ttf', 20)
        button_text = button_font.render('Submit', True, (255,255,255))
        button_rect = button_text.get_rect()
        button_rect.center = (337, 215)
        
        #adding the elements to the 'questions' screen
        questions.blit(question_text, textbox)
        questions.blit(answer_text, (answer.x, answer.y))
        questions.blit(button_text, button_rect)
        
        pygame.display.update()
    
        pygame.display.flip()
        
#hint window
def hint_window(hint):
    
    pressed = True
    while pressed:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pop = False 
                
        hint_w = pygame.display.set_mode((800,600))
        hint_w.fill((255,255,255))
        
        #settings    
        settings_icon = pygame.image.load('C:/Users/rkwan/Desktop/Settings.png')
        settings_sized = pygame.transform.scale(settings_icon, (50,50))
        #display settings onto the screen
        screen.blit(settings_sized, (740, 15))
        
        #font settings for the hint 
        hintText_font = pygame.font.Font('freesansbold.ttf', 30) 
        hintText_text = hintText_font.render(hint, True, (0,0,0)) 
        hintText_rect = hintText_text.get_rect()
        hintText_rect.center = (400,300)
        
        if 350 < mouse_pos[0] < 450 and 400 < mouse_pos[1] < 440:
            pygame.draw.rect(hint_w, (216,191,216), (350,400,100,40))
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = False
        else:
            pygame.draw.rect(hint_w, (153,50,204), (350,400,100,40))
        
        button_font = pygame.font.Font('freesansbold.ttf', 30)
        button_text = button_font.render('Okay', True, (255,255,255))
        button_rect = button_text.get_rect()
        button_rect.center = (400, 420)
        
        hint_w.blit(button_text, button_rect)
        hint_w.blit(hintText_text, hintText_rect)
        
        pygame.display.flip()
        

#'b' boolean is returned and reassigned as 'run' to determine whether or not round 1 will continue            
def outcome(popup_text, b):
    
    pop = True
    
    while pop:
        
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pop = False
                
        window = pygame.display.set_mode((800,600))
        window.fill((255,255,255))
#         
#         #settings    
#         settings_icon = pygame.image.load('C:/Users/rkwan/Desktop/Settings.png')
#         settings_sized = pygame.transform.scale(settings_icon, (50,50))
#         #display settings onto the screen
#         screen.blit(settings_sized, (740, 15))
        
        font = pygame.font.Font('freesansbold.ttf', 80) 
        display_text = font.render(popup_text, True, (0,0,0)) 
            
        #textbox to hold questions
        textbox = display_text.get_rect()
        textbox.center = (400,300)
        
        #take the position of the mouse and check if it matches the position of the rectangle. 
        #If the position matches, then the colour of the rectangle will change.
        if 350 < mouse_pos[0] < 450 and 400 < mouse_pos[1] < 440:
            pygame.draw.rect(window, (216,191,216), (350,400,100,40))
            if event.type == pygame.MOUSEBUTTONDOWN:
                pop = False
                return b;
        else:
            pygame.draw.rect(window, (153,50,204), (350,400,100,40))
        
        button_font = pygame.font.Font('freesansbold.ttf', 30)
        button_text = button_font.render('Okay', True, (255,255,255))
        button_rect = button_text.get_rect()
        button_rect.center = (400, 420)
        
        window.blit(display_text, textbox)
        window.blit(button_text, button_rect)
        
        pygame.display.flip()
    
        
def spell(round1, round2, round3, round4, test1, ice, fire):
    
    spell = True
    while spell: 
        mouse_pos = pygame.mouse.get_pos()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spell = False
        
        spell_window = pygame.display.set_mode((800,600))
        spell_window.fill((255,255,255))
       
#         #settings    
#         settings_icon = pygame.image.load('C:/Users/rkwan/Desktop/Settings.png')
#         settings_sized = pygame.transform.scale(settings_icon, (50,50))
#         #display settings onto the screen
#         screen.blit(settings_sized, (740, 15))
        
        #title font settings
        title_font = pygame.font.Font('freesansbold.ttf', 40)
        title_text = title_font.render('Choose an attack!', True, (0,0,0))
        title_rect = title_text.get_rect()
        title_rect.center = (230,100)
        
        #displaying the title
        spell_window.blit(title_text, title_rect)
        
        if round1:
            #get the mouse position and see if it matches the button
            if 250 < mouse_pos[0] < 370 and 200 < mouse_pos[1] < 320:
                pygame.draw.rect(spell_window, (216,191,216), (250,200,120,120))
                if event.type == pygame.MOUSEBUTTONDOWN:            
                    test1 = False
                    ice = True
                    return test1, ice, fire 
                    break
                    
            else:
                pygame.draw.rect(spell_window, (153,50,204), (250,200,120,120))

            #font for the button attack text
            button_font = pygame.font.Font('freesansbold.ttf', 22)
            button_text = button_font.render('Icy blast', True, (255,255,255))
            button_rect = button_text.get_rect()
            button_rect.center = (310, 260)
            
            #draw all the rectangles for the attacks
            pygame.draw.rect(spell_window, (211,211,211), (420,200,120,120))
            pygame.draw.rect(spell_window, (211,211,211), (250,350,120,120))
            pygame.draw.rect(spell_window, (211,211,211), (420,350,120,120))
            
            #set all the text for the attack rectangles 
            round2_font = pygame.font.Font('freesansbold.ttf', 12)
            round2_text = round2_font.render('Unlock on level 2', True, (255,255,255))
            round2_rect = round2_text.get_rect()
            round2_rect.center = (480, 260)
            
            round3_font = pygame.font.Font('freesansbold.ttf', 12)
            round3_text = round3_font.render('Unlock on level 3', True, (255,255,255))
            round3_rect = round3_text.get_rect()
            round3_rect.center = (310, 410)
            
            round4_font = pygame.font.Font('freesansbold.ttf', 12)
            round4_text = round4_font.render('Unlock on level 4', True, (255,255,255))
            round4_rect = round4_text.get_rect()
            round4_rect.center = (480, 410)

            #display the text on the window
            spell_window.blit(button_text, button_rect)
            spell_window.blit(round2_text, round2_rect)
            spell_window.blit(round3_text, round3_rect)
            spell_window.blit(round4_text, round4_rect)
            
        
            pygame.display.flip()
            
        if round2:
            #get the mouse position and see if it matches the button
            if 250 < mouse_pos[0] < 370 and 200 < mouse_pos[1] < 320:
                pygame.draw.rect(spell_window, (216,191,216), (250,200,120,120))
                if event.type == pygame.MOUSEBUTTONDOWN:            
                    test1 = False
                    ice = True
                    return test1, ice, fire 
                    break
                    
            else:
                pygame.draw.rect(spell_window, (153,50,204), (250,200,120,120))

            #font for the button attack text
            button_font = pygame.font.Font('freesansbold.ttf', 22)
            button_text = button_font.render('Icy blast', True, (255,255,255))
            button_rect = button_text.get_rect()
            button_rect.center = (310, 260)
            
            #set up for button 2
            if 420 < mouse_pos[0] < 540 and 200 < mouse_pos[1] < 320:
                pygame.draw.rect(spell_window, (216,191,216), (420,200,120,120))
                if event.type == pygame.MOUSEBUTTONDOWN:            
                    test1 = False
                    fire = True
                    return test1, ice, fire
                    break
                    
            else:
                pygame.draw.rect(spell_window, (153,50,204), (420,200,120,120))
            
            #draw all the rectangles for the attacks
            pygame.draw.rect(spell_window, (211,211,211), (250,350,120,120))
            pygame.draw.rect(spell_window, (211,211,211), (420,350,120,120))
            
            #settings for button 2
            round2_font = pygame.font.Font('freesansbold.ttf', 22)
            round2_text = round2_font.render('Fire Melt', True, (255,255,255))
            round2_rect = round2_text.get_rect()
            round2_rect.center = (480, 260)
            
            round3_font = pygame.font.Font('freesansbold.ttf', 12)
            round3_text = round3_font.render('Unlock on level 3', True, (255,255,255))
            round3_rect = round3_text.get_rect()
            round3_rect.center = (310, 410)
            
            round4_font = pygame.font.Font('freesansbold.ttf', 12)
            round4_text = round4_font.render('Unlock on level 4', True, (255,255,255))
            round4_rect = round4_text.get_rect()
            round4_rect.center = (480, 410)

            #display the text on the window
            spell_window.blit(button_text, button_rect)
            spell_window.blit(round2_text, round2_rect)
            spell_window.blit(round3_text, round3_rect)
            spell_window.blit(round4_text, round4_rect)
            
        
            pygame.display.flip()
            
        if round3:
            #get the mouse position and see if it matches the button
            if 250 < mouse_pos[0] < 370 and 200 < mouse_pos[1] < 320:
                pygame.draw.rect(spell_window, (216,191,216), (250,200,120,120))
                if event.type == pygame.MOUSEBUTTONDOWN:            
                    test1 = False
                    ice = True
                    return test1, ice, fire
                    break
                    
            else:
                pygame.draw.rect(spell_window, (153,50,204), (250,200,120,120))

            #font for the button attack text
            button_font = pygame.font.Font('freesansbold.ttf', 22)
            button_text = button_font.render('Icy blast', True, (255,255,255))
            button_rect = button_text.get_rect()
            button_rect.center = (310, 260)
            
            #set up for button 2
            if 420 < mouse_pos[0] < 540 and 200 < mouse_pos[1] < 320:
                pygame.draw.rect(spell_window, (216,191,216), (420,200,120,120))
                if event.type == pygame.MOUSEBUTTONDOWN:            
                    test1 = False
                    fire = True
                    return test1, ice, fire
                    break
                    
            else:
                pygame.draw.rect(spell_window, (153,50,204), (420,200,120,120))
            
            #setup for button 3
            if 250 < mouse_pos[0] < 370 and 410 < mouse_pos[1] < 530:
                pygame.draw.rect(spell_window, (216,191,216), (250,410,120,120))
                if event.type == pygame.MOUSEBUTTONDOWN:            
                    test1 = False
                    return test1, ice, fire
                    break
                    
            else:
                pygame.draw.rect(spell_window, (153,50,204), (250,410,120,120))
            
            #draw all the rectangles for the attacks
            pygame.draw.rect(spell_window, (211,211,211), (250,350,120,120))
            pygame.draw.rect(spell_window, (211,211,211), (420,350,120,120))
            pygame.draw.rect(spell_window, (211,211,211), (250,410,120,120))
            
            #settings for button 2
            round2_font = pygame.font.Font('freesansbold.ttf', 22)
            round2_text = round2_font.render('Fire Melt', True, (255,255,255))
            round2_rect = round2_text.get_rect()
            round2_rect.center = (480, 260)
            
            round3_font = pygame.font.Font('freesansbold.ttf', 12)
            round3_text = round3_font.render('Magic Melt', True, (255,255,255))
            round3_rect = round3_text.get_rect()
            round3_rect.center = (310, 410)
            
            round4_font = pygame.font.Font('freesansbold.ttf', 12)
            round4_text = round4_font.render('Unlock on level 4', True, (255,255,255))
            round4_rect = round4_text.get_rect()
            round4_rect.center = (480, 410)

            #display the text on the window
            spell_window.blit(button_text, button_rect)
            spell_window.blit(round2_text, round2_rect)
            spell_window.blit(round3_text, round3_rect)
            spell_window.blit(round4_text, round4_rect)
            
        
            pygame.display.flip()
            
        if round4:
            #get the mouse position and see if it matches the button
            if 250 < mouse_pos[0] < 370 and 200 < mouse_pos[1] < 320:
                pygame.draw.rect(spell_window, (216,191,216), (250,200,120,120))
                if event.type == pygame.MOUSEBUTTONDOWN:            
                    test1 = False
                    return test1 
                    break
                    
            else:
                pygame.draw.rect(spell_window, (153,50,204), (250,200,120,120))

            #font for the button attack text
            button_font = pygame.font.Font('freesansbold.ttf', 22)
            button_text = button_font.render('Icy blast', True, (255,255,255))
            button_rect = button_text.get_rect()
            button_rect.center = (310, 260)
            
            #set up for button 2
            if 420 < mouse_pos[0] < 540 and 200 < mouse_pos[1] < 320:
                pygame.draw.rect(spell_window, (216,191,216), (420,200,120,120))
                if event.type == pygame.MOUSEBUTTONDOWN:            
                    test1 = False
                    return test1 
                    break
                    
            else:
                pygame.draw.rect(spell_window, (153,50,204), (420,200,120,120))
                
            #setup for button 3
            if 250 < mouse_pos[0] < 370 and 410 < mouse_pos[1] < 530:
                pygame.draw.rect(spell_window, (216,191,216), (250,410,120,120))
                if event.type == pygame.MOUSEBUTTONDOWN:            
                    test1 = False
                    return test1, ice, fire
                    break
                    
            else:
                pygame.draw.rect(spell_window, (153,50,204), (250,410,120,120))
                
            #setup for button 3
            if 420 < mouse_pos[0] < 540 and 410 < mouse_pos[1] < 530:
                pygame.draw.rect(spell_window, (216,191,216), (420,410,120,120))
                if event.type == pygame.MOUSEBUTTONDOWN:            
                    test1 = False
                    return test1, ice, fire
                    break
                    
            else:
                pygame.draw.rect(spell_window, (153,50,204), (420,410,120,120))
            
            #draw all the rectangles for the attacks
            pygame.draw.rect(spell_window, (211,211,211), (250,350,120,120))
            pygame.draw.rect(spell_window, (211,211,211), (420,350,120,120))
            pygame.draw.rect(spell_window, (211,211,211), (250,410,120,120))

            #settings for button 2
            round2_font = pygame.font.Font('freesansbold.ttf', 22)
            round2_text = round2_font.render('Fire Melt', True, (255,255,255))
            round2_rect = round2_text.get_rect()
            round2_rect.center = (480, 260)
            
            round3_font = pygame.font.Font('freesansbold.ttf', 12)
            round3_text = round3_font.render('Magic Melt', True, (255,255,255))
            round3_rect = round3_text.get_rect()
            round3_rect.center = (310, 410)
            
            round4_font = pygame.font.Font('freesansbold.ttf', 12)
            round4_text = round4_font.render('Goo of Doom', True, (255,255,255))
            round4_rect = round4_text.get_rect()
            round4_rect.center = (480, 410)

            #display the text on the window
            spell_window.blit(button_text, button_rect)
            spell_window.blit(round2_text, round2_rect)
            spell_window.blit(round3_text, round3_rect)
            spell_window.blit(round4_text, round4_rect)
            
        
            pygame.display.flip()

        
def spell_ball(correct, health, user_damage, enemy_damage, space, user_dead, enemy_dead, ice, fire):
    
    spell = True
    x = 240
    
    global correct_variable
    global incorrect_variable
    global i

    if correct:
        correct_variable += 1
        
    else:
        incorrect_variable +=1
    
    #enemy image    
    global enemy_sized
        
    #spell animation
    ice_ball = pygame.image.load('C:/Users/rkwan/Desktop/spell.png')
    fire_ball = pygame.image.load('C:/Users/rkwan/Desktop/fireball.png')
    
    #determining which spell to use with the boolean variables passed into this function
    if ice:
        small_ball = pygame.transform.scale(ice_ball, (50, 30))
        
    elif fire:
        small_ball = pygame.transform.scale(fire_ball, (50, 30))

    #background image
    background = pygame.image.load('C:/Users/rkwan/Desktop/picture.PNG').convert()
    
    #standing character image
    standing_sized = pygame.transform.scale(standing, (125,125))     
   
    if correct:
        enemy_1.health = enemy_1.health - enemy_1.damage
        
    else:
        user.health = user.health - user.damage
        x = 420

        
    while spell: 
             
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                questions = False  
                
        screen.blit(background, (-250,0))
        screen.blit(standing_sized, (220,400))
        screen.blit(enemy_sized, (220 + 220, 400))
        
#         #settings    
#         settings_icon = pygame.image.load('C:/Users/rkwan/Desktop/Settings.png')
#         settings_sized = pygame.transform.scale(settings_icon, (50,50))
#         #display settings onto the screen
#         screen.blit(settings_sized, (740, 15))
        
        #user health bar
        pygame.draw.rect(screen, (255,0,0), (50,75,health*2,50))
        #enemy health bar
        pygame.draw.rect(screen, (255,0,0),(550,75, health*2,50))

        #if statement to avoid x values from being multiplied by -1 when the correct_variable is = 0. 
        #This avoids the code from drawing a black rectangle when it is not needed
        if correct_variable == 0 or correct_variable == 1:
            #drawing a black rectangle over the enemy health bar between questions answered
            pygame.draw.rect(screen, (0,0,0), (550,75,enemy_1.damage*2*(correct_variable),50))
            
        else: 
            pygame.draw.rect(screen, (0,0,0), (550,75,enemy_1.damage*2*(correct_variable -1),50))

        #same logic for the incorrect_variable
        if incorrect_variable == 0 or incorrect_variable == 1:
            #drawing a black rectangle over the user health bar between questions answered
            pygame.draw.rect(screen, (0,0,0), ((50+health*2) - user.damage*2*(incorrect_variable),75,user.damage*2*(incorrect_variable),50))
        
        else:
            pygame.draw.rect(screen, (0,0,0), ((50+health*2) - user.damage*2*(incorrect_variable-1),75,user.damage*2*(incorrect_variable-1),50))


        if correct: 
            #stop the while loop if the spell reaches the enemy
            if x < 420:
                #move the spell image 
                x = x + 1
                hit_sound.play()

             
            else:
                #the spell will disappear from the screen
                small_ball.fill(transparent) 
                x = x + 0
                
                #drawing a black rectangle over the enemy health bar to show that some damage was lost 
                pygame.draw.rect(screen, (0,0,0), (550,75,(enemy_1.damage*2)*correct_variable,50))
                 
                if enemy_1.health <= 0:
                    enemy_sized.fill(transparent)
                    dying_sound.play()

                    enemy_dead = True

                                 
                #acting as a transition controller to go to the next screen 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    space = True
                    spell = False
                    return space, user_dead, enemy_dead
                 
            #display the spell image
            screen.blit(small_ball, (x, 450))
                     
            pygame.display.update()       
            
        else:     

            #stop the while loop if the spell reaches the enemy
            if x > 220:
                #move the spell image 
                x = x - 1
                hit_sound.play()
                  
            else:
                small_ball.fill(transparent)
                x = x+0
                  
                #drawing a black rectangle over the enemy health bar to show that some damage was lost 
                pygame.draw.rect(screen, (0,0,0), ((50 + health*2)- ((user.damage*2)*incorrect_variable),75, (user.damage*2)*incorrect_variable,50))
                  
                if user.health <= 0:
                    dying_sound.play()
                    #push the enemy back one round
                    if i == 1:
                        i =1
                    else:
                        i-=1

                    user_dead = True
#                     enemy_sized.fill(transparent)
                  
                if event.type == pygame.MOUSEBUTTONDOWN:
                    spell = False
                    space = True
                    return space, user_dead, enemy_dead
                  
            #display the spell image
            screen.blit(pygame.transform.flip(small_ball, True, False), (x, 450))
            
            pygame.display.update()
            



            
run()


    
    
    



        
        
        
        
    
    
    
