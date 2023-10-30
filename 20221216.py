from collections import defaultdict
from itertools import combinations
from functools import cache

def loadData(fname):
    inputs = {}
    valves = {}
    data = open(fname).read().strip()
    for l in data.split("\n"):
        line = l.split(';')
        node = line[0].split()
        inputs[node[1]] = [ t.strip() for t in line[1][len('tunnels lead to valves '):].split(',') ]
        valves[node[1]] = int(node[4].split('=')[1])
    return inputs, valves


def explore_A(graph, start, end):
    cost = defaultdict(lambda: 0)
    priority = defaultdict(lambda: 0)
    paths = [ start ]
    while len(paths)>0:
        paths.sort(key=lambda e: priority[e], reverse=False)
        pc = paths.pop()
       
        for m in graph[pc]:
            new_cost = cost[pc]+1
            if m not in cost.keys() or new_cost < cost[m]:
                cost[m] = new_cost
                priority[m] = new_cost + 1
                paths.append(m)
    return cost[end]


def flow(valves_max, valves):
    return sum([ valves_max[n[0]] for n in valves.items() if n[1]!=0 ])


def simul2(paths_costs, valves_max, valves_order, t_max=30):
    valves = defaultdict(int)
    flow_total = 0
    t = 0
    t_last = 0
    i = 1
    while t<t_max and i<len(valves_order):
        t_last = t
        delta_t = paths_costs[(valves_order[i-1],valves_order[i])] + 1
        t += delta_t
        if t<t_max:
            flow_total += delta_t * flow(valves_max, valves)
            valves[valves_order[i]] = 1
        else:
            flow_total += (t_max-t_last) * flow(valves_max, valves)
        i += 1
    if t<t_max:
        flow_total += (t_max-t) * flow(valves_max, valves)
    return flow_total, valves.keys()


def explore_AAA(nodes, time_card, valves_max, path = ['AA'], t_max=30, t2_max=30, debug = None):
    edges = [ n for n in nodes if n not in path ]
    if t_max > 0 and len(edges) != 0:
        v = path[-1]
        tmp = [explore_AAA(nodes, time_card, valves_max, path + [w], t_max-(time_card[(v, w)] + 1), t2_max, debug) for w in edges]
        ret = max(tmp)
    else:
        ret, valves = simul2(time_card, valves_max, path, t_max=t2_max)
        if debug is not None: debug[f'{",".join(valves)}'] = ret
    return ret
        

def part1(graph, valves_max):
    paths = {}
    nodes_withvalve = [ n[0] for n in valves_max.items() if n[1]!=0 ]
    for x in combinations(['AA'] + nodes_withvalve, 2):
        paths[x] = explore_A(graph, x[0], x[1] )
        paths[(x[1], x[0])] = paths[x]
    debug = None
    ret =  explore_AAA(nodes_withvalve, paths, valves_max, debug=debug)
    #print("\n".join([v[0] for v in debug.items() if v[1]==ret]))
    return ret

def part2(graph, valves_max):
    paths = {}
    nodes_withvalve = [ n[0] for n in valves_max.items() if n[1]!=0 ]
    for x in combinations(['AA'] + nodes_withvalve, 2):
        paths[(x[1], x[0])] = paths[x] = explore_A(graph, x[0], x[1] )
    debug = {}
    ret1 =  explore_AAA(nodes_withvalve, paths, valves_max, t_max=26, t2_max=26, debug=debug)
    solutions = [v[0] for v in debug.items() if v[1]==ret1]
    nodes_withvalve = [ n[0] for n in valves_max.items() if n[1]!=0 and solutions[0].find(n[0]) == -1 ]
    ret2 =  explore_AAA(nodes_withvalve, paths, valves_max, t_max=26, t2_max=26, debug=debug)
    return ret1+ret2

if __name__ == "__main__":

    graph, valves = loadData('20221216-t1.txt')
    ret = part1(graph, valves)
    print(f'Test 1 (1651): {ret}')

    graph, valves = loadData('20221216-t1.txt')
    #ret = part2(graph, valves)
    #print(f'Test 2 (1707): {ret}')

    graph, valves = loadData('20221216.txt')
    ret = part1(graph, valves)
    print(f'Part 1 (1896): {ret}')

    graph, valves = loadData('20221216.txt')
    ret = part2(graph, valves)
    print(f'Part 2 (2576): {ret}')
