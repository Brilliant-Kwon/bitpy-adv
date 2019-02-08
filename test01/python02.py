data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

slice1 = data[0:5]  # => (1, 2, 3, 4, 5)
slice2 = data[2:7]  # => (3, 4, 5, 6, 7)
slice3 = data[5:]  # => (6, 7, 8, 9, 10)

# BEGIN: 점검을 위한 코드이니 수정하지 마십시오
print(slice1)
print(slice1 == (1, 2, 3, 4, 5))
print(slice2)
print(slice2 == (3, 4, 5, 6, 7))
print(slice3)
print(slice3 == (6, 7, 8, 9, 10))
# END: 점검을 위한 코드이니 수정하지 마십시오
