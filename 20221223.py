from collections import defaultdict
from colorama import Fore, Style
import numpy as np


def load_data(fname):
    data = open(fname, encoding='UTF8').read()
    nb = sum([ c=='#' for l in data.split('\n') for c in l ])
    ret = np.zeros((5, nb), dtype=int)
    nb = 0
    for i,l in enumerate(data.split('\n')):
        for j,c in enumerate(l):
            if c=='#':
                ret[0][nb] = j
                ret[1][nb] = i
                nb+=1
    return ret


def display(data, ite=-1):
    min_x, max_x = data[0].min(), data[0].max()
    min_y, max_y = data[1].min(), data[1].max()
    max_elves = data.shape[1]
    print('== Initial State ==' if ite==-1 else f'-- End of Round {ite} ==')
    for y in range(min_y, max_y+1):
        l = []
        for x in range(min_x, max_x+1):
            found = False
            for k in range(max_elves):
                if data[1][k]==y and data[0][k]==x:
                    found = True
                    break
            l.append(Fore.LIGHTGREEN_EX+'#'+Style.RESET_ALL if found else '.')
        print(''.join(l))
    print()


def part_1(data, max_rounds=10, debug=False):
    ret1, ret2 = -1, 1
    directions = { 0: (0,-1), 1:(0,1), 2:(-1,0), 3:(1,0), 4:(0,0) } #xy
    square = [ (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1) ] #xy
    arretes = [ [0,1,2], [4,5,6], [0,6,7], [2,3,4] ]
    direction = 0
    max_elves = data.shape[1]
    available = np.ones((max_elves, 8), dtype=bool)

    if debug:
        display(data)
    #for _ in range(max_rounds) if debug else trange(max_rounds):
    while True:
        # build 2D World
        min_x, max_x = data[0].min(), data[0].max()
        min_y, max_y = data[1].min(), data[1].max()
        world = np.ones((3+max_y-min_y, 3+max_x-min_x), dtype=bool) # LC
        for elf in range(max_elves):
            world[1+data[1][elf]-min_y][1+data[0][elf]-min_x] = False
        # Plan evaluate neighborhood
        available.fill(True)
        for elf in range(max_elves):
            x, y = data[0][elf], data[1][elf]
            for i, ee in enumerate(square):
                available[elf][i] = world[1+y+ee[0]-min_y][1+x+ee[1]-min_x]
        # Plan choose direction  
        data[2].fill(4)
        for elf in range(max_elves):
            if not available[elf].all(): 
                for d in range(4):
                    dd = (d+direction)%4
                    if available[elf][arretes[dd]].all():
                        data[2][elf] = dd
                        break      
        # move / no move ?
        for elf in range(max_elves):
            data[3][elf] = data[0][elf]+directions[data[2][elf]][0]
            data[4][elf] = data[1][elf]+directions[data[2][elf]][1]
        # collide
        collisions = defaultdict(list)
        for elf in range(max_elves):
            collisions[(data[3][elf], data[4][elf])].append(elf)
        # move
        has_moved = False
        for elf in range(max_elves):
            if len(collisions[(data[3][elf], data[4][elf])])==1:
                data[0][elf], data[1][elf] = data[3][elf], data[4][elf]
                if data[2][elf] != 4:
                    has_moved = True
        if debug:
            display(data, ret2+1)
        if not has_moved:
            break
        # pivot
        direction = (direction+1)%4
        if ret2 == max_rounds:
            ret1 = (1+np.max(data[0])-np.min(data[0])) * (1+np.max(data[1])-np.min(data[1])) - max_elves
        ret2 += 1
    if ret1 == -1:
        ret1 = (1+np.max(data[0])-np.min(data[0])) * (1+np.max(data[1])-np.min(data[1])) - max_elves
    return ret1, ret2

if __name__ == "__main__":
    ko_red = Fore.RED + Style.NORMAL + 'KO' + Style.RESET_ALL
    ok_green = Fore.GREEN + Style.NORMAL + 'OK' + Style.RESET_ALL
    inputs = load_data('20221223-t2.txt')
    RET1, RET2 = part_1(inputs, debug=True)
    print(f'Test 2P1 (25): {RET1} [{ok_green if RET1==25 else ko_red}]')
    print(f'Test 2P2 (4): {RET2} [{ok_green if RET2==4 else ko_red}]')
    inputs = load_data('20221223-t1.txt')
    RET1, RET2 = part_1(inputs, debug=False)
    print(f'Test 1P1 (110): {RET1} [{ok_green if RET1==110 else ko_red}]')
    print(f'Test 1P2 (20):  {RET2} [{ok_green if RET2==20 else ko_red}]')
    inputs = load_data('20221223.txt')
    RET1, RET2 = part_1(inputs)
    print(f'Part 1 (3800): {RET1} [{ok_green if RET1 == 3800 else ko_red}]')
    print(f'Part 2 (916): {RET2} [{ok_green if RET2==916 else ko_red}]')