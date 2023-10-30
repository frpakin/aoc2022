
def loaddata(fname):
    data = open(fname).read().strip()
    return [ tuple( [ int(t) for t in l.strip().split(',') ] ) for l in data.split('\n') ]


def adjs(c):
    return [(c[0]-1, c[1], c[2]), (c[0]+1, c[1], c[2]), 
            (c[0], c[1]-1, c[2]), (c[0], c[1]+1, c[2]), 
            (c[0], c[1], c[2]-1), (c[0], c[1], c[2]+1)]


def calc(inputs, c):
    return 6-len([d for d in adjs(c) if d in inputs ])


def part1(inputs):
    return sum([calc(inputs, c) for c in inputs ])


def part2(inputs):
    min_c = tuple([ min([c[i] for c in inputs ])-1 for i in range(3) ])
    max_c = tuple([ max([c[i] for c in inputs ])+1 for i in range(3) ])
    surfaced = []
    visited = []
    stacked = [ min_c ]
    while len(stacked)!=0:
        c = stacked.pop()
        visited.append(c)
        for d in [ e for e in adjs(c) if e not in visited ]:
            if d in inputs:
                surfaced.append(c)
            else:
                if all([ d[i]>=min_c[i] and d[i]<=max_c[i] for i in range(3) ]) and d not in stacked:
                    stacked.append(d)
    return len(surfaced)


if __name__ == "__main__":
    inputs = loaddata('20221218-t1.txt')
    ret = part1(inputs)
    print(f'Test 1 (64): {ret}')
    inputs = loaddata('20221218.txt')
    ret = part1(inputs)
    print(f'Part 1 (4604): {ret}')

    inputs = loaddata('20221218-t1.txt')
    ret = part2(inputs)
    print(f'Test 2 (58): {ret}')
    inputs = loaddata('20221218.txt')
    ret = part2(inputs)
    print(f'Part 2 (2604): {ret}')