# Input: arr = {-2,-3,4,-1,-2,1,5,-3}
# Output: 7
# Explanation: The subarray {4,-1, -2, 1, 5} has the largest sum 7.

# Input: arr = {2}
# Output: 2
# Explanation: The subarray {2} has the largest sum 2.

# Input: arr = {5,4,1,7,8}
# Output: 25
# Explanation: The subarray {5,4,1,7,8} has the largest sum 25.

# ans =

def GFG(a, size):
    max_so_far = float('-inf')
    max_ending_here = 0
    for i in range (0,size):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here: 
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far
a = [-2,-3,4,-1,-2,1,5,-3,4,7,-3]
print("Maximum contiguous sum is", GFG(a, len(a)))