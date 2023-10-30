import re
from collections import defaultdict
import concurrent.futures
from tqdm import trange
from tqdm import tqdm

def loaddata(fname):
    data = open(fname, encoding='UTF8').read()
    return [ tuple( [ int(t) for t in re.findall(r'\d+', l) ] ) for l in data.split('\n') ]


def calc(bp, time_max=24):
    ret = 0                                                 # ore -> clay -> obsidian -> geode
    fact_cost= { (0, 0, 0, 0) : (0, 0, 0, 0),               # Do nothing
                 (1, 0, 0, 0) : (bp[1], 0, 0, 0),           # Build ore fact
                 (0, 1, 0, 0) : (bp[2], 0, 0, 0),           # Build clay fact
                 (0, 0, 1, 0) : (bp[3], bp[4], 0, 0),       # Build obsidian fact
                 (0, 0, 0, 1) : (bp[5], 0, bp[6], 0)  }     # Build geode fact

    def ofilter(f, o, mult=2):
        if f[1]==0 and f[2]==0:
            return o[0]<=mult*max(bp[1], bp[2]) 
        elif f[2] == 0:
            return o[0]<=mult*max(bp[1], bp[2], bp[3]) or o[1]<=mult*bp[4] 
        else:
            return o[0]<=mult*max(bp[1], bp[2], bp[3], bp[5]) or o[1]<=mult*bp[4] or o[2]<=mult*bp[6]

    def ffilter(f, mult=2):
        if f[1]==0 and f[2]==0:
            return f[0]<=mult*max(bp[1], bp[2]) 
        elif f[2] == 0:
            return f[0]<=mult*max(bp[1], bp[2], bp[3]) or f[1]<=mult*bp[4] 
        else:
            return f[0]<=mult*max(bp[1], bp[2], bp[3], bp[5]) or f[1]<=mult*bp[4] or f[2]<=mult*bp[6]

    def onorm(o):
        return o[0]*1000000+o[1]*10000+o[2]*100+o[3]

    def prune(ol):
        if len(ol)==1:
            return ol
        ol2 = [ o for o in ol if any([ o[0]<=oo[0] and o[1]<=oo[1] and o[2]<=oo[2] and o[3]<=oo[3] for oo in ol if oo != o])]
        tmp = defaultdict(list)
        for o in filter(lambda o: o not in ol2, ol):            
            i = 3
            while i>=0 and o[i]==0: i+=-1
            sig = tuple([o[j] for j in range(i)])
            tmp[sig].append(o)
        for sig in tmp:
            tmp[sig].sort(key=onorm)
        return [ tmp[sig][-1] for sig in tmp ]

    status = { (1,0,0,0): [(0,0,0,0)] }
    for _ in range(time_max):
        for tmp in [ current_facto for current_facto in status if not ffilter(current_facto) ]:
            del status[tmp]
        for current_facto in status:
            if len(status[current_facto])>1:
                status[current_facto] = prune(status[current_facto])
        status_next = defaultdict(list)
        for current_facto in status:
            for current_ores in status[current_facto]:
                builds = [ f for f in fact_cost.items() if all([current_ores[i]>=f[1][i] for i in range(3)])]
                for b in builds:
                    ores = tuple(map(lambda i, j, k: i+j-k, current_facto, current_ores, b[1]))
                    ret = max(ret, ores[3])
                    if ofilter(current_facto, ores):
                        facto = tuple(map(lambda i, j: i+j, current_facto, b[0]))
                        status_next[facto].append(ores)
        status = status_next
    return ret


def part1(inputs, nb_workers=1):
    qlevel = {}
    if nb_workers<=1:
        qlevel = { b: calc(b, time_max=24) for b in tqdm(inputs) }
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(8, nb_workers)) as executor:
            futures = { executor.submit(calc, b, time_max=24):b for b in inputs }
            for future in concurrent.futures.as_completed(futures.keys()):
                b = futures[future]
                qlevel[b]=future.result()
    return sum([ r[0][0]*r[1] for r in qlevel.items() ])

def part2(inputs):
    qlevel = { b: calc(b, time_max=32) for b in tqdm(inputs[0:min(3, len(inputs))]) }
    ret = 1
    for r in qlevel.values():
        ret = ret*r
    return ret


if __name__ == "__main__":
    inputs = loaddata('20221219-t1.txt')
    ret = part1(inputs)
    print(f'Test 1 (33): {ret}')
    inputs = loaddata('20221219.txt')
    ret = part1(inputs)
    print(f'Part 1 (1294): {ret}')

    #inputs = loaddata('20221219-t1.txt')
    #ret = part2(inputs)
    #print(f'Test 2 ({56*62}): {ret}')
    inputs = loaddata('20221219.txt')
    ret = part2(inputs)
    print(f'Part 2 (13640): {ret}')