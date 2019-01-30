lst = [1, 3.14, 'python', 7, 89.1, 3]
lst_copy = []
for x in lst:
    if isinstance(x, (int, float)):
        lst_copy.append(x)

# lst_copy = get_total2(lst_copy)
print(lst_copy)
