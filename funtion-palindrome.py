#function which return reverse of a string
def paleidrome(s):
    return s == s[::-1]

#driver code

s = "dogeeseseegod"
ans = paleidrome(s)

if ans:
    print("yes")
else:
    print("no")










