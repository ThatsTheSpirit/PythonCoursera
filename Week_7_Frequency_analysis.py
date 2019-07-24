d = {}
with open('input.txt', 'r', encoding='utf8') as textfile:
    lines = textfile.read()
    for line in lines.split():
        if line not in d:
            d[line] = 1
        else:
            d[line] += 1
for let in sorted(sorted(d), key=d.get, reverse=True):
    print(let)
