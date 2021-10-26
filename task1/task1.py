n, m = map(int, input().split(' '))

array = list(range(1, n+1))
last_num = None
answer = []
start = 0
stop = m

while last_num != 1:
    step_array = []
    for i in range(start, stop):
        step_array.append(array[i])
    last_num = step_array[-1]
    start += m - 1
    stop += m - 1
    if stop > n - 1:
        start -= n
        stop -= n

    answer.append(step_array[0])
print(*answer, sep='')