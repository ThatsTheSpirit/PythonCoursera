n = int(input())
mySet = set(map(int, [i for i in range(1, n + 1)]))
s = input()

while s != 'HELP':
    s = set(map(int, s.split()))
    command = input()
    if command == 'YES':
        if s < mySet:
            mySet = s
        else:
            mySet &= s
    elif command == 'NO':
        mySet.difference_update(s)

    s = input()
print(*sorted(mySet))
