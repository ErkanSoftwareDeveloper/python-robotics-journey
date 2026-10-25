distance = 40
speed = 5

while distance >= 0:

    if distance < 20:
        speed = 0
        print("The robot is stopped.", distance)
        break

    else:
        speed = 5
        print("The robot is moving.", distance)
        distance -= 5
