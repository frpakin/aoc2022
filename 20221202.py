
def p1(a, x):
    outcome = { 'AX': 3, 'BY': 3, 'CZ': 3, 
                'AY': 6, 'AZ': 0, 
                'BX': 0, 'BZ': 6,
                'CX': 6, 'CY': 0,}
    return outcome[a+x]


def p2(a, x):
    outcome = { 'AX': 'C', 'AY': 'A', 'AZ': 'B', 
                'BX': 'A', 'BY': 'B', 'BZ': 'C',
                'CX': 'B', 'CY': 'C','CZ':  'A' }
    return outcome[a+x]


if __name__ == "__main__":
    win = { 'X':0, 'Y':3, 'Z': 6 }
    val = { 'X':1, 'Y':2, 'Z':3, 'A':1, 'B':2, 'C':3 }

    input = "A Y\nB X\nC Z"
    game = [ hand.split(' ') for hand in input.split('\n') ]
    scores = [ val[g[1]] + p1(g[0], g[1]) for g in game ]
    print(f'Test 1 (15): {sum(scores)}')
    scores = [ val[p2(g[0], g[1])] + win[g[1]] for g in game ]
    print(f'Test 2 (12): {sum(scores)}')

    with open('20221202.txt', 'r') as f:
        input = [ l.strip() for l in f ]
    game = [ hand.split(' ') for hand in input ]
    scores = [ val[g[1]] + p1(g[0], g[1]) for g in game ]
    print(f'Part 1 (10941): {sum(scores)}')
    scores = [ val[p2(g[0], g[1])] + win[g[1]] for g in game ]
    print(f'Part 2 (13071): {sum(scores)}')
