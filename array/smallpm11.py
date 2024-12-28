# Input : {‘a’: 100, ‘b’:200, ‘c’:300}
# Output : 600

# Input : {‘x’: 25, ‘y’:18, ‘z’:45}
# Output : 88

def returnsum(myDict):

    list = []
    for i in myDict:
        list.append(myDict[i])
        final = sum(list)
        return final

dict = {'a':100,'b':200,'c':300}
print("sum:",returnsum(dict))