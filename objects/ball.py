def move_ball(x, y, x_vel, y_vel):
    if x != 490:
        x += x_vel
        y += y_vel
    return (x, y)
