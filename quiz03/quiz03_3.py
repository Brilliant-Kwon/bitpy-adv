def summary(*args):
    total = 0
    maxval = 0
    minval = 0
    avg = 0
    for x in args:
        total += x
    maxval = max(args)
    minval = min(args)
    avg = total / len(args)

    return total, maxval, minval, avg


total, maxval, minval, avg = summary(80, 75, 90, 95, 85)
print(total, maxval, minval, avg)
