import numpy as np

with open("input.txt", encoding='utf8') as f:
    grids = []
    for line in f:
        grids.append([int(i) for i in line.strip().split(" ")])
    #print(grids)

