def turn_right():
   turn_left()
   turn_left()
   turn_left()

#Change starting point and not fall into the loop
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()

    