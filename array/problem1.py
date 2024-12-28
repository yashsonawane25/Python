# Input: arr[] = {0, -1, 2, -3, 1}, x= -2
# Output: Yes
# Explanation: If we calculate the sum of the output,1 + (-3) = -2

# Input: arr[] = {1, -2, 1, 0, 5}, x = 0
# Output: No

# ans

def chkpair(A,size,x):
    for i in range(0, size - 1):
        for j in range(i + 1,size):
            if(A[i] + A[j] == x):
                  return 1
            return 0
        
if __name__=="__main__":
     A =[0,-1,4,-3,1]
     x = -2
     size = len(A)

     if (chkpair(A , size , x)):
        print("Yes")

     else:
      print("No")