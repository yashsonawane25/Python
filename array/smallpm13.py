def swapList(list):
    list[0],list[-2] = list[-2],list[0]
    return list

list = [23,65,19,90]
print(swapList(list))
