# Input: 'Geeks123For123Geeks'
# Output: GeeksForGeeks
# Explanation: In This, we have removed the '123' character from a string.

test_str = "GeeksForGeeks"
new_str = test_str.replace('e','')
print("The string after removal of i'th character(dosen't work: " + new_str)
new_str = test_str.replace('s',"",1)
print("The string after removal of i'th character( works) :" + new_str)

# second method
str = 'Geeks123For123Geeks'
print(str.translate({ord(i): None for i in '123'}))