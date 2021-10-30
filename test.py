import math

test_case = [0, 1, 2, 3, 4]

length = (len(test_case))
print(length)
print((length//2))
print((length//2)+1)

if length % 2 ==0:
    half_even = length // 2
    print(test_case[:half_even])
else:
    half_odd = (length // 2 + 1)
    print(test_case[:half_odd])
