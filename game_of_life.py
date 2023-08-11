# Python implementation of Conway's Game of Life


from colorama import Fore, Back, Style
import time


def calc_next_field(field):
    new_field = [[0,] * len(field[0]),] * len(field) 

    for rowi in range(len(field)):
        for coloumni in range(0, len(field[rowi])):
            if False:
                new_field[rowi][coloumni] = 1

    new_field = field
    return new_field
    

def draw_field(field, gen):
    width = coloumns * 2 + 2
    print("-" * int((width - 16) / 2), end="")
    print("Generation-" + str(gen).zfill(5), end="")
    print("-" * int((width - 16) / 2))
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


if __name__ == "__main__":

    # define the desired values
    rows = 10
    coloumns = 10
    gens = 10

    # generate field
    cur_field = []
    for row in range(rows):
        cur_field.append([0,] * coloumns)

    # define the pattern
    cur_field[3][8] = 1

    # print the fields of the generations
    for gen in range(gens):
        draw_field(cur_field, gen)
        cur_field = calc_next_field(cur_field)


print("Hello, World!")
