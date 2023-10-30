import math
from tqdm import tqdm

def loadData(fname):
    with open(fname, 'r') as fd:
        inputs = [ l.strip() for l in fd ]
    monkeys = {}
    i = 0
    while i<len(inputs):
        id = int(inputs[i].split(' ')[1][:-1])
        items = [ int(v.strip()) for v in inputs[i+1].split(':')[1].split(',') ]
        op = inputs[i+2].split('=')[1].strip()
        test = ( int(inputs[i+3].split(' ')[3]), int(inputs[i+4].split(' ')[5]), int(inputs[i+5].split(' ')[5]))
        monkeys[id] = [op, test, items, len(items)]
        i += 7
    return monkeys


def part1(monkeys):
    inspect = [ 0 for _ in range(len(monkeys)) ]
    for _ in range(20):
        for i, m in enumerate(monkeys.values()):
            while len(m[2])>0:
                item = m[2].pop(0)
                item = eval(m[0], { 'old': item })
                item = int(math.floor(item / 3))
                inspect[i] += 1
                if item % m[1][0] == 0:
                    monkeys[m[1][1]][2].append(item)
                else:
                    monkeys[m[1][2]][2].append(item)
    tmp = sorted(inspect, reverse=True)
    return tmp[0]*tmp[1]


def myeval(l3, old):
    a = old if l3[1] == -1 else l3[1]
    b = old if l3[2] == -1 else l3[2]
    return a+b if l3[0]== '+' else a*b


def part2(monkeys):
    inspect = [ 0 for _ in range(len(monkeys)) ]
    items_val = []
    items_mon = []
    items_loc = []
    mon_run = []
    coef = 1
    for i, m in enumerate(monkeys.values()):
        coef = coef*m[1][0]
        tmp = m[0].split()
        mon_run.append((tmp[1], int(tmp[0]) if tmp[0].isdigit() else -1, int(tmp[2]) if tmp[2].isdigit() else -1))
        for j, w in enumerate(m[2]):
            items_val.append(w)
            items_mon.append(i)
            items_loc.append(j)

    for _ in tqdm(range(10000)):
        age = max(items_loc)+1
        for i, m in enumerate(monkeys.values()):
            
            while True:
                min_loc = age
                min_k = -1

                current = [ k for k, j in enumerate(items_mon) if j==i ]
                for k in current:
                    if items_loc[k] < min_loc:
                        min_loc = items_loc[k]
                        min_k = k
                if min_k ==-1:
                    break

                items_val[min_k] = myeval(mon_run[i], items_val[min_k]) % coef

                inspect[i] += 1
                if items_val[min_k] % m[1][0] == 0:
                    items_mon[min_k] = m[1][1]
                else:
                    items_mon[min_k] = m[1][2]
                items_loc[min_k] = age
                age += 1

    tmp = sorted(inspect, reverse=True)
    return tmp[0]*tmp[1]


    

if __name__ == "__main__":
    inputs = loadData('20221211-t1.txt')
    ret = part1(inputs)
    print(f'Test 1 (10605): {ret}')
    inputs = loadData('20221211.txt')
    ret = part1(inputs)
    print(f'Part 1 (121450): {ret}')

    inputs = loadData('20221211-t1.txt')
    ret = part2(inputs)
    print(f'Test 2 (2713310158): {ret}')
    inputs = loadData('20221211.txt')
    ret = part2(inputs)
    print(f'Part 2 (28244037010): {ret}')

    