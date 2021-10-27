from math import log2
def isThueMorse(seq):
    pot=log2(len(seq))
    item='0'
    seq = ''.join(map(str,seq))
    for i in range(int(pot)):
        pile=''
        for j in item:
            if j=='0':pile+='1'
            else:pile+='0'
        item+=pile
    return seq.startswith(item)
