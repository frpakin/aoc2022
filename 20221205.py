from collections import defaultdict


def loadData(filename):
    with open(filename, 'r') as f:
        input = [ l.strip('\n') for l in f ]
        i = 0
        stacks = defaultdict(list)
        while len(input[i])>0:
            for j,c in enumerate(input[i]):
                if 'A' <= c <= 'Z':
                    stacks[(j-1)//4].insert(0, c)
            i+=1
        i+=1    # skip new line
        cmds = []
        while i <len(input):
            cmd = input[i].split(' ')
            cmds.append((int(cmd[1]), int(cmd[3])-1, int(cmd[5])-1))
            i+=1
    return stacks, cmds


def part1(stacks, cmds):
    for cmd in cmds:
        for _ in range(cmd[0]):
            v = stacks[cmd[1]][-1]
            stacks[cmd[1]].pop()
            stacks[cmd[2]].append(v)
    ret = "".join([ stacks[i][-1] for i in sorted(stacks.keys()) ])
    return ret


def part2(stacks, cmds):
    for cmd in cmds:
        tmp = []
        for _ in range(cmd[0]):
            v = stacks[cmd[1]][-1]
            stacks[cmd[1]].pop()
            tmp.insert(0, v)
        stacks[cmd[2]].extend(tmp)
    ret = "".join([ stacks[i][-1] for i in sorted(stacks.keys()) ])
    return ret

if __name__ == "__main__":    
    stacks, cmds = loadData('20221205-t1.txt')
    ret = part1(stacks, cmds)
    print(f'Test1 (CMZ) : {ret}')
    stacks, cmds = loadData('20221205-t1.txt')
    ret = part2(stacks, cmds)
    print(f'Test2 (MCD) : {ret}')

    stacks, cmds = loadData('20221205.txt')
    ret = part1(stacks, cmds)
    print(f'Part1 (SHQWSRBDL) : {ret}')
    stacks, cmds = loadData('20221205.txt')
    ret = part2(stacks, cmds)
    print(f'Part2 (CDTQZHBRS) : {ret}')
    