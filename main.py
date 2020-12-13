import pygame, sys
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Python Game by PasKa')
screen = pygame.display.set_mode((500, 500), 0, 32)

# variables
TILE_SIZE = 16
GRAVITY = 0
SPEED = 2
ORIENTATION = "Right"
anim_count = 0
idle_count = 0

# player = pygame.Rect(100, 100, 40, 80)
# player_image = pygame.image.load('images/1.png')
# player_image1 = pygame.image.load('images/adventurer-jump-00.png')

# tilemap images
ground_image_1 = pygame.image.load('tiles/tile_1.png')
ground_image_4 = pygame.image.load('tiles/tile_4.png')
bg = pygame.image.load("tiles/Wasteland_Sky.png")
mountain_1 = pygame.image.load("tiles/Wasteland_Mountains_1.png")
mountain_2 = pygame.image.load("tiles/Wasteland_Mountains_2.png")

# ==== animation images sequences ====
game_map = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '4', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '1', '1', '1', '4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['4', '4', '4', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['4', '4', '4', '4', '4', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4'],
            ['4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4'],
            ['4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4'],
            ['4', '4', '4', '4', '4', '14', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4']]
runRight = [pygame.image.load('images/adventurer-run-00.png'),
            pygame.image.load('images/adventurer-run-01.png'),
            pygame.image.load('images/adventurer-run-02.png'),
            pygame.image.load('images/adventurer-run-03.png'),
            pygame.image.load('images/adventurer-run-04.png'),
            pygame.image.load('images/adventurer-run-05.png')]
runLeft = [pygame.image.load('images/adventurer-run-left-00.png'),
           pygame.image.load('images/adventurer-run-left-01.png'),
           pygame.image.load('images/adventurer-run-left-02.png'),
           pygame.image.load('images/adventurer-run-left-03.png'),
           pygame.image.load('images/adventurer-run-left-04.png'),
           pygame.image.load('images/adventurer-run-left-05.png')]
playerStand = [pygame.image.load('images/adventurer-idle-3-00.png'),
               pygame.image.load('images/adventurer-idle-3-00.png'),
               pygame.image.load('images/adventurer-idle-3-01.png'),
               pygame.image.load('images/adventurer-idle-3-01.png'),
               pygame.image.load('images/adventurer-idle-3-02.png'),
               pygame.image.load('images/adventurer-idle-3-03.png')]
playerStand1 = [pygame.image.load('images/adventurer-idle-2-00.png'),
                pygame.image.load('images/adventurer-idle-2-00.png'),
                pygame.image.load('images/adventurer-idle-2-01.png'),
                pygame.image.load('images/adventurer-idle-2-01.png'),
                pygame.image.load('images/adventurer-idle-2-02.png'),
                pygame.image.load('images/adventurer-idle-2-03.png')]
playerJump = [pygame.image.load('images/adventurer-jump-02.png'),
              pygame.image.load('images/adventurer-jump-02.png'),
              pygame.image.load('images/adventurer-jump-02.png'),
              pygame.image.load('images/adventurer-jump-03.png'),
              pygame.image.load('images/adventurer-jump-03.png'),
              pygame.image.load('images/adventurer-jump-03.png')]
playerJumpLeft = [pygame.image.load('images/adventurer-jump-left-02.png'),
                  pygame.image.load('images/adventurer-jump-left-02.png'),
                  pygame.image.load('images/adventurer-jump-left-02.png'),
                  pygame.image.load('images/adventurer-jump-left-03.png'),
                  pygame.image.load('images/adventurer-jump-left-03.png'),
                  pygame.image.load('images/adventurer-jump-left-03.png')]
playerJump1Left = [pygame.image.load('images/adventurer-jump-l-01.png'),
                   pygame.image.load('images/adventurer-jump-l-01.png'),
                   pygame.image.load('images/adventurer-jump-l-01.png'),
                   pygame.image.load('images/adventurer-jump-l-01.png'),
                   pygame.image.load('images/adventurer-jump-l-01.png'),
                   pygame.image.load('images/adventurer-jump-l-01.png')]
playerJump1 = [pygame.image.load('images/adventurer-jump-01.png'),
               pygame.image.load('images/adventurer-jump-01.png'),
               pygame.image.load('images/adventurer-jump-01.png'),
               pygame.image.load('images/adventurer-jump-01.png'),
               pygame.image.load('images/adventurer-jump-01.png'),
               pygame.image.load('images/adventurer-jump-01.png')]
attack_right = [pygame.image.load('images/adventurer-attack2-01.png'),
                pygame.image.load('images/adventurer-attack2-02.png'),
                pygame.image.load('images/adventurer-attack2-03.png'),
                pygame.image.load('images/adventurer-attack2-04.png'),
                pygame.image.load('images/adventurer-attack2-05.png'),
                pygame.image.load('images/adventurer-attack2-05.png')]
attack_left = [pygame.image.load('images/adventurer-attack4-01.png'),
               pygame.image.load('images/adventurer-attack4-02.png'),
               pygame.image.load('images/adventurer-attack4-03.png'),
               pygame.image.load('images/adventurer-attack4-04.png'),
               pygame.image.load('images/adventurer-attack4-05.png'),
               pygame.image.load('images/adventurer-attack4-05.png')]


def collision_test(rect, tiles):
    collisions = []
    for tile in tiles:
        if rect.colliderect(tile):
            collisions.append(tile)
    return collisions


def move(rect, movement, tiles):
    rect.x += movement[0]
    collisions = collision_test(rect, tiles)
    for tile in collisions:
        if movement[0] > 0:
            # right collision
            rect.right = tile.left
        if movement[0] < 0:
            # left collision
            rect.left = tile.right
    rect.y += movement[1]
    collisions = collision_test(rect, tiles)
    for tile in collisions:
        if movement[1] > 0:
            # bottom collision
            rect.bottom = tile.top
        if movement[1] <= 0:
            # top collision
            rect.top = tile.bottom

    return rect


# ==== animation variables ====
right = False
isJump = False
left = False
up = False
attack = False
down = False

WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
# Surface is a half resolution of main screen
display = pygame.Surface((400, 300))

# player hitbox
player_rect = pygame.Rect(50, 50, 15, 20)

jump_timer = 30
# ==== GAME LOOP ====
while True:
    # print(orientation)
    jump_timer += 1
    if jump_timer >= 30:
        jump_timer = 30
    elif jump_timer == 28:
        isJump = False
    # print(jump_timer)
    # ==== tilemap ====
    tiles = []
    # display.fill((0, 0, 0))
    display.blit(bg, (0, 0))
    display.blit(mountain_1, (0, 0))
    display.blit(mountain_2, (0, 0))
    for i in range(len(game_map) - 1):
        for j in range(len(game_map[0]) - 1):
            if game_map[i][j] == '1':
                display.blit(ground_image_1, (j * TILE_SIZE, i * TILE_SIZE))
            if game_map[i][j] == '4':
                display.blit(ground_image_4, (j * TILE_SIZE, i * TILE_SIZE))
            if game_map[i][j] != '0':
                tiles.append(pygame.Rect(j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    movement = [0, 0]
    if right:
        movement[0] += SPEED
    if left:
        movement[0] -= SPEED
    movement[1] += GRAVITY
    GRAVITY += 0.5
    if GRAVITY > 6:
        GRAVITY = 6

    # invisible hitbox movement
    player_rect = move(player_rect, movement, tiles)

    # ======= animation =======
    if anim_count + 1 >= 30:
        anim_count = 0
        attack = False
    if idle_count + 1 >= 30:
        idle_count = 0

    if isJump:
        if right:
            display.blit(playerJump[anim_count // 6], (player_rect.x - 17, player_rect.y - 16))
            anim_count += 1
            attack = False
        elif left:
            display.blit(playerJumpLeft[anim_count // 6], (player_rect.x - 17, player_rect.y - 16))
            anim_count += 1
            attack = False
        else:
            if ORIENTATION == "Right":
                display.blit(playerJump1[anim_count // 6], (player_rect.x - 17, player_rect.y - 16))
            if ORIENTATION == "Left":
                display.blit(playerJump1Left[anim_count // 6], (player_rect.x - 17, player_rect.y - 16))
            anim_count += 1
            attack = False
    elif right:
        display.blit(runRight[anim_count // 6], (player_rect.x - 17, player_rect.y - 16))
        ORIENTATION = "Right"
        anim_count += 1
    elif left:
        display.blit(runLeft[anim_count // 6], (player_rect.x - 17, player_rect.y - 16))
        ORIENTATION = "Left"
        anim_count += 1
    elif attack:
        if ORIENTATION == "Right":
            display.blit(attack_right[anim_count // 6], (player_rect.x - 17, player_rect.y - 16))
        if ORIENTATION == "Left":
            display.blit(attack_left[anim_count // 6], (player_rect.x - 17, player_rect.y - 16))
        anim_count += 2
        left, right = False, False
    else:
        if ORIENTATION == "Right":
            # hitbox draw
            # pygame.draw.rect(display, (255, 255, 0), player_rect)
            display.blit(playerStand[idle_count // 6], (player_rect.x - 17, player_rect.y - 16))

        if ORIENTATION == "Left":
            display.blit(playerStand1[idle_count // 6], (player_rect.x - 17, player_rect.y - 16))
        idle_count += 1
        anim_count = 0

    # for tile in tiles:
    # pygame.draw.rect(display, (225, 0, 0), tile)
    # display.blit(ground_image, ())

    # ==== get key down ====
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_d:
                right = True
            if event.key == K_a:
                left = True
            if event.key == K_SPACE and jump_timer >= 30:
                isJump = True
                jump_timer = 0
                GRAVITY = -8
            if event.key == K_f:
                attack = True
                right, left = False, False
        if event.type == KEYUP:
            if event.key == K_d:
                right = False
            if event.key == K_a:
                left = False

    # ==== transform display to screen and scaling ====
    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
    pygame.display.update()
    mainClock.tick(60)