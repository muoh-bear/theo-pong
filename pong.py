# import pygame module in this program
from objects.ball import move_ball

import pygame

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension..e(500, 500).
win = pygame.display.set_mode((500, 500))

# set the pygame window name
pygame.display.set_caption("Theo's PONG!!")

# object current co-ordinates
ball_x = 200
ball_y = 200

# dimensions of the object
ball_width = 10
ball_height = 10

# velocity / speed of movement
ball_x_vel = 0
ball_y_vel = 0

# left bar
left_bar_width = 5
left_bar_height = 100
left_bar_y = 20
left_bar_x = 10
left_bar_colour = (0, 0, 255)
left_bar_vel = 10

# right bar
right_bar_width = 5
right_bar_height = 100
right_bar_y = 20
right_bar_x = 480
right_bar_colour = (255, 0, 0)
right_bar_vel = 10
# Indicates pygame is running
run = True

# infinite loop
while run:
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # it will make exit the while loop
            run = False

    # creates time delay of 20ms
    pygame.time.delay(100)

    # stores keys pressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and right_bar_y == 20 and left_bar_y == 20:
        if ball_x_vel == 0:
            ball_x_vel = 5
        ball_x_vel = -5
    if ball_x == 0:
        print("Red Team Won!!!")
        pygame.time.delay(5000)
        break
    if ball_x == 490:
        print("Blue Team Won!!!")
        pygame.time.delay(5000)
        break
    if keys[pygame.K_v]:
        ball_x_vel -= 1
    if keys[pygame.K_b]:
        ball_x_vel += 1
    (ball_x, ball_y) = move_ball(ball_x, ball_y, ball_x_vel, ball_y_vel)

    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and ball_x > 0:
        pass

    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and ball_x < 500 - ball_width:
        pass

    # if left arrow key is pressed
    if keys[pygame.K_UP] and ball_y > 0:
        pass

    # if left arrow key is pressed
    if keys[pygame.K_DOWN] and ball_y < 500 - ball_height:
        pass

    if keys[pygame.K_w] and left_bar_y > 0:
        left_bar_y -= left_bar_vel

    if keys[pygame.K_s] and left_bar_y < 500 - left_bar_height:
        left_bar_y += left_bar_vel

    if keys[pygame.K_UP] and right_bar_y > 0:
        right_bar_y -= right_bar_vel

    if keys[pygame.K_DOWN] and right_bar_y < 500 - right_bar_height:
        right_bar_y += right_bar_vel
    # completely fill the surface object
    # with black colour
    win.fill((0, 255, 0))

    # drawing object on screen which is rectangle here
    pygame.draw.rect(win, (255, 0, 0), (ball_x, ball_y, ball_width, ball_height))

    # draw line on right side
    pygame.draw.rect(
        win, left_bar_colour, (left_bar_x, left_bar_y, left_bar_width, left_bar_height)
    )
    pygame.draw.rect(
        win,
        right_bar_colour,
        (right_bar_x, right_bar_y, right_bar_width, right_bar_height),
    )

    # it refreshes the window
    pygame.display.update()

# closes the pygame window
pygame.quit()
