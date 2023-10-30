from tqdm import tqdm


def loadData(fname):
    data = open(fname).read().strip()
    return [ [ [ int(c.strip().split('=')[1]) for c in b.split(',') ] for b in l[10:].split(': closest beacon is at ') ] for l in data.split("\n") ]


def part1(input, y):
    dist = [ abs(d[0][0]-d[1][0])+abs(d[0][1]-d[1][1])  for d in input ]
    scans = []
    for i, d in enumerate(input):
        if d[0][1] - dist[i] <= y <= d[0][1] + dist[i]:
            avail = dist[i] - abs(y-d[0][1])
            scans.append( (d[0][0]-avail, d[0][0]+avail) )

    scans.sort(key=lambda s:s[0])
    ret = scans[0][1]-scans[0][0]
    min_x = scans[0][0]
    max_x = scans[0][1]
    for i,s in enumerate(scans[1:], 1):
        if min_x <= s[0] <= max_x:
            if min_x <= s[1] <= max_x:
                pass
            else:
                ret += s[1]-max_x
                max_x = s[1]
        else:
            ret += s[1]-s[0]
            min_x = s[0]
            max_x = s[1]
    return ret


def part2(input, min_xy=0, max_xy=20):
    rez = []
    dist = [ abs(d[0][0]-d[1][0])+abs(d[0][1]-d[1][1])  for d in input ]
    for y in tqdm(range(max_xy)):
        scans = []
        for i, d in enumerate(input):
            if d[0][1] - dist[i] <= y <= d[0][1] + dist[i]:
                avail = dist[i] - abs(y-d[0][1])
                if d[0][0]+avail >= min_xy or d[0][0]-avail <= max_xy:
                    scans.append( (max(d[0][0]-avail, min_xy), min(d[0][0]+avail, max_xy)) )

        scans.sort(key=lambda s:s[0])

        ret = scans[0][1]-scans[0][0]
        min_x = scans[0][0]
        max_x = scans[0][1]
        for i,s in enumerate(scans[1:], 1):
            if min_x <= s[0] <= max_x:
                if min_x <= s[1] <= max_x:
                    pass
                else:
                    ret += s[1]-max_x
                    max_x = s[1]
            else:
                ret += 1+s[1]-s[0]
                min_x = max(s[0], min_x)
                max_x = s[1]
        if ret < (max_xy-min_xy):
            rez.append((min_x-1, y, 4000000*(min_x-1)+y))
    return rez   

if __name__ == "__main__":

    input = loadData('20221215-t1.txt')
    ret = part1(input, 10)
    print(f'Test 1 (26): {ret}')

    input = loadData('20221215.txt')
    ret = part1(input, 2000000)
    print(f'Part 1 (4502208): {ret}')

    input = loadData('20221215-t1.txt')
    ret = part2(input, max_xy=20)
    print(f'Test 2 (56000011): {ret}')

    input = loadData('20221215.txt')
    ret = part2(input, max_xy=4000000)
    print(f'Part 2 (13784551204480): {ret}')
