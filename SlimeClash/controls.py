import pygame

def keys_down(event, player_sprites):

    for player in player_sprites:
        if player.get_id() == 0:
            move_left = pygame.K_a
            move_right = pygame.K_d
            jump = pygame.K_s

        elif player.get_id() == 1:
            move_left = pygame.K_LEFT
            move_right = pygame.K_RIGHT
            jump = pygame.K_DOWN

        elif player.get_id() == 2:
            move_left = pygame.K_f
            move_right = pygame.K_h
            jump = pygame.K_g

        elif player.get_id() == 3:
            move_left = pygame.K_j
            move_right = pygame.K_l
            jump = pygame.K_k
        else:
            move_left = 0
            move_right = 0
            jump = 0

        if event.key == move_left:
            player.set_move_left(True)
        if event.key == move_right:
            player.set_move_right(True)
        if event.key == jump:
            player.set_jump(True)


def keys_up(event, list_of_player):
    for player in list_of_player:
        if player.get_id() == 0:
            move_left = pygame.K_a
            move_right = pygame.K_d
            jump = pygame.K_s

        elif player.get_id() == 1:
            move_left = pygame.K_LEFT
            move_right = pygame.K_RIGHT
            jump = pygame.K_DOWN

        elif player.get_id() == 2:
            move_left = pygame.K_f
            move_right = pygame.K_h
            jump = pygame.K_g

        elif player.get_id() == 3:
            move_left = pygame.K_j
            move_right = pygame.K_l
            jump = pygame.K_k
        else:
            move_left = 0
            move_right = 0
            jump = 0

        if event.key == move_left:
            player.set_move_left(False)
        if event.key == move_right:
            player.set_move_right(False)
        if event.key == jump:
            player.set_jump(False)


def hat_down(event, list_of_player):
    for player in list_of_player:
        if player.get_id() == event.joy:
            if event.value[0] == 1:
                player.set_move_right(True)
            if event.value[0] == 0:
                player.set_move_left(False)
                player.set_move_right(False)
            if event.value[0] == -1:
                player.set_move_left(True)


def button_down(event, list_of_player):
    for player in list_of_player:
        if player.get_id() == event.joy:
            if event.button == 0 or event.button == 1 or event.button == 2 or event.button == 3:
                player.set_jump(True)


def button_up(event, list_of_player):
    for player in list_of_player:
        if player.get_id() == event.joy:
            if event.button == 0 or event.button == 1 or event.button == 2 or event.button == 3:
                player.set_jump(False)
