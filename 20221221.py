from colorama import Fore, Back, Style


def loaddata(fname):
    data = open(fname, encoding='UTF8').read()
    ret = {}
    for l in data.split('\n'):
        a = l.split(':')
        k = a[0]
        v = a[1].strip().split(' ')
        ret[k] = int(v[0]) if len(v)==1 else v
    return ret



def eval(inputs, k):
    ret = 0
    v = inputs[k]
    if isinstance(v, list):
        a = eval(inputs, v[0])
        b = eval(inputs, v[2])
        if v[1]=='+': ret = a+b
        elif v[1]=='-': ret = a-b
        elif v[1]=='*': ret = a*b
        elif v[1]=='/': ret = a//b
        inputs[k] = ret
        return ret
    else:
        return v


def part1(inputs, debug=False):
    return eval(inputs, 'root')
    

def solve(inputs, root, me):
    h = 1
    x0 = 0
    tmp = inputs.copy()
    tmp[me] = x0
    y0 = eval(tmp, root)
    x1 = x0+h
    tmp = inputs.copy()
    tmp[me] = x1
    y1 = eval(tmp, root)
    while y0 != 0 and y1 == y0:
            x1 = x1+h
            tmp = inputs.copy()
            tmp[me] = x1
            y1 = eval(tmp, root)
    while y0 != 0:
        x0 = int(x0 - y0*(x1-x0)/(y1-y0))
        tmp = inputs.copy()
        tmp[me] = x0
        y0 = eval(tmp, root)
        x1 = x0+h
        tmp = inputs.copy()
        tmp[me] = x1
        y1 = eval(tmp, root)
        while y0 != 0 and y1 == y0:
            x1 = x1+h
            tmp = inputs.copy()
            tmp[me] = x1
            y1 = eval(tmp, root)

    return x0


def part2(inputs, debug=False):
    inputs['root'][1] = '-'
    return solve(inputs, 'root', 'humn')

if __name__ == "__main__":
    inputs = loaddata('20221221-t1.txt')
    ret = part1(inputs, debug=True)
    ko_red = Fore.RED + Style.NORMAL + 'KO' + Style.RESET_ALL
    ok_green = Fore.GREEN + Style.NORMAL + 'OK' + Style.RESET_ALL
    print(f'Test 1 (152): {ret} [{ok_green if ret==152 else ko_red}]')
    inputs = loaddata('20221221.txt')
    ret = part1(inputs)
    print(f'Part 1 (41857219607906): {ret} [{ok_green if ret == 41857219607906 else ko_red}]')
    inputs = loaddata('20221221-t1.txt')
    ret = part2(inputs, debug=True)
    print(f'Test 2 (301): {ret} [{ok_green if ret==301 else ko_red}]')
    inputs = loaddata('20221221.txt')
    ret = part2(inputs, debug=True)
    print(f'Part 2 (3916936880448): {ret} [{ok_green if ret==3916936880448 else ko_red}]')