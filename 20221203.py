
def prio(s):        
    return [ 1 + ord(c) - ord('a') if 'a' <= c <= 'z' else 27 + ord(c) - ord('A') for c in s ]


def part1(input):
    ret = 0
    for l in input:
        c1 = l[:len(l)//2]
        c2 = l[len(l)//2:]
        c3 = ''.join(sorted(set(c1) & set(c2), key = c1.index))
        p = sum(prio(c3))
        #print(f'{c1} - {c2} -> {c3} | {p}')
        ret += p
    return ret

def part2(input):
    ret = 0
    i = 0
    while i<len(input):
        c1 = input[i]
        c2 = input[i+1]
        c3 = input[i+2]
        c4 = ''.join(sorted(set(c1) & set(c2) & set(c3), key = c1.index))
        p = sum(prio(c4))
        #print(f'{i} -> {c4} | {p}')
        ret += p
        i+= 3
    return ret

if __name__ == "__main__":
    input = [   "vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                "PmmdzqPrVvPwwTWBwg",
                "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                "ttgJtRGJQctTZtZT",
                "CrZsJsPPZsGzwwsLwLmpwMDw" ]
    print(f'Test1 (157): {part1(input)}')
    print(f'Test2 (70): {part2(input)}')

    with open('20221203.txt', 'r') as f:
        input = [ l.strip() for l in f ]
    print(f'Part1 (8202): {part1(input)}')
    print(f'Part2 (2864): {part2(input)}')