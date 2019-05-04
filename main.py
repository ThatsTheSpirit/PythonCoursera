'''A few people took part in the computer science competition.

Determine and output the average points of the participants of 
the Olympiad in the 9th grade, in the 10th grade, in the 11th grade.'''

classes = {'9': [], '10': [], '11': []}

with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        sp = line.split(' ')
        classes[sp[-2]].append(int(sp[-1].strip()))

f.close()
c = list(map(lambda cl: sum(cl) / len(cl), classes.values()))
print(*c)
