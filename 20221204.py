def included(s1, s2):
    return s2[0] <= s1[0] <= s2[1] and s2[0] <= s1[1] <= s2[1]

def part1(l):
    field = [ [int(v) for v in e.split('-')] for e in l.split(',') ]
    return included(field[0], field[1]) or included(field[1], field[0])


def overlap(s1, s2):
    return s2[0] <= s1[0] <= s2[1] or s2[0] <= s1[1] <= s2[1] 

def part2(l):
    field = [ [int(v) for v in e.split('-')] for e in l.split(',') ]
    return overlap(field[0], field[1]) or overlap(field[1], field[0])


if __name__ == "__main__":
    input = [   "2-4,6-8",
                "2-3,4-5",
                "5-7,7-9",
                "2-8,3-7",
                "6-6,4-6",
                "2-6,4-8"  ]
    ret = list(filter(part1, input))
    print(f'Test1 (2): {len(ret)}')
    ret = list(filter(part2, input))
    print(f'Test2 (4): {len(ret)}')

    with open('20221204.txt', 'r') as f:
        input = [ l.strip() for l in f ]
    ret = list(filter(part1, input))
    print(f'Part1 (513): {len(ret)}')
    ret = list(filter(part2, input))
    print(f'Part2 (878): {len(ret)}')
