from tqdm import tqdm

import tatsu
from tatsu.ast import AST

from functools import cmp_to_key
from math import prod

GRAMMAR = '''
    @@grammar::PAK


    start = factor $ ;

    factor = '[' expression ']';

    expression = ','%{term}* ;

    term = factor | number ;

    number = /\\d+/ ;
'''


class MyBasicSemantics:
    def start(self, ast):
        return list(ast) if isinstance(ast, tuple) else ast

    def number(self, ast):
        return int(ast)

    def factor(self, ast):
        return ast[1]

    def expression(self, ast):
        return [ x for i,x in enumerate(ast) if i%2==0 ]

    def term(self, ast):
        return list(ast) if isinstance(ast, tuple) else ast


def loadData(fname):
    with open(fname, 'r') as fd:
        inputs = [ l.strip() for l in fd ]
    i = 0
    pairs = []
    parser = tatsu.compile(GRAMMAR)
    with tqdm(total=len(inputs)) as pbar:
        while i< len(inputs):
            ast_l = parser.parse(inputs[i], semantics=MyBasicSemantics())
            ast_r = parser.parse(inputs[i+1], semantics=MyBasicSemantics())
            pairs.append((ast_l, ast_r))
            i+=3
            pbar.update(3)
    return pairs


def main2(fname):
    data = open(fname).read().strip()
    pairs = [list(map(eval, p.split("\n"))) for p in data.split("\n\n")]
    packets = sorted([y for x in pairs for y in x] + [[[2]], [[6]]], key=cmp_to_key(compare), reverse=True)
    print(f"Part 1bis: {sum(i for i, (l, r) in enumerate(pairs, 1) if compare(l, r) > 0)}")
    print(f"Part 2bis: {prod([n for n, packet in enumerate(packets, 1) if packet in ([[2]], [[6]])])}")
    return pairs

def compare(l, r):
    ll = [l] if isinstance(l, int) else l
    rr = [r] if isinstance(r, int) else r
    for l2, r2 in zip(ll, rr):
        if isinstance(l2, list) or isinstance(r2, list):
            rec = compare(l2, r2)
        else:
            rec = r2 - l2
        if rec != 0:
            return rec
    return len(rr) - len(ll)


def part1(pairs):
    return sum([i+1 for i in range(len(pairs)) if compare(*pairs[i])>0])


def part2(pairs):
    keys = [[[2]], [[6]]]
    flattened = [y for x in pairs for y in x] + keys
    packets = sorted(flattened, key=cmp_to_key(compare), reverse=True)
    return prod([ 1+packets.index(k) for k in keys ])


if __name__ == "__main__":
    main2('20221213.txt')

    inputs = loadData('20221213-t1.txt')
    ret = part1(inputs)
    print(f'Test 1 (13): {ret}')
    inputs = loadData('20221213.txt')
    ret = part1(inputs)
    print(f'Part 1 (6395): {ret}')
    ret = part2(inputs)
    print(f'Part 2 (24921): {ret}')


