marks = []
g = ''
while g != '!':
    g = input('Поставьте оценки, ! если хотите закончить: ')
    if g != '!':
        marks.append(int(g))
print(marks)
a = sum(marks)
b = len(marks)
print(a / b)