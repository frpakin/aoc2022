def loadData(fname):
    with open(fname, 'r') as fd:
        inputs = [ tuple([ int(ll) if i==1 else ll for i, ll in enumerate(l.strip().split()) ]) for l in fd ]
    return inputs


def part1(inputs):
    outputs = {}
    X = 1
    cycle = 1
    outputs[cycle] = X*cycle
    pc = 0
    while cycle<=220 and pc<len(inputs):
        if inputs[pc][0] == 'noop':
            cycle+=1
            outputs[cycle] = X*cycle
            pc+=1
        elif inputs[pc][0] == 'addx':
            cycle+=1
            outputs[cycle] = X*cycle
            X += inputs[pc][1]
            cycle+=1
            outputs[cycle] = X*cycle
            pc+=1
    return outputs[20]+outputs[60]+outputs[100]+outputs[140]+outputs[180]+outputs[220]


def part2(inputs):
    output = [ '.' for _ in range(6*40)]
    X = 1
    cycle = 1
    pc = 0
    while cycle<=240 and pc<len(inputs):
        if inputs[pc][0] == 'noop':
            output[cycle-1]= '#' if X-1<=(cycle-1)%40<=X+1 else '.'
            cycle+=1
            pc+=1
        elif inputs[pc][0] == 'addx':
            output[cycle-1]= '#' if X-1<=(cycle-1)%40<=X+1 else '.'
            cycle+=1
            output[cycle-1]= '#' if X-1<=(cycle-1)%40<=X+1 else '.'
            cycle+=1
            X += inputs[pc][1]
            pc+=1
        else:
            raise ValueError
    print()
    for l in range(6):
        print(''.join(output[l*40:(l+1)*40]))
    

if __name__ == "__main__":
    inputs = loadData('20221210-t1.txt')
    ret = part1(inputs)
    print(f'Test 1 (13140): {ret}')
    inputs = loadData('20221210.txt')
    ret = part1(inputs)
    print(f'Part 1 (16880): {ret}')

    inputs = loadData('20221210-t1.txt')
    ret = part2(inputs)
    inputs = loadData('20221210.txt')
    ret = part2(inputs)
    