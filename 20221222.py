from colorama import Fore, Back, Style
import re

def loaddata(fname):
    data = open(fname, encoding='UTF8').read()
    ret = { 'map': [ l for l in data.split('\n') ],
            'F': 0}
    ret['path'] = re.findall('\\d+|R|L', ret['map'][-1])
    ret['map'].pop()
    ret['map'].pop()
    ret['L'], ret['C'], ret['face'], ret['l'], ret['c'] = lookupStart(ret) 
    ret['face_size'] = max([len(l) for l in ret['map']])//4
    ret['cube'] = { (1,0): (6,3), (1,1): (4,1), (1,2): (3,0), (1,3): (2,0) }
    return ret


def lookupStart(data):
    l, c = 0, 0
    while l<len(data['map']) and data['map'][l][c]!='.':
        while c<len(data['map'][0]) and data['map'][0][c]!='.': c+=1
        if not c<len(data['map'][0]): l+=1
    return l,c,1,0,0


def wmove(data, steps):
    l, c, s, ll, cc = data['L'], data['C'], steps, data['L'], data['C']
    while s!=0:
        if data['F'] == 0:
            cc = (cc+1)%len(data['map'][l])
            while data['map'][l][cc] == ' ': cc = (cc+1)%len(data['map'][l])
        elif data['F'] == 2:
            cc = cc-1 if cc>0 else len(data['map'][ll])-1
            while data['map'][l][cc] == ' ': cc = cc-1 if cc>0 else len(data['map'][ll])-1
        if data['F'] == 1:
            ll = (ll+1)%len(data['map'])            
            while c>=len(data['map'][ll]) or data['map'][ll][c] == ' ': ll = (ll+1)%len(data['map'])
        if data['F'] == 3:
            ll = ll-1 if ll>0 else len(data['map'])-1
            while c>=len(data['map'][ll]) or data['map'][ll][c] == ' ': ll = ll-1 if ll>0 else len(data['map'])-1
        if data['map'][ll][cc]=='#': break
        else:
            l,c  = ll, cc
        s+=-1
    return l, c


def display(data):
    for l, s in enumerate(data['map']):
        if l==data['L']:
            s = data['map'][l][:data['C']] + ['>', 'v', '<', '^'] [data['F']] + data['map'][l][data['C']+1:]
        print(s)
    print()

def part1(data, debug=False):
    for m in data['path']:
        if debug==True: display(data)
        if m == 'R': data['F'] = (data['F']+1) % 4
        elif m =='L': data['F'] = (data['F']+4-1) % 4
        else: data['L'], data['C'] = wmove(data, int(m))
    return 1000*(1+data['L']) + 4*(1+data['C']) + data['F']
    

def part2(inputs, debug=False):
    
    return 0

if __name__ == "__main__":
    inputs = loaddata('20221222-t1.txt')
    ret = part1(inputs, debug=True)
    ko_red = Fore.RED + Style.NORMAL + 'KO' + Style.RESET_ALL
    ok_green = Fore.GREEN + Style.NORMAL + 'OK' + Style.RESET_ALL
    print(f'Test 1 (6032): {ret} [{ok_green if ret==6032 else ko_red}]')
    inputs = loaddata('20221222.txt')
    ret = part1(inputs)
    print(f'Part 1 (?): {ret} [{ok_green if ret == 89224 else ko_red}]')
   