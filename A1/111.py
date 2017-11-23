x = 'abc'
def function(x):
    ans = list(x)
    for i in x:
        ans[i] = i+'a'
    return ans
print(function('abc'))