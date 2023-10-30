from functools import reduce
from operator import mul


def loadData(fname):
    with open(fname, 'r') as fd:
        inputs = [ list(map(int, ll)) for ll in [ l.strip() for l in fd ] ]
    return inputs


def visible(trees, l, c):
    max_l = len(trees)
    max_c = len(trees[0])
    val = trees[l][c]
    n = [ trees[ll][c] for ll in range(l) ]
    s = [ trees[ll][c] for ll in range(l+1, max_l) ]
    e = [ trees[l][cc] for cc in range(c+1, max_c) ]
    w = [ trees[l][cc] for cc in range(c) ]
    return val > max(n) or val > max(s) or val > max(e) or val > max(w)


def part1(trees):
    max_l = len(trees)
    max_c = len(trees[0])
    ret = 0
    for l, line in enumerate(trees):
        for c, column in enumerate(line):
            if l==0 or c==0 or l==max_l-1 or c==max_c-1:
                ret += 1
            elif visible(trees, l, c):
                ret += 1
    return ret


def scenic(trees, l, c):

    def sub(line, v):
        sl = 0
        while sl<len(line) and v>line[sl]:
            sl +=1
        if sl<len(line):
            sl +=1
        return sl

    max_l = len(trees)
    max_c = len(trees[0])
    val = trees[l][c]
    n = [ trees[ll][c] for ll in range(l-1, -1, -1) ]
    s = [ trees[ll][c] for ll in range(l+1, max_l) ]
    e = [ trees[l][cc] for cc in range(c+1, max_c) ]
    w = [ trees[l][cc] for cc in range(c-1, -1, -1) ]
    return reduce(mul, map(lambda x: sub(x, val), [s, n, e, w]))
    

def part2(trees):
    max_l = len(trees)
    max_c = len(trees[0])
    scores = {}
    for l, line in enumerate(trees):
        for c, column in enumerate(line):
            if l==0 or c==0 or l==max_l-1 or c==max_c-1:
                scores[(l,c)] = 0
            else:
                scores[(l,c)] = scenic(trees, l, c)
    return max(scores.values())


if __name__ == "__main__":
    trees = loadData('20221208-t1.txt')
    ret = part1(trees)
    print(f'Test 1 (21): {ret}')
    trees = loadData('20221208-t1.txt')
    ret = scenic(trees, 1, 2)
    print(f'Test 2 (4): {ret}')
    ret = scenic(trees, 3, 2)
    print(f'Test 2 (8): {ret}')
    ret = part2(trees)
    print(f'Test 2 (8): {ret}')

    trees = loadData('20221208.txt')
    ret = part1(trees)
    print(f'Part 1 (1715): {ret}')
    trees = loadData('20221208.txt')
    ret = part2(trees)
    print(f'Part 2 (374400): {ret}')