import pygame
import random
import os
###############################################################################
pygame.init() # initialize ( MUST DO )

# secreen resolution setup
screen_width = 480 # horizontal 
screen_height = 640 # vertical
screen = pygame.display.set_mode((screen_width, screen_height))

# screen title setup
pygame.display.set_caption("Catharziz Games") # Game name

# FPS
clock = pygame.time.Clock()
############################################################################################

# 1. User game initialization ( resolution, game image, coordinates, speed, font, etc)
current_path = os.path.dirname(__file__) # get file directory
image_path = os.path.join(current_path, "images")  # get images folder 

# background
background = pygame.image.load(os.path.join(image_path, "background.png"))

# Character
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height 

# character movement
character_speed = 0.6

# Enemy
enemy = pygame.image.load(os.path.join(image_path, "enemy.png"))
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0,480-enemy_width)
enemy_y_pos = 0

# enemy movement
enemy_speed = 0.6
 
# movement location
to_x = 0
to_y = 0


running = True 
while running:
    dt = clock.tick(30) 

    # 2. Event Handler ( Keyboard, Mouse, etc )
    for event in pygame.event.get(): # check events
        if event.type == pygame.QUIT: # X clicked
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # move left
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # move right
                to_x += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            
        


    # 3. Definition for game character location 
    character_x_pos += to_x * dt
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > 480 - character_width:
        character_x_pos = 480-character_width
    # enemy movement
    enemy_y_pos += 5
    if enemy_y_pos > 640:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0,480-enemy_x_pos)

    # 4. Collision 
    # rect info for collision 
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # check collision
    if character_rect.colliderect(enemy_rect):
        print("Collided")
        running = False

    # 5. Draw on Screen
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos,character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update() # redrawing game screen

# delay before ending
pygame.time.delay(1000) # wait 2 seconds before ending (ms)

#pygame exit
pygame.quit()

