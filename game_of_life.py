# Python implementation of Conway's Game of Life

print("Hello, World!")
def is_alive(y, x):
    count = 0
    for yf in range(-1, 2):
        for xf in range(-1, 2):
            print(yf,xf)
  
            if field[y+yf][x+xf] == 1:
                if yf != 0 and xf != 0:
                    count += 1
                
    if count <= 1:
        return False
    elif count == 2 or count == 3:
        return True
    elif count > 3:
        return False
print(is_alive(1,1))

    