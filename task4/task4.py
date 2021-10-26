directory = input('File: ')
file = open(directory, 'r')

array = []
for line in file.readlines():
    array.append(int(line))

min_dif = float('inf')

for num_1 in array:
    new_dif = 0
    for num_2 in array:
        new_dif += num_2 - num_1 if (num_2 - num_1) > 0 else num_1 - num_2
    if new_dif < min_dif:
        min_dif = new_dif

print(min_dif)
