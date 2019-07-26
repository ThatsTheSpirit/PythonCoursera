classes = {'9': [], '10': [], '11': []}

with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        sp = line.split(' ')
        classes[sp[-2]].append(int(sp[-1].strip()))
for i in classes.values():
    print(max(i), end=' ')
