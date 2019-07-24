d = {}
with open('input.txt', 'r', encoding='utf8') as textfile:
    lines = textfile.read()
    for line in lines.split('\n'):
        if line not in d:
            d[line] = 1
        else:
            d[line] += 1
d.pop("")
with open('output.txt', 'w', encoding='utf8') as outfile:
    if max(d.values()) > sum(d.values()) / 2:
        outfile.write(sorted(d, key=d.get, reverse=True)[0])
    else:
        d = sorted(d, key=d.get, reverse=True)
        outfile.writelines("\n".join(d[:2]))
