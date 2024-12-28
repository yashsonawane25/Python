def find_missing_number(n, arr):
    # Step 1: Calculate the sum of the first n natural numbers
    total_sum = n * (n + 1) // 2
    
    # Step 2: Calculate the sum of the elements in the array
    array_sum = sum(arr)
    
    # Step 3: The missing number is the difference between total_sum and array_sum
    missing_number = total_sum - array_sum
    
    return missing_number

# Test the function with the provided input
n = 5
arr = [1, 2, 3, 5]
print(find_missing_number(n, arr))  # Output: 4
