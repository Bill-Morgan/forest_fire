from random import randint

def make_forest(width, height, density):
    forest = [['_' for x in range(width)] for y in range(height)]    
    for x in range(width):
        for y in range(height):
            if density*10 >= randint(1,10):
                forest[x][y] = '#'
    return (forest)


def print_forest(forest, width, height):
    for x in range(width):
        for y in range(height):
            print(forest[x][y], end=' ')
        print ()
    print()


def burn_cycle(bc_forest, width, height):
    onfire = []
    burn_count = 0
    for x in range(width):
        for y in range(height):
            if bc_forest[x][y] == '@':
                onfire.append((x,y),)
    for each_onfire in onfire:
        x, y = each_onfire
        bc_forest[x][y] = 'X'
        if x > 0:
            if bc_forest[x-1][y] == '#':
                bc_forest[x-1][y] = '@'
                burn_count += 1
        if x < width -1:
            if bc_forest[x+1][y] == '#':
                bc_forest[x+1][y] = '@'
                burn_count += 1
        if y > 0:
            if bc_forest[x][y-1] == '#':
                bc_forest[x][y-1] = '@'
                burn_count += 1
        if y < height -1:
            if bc_forest[x][y+1] == '#':
                bc_forest[x][y+1] = '@'
                burn_count += 1
    return (bc_forest, burn_count)

def burn_it_down(bid_forest, width, height):
    cycle_burn_count = True
    burn_count = 0
    cycles = 0
    while cycle_burn_count:
        bid_forest, cycle_burn_count = burn_cycle(bid_forest, width, height)
        cycles += 1
        burn_count += cycle_burn_count
    return (cycles, burn_count)

def most_lethal(ml_forest, width, height):
    largest_fire = [0,0,0]
    most_burned_trees = [0,0,0]
    for x in range(width):
        for y in range(height):
            forest_copy = ml_forest.copy()
            forest_copy[x][y] = '@'
            fire_size, trees_burned = burn_it_down(forest_copy, width, height)
            print_forest(ml_forest, width, height)
            print_forest(forest_copy, width, height)
            if fire_size > largest_fire[2]:
                largest_fire[0] = x
                largest_fire[1] = y
                largest_fire[2] = fire_size
            if trees_burned > most_burned_trees[2]:
                most_burned_trees[0] = x
                most_burned_trees[0] = y
                most_burned_trees[2] = trees_burned
    print(largest_fire, most_burned_trees)

if __name__ == "__main__":
    width = 10
    height = 10
    density = 0.7
    forest = make_forest(width, height, density)
    print_forest(forest, width, height)
    most_lethal(forest, width, height)
    print_forest(forest, width, height)
    #forest[randint(0,width-1)][randint(0,height-1)] = '@'
    #print_forest(forest, width, height)
    #print (burn_it_down(forest,width,height))
    #print_forest(forest, width, height)

