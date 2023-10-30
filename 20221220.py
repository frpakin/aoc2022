from tqdm import trange
from tqdm import tqdm
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
    print(inputs[0][inputs[1]])


def part1(inputs):
    a, b, inc = 0, 0, 0
    len_cycle = len(inputs[0])
    for i in trange(len_cycle):
        # index_print(inputs)
        pos_init = inputs[1][i]
        if pos_init + inputs[0][i] < 0:
            pos_target = (pos_init + inputs[0][i]-1 + len_cycle) % len_cycle
        elif pos_init + inputs[0][i] > len_cycle:
            pos_target = (pos_init + inputs[0][i]+1 + len_cycle) % len_cycle
        else:
            pos_target = (pos_init + inputs[0][i] + len_cycle) % len_cycle
        if pos_init == pos_target:
            continue
        if pos_init < pos_target and inputs[0][i] > 0:
            a, b, inc = pos_init, pos_target+1, -1
        elif pos_init > pos_target and inputs[0][i] > 0:
            a, b, inc = pos_target-1, pos_init, 1
        elif pos_init < pos_target and inputs[0][i] < 0:
            a, b, inc = pos_init, pos_target+1, -1
        elif pos_init > pos_target and inputs[0][i] < 0:
            a, b, inc = pos_target-1, pos_init, 1
        for j in range(len_cycle):
            if a < inputs[1][j] < b:
                inputs[1][j] += inc
        inputs[1][i] = pos_target
    zero_index = inputs[1][np.where(inputs[0] == 0)]
    thou_index = (zero_index+1000)%len_cycle
    twot_index = (zero_index+2000)%len_cycle
    thre_index = (zero_index+3000)%len_cycle
    return inputs[0][thou_index] + inputs[0][twot_index] + inputs[0][thre_index]


if __name__ == "__main__":
    inputs = loaddata('20221220-t1.txt')
    ret = part1(inputs)
    print(f'Test 1 (3): {ret}')
    #inputs = loaddata('20221220.txt')
    #ret = part1(inputs)
    #print(f'Part 1 (???): {ret}')