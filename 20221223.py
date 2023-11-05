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
    ret = np.zeros((3, nb), dtype=int)
    nb = 0
    for i,l in enumerate(data.split('\n')):
        for j,c in enumerate(l):
            if c=='#':
                ret[0][nb] = j
                ret[1][nb] = i
                nb+=1
    return ret


def display(data, ite=-1):
    min_x = data[0].min()
    max_x = data[0].max()
    min_y = data[1].min()
    max_y = data[1].max()
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
    # directions = { 0:'N', 1:'S', 2:'W', 3:'E', 4:'X' }
    arretes = [ (0,1,2), (4,5,6), (0,6,7), (2,3,4) ]
    direction = 0
    max_elves = data.shape[1]
    neighbors = np.zeros(8, dtype=int)
    if debug:
        display(data)
    for _ in range(max_rounds) if debug else trange(max_rounds):
        # Plan
        for elf in range(max_elves):
            x, y = data[0][elf], data[1][elf]
            for i in range(8):
                neighbors[i] = -1
            for neighbor in range(max_elves):
                if elf != neighbor:
                    if data[0][neighbor] == x-1 and data[1][neighbor] == y-1:   # NW
                        neighbors[0] = neighbor
                    elif data[0][neighbor] == x and data[1][neighbor] == y-1:   # N
                        neighbors[1] = neighbor
                    elif data[0][neighbor] == x+1 and data[1][neighbor] == y-1: # NE
                        neighbors[2] = neighbor
                    elif data[0][neighbor] == x+1 and data[1][neighbor] == y:   # E
                        neighbors[3] = neighbor
                    elif data[0][neighbor] == x+1 and data[1][neighbor] == y+1: # SE
                        neighbors[4] = neighbor
                    elif data[0][neighbor] == x and data[1][neighbor] == y+1:   # S
                        neighbors[5] = neighbor
                    elif data[0][neighbor] == x-1 and data[1][neighbor] == y+1: # SW
                        neighbors[6] = neighbor
                    elif data[0][neighbor] == x-1 and data[1][neighbor] == y:   # W
                        neighbors[7] = neighbor
            if (neighbors==np.array([-1, -1, -1, -1, -1, -1, -1, -1])).all():
                data[2][elf] = 4
            else:
                found = False
                for d in range(4):
                    dd = (d+direction)%4
                    if all( [neighbors[arretes[dd][_]]==-1 for _ in range(3)] ):
                        data[2][elf] = dd
                        found = True
                        break
                if not found:
                    data[2][elf] = 4
        # no move ?
        if all([data[2][elf] == 4 for elf in range(max_elves)]):
            break
        # next move
        next_pos = np.zeros_like(data)
        for elf in range(max_elves):
            if data[2][elf] == 0:
                next_pos[0][elf], next_pos[1][elf] = data[0][elf], data[1][elf]-1
            elif data[2][elf] == 1:
                next_pos[0][elf], next_pos[1][elf] = data[0][elf], data[1][elf]+1
            elif data[2][elf] == 2:
                next_pos[0][elf], next_pos[1][elf] = data[0][elf]-1, data[1][elf]
            elif data[2][elf] == 3:
                next_pos[0][elf], next_pos[1][elf] = data[0][elf]+1, data[1][elf]
            else:
                next_pos[0][elf], next_pos[1][elf] = data[0][elf], data[1][elf]
        # collide
        collisions = []
        for elf in range(max_elves):
            for neighbor in range(max_elves):
                if (elf != neighbor) and all([next_pos[_][elf]==next_pos[_][neighbor] for _ in range(2)]):
                    collisions.append(elf)
                    break
        # move
        for elf in range(max_elves):
            if elf not in collisions:
                data[0][elf], data[1][elf] = next_pos[0][elf], next_pos[1][elf]
        # pivot
        direction = (direction+1)%4
        # print
        if debug:
            display(data, _+1)
    return (1+np.max(data[0])-np.min(data[0])) * (1+np.max(data[1])-np.min(data[1])) - max_elves


def part_2(data, debug=False):
    if debug:
        display(data)
    return 0


if __name__ == "__main__":
    ko_red = Fore.RED + Style.NORMAL + 'KO' + Style.RESET_ALL
    ok_green = Fore.GREEN + Style.NORMAL + 'OK' + Style.RESET_ALL
    inputs = load_data('20221223-t2.txt')
    RET = part_1(inputs, debug=False)
    print(f'Test 2 (25): {RET} [{ok_green if RET==25 else ko_red}]')
    inputs = load_data('20221223-t1.txt')
    RET = part_1(inputs, debug=False)
    print(f'Test 1 (110): {RET} [{ok_green if RET==110 else ko_red}]')
    inputs = load_data('20221222.txt')
    RET = part_1(inputs)
    print(f'Part 1 (?): {RET} [{ok_green if RET == 0 else ko_red}]')
    # ko 29344
    #inputs = load_data('20221222-t1.txt')
    #RET = part_2(inputs, debug=True)
    #print(f'Test 2 (5031): {RET} [{ok_green if RET==5031 else ko_red}]')
   