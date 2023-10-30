from collections import defaultdict


def loadData(fname):
    fs = defaultdict(list)
    cwd = []
    with open(fname, 'r') as fd:
        inputs = [ l.strip() for l in fd ]
        i=0
        while(i<len(inputs)):
            l = inputs[i]
            if l[0]=='$':
                cmds = l.split()
                if cmds[1]=='cd':
                    if cmds[2]=='..':
                        cwd.pop()
                    elif cmds[2]=='/':
                        cwd.clear()
                    else:
                        cwd.append(cmds[2])
                    i += 1
                elif cmds[1]=='ls':
                    i += 1
                    path = '/'.join(cwd)
                    while i<len(inputs) and inputs[i][0]!='$':
                        fs[path].append(inputs[i].split())
                        i += 1
    return fs


def part1(fs):
    dirs = {}
    def scanData(fs, context=''):
        tt = 0
        for e in fs[context]:
            if e[0] == 'dir':
                tt += scanData(fs, e[1] if context=='' else context + '/' + e[1])
            else:
                tt += int(e[0])
        dirs[context] = tt
        return tt
    
    scanData(fs)
    return sum([ dirs[d] for d in dirs.keys() if dirs[d]<=100000 ])


def part2(fs):
    dirs = {}
    def scanData(fs, context=''):
        dirs[context] = sum([ scanData(fs, e[1] if context=='' else context + '/' + e[1]) if e[0] == 'dir' else int(e[0]) for e in fs[context]])
        return dirs[context]
    
    scanData(fs)
    unused_space = 70000000 - max([dirs[d] for d in dirs.keys()])
    required_space = 30000000 - unused_space
    return min([ d[1] for d in dirs.items() if d[1]>=required_space ])


if __name__ == "__main__":
    fs = loadData('20221207-t1.txt')
    ret = part1(fs)
    print(f'Test 1 (95437): {ret}')
    fs = loadData('20221207-t1.txt')
    ret = part2(fs)
    print(f'Test 2 (24933642): {ret}')

    fs = loadData('20221207.txt')
    ret = part1(fs)
    print(f'Part 1 (1583951): {ret}')
    fs = loadData('20221207.txt')
    ret = part2(fs)
    print(f'Part 2 (214171): {ret}')
