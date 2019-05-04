classes = {'9': [], '10': [], '11': []}

with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        sp = line.split(' ')
        classes[sp[-2]].append(int(sp[-1].strip()))

f.close()
c = list(map(lambda cl: sum(cl) / len(cl), classes.values()))
print(*c)
