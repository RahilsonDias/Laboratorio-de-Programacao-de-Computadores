from modules.config import *


def draw_arena(file_name):
    list_of_rect = []
    mc = 1332/222
    ml = 626/40
    archive = open(file_name, "r")
    lista_of_lines = archive.readlines()
    t1, t2, t3, t4 = 0, 0, 0, 0
    location1, location2, location3, location4 = 0, 0, 0, 0
    for line in range(len(lista_of_lines)):
        for column in range(len(lista_of_lines[line])):
            if lista_of_lines[line][column] == "2":
                w = 1
                h = 1
                while lista_of_lines[line][column + w] == "1":
                    w += 1
                while lista_of_lines[line + h][column] == "3":
                    h += 1
                rect = (((column * mc) + 17), ((line * ml) + 77), (w * mc), (h * ml))
                list_of_rect.append(rect)
            if lista_of_lines[line][column] == "a" and t1 == 0:
                t1 += 1
                location3 = (((column * mc) + 39), ((line * ml) + 99))
            if lista_of_lines[line][column] == "b" and t2 == 0:
                t2 += 1
                location1 = (((column * mc) + 39), ((line * ml) + 99))
            if lista_of_lines[line][column] == "c" and t3 == 0:
                t3 += 1
                location2 = (((column * mc) + 39), ((line * ml) + 99))
            if lista_of_lines[line][column] == "d" and t4 == 0:
                t4 += 1
                location4 = (((column * mc) + 39), ((line * ml) + 99))
    list_spawn_position = [location1, location2, location3, location4]

    archive.close()
    return list_of_rect, list_spawn_position


def draw_walls(surface, color, rects):
    pygame.draw.rect(surface, color, rects[0])
    pygame.draw.rect(surface, color, rects[1])
    pygame.draw.rect(surface, color, rects[2])
    pygame.draw.rect(surface, color, rects[3])


def victory_texts(font, size):
    victory_text1 = font.render("Red player wins!", True, red, black)
    victory_text2 = font.render("Blue player wins!", True, blue, black)
    victory_text3 = font.render("Yellow player wins!", True, yellow, black)
    victory_text4 = font.render("Purple player wins!", True, purple, black)
    victory_text1_rect = victory_text1.get_rect()
    victory_text2_rect = victory_text2.get_rect()
    victory_text3_rect = victory_text3.get_rect()
    victory_text4_rect = victory_text4.get_rect()
    victory_text1_rect.center = (size[0]/2, 350)
    victory_text2_rect.center = (size[0]/2, 350)
    victory_text3_rect.center = (size[0]/2, 350)
    victory_text4_rect.center = (size[0]/2, 350)
    vc1 = (victory_text1, victory_text1_rect)
    vc2 = (victory_text2, victory_text2_rect)
    vc3 = (victory_text3, victory_text3_rect)
    vc4 = (victory_text4, victory_text4_rect)
    list_vic = [vc1, vc2, vc3, vc4]
    return list_vic


def hud(font):
    hud_text1 = font.render("0", True, red, black)
    hud_text2 = font.render("0", True, blue, black)
    hud_text3 = font.render("0", True, yellow, black)
    hud_text4 = font.render("0", True, purple, black)
    hud_text1_rect = hud_text1.get_rect()
    hud_text2_rect = hud_text2.get_rect()
    hud_text3_rect = hud_text3.get_rect()
    hud_text4_rect = hud_text4.get_rect()
    hud_text1_rect.center = (40, 30)
    hud_text2_rect.center = (370, 30)
    hud_text3_rect.center = (740, 30)
    hud_text4_rect.center = (1110, 30)
    hd1 = [hud_text1, hud_text1_rect]
    hd2 = [hud_text2, hud_text2_rect]
    hd3 = [hud_text3, hud_text3_rect]
    hd4 = [hud_text4, hud_text4_rect]
    list_hud = [hd1, hd2, hd3, hd4]
    return list_hud


def draw_menu1(archive1, archive2, surface, font):
    image1 = pygame.image.load(archive1)
    image1_rect = image1.get_rect()
    image1_rect.center = (355, 350)
    surface.blit(image1, image1_rect)
    image2 = pygame.image.load(archive2)
    image2_rect = image2.get_rect()
    image2_rect.center = (1010, 350)
    surface.blit(image2, image2_rect)
    text = font.render("Stage Select", True, white, black)
    chose1 = font.render("Classic (1)", True, white, black)
    chose2 = font.render("Crossroads (2)", True, white, black)
    text_rect = text.get_rect()
    text_rect.center = (683, 100)
    surface.blit(text, text_rect)
    chose1_rect = chose1.get_rect()
    chose1_rect.center = (355, 183)
    surface.blit(chose1, chose1_rect)
    chose2_rect = chose2.get_rect()
    chose2_rect.center = (1010, 183)
    surface.blit(chose2, chose2_rect)


def draw_menu2(archive1, archive2, archive3, archive4, surface, font):
    list_archive = [archive1, archive2, archive3, archive4]
    x = 273
    for a in range(4):
        photo = pygame.image.load(list_archive[a])
        photo_rect = photo.get_rect()
        photo_rect.center = (x, 350)
        surface.blit(photo, photo_rect)
        x += 273
    text = font.render("N° of players? Press (2) (3) (4)", True, white, black)
    text_rect = text.get_rect()
    text_rect.center = (683, 100)
    surface.blit(text, text_rect)
