import sys
from string import ascii_uppercase as uc

enfreq = 'AEOSRINDMUTCLPVGHQBFZJXKYW'

ltcount= {'A': 0, 'E': 0, 'O': 0, 'S': 0, 'R': 0, 'I': 0, 'N': 0, 'D': 0, 'M': 0, 'U': 0, 'T': 0, 'C': 0, 'L': 0, 'P': 0, 'V': 0, 'G': 0, 'H': 0, 'Q': 0, 'B': 0, 'F': 0, 'Z': 0, 'J': 0, 'X': 0, 'K': 0, 'Y': 0, 'W': 0}
file = open(sys.argv[1], 'r').read().upper()

for lt in file:
    if lt in uc:
        ltcount[lt] += 1

order = []
score = 0

for w in sorted(ltcount, key=ltcount.get, reverse=True):
    print (w, ltcount[w])
    order.append(w)

order = ''.join(order)

for clt in enfreq[:6]:
    if clt in order[:6]:
        score += 1

for ult in enfreq[-6:]:
    if ult in order[-6:]:
        score += 1

print ('Nota:', score, 'de 12')