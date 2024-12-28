# Input: s = "This is a python language"
# Output: This is python language

# Input: s = "i am laxmi"
# Output: am


n = "this is a next level"
s=n.split(" ")
for i in s:
    if len(i)%2==0:
        print(i)