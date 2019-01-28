from random import randint

def make_forest(width, height, density):
    forest = [['_' for x in range(width)] for y in range(height)]
    for _ in range(int(width*height*density)):
        while True:
            x = randint(0, width-1)
            y = randint(0, height-1)
            if forest[x][y] == '_':
                forest[x][y] = '#'
                break
    return (forest)

def print_forest(forest, width, height):
    for x in range(width):
        for y in range(height):
            print(forest[x][y], end=' ')
        print ()
    print()


def burn_cycle(forest, width, height):
    onfire = []
    still_burning = False
    for x in range(width):
        for y in range(height):
            if forest[x][y] == '@':
                onfire.append((x,y),)
    for each_onfire in onfire:
        x, y = each_onfire
        forest[x][y] = 'X'
        if x > 0:
            if forest[x-1][y] == '#':
                forest[x-1][y] = '@'
                still_burning = True
        if x < width -1:
            if forest[x+1][y] == '#':
                forest[x+1][y] = '@'
                still_burning = True
        if y > 0:
            if forest[x][y-1] == '#':
                forest[x][y-1] = '@'
                still_burning = True
        if y < height -1:
            if forest[x][y+1] == '#':
                forest[x][y+1] = '@'
                still_burning = True
    return (forest, still_burning)

width = 10
height = 10
density = 0.6
forest = make_forest(width, height, density)
forest[randint(0,width-1)][randint(0,height-1)] = '@'
still_burning = True
print_forest(forest, width, height)
cycles = 0
while still_burning:
    forest, still_burning = burn_cycle(forest, width, height)
    cycles += 1
print_forest(forest, width, height)
print (cycles)

