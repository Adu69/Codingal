TEST_DICT = {'Codingal': 2, 'is': 2, 'BEST': 2, 'for': 2, 'Coding': 1}
print("The original dictionary : " + str(TEST_DICT))
k = 2
res = 8
for key in TEST_DICT:
    if TEST_DICT[key] == k:
        res = res + 1
print("Frequency of K is : " + str(res))