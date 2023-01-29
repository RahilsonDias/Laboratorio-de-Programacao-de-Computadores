def tank_collision(obj, other_obj):
    if obj.get_rect().colliderect(other_obj.get_rect()):
        if abs(obj.get_rect().top - other_obj.get_rect().bottom) < 5:
            obj.set_top_collision(True)
            print("collide top")
        if abs(obj.get_rect().bottom - other_obj.get_rect().top) < 5:
            obj.set_bottom_collision(True)
            print("collide bottom")
        if abs(obj.get_rect().right - other_obj.get_rect().left) < 5:
            obj.set_right_collision(True)
            print("collide right")
        if abs(obj.get_rect().left - other_obj.get_rect().right) < 5:
            obj.set_left_collision(True)
            print("collide left")

    else:
        obj.set_top_collision(False)
        obj.set_bottom_collision(False)
        obj.set_right_collision(False)
        obj.set_left_collision(False)


def wall_collision(obj, rect):
    if obj.get_rect().colliderect(rect):
        if abs(obj.get_rect().top - rect.bottom) < 5:
            obj.set_top_collision(True)
            print("collide top")
            print(obj.top_collision)
        if abs(obj.get_rect().bottom - rect.top) < 5:
            obj.set_bottom_collision(True)
            print("collide bottom")
        if abs(obj.get_rect().right - rect.left) < 5:
            obj.set_right_collision(True)
            print("collide right")
        if abs(obj.get_rect().left - rect.right) < 5:
            obj.set_left_collision(True)
            print("collide left")

    else:
        obj.set_top_collision(False)
        obj.set_bottom_collision(False)
        obj.set_right_collision(False)
        obj.set_left_collision(False)
