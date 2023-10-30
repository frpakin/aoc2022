from tqdm import trange
from tqdm import tqdm
from colorama import Fore, Back, Style
import numpy as np


def loaddata(fname):
    data = open(fname, encoding='UTF8').read()
    inputs = [ int(l) for l in data.split('\n') ]
    index = [ np.empty(len(inputs), dtype=np.int32) for _ in range(2) ]
    for i in range(len(inputs)):
        index[0][i] = inputs[i]
        index[1][i] = i
    return index



def index_print(inputs):
    ret = []
    for i in range(len(inputs[0])):
        for j in range(len(inputs[1])):
            if i==inputs[1][j]:
                ret.append(int(inputs[0][j]))
                break
    print(ret)
    #print(inputs[0][inputs[1]])


def part1(inputs, debug=False):
    if debug: index_print(inputs)
    a, b, inc = 0, 0, 0
    len_cycle = len(inputs[0])
    for i in range(len_cycle) if debug else trange(len_cycle):
        pos_init = inputs[1][i]
        pos_target = pos_init + inputs[0][i]
        if pos_target <= 0:
            pos_target = (pos_target-1 + len_cycle) % len_cycle
        elif pos_target >= len_cycle:
            pos_target = (pos_target+1) % len_cycle
        if debug: print(f"Moving {inputs[0][i]} to {pos_target}")
        if pos_init == pos_target:
            continue
        inc = -1 if pos_init < pos_target else 1
        a = min(pos_init, pos_target)
        b = max(pos_init, pos_target)
        for j in range(len_cycle):
            if a <= inputs[1][j] <= b:
                inputs[1][j] += inc
        inputs[1][i] = pos_target
        if debug: index_print(inputs)
    zero_index = int(inputs[1][np.where(inputs[0] == 0)])
    ret = [ inputs[0][int(np.where(inputs[1] == (zero_index+n)%len_cycle)[0])] for n in (1000, 2000, 3000)]
    return sum(ret)
    

if __name__ == "__main__":
    inputs = loaddata('20221220-t1.txt')
    ret = part1(inputs, debug=True)
    ko_red = Fore.RED + Style.NORMAL + 'KO' + Style.RESET_ALL
    ok_green = Fore.GREEN + Style.NORMAL + 'OK' + Style.RESET_ALL
    print(f'Test 1 (3): {ret} [{ok_green if ret==3 else ko_red}]')
    inputs = loaddata('20221220.txt')
    ret = part1(inputs)
    print(f'Part 1 (?): {ret} [{ok_green if ret not in [ -104 ] else ko_red}]')