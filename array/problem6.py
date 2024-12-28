# Input: arr[] = {6, -3, -10, 0, 2}
# Output:  180
# Explanation: The subarray is {6, -3, -10}

# Input: arr[] = {-1, -3, -10, 0, 60}
# Output:   60
# Explanation: The subarray is {60}

# ans =

def maxsubarrayproduct(arr, n):
    result = arr[0]
    for i in range(n):
        mul = arr[i]
        for j in range(i + 1, n):
            result = max(result,mul)
            mul *= arr[j]

        result = max (result,mul)
    return result

arr = [1,-2,-3,0,7,-8,-2]
n = len(arr)
print("Maximum sub array product is ", maxsubarrayproduct(arr,n))