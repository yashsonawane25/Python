# Input: arr[]  = {10, 3, 5, 6, 2}
# Output: prod[]  = {180, 600, 360, 300, 900}
# 3 * 5 * 6 * 2 product of other array 
# elements except 10 is 180
# 10 * 5 * 6 * 2 product of other array 
# elements except 3 is 600
# 10 * 3 * 6 * 2 product of other array 
# elements except 5 is 360
# 10 * 3 * 5 * 2 product of other array 
# elements except 6 is 300
# 10 * 3 * 6 * 5 product of other array 
# elements except 2 is 900


# Input: arr[]  = {1, 2, 3, 4, 5}
# Output: prod[]  = {120, 60, 40, 30, 24 }
# 2 * 3 * 4 * 5  product of other array 
# elements except 1 is 120
# 1 * 3 * 4 * 5  product of other array 
# elements except 2 is 60
# 1 * 2 * 4 * 5  product of other array 
# elements except 3 is 40
# 1 * 2 * 3 * 5  product of other array 
# elements except 4 is 30
# 1 * 2 * 3 * 4  product of other array 
# elements except 5 is 24

# ans =

def productArray(arr,n):
    if(n == 1):
        print(0)
        return
    left =[0]*n
    right =[0]*n
    prod = [0]*n
    left[0]= 1
    right[n-1] = 1

    for i in range(1,n):
        left[i] = arr[i - 1] * left[i - 1]

    for j in range(n-2, -1, -1):
        right[j] = arr[j + 1] * right[j + 1]

    for i in range(n):
        prod[i] = left[i] * right[i]

    for i in range(n):
        print(prod[i],end='')

arr = [10 , 3, 5, 6, 2]
n = len( arr)
print("The product array is: ")
productArray(arr , n)