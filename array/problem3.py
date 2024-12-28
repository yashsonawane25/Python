# Input: n=7 , array[]={1, 2, 3, 6, 3, 6, 1}
# Output: 1, 3, 6
# Explanation: The numbers 1 , 3 and 6 appears more than once in the array.

# Input : n = 5 and array[] = {1, 2, 3, 4 ,3}
# Output: 3
# Explanation: The number 3 appears more than once in the array.

# ans =

def duplicates(arr):
    freq_map = {}
    result = []

    for num in arr:
        freq_map[num] = freq_map.get(num,0) + 1

    for key,value in freq_map.items():
        if value > 1:
            result.append(key)
    
    if not result:
        result.append(-1)
    result.sort()
    return result

if __name__ == '__main__':
    a = [1,6,5,2,3,3,2,5,5]
    duplicates_found = duplicates(a)

    print ("Duplicates elements:",end = "")
    for element in duplicates_found:
        print(element,end =" ")
        print()