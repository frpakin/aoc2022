from collections import defaultdict
from itertools import permutations
from colorama import Fore, Style
import numpy as np
from tqdm import trange

def load_data(fname):
    data = open(fname, encoding='UTF8').read()
    nb = 0
    for l in data.split('\n'):
        for c in l:
            if c=='#':
                nb+=1
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
            l.append('#' if found else '.')
        print(''.join(l))
    print()


def part_1(data, max_rounds=10, debug=False):
    ret1, ret2 = -1, 1
    # directions = { 0:'N', 1:'S', 2:'W', 3:'E', 4:'X' }
    inc = { 0:(0,-1), 1:(0,1), 2:(-1,0), 3:(1,0), 4:(0,0) }
    arretes = [ [0,1,2], [4,5,6], [0,6,7], [2,3,4] ]
    direction = 0
    max_elves = data.shape[1]
    available = np.ones((max_elves, 8), dtype=bool)
    if debug:
        display(data)
    #for _ in range(max_rounds) if debug else trange(max_rounds):
    while True:
        # Plan evaluate neighborhood
        available.fill(True)
        for elf, neighbor in permutations(range(max_elves), 2):
            x, y = data[0][elf], data[1][elf]
            if data[0][neighbor] == x-1 and data[1][neighbor] == y-1:   # NW
                available[elf][0], available[neighbor][4] = False, False
            elif data[0][neighbor] == x and data[1][neighbor] == y-1:   # N
                available[elf][1], available[neighbor][5] = False, False
            elif data[0][neighbor] == x+1 and data[1][neighbor] == y-1: # NE
                available[elf][2], available[neighbor][6] = False, False
            elif data[0][neighbor] == x+1 and data[1][neighbor] == y:   # E
                available[elf][3], available[neighbor][7] = False, False
            elif data[0][neighbor] == x+1 and data[1][neighbor] == y+1: # SE
                available[elf][4] , available[neighbor][0] = False, False
            elif data[0][neighbor] == x and data[1][neighbor] == y+1:   # S
                available[elf][5], available[neighbor][1] = False, False
            elif data[0][neighbor] == x-1 and data[1][neighbor] == y+1: # SW
                available[elf][6], available[neighbor][2] = False, False
            elif data[0][neighbor] == x-1 and data[1][neighbor] == y:   # W
                available[elf][7], available[neighbor][3] = False, False
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
            data[3][elf], data[4][elf] = data[0][elf]+inc[data[2][elf]][0], data[1][elf]+inc[data[2][elf]][1]
        # collide
        collisions = defaultdict(list)
        for elf in range(max_elves):
            collisions[(data[3][elf], data[4][elf])].append(elf)
        # move
        has_moved = False
        for elf in range(max_elves):
            if len(collisions[(data[3][elf], data[4][elf])])<=1:
                data[0][elf], data[1][elf] = data[3][elf], data[4][elf]
                if data[2][elf] != 4:
                    has_moved = True
            #else:
            #    print(f'{elf} - collisions[({next_pos[0][elf]}, {next_pos[1][elf]})] = {collisions[(next_pos[0][elf], next_pos[1][elf])]}')
        if not has_moved:
            break


        # pivot
        direction = (direction+1)%4
        # print
        if debug:
            display(data, ret2+1)
        if ret2 == max_rounds:
            ret1 = (1+np.max(data[0])-np.min(data[0])) * (1+np.max(data[1])-np.min(data[1])) - max_elves
        ret2 += 1
    if ret1 == -1:
        ret1 = (1+np.max(data[0])-np.min(data[0])) * (1+np.max(data[1])-np.min(data[1])) - max_elves
    return ret1, ret2


def part_2(data, debug=False):
    if debug:
        display(data)
    return 0


if __name__ == "__main__":
    ko_red = Fore.RED + Style.NORMAL + 'KO' + Style.RESET_ALL
    ok_green = Fore.GREEN + Style.NORMAL + 'OK' + Style.RESET_ALL
    inputs = load_data('20221223-t2.txt')
    RET1, RET2 = part_1(inputs, debug=False)
    print(f'Test 2P1 (25): {RET1} [{ok_green if RET1==25 else ko_red}]')
    print(f'Test 2P2 (4): {RET2} [{ok_green if RET2==4 else ko_red}]')
    inputs = load_data('20221223-t1.txt')
    RET1, RET2 = part_1(inputs, debug=False)
    print(f'Test 1P1 (110): {RET1} [{ok_green if RET1==110 else ko_red}]')
    print(f'Test 1P2 (20):  {RET2} [{ok_green if RET2==20 else ko_red}]')
    inputs = load_data('20221223.txt')
    RET1, RET2 = part_1(inputs)
    print(f'Part 1 (3800): {RET1} [{ok_green if RET1 == 3800 else ko_red}]')
    print(f'Part 2 (????): {RET2} [{ok_green if RET2==0 else ko_red}]')
    # ko 29344
    
   