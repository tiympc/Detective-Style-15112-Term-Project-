import random
# made the strings spawn in random points
def randomPoints():
    zeroXorY = random.choice(["x", "y"])
    if zeroXorY == "x":
        x = 0
        y = random.randint(-80, 600 + 80)
    else:
        x = random.randint(-80, 800 + 80)
        if 300 < x < 500:
            randomPoints()
        y = 0
    return (x, y)
