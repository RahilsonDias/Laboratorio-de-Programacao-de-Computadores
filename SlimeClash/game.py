import random
import sys
import pygame.sprite
import controls
from settings import *
from tile import Tile
from player import Player
from powerup import Pow


class Game:
    def __init__(self):
        # level setup
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.active_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.powerups_sprites = pygame.sprite.Group()

        # game settings
        self.player_id = 0
        self.player_count = 0
        self.level_id = ""

        # joysticks
        self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

        # draw menu
        self.bg = pygame.image.load("sprites/SlimeClashTitle.png")
        self.menu()

        # powerups
        self.powerup_count = 0
        self.powerup_spawn = []

    def menu(self):
        MENU_THEME.set_volume(0.25)
        MENU_THEME.play(loops=-1)
        menu = True
        while menu:
            self.display_surface.blit(self.bg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_RETURN:
                        CONFIRM_SOUND.play()
                        menu = False
            pygame.display.flip()

        menu = True
        while menu:
            self.bg = pygame.image.load("sprites/SlimeClashPlayers.png")
            self.display_surface.blit(self.bg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_2:
                        CONFIRM_SOUND.play()
                        self.player_count = 2
                        menu = False
                    if event.key == pygame.K_3:
                        CONFIRM_SOUND.play()
                        self.player_count = 3
                        menu = False
                    if event.key == pygame.K_4:
                        CONFIRM_SOUND.play()
                        self.player_count = 4
                        menu = False
            pygame.display.flip()

        menu = True
        while menu:
            self.bg = pygame.image.load("sprites/SlimeClashStages.png")
            self.display_surface.blit(self.bg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_1:
                        CONFIRM_SOUND.play()
                        MENU_THEME.stop()
                        self.level_id = LEVEL_1_MAP
                        menu = False
                        self.setup_level("sprites/StageBeach.png", "sprites/TileBeach1.png",
                                         "sprites/TileBeach2.png", BEACH_THEME)
                    if event.key == pygame.K_2:
                        CONFIRM_SOUND.play()
                        MENU_THEME.stop()
                        self.level_id = LEVEL_2_MAP
                        menu = False
                        self.setup_level("sprites/StageCave.png", "sprites/TileCave1.png",
                                         "sprites/TileCave2.png", CAVE_THEME)
                    if event.key == pygame.K_3:
                        CONFIRM_SOUND.play()
                        MENU_THEME.stop()
                        self.level_id = LEVEL_3_MAP
                        menu = False
                        self.setup_level("sprites/StageClouds.png", "sprites/TileCloud1.png",
                                         "sprites/TileCloud2.png", CLOUDS_THEME)
            pygame.display.flip()

    def setup_level(self, level_bg, tile_g, tile_ug, theme):
        theme.set_volume(0.25)
        theme.play(loops=-1)
        self.bg = pygame.image.load(level_bg)
        ground = pygame.image.load(tile_g)
        under_ground = pygame.image.load(tile_ug)
        self.display_surface.blit(self.bg, (0, 0))
        for row_index, row in enumerate(self.level_id):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == 'X':
                    Tile((x, y), (self.visible_sprites, self.collision_sprites), under_ground)
                if col == 'Y':
                    Tile((x, y), (self.visible_sprites, self.collision_sprites), ground)
                # if col == 'W':
                    # self.powerup_spawn.append((row, col))
                if col == 'P' and len(self.player_sprites) < self.player_count:
                    self.player_sprites.add(Player((x, y),
                                            (self.visible_sprites, self.active_sprites),
                                            self.collision_sprites, self.player_sprites, self.powerups_sprites, self.player_id))
                    self.player_id += 1

    def win_menu(self):
        pygame.mixer.stop()
        VICTORY_THEME.set_volume(0.5)
        VICTORY_THEME.play()
        win_menu = True
        while win_menu:
            self.bg = pygame.image.load("sprites/SlimeClashResults.png")
            self.display_surface.blit(self.bg, (0, 0))
            winner = pygame.image.load(f"sprites/slime{self.player_sprites.sprites()[0].get_id()}idle.png")
            self.display_surface.blit(winner, (SCREEN_WIDTH//2 - TILE_SIZE, SCREEN_HEIGHT//2 - TILE_SIZE))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_RETURN:
                        sys.exit()
            pygame.display.flip()

    def hud(self):
        hud_text1 = FONT.render("0", True, (255, 255, 255))
        hud_text2 = FONT.render("0", True, (255, 255, 255), (0, 0, 0))
        hud_text3 = FONT.render("0", True, (255, 255, 255), (0, 0, 0))
        hud_text4 = FONT.render("0", True, (255, 255, 255), (0, 0, 0))
        hud_text1_rect = hud_text1.get_rect()
        hud_text2_rect = hud_text2.get_rect()
        hud_text3_rect = hud_text3.get_rect()
        hud_text4_rect = hud_text4.get_rect()
        hud_text1_rect.center = (80, 35)
        hud_text2_rect.center = (380, 35)
        hud_text3_rect.center = (680, 35)
        hud_text4_rect.center = (980, 35)

        if len(self.player_sprites) == 2:
            hud_text1 = FONT.render(f"{self.player_sprites.sprites()[0].get_lives()}",
                                    True, (255, 255, 255), self.player_sprites.sprites()[0].get_color())
            hud_text2 = FONT.render(f"{self.player_sprites.sprites()[1].get_lives()}",
                                    True, (255, 255, 255), self.player_sprites.sprites()[1].get_color())
            # P1 HUD
            self.display_surface.blit(
                pygame.image.load(f"sprites/slime{self.player_sprites.sprites()[0].get_id()}idle.png"), (45, 30))
            self.display_surface.blit(hud_text1, hud_text1_rect.center)
            # P2 HUD
            self.display_surface.blit(
                pygame.image.load(f"sprites/slime{self.player_sprites.sprites()[1].get_id()}idle.png"), (345, 30))
            self.display_surface.blit(hud_text2, hud_text2_rect.center)
        elif len(self.player_sprites) == 3:
            hud_text1 = FONT.render(f"{self.player_sprites.sprites()[0].get_lives()}",
                                    True, (255, 255, 255), self.player_sprites.sprites()[0].get_color())
            hud_text2 = FONT.render(f"{self.player_sprites.sprites()[1].get_lives()}",
                                    True, (255, 255, 255), self.player_sprites.sprites()[1].get_color())
            hud_text3 = FONT.render(f"{self.player_sprites.sprites()[2].get_lives()}",
                                    True, (255, 255, 255), self.player_sprites.sprites()[2].get_color())
            # P1 HUD
            self.display_surface.blit(
                pygame.image.load(f"sprites/slime{self.player_sprites.sprites()[0].get_id()}idle.png"), (45, 30))
            self.display_surface.blit(hud_text1, hud_text1_rect.center)
            # P2 HUD
            self.display_surface.blit(
                pygame.image.load(f"sprites/slime{self.player_sprites.sprites()[1].get_id()}idle.png"), (345, 30))
            self.display_surface.blit(hud_text2, hud_text2_rect.center)
            # P3 HUD
            self.display_surface.blit(
                pygame.image.load(f"sprites/slime{self.player_sprites.sprites()[2].get_id()}idle.png"), (645, 30))
            self.display_surface.blit(hud_text3, hud_text3_rect.center)
        elif len(self.player_sprites) == 4:
            hud_text1 = FONT.render(f"{self.player_sprites.sprites()[0].get_lives()}",
                                    True, (255, 255, 255), self.player_sprites.sprites()[0].get_color())
            hud_text2 = FONT.render(f"{self.player_sprites.sprites()[1].get_lives()}",
                                    True, (255, 255, 255), self.player_sprites.sprites()[1].get_color())
            hud_text3 = FONT.render(f"{self.player_sprites.sprites()[2].get_lives()}",
                                    True, (255, 255, 255), self.player_sprites.sprites()[2].get_color())
            hud_text4 = FONT.render(f"{self.player_sprites.sprites()[3].get_lives()}",
                                    True, (255, 255, 255), self.player_sprites.sprites()[3].get_color())
            # P1 HUD
            self.display_surface.blit(
                pygame.image.load(f"sprites/slime{self.player_sprites.sprites()[0].get_id()}idle.png"), (45, 30))
            self.display_surface.blit(hud_text1, hud_text1_rect.center)
            # P2 HUD
            self.display_surface.blit(
                pygame.image.load(f"sprites/slime{self.player_sprites.sprites()[1].get_id()}idle.png"), (345, 30))
            self.display_surface.blit(hud_text2, hud_text2_rect.center)
            # P3 HUD
            self.display_surface.blit(
                pygame.image.load(f"sprites/slime{self.player_sprites.sprites()[2].get_id()}idle.png"), (645, 30))
            self.display_surface.blit(hud_text3, hud_text3_rect.center)
            # P4 HUD
            self.display_surface.blit(
                pygame.image.load(f"sprites/slime{self.player_sprites.sprites()[3].get_id()}idle.png"), (945, 30))
            self.display_surface.blit(hud_text4, hud_text4_rect.center)

    def actions(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                controls.keys_down(event, self.player_sprites)

            if event.type == pygame.KEYUP:
                controls.keys_up(event, self.player_sprites)

            if event.type == pygame.JOYHATMOTION:
                controls.hat_down(event, self.player_sprites)

            if event.type == pygame.JOYBUTTONDOWN:
                controls.button_down(event, self.player_sprites)

            if event.type == pygame.JOYBUTTONUP:
                controls.button_up(event, self.player_sprites)

    def run(self):
        # run the entire game (level)
        self.display_surface.blit(self.bg, (0, 0))
        self.active_sprites.update()
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        self.actions()
        self.powerup_count += 1
        if self.powerup_count > 400:
            if random.random() > 0.9:
                self.powerup_count = 0
                power = Pow((512, 384))
                self.visible_sprites.add(power)
                self.powerups_sprites.add(power)
        if len(self.player_sprites) < 2:
            print("End")
            self.win_menu()
        self.hud()
