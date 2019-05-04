classes = []

with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        sp = line.split(' ')
        classes.append([sp[0], sp[1], sp[3].strip()])

f.close()
classes.sort(key=lambda p: [p[0]])
for i in classes:
    print(*i)
