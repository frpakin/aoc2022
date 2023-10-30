from tqdm import tqdm
from collections import defaultdict


def loadData(fname):
    with open(fname, 'r') as fd:
        inputs = [ l.strip() for l in fd ]
    return inputs

def height(v):
    if v=='E':
        return ord('z')
    elif v=='S':
        return ord('a')
    else:
        return ord(v)

shortest = 100000

def lookup(inputs, dest, path):
    global shortest
    ret = {}

    if len(path) < shortest:
        max_l = len(inputs)
        max_c = len(inputs[0])
        pc = path[-1]
        val = height(inputs[pc[0]][pc[1]])
        moves = []
        if pc[0]>0 and val+1 >= height(inputs[pc[0]-1][pc[1]]) : moves.append((pc[0]-1, pc[1]))
        if pc[1]>0 and val+1 >= height(inputs[pc[0]][pc[1]-1]) : moves.append((pc[0], pc[1]-1))
        if pc[0]<max_l-1 and val+1 >= height(inputs[pc[0]+1][pc[1]]) : moves.append((pc[0]+1, pc[1]))
        if pc[1]<max_c-1 and val+1 >= height(inputs[pc[0]][pc[1]+1]) : moves.append((pc[0], pc[1]+1))
        
        ll = [ n for n in moves if n not in path ]
        ll.sort(reverse=True, key=lambda x: height(inputs[x[0]][x[1]]))
        for m in ll:
            if m == dest:
                path.append(m)
                shortest = min(len(path), shortest)
                return len(path)
            else:
                tmp = lookup(inputs, dest, path + [m])
                if tmp != -1:
                    ret[m] = tmp
    return -1 if len(ret)==0 else min(ret.values())


def lookup_A(inputs, dest, path):
    max_l = len(inputs)
    max_c = len(inputs[0])

    came_from = {}
    cost = defaultdict(lambda: 1000000)
    priority = {}
    came_from[path[-1]] = (-1, -1)
    cost[path[-1]] = 0
    priority[path[-1]] = height('z') - height('a')
    while len(path)>0:
        path.sort(key=lambda e:priority[e])
        pc = path[-1]
        path.pop()
        
        val = height(inputs[pc[0]][pc[1]])
        moves = []
        if pc[0]>0 and val+1 >= height(inputs[pc[0]-1][pc[1]]) : moves.append((pc[0]-1, pc[1]))
        if pc[1]>0 and val+1 >= height(inputs[pc[0]][pc[1]-1]) : moves.append((pc[0], pc[1]-1))
        if pc[0]<max_l-1 and val+1 >= height(inputs[pc[0]+1][pc[1]]) : moves.append((pc[0]+1, pc[1]))
        if pc[1]<max_c-1 and val+1 >= height(inputs[pc[0]][pc[1]+1]) : moves.append((pc[0], pc[1]+1))
        
        for m in moves:
            new_cost = cost[pc]+1
            if m not in cost.keys() or new_cost < cost[m]:
                cost[m] = new_cost
                new_priority = new_cost + height('z') - height(inputs[m[0]][m[1]])
                priority[m] = new_priority
                path.append(m)
                came_from[m] = pc
    return cost[dest]


def find(inputs, val):
    l=c=0
    while l<len(inputs):
        c=0
        while c<len(inputs[l]) and inputs[l][c]!=val:
            c += 1
        if c<len(inputs[l]) and inputs[l][c]==val:
            break
        l += 1
    return l,c


def part1(inputs):
    return lookup_A(inputs, find(inputs, 'E'), [find(inputs, 'S')])


def part2(inputs):
    result = {}
    start_list = [ (i,j) for i, l in enumerate(inputs) for j, c in enumerate(l) if c in 'aS' ]        
    for start in tqdm(start_list):
        result[start] = lookup_A(inputs, find(inputs, 'E'), [start])
    return min(result.values())

if __name__ == "__main__":
    inputs = loadData('20221212-t1.txt')
    ret = part1(inputs)
    print(f'Test 1 (31): {ret}')
    inputs = loadData('20221212.txt')
    #ret = part1(inputs)
    print(f'Part 1 (361): {ret}')
    inputs = loadData('20221212-t1.txt')
    ret = part2(inputs)
    print(f'Test 2 (29): {ret}')
    inputs = loadData('20221212.txt')
    ret = part2(inputs)
    print(f'Part 2 (354): {ret}')