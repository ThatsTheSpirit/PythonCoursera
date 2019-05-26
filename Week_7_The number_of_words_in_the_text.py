fname = 'input.txt'
sp = set()
with open(fname, 'r', encoding='utf8') as textfile:
    lines = textfile.readlines()
    for line in lines:
        sp.update(set(line.rstrip().split(' ')))
sp.discard('')
print(len(sp))
