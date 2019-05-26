lines = []
with open('input.txt', encoding='utf8') as textfile:
    lines = textfile.read().split()

countDict = {}
for line in lines:
    countDict[line] = countDict.get(line, 0) + 1
    print(countDict[line] - 1, end=' ')
