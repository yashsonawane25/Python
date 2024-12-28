# Input: khokho
# Output: 
# The entered string is symmetrical
# The entered string is not palindrome

# Input:amaama
# Output:
# The entered string is symmetrical
# The entered string is palindrome

string = 'khokho'

length = len(string)
half = length // 2

first_str = string[:half]
second_str = string[half + length % 2:]
if first_str == second_str:
    print(string, 'string is symmetrical')
else:
    print(string,'string is not symetrical')

if first_str == second_str[::-1]:
        print(string, 'string is symmetrical')
else:
         print(string, 'string is not palindrome')
