from string import ascii_uppercase
from random import choice

def make_grid(columns, rows):
    return {(c,r): choice(ascii_uppercase) 
                        for r in range (rows)   
                            for c in range(columns)}
    
    
#curly brackets for dictionary. (,) tupple is used to find ecact location (eg. row e and column 2 or 20 degrees farenheit).the tupple will represent the key in this dictionary.
 
def potential_neighbours(position):
    c, r = position
    return [(c-1, r-1), (c, r-1),  (c+1, r-1), 
            (c-1, r),              (c+1, r), 
            (c-1, r+1), (c, r+1),  (c+1, r+1)]
 
 
    
# grid = make_grid(2, 2)
# print(grid[(1, 1)]) #1,1 here is the position on a 2x2 grid, hence only one letter is printed.


def path_to_word(path, grid):
    word = ""
    for position in path:
        word += grid[position]
    return word
    
# def load_word_list(filename):
#     with open (filename) as f:
#         text = f.read().split("\n")
#     return text

def get_real_neighbours(grid):
    real_neighbours = {}
    
    for position in grid:
        pn = potential_neighbours(position)
        on_the_grid = [ p for p in pn if p in grid]
        real_neighbours[position] = on_the_grid
    
    return real_neighbours
    

grid = make_grid(3, 3)
rn = get_real_neighbours(grid)
print(rn)
    
    