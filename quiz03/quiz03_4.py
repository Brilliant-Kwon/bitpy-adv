s = """
We encourage everyone to contribute to Python. 
If you still have questions after reviewing the material
in this guide, then the Python Mentors 
group is available to help guide new contributors through the process.
"""

strings = s.upper().replace("," or "." or "\n", "").split()
print(strings)
count = dict()

for x in strings:
    if x not in count.keys():
        count[x] = 1
    else:
        count[x] += 1

for key, value in count.items():
    print(key, " : ", value)
