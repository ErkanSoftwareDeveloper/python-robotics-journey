distance = 40
speed = 5


def stop_robot(distance):
    print("Robot is stopped. Distance:", distance)


def move_robot(distance):
    print("Robot is moving. Distance:", distance)


while distance >= 0:

    if distance < 20:
        speed = 0
        stop_robot(distance)
        break

    else:
        move_robot(distance)
        distance -= speed
