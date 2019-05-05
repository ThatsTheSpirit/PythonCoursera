def count_sort(myList):
    new_list = [0] * max(myList) * 2
    for i in myList:
        new_list[i] += 1
    return new_list


myList = list(map(int, input().split()))
new_list = count_sort(myList)

for i in range(len(new_list)):
    print((str(i) + ' ') * new_list[i], end='')
