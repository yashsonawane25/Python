# Input  : arr[] = {4, 5, 6, 7, 0, 1, 2}, target = 3
# Output : 4

# Input  : arr[] = { 4, 5, 6, 7, 0, 1, 2 }, target = 3
# Output : -1

# Input : arr[] = {30, 40, 50, 10, 20}, target = 10   
# Output : 3

# ans =

def search(nums,target):
    left,right =0 ,len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[left]:
            if target >= num[left] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target > nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

arr1 = [4,5,6,7,0,1,2]
target1 = 0
print(search(arr1,target1))

arr1 = [4,5,6,7,0,1,2]
target1 = 3
print(search(arr1,target1))