from collections import defaultdict
import math


def loadData(fname):
    with open(fname, 'r') as fd:
        inputs = [ tuple([ int(ll) if i==1 else ll for i, ll in enumerate(l.strip().split()) ]) for l in fd ]
    return inputs


def processH(head, inc):
    return head[0] + inc[0], head[1] + inc[1]


def processT(head, tail):
    if abs(head[1]-tail[1])<2 and abs(head[0]-tail[0])<2:
        return tail
    else:
        tinc = [0,0]
        for i in range(2):
            tinc[i] = int(math.copysign(min(1, abs(head[i] - tail[i])), head[i] - tail[i]))
        return tail[0] + tinc[0], tail[1] + tinc[1]

def part1(inputs):
    head = (0,0)
    tail = (0,0)
    moves = { 'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0) }
    world = {}
    world[tail]=1
    for cmds in inputs:
        for _ in range(cmds[1]):
            head = processH(head, moves[cmds[0]])
            tail = processT(head, tail)
            world[tail]=1
    return len(world)


def display(world):
    bl = ( min ([p[0] for p in world]), min ([p[1] for p in world]))
    tr = ( max ([p[0] for p in world]), max ([p[1] for p in world]))
    max_ll = 1 + tr[0] - bl[0]
    max_cc = 1 + tr[1] - bl[1]
    print("".join([ '-' for _ in range(max_cc) ]))
    for ll in range(max_ll):
        line = ""
        for cc in range(max_cc):
            l = bl[0]+ll
            c = bl[1]+cc
            if l==0 and c==0:
                line += 's'
            elif (l,c) in world:
                line += '#'
            else:
                line += '.'
        print(line)


def part2(inputs, ropelength=10):
    moves = { 'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0) }
    rope = [ (0,0) for _ in range(ropelength)]
    world = []
        
    for cmds in inputs:
        for _ in range(cmds[1]):
            for i, node in enumerate(rope):
                rope[i] = processH(node, moves[cmds[0]]) if i==0 else processT(rope[i-1], node)
            world.append(rope[-1])
    #display(world)
    return len(set(world))

if __name__ == "__main__":
    inputs = loadData('20221209-t1.txt')
    ret = part1(inputs)
    print(f'Test 1 (13): {ret}')
    inputs = loadData('20221209.txt')
    ret = part1(inputs)
    print(f'Part 1 (5960): {ret}')
    inputs = loadData('j-day9.txt')
    ret = part1(inputs)
    print(f'Part 1 (6357): {ret}')

    inputs = loadData('20221209-t2.txt')
    ret = part2(inputs)
    print(f'Test 2 (36): {ret}')
    inputs = loadData('20221209.txt')
    ret = part2(inputs)
    print(f'Part 2 (2327): {ret}')
    inputs = loadData('j-day9.txt')
    ret = part2(inputs)
    print(f'Part 2 (???): {ret}')