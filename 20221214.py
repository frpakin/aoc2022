



from collections import defaultdict


def draw(plane, st, en, ty):
    if st[0] == en[0]:
        for i in range(min(st[1],en[1]), 1+max(st[1],en[1])):
            plane[(st[0], i)] = ty
    else:
        for i in range(min(st[0],en[0]), 1+max(st[0],en[0])):
            plane[(i, st[1])] = ty

def loadData(fname):
    plane = defaultdict(lambda: '.')
    data = open(fname).read().strip()
    coords = [ [ tuple(map(int, s.split(","))) for s in p.split("->") ] for p in data.split("\n") ]
    for line in coords:
        for i, p in enumerate(line[1:], 1):
            draw(plane, line[i-1], p, '#')
    return plane


def part1(plane, sand_x=500, sand_y=0):
    sand_maxy = max(y[1] for y in plane.keys())
    x = 0
    y = 0
    while x==0 and y==0 and y<1+sand_maxy:
        while y<1+sand_maxy:
            if plane[(sand_x+x, sand_y+y+1)] == '.':
                y += 1
            else:
                if plane[(sand_x+x-1, sand_y+y+1)] == '.':
                    x += -1
                elif plane[(sand_x+x+1, sand_y+y+1)] == '.':
                    x += 1
                else:
                    plane[(sand_x+x, sand_y+y)] = 'O'
                    x = 0
                    y = 0
                    break
    return len([v for v in plane.values() if v=='O'])


def part2(plane, sand_x=500, sand_y=0):
    sand_maxy = max(y[1] for y in plane.keys())
    sand_floor = 2+sand_maxy
    x = 0
    y = 0
    while True:
        while y<sand_floor:
            if plane[(sand_x+x, sand_y+y+1)] == '.' and sand_y+y+1<sand_floor:
                y += 1
            else:
                if plane[(sand_x+x-1, sand_y+y+1)] == '.' and sand_y+y+1<sand_floor:
                    x += -1
                elif plane[(sand_x+x+1, sand_y+y+1)] == '.' and sand_y+y+1<sand_floor:
                    x += 1
                else:
                    plane[(sand_x+x, sand_y+y)] = 'O'       
                    break
        if x == 0 and y == 0:
            break
        x = 0
        y = 0
    return len([v for v in plane.values() if v=='O'])


if __name__ == "__main__":

    inputs = loadData('20221214-t1.txt')
    ret = part1(inputs)
    print(f'Test 1 (24): {ret}')

    inputs = loadData('20221214.txt')
    ret = part1(inputs)
    print(f'Part 1 (672): {ret}')

    inputs = loadData('20221214-t1.txt')
    ret = part2(inputs)
    print(f'Test 2 (93): {ret}')
    inputs = loadData('20221214.txt')
    ret = part2(inputs)
    print(f'Test 2 (??): {ret}')
