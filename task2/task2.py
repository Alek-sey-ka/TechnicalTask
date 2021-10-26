directory_1 = input('1st file: ')
directory_2 = input('2nd file: ')

file_1 = open(directory_1, 'r')
file_2 = open(directory_2, 'r')

x, y = map(float, file_1.readline().split(' '))
r = float(file_1.readline())

dots = []
for line in file_2.readlines():
    dots.append(tuple(map(float, line.split(' '))))

answer = []
for i in dots:
    if (i[0] - x)**2 + (i[1] - y)**2 == r**2:
        answer.append(0)
    elif (i[0] - x)**2 + (i[1] - y)**2 < r**2:
        answer.append(1)
    else:
        answer.append(2)

for location in answer:
    print(location)