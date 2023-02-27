from os.path import join
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites, player_sprites, id_num):
        super().__init__(groups)
        self.sprites = []
        self.sprites.append(pygame.image.load(join("sprites", f"slime{id_num}idle.png")))
        self.sprites.append(pygame.image.load(join("sprites", f"slime{id_num}walk.png")))
        self.sprites.append(pygame.image.load(join("sprites", f"slime{id_num}jump.png")))
        self.sprites.append(pygame.image.load(join("sprites", f"slime{id_num}mash.png")))
        self.left_sprites = [pygame.transform.flip(sprite, True, False) for sprite in self.sprites]
        self.right_sprites = self.sprites
        self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]
        self.rect = self.image.get_rect(topleft=pos)
        self.respawn_pos = pos

        # player movement
        self.direction = pygame.math.Vector2()
        self.speed = PLAYER_SPEED
        self.gravity = PLAYER_GRAVITY
        self.jump_speed = PLAYER_JUMP_SPEED
        self.collision_sprites = collision_sprites
        self.player_sprites = player_sprites
        self.player_id = id_num
        self.on_floor = False
        self.move_left = False
        self.move_right = False
        self.jump = False

        # player state
        self.facing = ""
        if self.player_id == 0 or self.player_id == 2:
            self.facing = "right"
        else:
            self.facing = "left"

        self.is_moving = False
        self.on_air = False
        self.is_invincible = False
        self.inv_anim_time = 0
        self.is_dead = False
        self.dead_anim_time = 0

        self.lives = PLAYER_LIVES

    def move(self):
        if not self.is_dead:
            if self.move_left:
                self.direction.x = -1
                self.is_moving = True
                self.facing = "left"
            elif self.move_right:
                self.direction.x = 1
                self.is_moving = True
                self.facing = "right"
            else:
                self.direction.x = 0
                self.is_moving = False

            if self.jump and self.on_floor:
                JUMP_SOUND.play()
                self.direction.y = -self.jump_speed
                self.on_air = True

    def horizontal_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left

        for sprite in self.player_sprites.sprites():
            if sprite.rect.colliderect(self.rect) and sprite.player_id != self.player_id and not sprite.is_dead:
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left

    def vertical_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_floor = True
                    self.on_air = False
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

        for sprite in self.player_sprites.sprites():
            if sprite.rect.colliderect(self.rect) and sprite.player_id != self.player_id \
                    and not sprite.is_dead and not self.is_dead:
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    if not sprite.is_invincible:
                        sprite.is_dead = True
                        HIT_SOUND.play()
                    else:
                        self.on_floor = True
                        self.on_air = False
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = TILE_SIZE
        if self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = 0
        if self.rect.y < 0:
            self.rect.y = SCREEN_HEIGHT

        if self.on_floor and self.direction.y != 0:
            self.on_floor = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def animate(self):
        # invincible mode
        if self.is_invincible:
            self.inv_anim_time += 0.1
            if self.inv_anim_time > PLAYER_INVIS_TIME:
                self.is_invincible = False
                self.inv_anim_time = 0

        # jump animation
        if self.on_air:
            self.current_sprite = 2
        else:
            self.current_sprite = 0

        # death animation
        if self.is_dead:
            self.current_sprite = 3
            self.dead_anim_time += 0.1
            if self.dead_anim_time > PLAYER_DEATH_TIME:
                if self.lives > 0:
                    self.respawn()
                    print("Respawn")
                    self.is_dead = False
                    self.dead_anim_time = 0
                else:
                    self.kill()

    def respawn(self):
        self.lives -= 1
        self.current_sprite = 0
        self.rect = self.image.get_rect(topleft=self.respawn_pos)
        self.direction = pygame.math.Vector2()
        self.is_invincible = True


    def update(self):
        self.move()
        self.animate()
        self.rect.x += self.direction.x * self.speed
        self.horizontal_collisions()
        self.apply_gravity()
        self.vertical_collisions()
        print(self.is_invincible)

        if self.is_moving and not self.on_air:
            self.current_sprite += 1
            if self.current_sprite > 1:
                self.current_sprite = 0

        if self.facing == "left":
            self.sprites = self.left_sprites
        else:
            self.sprites = self.right_sprites

        self.image = self.sprites[int(self.current_sprite)]
        if self.is_invincible:
            self.image.set_alpha(127)
        else:
            self.image.set_alpha(255)

    def get_id(self):
        return self.player_id

    def get_image(self):
        return self.image

    def get_lives(self):
        return self.lives

    def set_move_left(self, boolean):
        self.move_left = boolean

    def set_move_right(self, boolean):
        self.move_right = boolean

    def set_jump(self, boolean):
        self.jump = boolean
