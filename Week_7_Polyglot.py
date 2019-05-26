n = int(input())
myList = []
for i in range(n):
    numb = int(input())

    s = set()
    for j in range(numb):
        s.add(input())
    myList.append(s)

common = myList[0]
union = myList[0].copy()
for i in myList:
    common.intersection_update(i)
    union.update(i)

print(len(common), sep='\n', *common)
print(len(union), sep='\n', *sorted(union, reverse=True))
