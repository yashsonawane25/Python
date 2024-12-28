# Input : test_tup = (3, 7, 1, 18, 9), k = 2 
# Output : (3, 1, 9, 18)

# Input : test_tup = (3, 7, 1), k=1 
# Output : (1, 7) 

test_tup = (5,20,3,7,6,8)
print("The orginal tuple is:" + str(test_tup))
k = 2
res = []
test_tup = list(sorted(test_tup))
for idx, val in enumerate(test_tup):
    if idx < k or idx >= len(test_tup) - k:
        res.append(val)
res = tuple(res)

print("The extracted values: " + str(res))