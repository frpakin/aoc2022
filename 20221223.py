from colorama import Fore, Back, Style
import numpy as np

def loaddata(fname):
    data = open(fname, encoding='UTF8').read()
    nb = 0
    for i,l in enumerate(data.split('\n')):
        for j,c in enumerate(l):
            if c=='#':
                nb+=1
    ret = np.zeros((3, nb), dtype=int)
    nb = 0
    for i,l in enumerate(data.split('\n')):
        for j,c in enumerate(l):
            if c=='#':
                ret[0][nb][0], ret[1][nb] = j, i
                nb+=1
    return ret


def display(data):
    for l, s in enumerate(data['map']):
        if l==data['L']:
            s = data['map'][l][:data['C']] + ['>', 'v', '<', '^'] [data['F']] + data['map'][l][data['C']+1:]
        print(s)
    print()


def part1(data, max_rounds=10, debug=False):
    directions = { 0:'N', 1:'S', 2:'W', 3:'E', 4:'X' }
    arretes = [ (0,1,2), (4,5,6), (2,3,4), (0,6,7) ]
    direction = 0
    max_elves = data.dimension()[1]
    neighbors = np.zeros(8, dtype=int)
    for round in range(max_rounds):
        # Plan
        for elf in range(max_elves):
            x, y = data[0][elf], data[1][elf]
            for i in range(8): neighbors[i] = -1
            for neighbor in range(max_elves):
                if elf != neighbor:
                    if data[0][neighbor] == x-1 and data[1][neighbor] == y-1:
                        neighbors[0] = neighbor
                    elif data[0][neighbor] == x and data[1][neighbor] == y-1:
                        neighbors[1] = neighbor
                    elif data[0][neighbor] == x+1 and data[1][neighbor] == y-1:
                        neighbors[2] = neighbor
                    elif data[0][neighbor] == x+1 and data[1][neighbor] == y:
                        neighbors[3] = neighbor
                    elif data[0][neighbor] == x+1 and data[1][neighbor] == y+1:
                        neighbors[4] = neighbor
                    elif data[0][neighbor] == x and data[1][neighbor] == y+1:
                        neighbors[5] = neighbor
                    elif data[0][neighbor] == x-1 and data[1][neighbor] == y+1:
                        neighbors[6] = neighbor
                    elif data[0][neighbor] == x-1 and data[1][neighbor] == y:
                        neighbors[7] = neighbor
            if (neighbors==np.array([-1, -1, -1, -1, -1, -1, -1, -1])).all():
                data[2][elf] = 4
            else:
                for d in range(4):
                    dd = (d+direction)%4
                    if (neighbors[arretes[dd][0]]==-1) and (neighbors[arretes[dd][1]]==-1) and (neighbors[arretes[dd][2]]==-1):
                        data[2][elf] = dd
        # move
        next = np.zeros_like(data)
        for elf in range(max_elves):
            if data[2][elf] == 0:
                next[0][elf], next[1][elf] = data[0][elf], data[1][elf]-1
            elif data[2][elf] == 1:
                next[0][elf], next[1][elf] = data[0][elf], data[1][elf]+1
            elif data[2][elf] == 2:
                next[0][elf], next[1][elf] = data[0][elf]-1, data[1][elf]
            elif data[2][elf] == 3:
                next[0][elf], next[1][elf] = data[0][elf]+1, data[1][elf]
        # collide
        collisions = []
        for elf in range(max_elves):
            for neighbor in range(max_elves):
                if (elf != neighbor) and (next[0][elf]==next[0][neighbor]) and (next[1][elf]==next[1][neighbor]):
                    collisions.append(elf)
                    break
        # move
        for elf in range(max_elves):
            if elf not in collisions:
                data[0][elf], data[1][elf] = next[0][elf], next[1][elf]
        # pivot
        direction = (direction+1) %4
    return 0
    

def part2(data, debug=False):
    return 0


if __name__ == "__main__":
    inputs = loaddata('20221223-t1.txt')
    ret = part1(inputs, debug=True)
    ko_red = Fore.RED + Style.NORMAL + 'KO' + Style.RESET_ALL
    ok_green = Fore.GREEN + Style.NORMAL + 'OK' + Style.RESET_ALL
    print(f'Test 1 (6032): {ret} [{ok_green if ret==6032 else ko_red}]')
    inputs = loaddata('20221222.txt')
    ret = part1(inputs)
    print(f'Part 1 (?): {ret} [{ok_green if ret == 89224 else ko_red}]')

    inputs = loaddata('20221222-t1.txt')
    ret = part2(inputs, debug=True)
    print(f'Test 2 (5031): {ret} [{ok_green if ret==5031 else ko_red}]')
   