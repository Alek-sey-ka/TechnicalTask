def get_num(line):
    num = ''
    for sym in line:
        if sym.isdigit():
            num += sym
    return  num


def get_id(lines):
    list_id = []
    for line in lines:
        if '"id"' in line:
            list_id.append(get_num(line))
    return list_id

directory_1 = input('1st file: ')
directory_2 = input('2nd file: ')
with open(directory_1, 'r') as file:
    data_tests = file.readlines()
with open(directory_2, 'r') as file:
    data_values = file.readlines()

id_tests = get_id(data_tests)
id_values = get_id(data_values)


value = []
for i in data_values:
    if "passed" in i:
        value.append("passed")
    elif "failed" in i:
        value.append("failed")

dict_value = dict(zip(id_values, value))
value.clear()
for i in id_tests:
    if i in dict_value:
        value.append(dict_value[i])

j = 0
for i in range(len(data_tests)):
    if '"value": ""' in data_tests[i]:
        data_tests[i] = data_tests[i].replace('"value": ""', '"value": ' + value[j])
        j += 1

with open('report.json', 'w') as file:
    file.writelines(data_tests)
