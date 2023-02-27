import pygame
pygame.init()

# size
TILE_SIZE = 32
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576

# gameplay
PLAYER_SPEED = 8
PLAYER_GRAVITY = 0.8
PLAYER_JUMP_SPEED = 16
PLAYER_LIVES = 10
PLAYER_DEATH_TIME = 10
PLAYER_INVIS_TIME = 10

# font
FONT = pygame.font.Font("fonts/PressStart2P.ttf", 25)

# sounds
pygame.mixer.init()
CONFIRM_SOUND = pygame.mixer.Sound("sounds/enter_stage.wav")
JUMP_SOUND = pygame.mixer.Sound("sounds/jump.wav")
HIT_SOUND = pygame.mixer.Sound("sounds/death.wav")
MENU_THEME = pygame.mixer.Sound("sounds/menu.ogg")
BEACH_THEME = pygame.mixer.Sound("sounds/theme_beach.ogg")
CAVE_THEME = pygame.mixer.Sound("sounds/theme_cave.ogg")
CLOUDS_THEME = pygame.mixer.Sound("sounds/theme_cloud.wav")
VICTORY_THEME = pygame.mixer.Sound("sounds/stage_clear.ogg")

# level
LEVEL_1_MAP = ['                                ',
               '                                ',
               '                                ',
               '             YYYYYYY            ',
               '       P                 P      ',
               '     YYYYY             YYYYY    ',
               '                                ',
               '                                ',
               '                                ',
               '                                ',
               '                                ',
               '                                ',
               '                                ',
               '   P                        P   ',
               'YYYYYYY                  YYYYYYY',
               'XXXXXXX                  XXXXXXX',
               'XXXXXXX      YYYYYY      XXXXXXX',
               'XXXXXXX      XXXXXX      XXXXXXX']

LEVEL_2_MAP = ['XXXXXXXXXXX          XXXXXXXXXXX',
               'XXXXXXXXX              XXXXXXXXX',
               'XXXXXXX                  XXXXXXX',
               'XXXXX                      XXXXX',
               '             YYYYYY             ',
               '                                ',
               '                                ',
               '      P                  P      ',
               'YYYYYYYYY              YYYYYYYYY',
               'XXXXX                      XXXXX',
               '                                ',
               '                                ',
               '                                ',
               '    P        YYYYYY        P    ',
               'YYYYY                      YYYYY',
               'XXXXXYY                  YYXXXXX',
               'XXXXXXXYY              YYXXXXXXX',
               'XXXXXXXXXYY          YYXXXXXXXXX']

LEVEL_3_MAP = ['                                ',
               '                                ',
               '                                ',
               '                                ',
               '                P               ',
               '              YYYYY             ',
               '                                ',
               '                                ',
               '     P                    P     ',
               '   YYYYY                YYYYY   ',
               '                                ',
               '                                ',
               '                P               ',
               '      YYYYYYYYYYYYYYYYYYYY      ',
               '       XXXXXXXXXXXXXXXXXX       ',
               '        XXXXXXXXXXXXXXXX        ',
               '         XXXXXXXXXXXXXX         ',
               '                                ']
