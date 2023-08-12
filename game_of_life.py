# Python implementation of Conway's Game of Life


from colorama import Fore, Back, Style
import time


def calc_next_field(field):
    field = field
    rows = len(field)
    coloumns = len(field[0])

    # generate new field
    new_field = []
    for row in range(rows):
        new_field.append([0,] * coloumns)
    
    # add left and right edge
    for row in range(rows):
        field[row].insert(0, field[row][-1])
        field[row].append(field[row][0])

    # add top and bottom edge
    top = []
    bottom = []
    for coloumn in range(coloumns+2):
        top.append(field[0][coloumn])
        bottom.append(field[-1][coloumn])
    field.insert(0, top)
    field.append(bottom)


    # fill the field with new values
    for y in range(1, rows+1):
        for x in range(1, coloumns+1):
            if is_alive(y, x, field):
                new_field[y-1][x-1] = 1
            else:
                new_field[y-1][x-1] = 0
    return new_field
    

def draw_field(field, gen=0):
    if gen != 0:
        width = coloumns * 2 + 2
        print("-" * int((width - 16) / 2), end="")
        print("generation-" + str(gen).zfill(5), end="")
        print("-" * int((width - 16) / 2))
    else:
        width = coloumns * 2 + 2
        print("-" * int((width - 18) / 2), end="")
        print("initial-generation", end="")
        print("-" * int((width - 18) / 2))

    for row in field:
        print("|", end="")
        for coloumn in row:
            if coloumn == 1:
                print(Back.GREEN + "  ", end="")
                print(Style.RESET_ALL, end="")
            else:
                print("  ", end="")
        print("|")
    print("-" * width)


def is_alive(y, x, field):
    count = 0

    for yf in range(-1, 2):
        for xf in range(-1, 2):
            if field[y+yf][x+xf] == 1:
                if yf != 0 and xf != 0:
                    count += 1

    # uncomment the print() statement for debugging
    #print(y, x, count)
    if count <= 1:
        return False
    elif count == 2 or count == 3:
        return True
    else:
        return False


if __name__ == "__main__":

    # define the desired values
    rows = 27
    coloumns = 49
    last_gen = 10

    # generate field
    cur_field = []
    for row in range(rows):
        cur_field.append([0,] * coloumns)

    # define the pattern
    # cur_field[3][1] = 1
    # cur_field[3][2] = 1
    # cur_field[3][3] = 1
    # cur_field[2][3] = 1
    # cur_field[1][2] = 1

    #test corners
    cur_field[0][0] = 1
    cur_field[0][coloumns-1] = 1
    cur_field[rows-1][0] = 1
    cur_field[rows-1][coloumns-1] = 1

    #test shape
    cur_field[rows // 2+1][coloumns // 2] =1
    cur_field[rows // 2][coloumns // 2] =1
    cur_field[rows // 2-1][coloumns // 2] =1

    # print the fields of the generations
    draw_field(cur_field)
    for gen in range(1, last_gen+1):
        time.sleep(0.5)
        print()
        cur_field = calc_next_field(cur_field)
        draw_field(cur_field, gen)


