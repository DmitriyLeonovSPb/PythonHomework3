unsorted_list = [1, 1, 2, 8, 9, 9, 6, 2, 0, 0, 0]
doubles = []
for i in unsorted_list:
    if unsorted_list.count(i) > 1 and i not in doubles:
        doubles.append(i)
print("Повторяющиеся элементы:", doubles)