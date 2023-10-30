
def part1(fname):
    dwarfs = [ [] ]
    with open(fname, 'r') as f:
        for l in f:
            m = l.strip()
            if len(m) == 0:
                dwarfs.append([])
            else:
                dwarfs[-1].append(int(m))
    snacks = [ sum(d) for d in dwarfs ]
    return max(snacks)


def part2(fname):
    dwarfs = [ [] ]
    with open(fname, 'r') as f:
        for l in f:
            m = l.strip()
            if len(m) == 0:
                dwarfs.append([])
            else:
                dwarfs[-1].append(int(m))
    snacks = [ sum(d) for d in dwarfs ]
    snacks.sort(reverse=True)
    return sum(snacks[0:3])


if __name__ == "__main__":
    ret = part1("20221201.txt")
    print(f'Part1 (71502) : {ret}')
    ret = part2("20221201.txt")
    print(f'Part2 (208191) : {ret}')

